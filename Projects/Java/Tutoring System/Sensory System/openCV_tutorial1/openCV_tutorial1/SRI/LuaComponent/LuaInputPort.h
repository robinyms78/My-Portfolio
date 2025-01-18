#ifndef LUA_INPUTPORT_H
#define LUA_INTPUTPORT_H


#ifdef LUACOMPONENT_EXPORTS
#define LUA_PACKAGE_API __declspec(dllexport)
#else
#define LUA_PACKAGE_API __declspec(dllimport)
#endif


#include "Logger.h"
#include "SRIRef.h"
#include "InputPort.h"

extern "C"
{
   #include <lua.h>
   #include <lauxlib.h>
   #include <lualib.h>
}


#define LUA_INPUTPORT_T "InputPort"   


namespace SRI{
	namespace LuaInputPortApi{
		Logger g_tLog("InputPortApi", SRI::LOG_DEBUG);
		int iReceive(lua_State* L);

		int iCreateInputPort(lua_State* L, InputPort* port);

		int iCheckInputPort(lua_State* L, int idx);
		Ref<InputPort> tGetInputPort(lua_State* L, int idx);

		static const struct luaL_reg InputPortObjApi[] = {
			{"receive", iReceive},
			{NULL, NULL}
		};

		static const struct luaL_reg InputPortApi[] = {
			{NULL, NULL}
		};
	}
}

extern "C" {
	LUA_PACKAGE_API int luaopen_LuaInputPort(lua_State* L);
}



#endif