

#ifndef	SRI_ENGINE_LIB
#define SRI_ENGINE_LIB

#ifdef WIN32

#include <SDKDDKVer.h>
#define WIN32_LEAN_AND_MEAN             // Selten verwendete Teile der Windows-Header nicht einbinden.
// Windows-Headerdateien:
#include <windows.h>


#ifdef SRIENGINE_EXPORTS  
#define SRI_E_API __declspec(dllexport)
#ifndef EXPIMP_TEMPLATE
#define EXPIMP_TEMPLATE
#endif
#else
#define SRI_E_API __declspec(dllimport)
#ifndef EXPIMP_TEMPLATE
#define EXPIMP_TEMPLATE extern
#endif
#pragma warning ( disable : 4231 )
#endif
#define INST_SRI_E_TEMPL EXPIMP_TEMPLATE template class SRI_E_API

#else   // here the non windows part
#define SRI_E_API
#ifndef EXPIMP_TEMPLATE
#define EXPIMP_TEMPLATE
#endif
#define INST_SRI_E_TEMPL template class
#endif



#endif // header already included
	