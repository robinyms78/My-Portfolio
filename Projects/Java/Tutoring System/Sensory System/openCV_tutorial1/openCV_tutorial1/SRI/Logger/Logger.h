#ifndef SRI_LOGGER_H
#define SRI_LOGGER_H

#include "SRI/Logger/LoggerExports.h"
//#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

#include <stdio.h> 
#include <stdarg.h>
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIList.h"
#include "SRI/SRIUtil/SRIRef.h"

#ifdef LOGGER_QTOUT
#include <qtextedit.h>
#endif

#ifdef LOGGER_XML_CONFIG
#include "xpath_processor.h"
#include "xpath_static.h"
#endif

namespace SRI{

typedef enum{
	LOG_DEBUG = 1,
	LOG_INFO,
	LOG_WARN,
	LOG_ERROR,
	LOG_CRITICAL,
	LOG_FATAL
} tLogLevel;

typedef enum{
	LOG_DEFAULT = 1,
	LOG_CONSOLE,
	LOG_STRING,
	LOG_FILE,
	LOG_QT
}tAppenderType;

SRI::String szLogLevelToStr(tLogLevel level);
SRI::String szAppenderTypeToStr(tAppenderType out);

tLogLevel eStrToLogLevel(SRI::String str);
tAppenderType eStrToAppenderType(SRI::String str);

//=======================================================================
	
class Logger;
class LoggerManager;

class LOGGER_API LogAppender{

protected:
	tAppenderType m_eAppenderType;
public:
	LogAppender();
	LogAppender(const LogAppender& c);
	LogAppender& operator=(const LogAppender& c);
	virtual ~LogAppender();
	virtual SRI::String szGetAppenderType();
	virtual tAppenderType eGetAppenderType();

	/** Creates a copy of current appender and returns the memory for it */
	virtual LogAppender* ptClone() = 0;
	virtual void vAppend(SRI::String msg) = 0;
	virtual void vAppend(const char *pszFormat, ...) = 0;	
	virtual void vAppend(const char *pszFormat, va_list argPtr) =0;
};

//=======================================================================
	
class LOGGER_API LogConsoleAppender : public LogAppender{

private:
	LogConsoleAppender(const LogConsoleAppender& c);
	LogConsoleAppender& operator=(const LogConsoleAppender& c);

public:
	LogConsoleAppender();
	virtual ~LogConsoleAppender();

	virtual LogAppender* ptClone();
	virtual void vAppend(SRI::String msg);
	virtual void vAppend(const char *pszFormat, ...);
	virtual void vAppend(const char *pszFormat, va_list argPtr);
};

//=======================================================================
	
class LOGGER_API LogStringAppender : public LogAppender{

private:
	LogStringAppender(const LogStringAppender& c);
	LogStringAppender& operator=(const LogStringAppender& c);
	SRI::String m_szLogString;

public:
	LogStringAppender();
	virtual ~LogStringAppender();

	virtual SRI::String szGetLogString();
	virtual void vClearLogString();

	virtual LogAppender* ptClone();
	virtual void vAppend(SRI::String msg);
	virtual void vAppend(const char *pszFormat, ...);
	virtual void vAppend(const char *pszFormat, va_list argPtr);
};

//=======================================================================

class LOGGER_API LogFileAppender : public LogAppender{

private:
	std::ofstream* m_ptFile;
	SRI::String m_szFileName;

public:
	LogFileAppender(SRI::String fileName);
	LogFileAppender(const LogFileAppender& c);
	LogFileAppender& operator=(const LogFileAppender& c);
	~LogFileAppender();
	virtual LogAppender* ptClone();

	/*This filename is taken as the default output file*/
	static SRI::String DefaultFileName;
	static std::ios::openmode DefaultOpenMode;
	static std::ios::openmode eStrToOpenMode(SRI::String mode);
	static SRI::String szOpenModeToString(std::ios::openmode mode);

	virtual SRI::String szGetFileName(){return m_szFileName;}
	virtual void vSetFileName(SRI::String fileName);
	virtual bool bFileIsOpen();
	virtual void vCloseFile();

	virtual void vAppend(SRI::String msg);
	virtual void vAppend(const char *pszFormat, ...);
	virtual void vAppend(const char *pszFormat, va_list argPtr);
};

////======================================================================================
////          AppenderOptions
////======================================================================================
/** The AppenderOptions class encapsulates options for creation of a logger.
* The options that are included are a union of all options off all supported
* loggers. Not all options are evaluated by all appenders.
*/
class LOGGER_API AppenderOptions{
private:
	bool m_bUseCentral;
	SRI::String  m_szFileName;	
	tAppenderType m_eAppenderType;
	void vInit();

public:
	AppenderOptions(tAppenderType type = LOG_CONSOLE);
	AppenderOptions(tAppenderType type, bool useCentral);
	AppenderOptions(const char* fileName, bool useCentral = false);
	AppenderOptions(const AppenderOptions& c);
	virtual ~AppenderOptions();

	AppenderOptions& operator=(const AppenderOptions& c);
	void vSetFileName(SRI::String fileName);

	tAppenderType eGetAppenderType() const;
	void vSetAppenderType(tAppenderType type);
	bool bIsCentral() const;
	void vSetCentral(bool isCentral);
	SRI::String szFileName() const;
};

//====================================================================================
//  Logger Configuration
//====================================================================================


class LOGGER_API LoggerConfig{
public:
	LoggerConfig();
	LoggerConfig(SRI::String loggerName, tLogLevel level, AppenderOptions options);
	virtual ~LoggerConfig();

	LoggerConfig(const LoggerConfig& c);
	LoggerConfig& operator=(const LoggerConfig& c);

	bool operator==(const LoggerConfig& c) const;

	void vSetLoggerName(SRI::String name);
	void vSetLogLevel(tLogLevel level);
	void vSetAppenderOptions(AppenderOptions options);

	SRI::String szGetLoggerName();
	tLogLevel eGetLogLevel();
	AppenderOptions tGetAppenderOptions();

	bool bLogLevelSet();
	bool bAppenderOptionsSet();

private:
	SRI::String m_szLoggerName; 
	tLogLevel m_eLogLevel;
	AppenderOptions m_tAppenderOptions;

	bool m_bLogLevelSet;
	bool m_bAppenderOptionsSet;
};

INST_LOG_TEMPL SRI::List<LoggerConfig>;


//====================================================================================
//  Logger Manager
//====================================================================================
// create an instance for dll export
INST_LOG_TEMPL SRI::List<Logger*>;
INST_LOG_TEMPL SRI::Ptr<LoggerManager>;
INST_LOG_TEMPL SRI::Ref<LoggerManager>;
INST_LOG_TEMPL SRI::Ptr<LogAppender>;
INST_LOG_TEMPL SRI::Ref<LogAppender>;

class LOGGER_API LoggerManager{
	friend class Logger;

private:
	SRI::List<Logger*> m_lLoggers;

	LoggerManager();
	LoggerManager(const LoggerManager& c);
	LoggerManager& operator=(const LoggerManager& c);

	static SRI::Ref<LoggerManager> m_ptInstance;
	//static SRI::Ref<LoggerManager> m_ptBaseRef;


	// Central Appenders
	Ref<LogAppender> m_ptLogConsoleAppender;
	Ref<LogAppender> m_ptLogFileAppender;
	Ref<LogAppender> m_ptLogStringAppender;


	SRI::List<LoggerConfig> m_lLoggerConfig;
	bool m_bConfigLoaded;


public:
	virtual ~LoggerManager();

	/** This function returns a LogAppender based on the configuration given in the options.
	* All appenders should be created and destroyed through this interface*/
	Ref<LogAppender> ptGetLogAppender(const AppenderOptions& options);
	bool bIsConfigFileLoaded();
	int iConfigure(Logger* logger);

	SRI::List<Ref<Logger>> ptlGetLoggers(SRI::String name);
	int iSetAppender(SRI::String loggerName, Ref<LogAppender> app, const AppenderOptions& options); // = AppenderOptions(app->eGetAppenderType());


#ifdef LOGGER_XML_CONFIG
	int iAddConfig(LoggerConfig& config);
	int iLoadXmlConfiguration(SRI::String fileName);
	int iLoadXmlConfigurationFile(SRI::String fileName);
	int iParseXmlConfigNode(TiXmlElement* elem, LoggerConfig& config);
#endif


	static SRI::Ref<LoggerManager> ptGetInstance();

	void vSetUseManagerConfig(bool useConf = true);

	/** Sets the logLevel of an existing Logger, identified by name*/
	int iSetLogLevel(const char* loggerName, tLogLevel level);
	int iSetLogLevel(SRI::String loggerName, tLogLevel level);

	/** Registers a logger at the central manager for configuration
	* \returns -1 in case a logger with the same name has already been registered. In
	*           this case the logger is not registered.
	* \returns 0 in case of success.
	*/
	int iRegisterLogger(Logger* logger);
	int iUnregisterLogger(const Logger* logger);
	int iUnregisterLogger(const SRI::String& c);
	void vUnregisterAll();
	const SRI::List<Logger*>& lGetLoggers();

};

//=======================================================================  

/** constant accessible default appender options*/
LOGGER_API extern SRI::LoggerConfig DefaultLoggerConfig;


/** The Logger provides a flexible logging mechanism. The logging system bases
* on local loggers. Each loggger has a logLevel that determins the messages
* that are logged. There are six logLevel available: 
*	LOG_DEBUG, LOG_INFO, LOG_WARN, LOG_ERROR, LOG_CRITICAL, LOG_FATAL.
* For every level there is a logfunction available that take an SRI::String or
* a c type format string as parameters. 
* Where the messages are logged is determined by the current LogAppender. 
* Currently there are a console appender and file appender available.
* In order to centralize logging use the LoggerManger facilities.
*/

class LOGGER_API Logger{
	friend class LoggerManager;
protected:

	tLogLevel m_eLogLevel;
	SRI::String m_szLoggerName;

	AppenderOptions m_tAppenderOptions;
	Ref<LogAppender> m_ptLogAppender;
	SRI::Ref<LoggerManager> m_ptLoggerManager;

	SRI::String szCreateTime() const;
	SRI::String szFormatMessage(tLogLevel level, SRI::String msg) const;

	int iInit(SRI::String loggerName, tLogLevel logLevel);
	void vSetLoggerManager(SRI::Ref<LoggerManager> manager);// only to be called by the loggerManager
	//Ref<Logger> m_ptSelfRef;

public:
	/** Creates a new Logger with logger name and a given log appender.
	* \param loggerName specifies the logger name that is used for logging and configuration
	* \param logLevel determins the logLevel of the Logger
	* \param options please see tAppenderType for a list of pssible values. This consturctor give a 
	* convenient form to specify a logger that options central logging facilities given by
	* the LoggerManager. E.g. if you want to log to a file see LogFileAppender. If you create
	* a local fileAppender then make sure that the LogFileAppender::DefaultFileName holds a
	* valid value.
	*/
	Logger(SRI::String loggerName, tLogLevel logLevel = DefaultLoggerConfig.eGetLogLevel(), const AppenderOptions& options = DefaultLoggerConfig.tGetAppenderOptions());
	
	/** Creates a new Logger with logger name and a given log appender.
	* \param loggerName specifies the logger name that is used for logging and configuration
	* \param appender Log appender
	* \param options must reflect the type of appender and its parameters
	* \param logLevel The default log level of the logger
	*/
	Logger(SRI::String loggerName, Ref<LogAppender> appender, const AppenderOptions& options, tLogLevel logLevel = DefaultLoggerConfig.eGetLogLevel());
	
	/** Creates a new Logger on the base of the given one.
	* It sets the same log level and creates a copy of the appender*/
	Logger(const Logger& c);
	/** Creates a new logger based on the given one. It sets the same loglevel and
	* creates a copy of the appender.*/
	virtual Logger& operator=(const Logger& c);

	virtual ~Logger(void);
	
	void vSetName(SRI::String name);
	SRI::String szGetName() const { return m_szLoggerName;}

	virtual void vSetLogLevel(tLogLevel level){m_eLogLevel = level;}
	virtual tLogLevel eGetLogLevel() const {return m_eLogLevel;}
	virtual void vSetLogLelvel(tLogLevel level){m_eLogLevel = level;}
	virtual void vSetLogAppender(Ref<LogAppender> appender, const AppenderOptions& options);

	virtual Ref<LogAppender> tGetAppender();

	virtual void log(tLogLevel level, SRI::String msg);
	virtual void log(tLogLevel level, const char* format, ...);
	virtual void log(tLogLevel level, const char* format, va_list argPtr);
	

	virtual void debug(SRI::String msg);
	virtual void info(SRI::String msg);
	virtual void warn(SRI::String msg);
	virtual void error(SRI::String msg);
	virtual void critical(SRI::String msg);
	virtual void fatal(SRI::String msg);
	
	virtual void debug(const char* format, ...);
	virtual void info(const char* format, ...);
	virtual void warn(const char* format, ...);
	virtual void error(const char* format, ...);
	virtual void critical(const char* format, ...);
	virtual void fatal(const char* format, ...);

	/** Functions to allow loggers to be used in const functions */
	virtual void log(tLogLevel level, const char* format, va_list argPtr) const;
	virtual void debug(const char* format, ...) const;
	virtual void info(const char* format, ...) const;
	virtual void warn(const char* format, ...) const;
	virtual void error(const char* format, ...) const;
	virtual void critical(const char* format, ...) const;
	virtual void fatal(const char* format, ...) const;
};


LOGGER_API void vCheckLogger(Logger* logger, const char* file, double line);

#define CHK_LOGGER(x) vCheckLogger(x, __FILE__, __LINE__)





} // end namespace SRI


#endif