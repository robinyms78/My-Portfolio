#ifndef SRI_LUA_UTIL_H
#define SRI_LUA_UTIL_H

#include "SRI/SRIGlobals.h"
#include "SRI_ExtensionsLib.h"
#include "SRI/Logger/Logger.h"

#ifdef SRI_USE_LUA
#include <lua.hpp>
//extern "C"
//{
//   #include <lua.h>
//   #include <lauxlib.h>
//   #include <lualib.h>
//}

#endif

namespace SRI{


#ifdef SRI_USE_LUA	
	SRI_EXT_API SRIErrorCode luaErrToSRIErr(int luaErr);

	/** Expects that a lua error message (string) is on top of the stack.
	* If so, the message will be added to the logging message */
	SRI_EXT_API void vLogLuaError(lua_State* L, Logger& log, const char* fmt, ...);
#endif


}//end namespace SRI


#endif