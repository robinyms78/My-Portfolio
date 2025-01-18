#ifndef SRI_CONFIG_READER_H
#define SRI_CONFIG_READER_H

#include "SRI/ConfigReader/ConfigReaderLib.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigParser.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIRef.h"

namespace SRI{

/** Config information can be given either directly or through a 
* config file. 
* In case a config string is given, the format has to be specified:
* @xml: <example var=3>c:\file.txt</example>
* The @ sign and everything that follows until the : are truncated before
* the actual parse. 
*
* @lua: var = 3; file="c:\\file.txt";
*
* In case it is a fileName the ending of the file is taken to determine 
* the type of configuration:
* c:\exampleConf.xml
* c:\exampleConf.lua
*/

class CR_API ConfigReader{

private:
	Logger m_tLog;
	ConfigParser* m_ptParser;

public:
	ConfigReader();
	ConfigReader(const SRI::String& config);
	ConfigReader(const ConfigReader& c);
	ConfigReader& operator=(const ConfigReader& c);
	virtual ~ConfigReader();

	/** This version tries to parse if the config is lua or xml.
	* Therefor it should start with @lua: or @xml:   directly followed
	* by the actual config string 
	* If this prefix is missing, it assumed that a filename is given and then
	* it takes the file suffix to decide which parser to use.
	*/
	virtual int iReadConfig(const SRI::String& config);

	virtual int iReadLuaConfig(const SRI::String luaConfig);
	virtual int iReadLuaFile(const SRI::String luaFileName);

	virtual int iReadXmlConfig(const SRI::String xmlConfig);
	virtual int iReadXmlConfigFile(const SRI::String xmlFileName);

	virtual bool bHasParameter(const SRI::String& configPath);

	//int iGetConfigNodes(const SRI::String& configPath, ConfigNode& node);

	virtual bool bGetBoolValue(const SRI::String& configPath);
	virtual int iGetIntValue(const SRI::String& configPath);
	virtual double dGetDoubleValue(const SRI::String& configPath);
	virtual SRI::String szGetStringValue(const SRI::String& configPath);
	
	virtual SRI::Ref<SRI::ConfigNode> ptGetNode(const SRI::String& configPath); 
	virtual SRI::Ref<SRI::ConfigNodeSet> ptGetNodeSet(const SRI::String& configPath);

};

}



#endif