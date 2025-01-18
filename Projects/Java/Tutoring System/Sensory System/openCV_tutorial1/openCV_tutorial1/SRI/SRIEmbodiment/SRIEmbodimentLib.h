#ifndef SRI_EMBODIMENT_LIB
#define SRI_EMBODIMENT_LIB

#ifdef WIN32

#include <SDKDDKVer.h>
#define WIN32_LEAN_AND_MEAN             // Selten verwendete Teile der Windows-Header nicht einbinden.
// Windows-Headerdateien:
#include <windows.h>


#ifdef SRIEMBODIMENT_EXPORTS  
#define EMBODIMENT_API __declspec(dllexport)
#ifndef EMBODIMENT_EXPIMP_TEMPLATE
#define EMBODIMENT_EXPIMP_TEMPLATE
#endif
#else
#define EMBODIMENT_API __declspec(dllimport)
#ifndef EMBODIMENT_EXPIMP_TEMPLATE
#define EMBODIMENT_EXPIMP_TEMPLATE extern
#endif
#pragma warning ( disable : 4231 )
#endif
#define INST_EMBODIMENT_TEMPL EMBODIMENT_EXPIMP_TEMPLATE template class EMBODIMENT_API

#else   // here the non windows part
#define EMBODIMENT_API
#ifndef EMBODIMENT_EXPIMP_TEMPLATE
#define EMBODIMENT_EXPIMP_TEMPLATE
#endif
#define INST_EMBODIMENT_TEMPL template class
#endif



#endif // header already included
	
