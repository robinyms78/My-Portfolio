#ifndef	SRI_CONFIG_PARSER_LIB
#define SRI_CONFIG_PARSER_LIB

#ifdef WIN32

#include <SDKDDKVer.h>
#define WIN32_LEAN_AND_MEAN             // Selten verwendete Teile der Windows-Header nicht einbinden.
// Windows-Headerdateien:
#include <windows.h>
//ConfigReader exports CR

#ifdef CONFIGREADER_EXPORTS  
#define CR_API __declspec(dllexport)
#ifndef EXPIMP_TEMPLATE
#define EXPIMP_TEMPLATE
#endif
#else
#define CR_API __declspec(dllimport)
#ifndef EXPIMP_TEMPLATE
#define EXPIMP_TEMPLATE extern
#endif
#pragma warning ( disable : 4231 )
#endif
#define INST_CR_TEMPL EXPIMP_TEMPLATE template class CR_API

#else   // here the non windows part
#define CR_API
#ifndef EXPIMP_TEMPLATE
#define EXPIMP_TEMPLATE
#endif
#define INST_CR_TEMPL template class
#endif


#endif