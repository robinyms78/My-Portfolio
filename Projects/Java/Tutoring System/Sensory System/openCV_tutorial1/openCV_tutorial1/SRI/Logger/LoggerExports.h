#ifndef LOGGER_EXPORTS_H
#define LOGGER_EXPORTS_H


#ifdef WIN32

#ifdef LOGGER_EXPORTS
#define LOGGER_API __declspec(dllexport)
#define EXPIMP_LOG_TEMPLATE
#else
#define LOGGER_API __declspec(dllimport)
#define EXPIMP_LOG_TEMPLATE extern
#endif
#define INST_LOG_TEMPL EXPIMP_LOG_TEMPLATE template class LOGGER_API

#else // Win32
#define LOGGER_API
#define EXPIMP_LOG_TEMPLATE
#define INST_LOG_TEMPL template class

#endif // WIN32






#endif // LOGGER_EXPORTS_H