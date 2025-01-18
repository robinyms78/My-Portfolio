

#ifndef	SRI_ANIMATION_LIB_H
#define SRI_ANIMATION_LIB_H

#ifdef WIN32

#include <SDKDDKVer.h>
#define WIN32_LEAN_AND_MEAN             // Selten verwendete Teile der Windows-Header nicht einbinden.
// Windows-Headerdateien:
#include <windows.h>


#ifdef SRIANIMATION_EXPORTS  
#define SRI_ANIMATION_API __declspec(dllexport)
#ifndef ANIMATION_EXPIMP_TEMPLATE
#define ANIMATION_EXPIMP_TEMPLATE
#endif
#else
#define SRI_ANIMATION_API __declspec(dllimport)
#ifndef ANIMATION_EXPIMP_TEMPLATE
#define ANIMATION_EXPIMP_TEMPLATE extern
#endif
#pragma warning ( disable : 4231 )
#endif
#define INST_SRI_ANIMATION_TEMPL ANIMATION_EXPIMP_TEMPLATE template class SRI_ANIMATION_API

#else   // here the non windows part
#define SRI_ANIMATION_API
#ifndef ANIMATION_EXPIMP_TEMPLATE
#define ANIMATION_EXPIMP_TEMPLATE
#endif
#define INST_SRI_ANIMATION_TEMPL template class
#endif


#ifdef SRI_USE_LUA

struct lua_State;

extern "C" {
	int luaopen_SRIAnimation(lua_State* L);
}


#endif

#endif // header already included
	