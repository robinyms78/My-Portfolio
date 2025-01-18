#ifndef SRI_AGENT_LIB
#define SRI_AGENT_LIB

#ifdef WIN32

#include <SDKDDKVer.h>
#define WIN32_LEAN_AND_MEAN             // Selten verwendete Teile der Windows-Header nicht einbinden.
// Windows-Headerdateien:
#include <windows.h>


#ifdef SRIAGENT_EXPORTS  
#define AGENT_API __declspec(dllexport)
#ifndef AGENT_EXPIMP_TEMPLATE
#define AGENT_EXPIMP_TEMPLATE
#endif
#else
#define AGENT_API __declspec(dllimport)
#ifndef AGENT_EXPIMP_TEMPLATE
#define AGENT_EXPIMP_TEMPLATE extern
#endif
#pragma warning ( disable : 4231 )
#endif
#define INST_AGENT_TEMPL AGENT_EXPIMP_TEMPLATE template class AGENT_API

#else   // here the non windows part
#define AGENT_API
#ifndef AGENT_EXPIMP_TEMPLATE
#define AGENT_EXPIMP_TEMPLATE
#endif
#define INST_AGENT_TEMPL template class
#endif



#endif // header already included
	