#ifndef LUA_OUTPUTPORT_H
#define LUA_OUTPUTPORT_H


#ifdef LUACOMPONENT_EXPORTS
#define LUA_PACKAGE_API __declspec(dllexport)
#else
#define LUA_PACKAGE_API __declspec(dllimport)
#endif

#include "Logger.h"
#include "SRIRef.h"
#include "OutputPort.h"

extern "C"
{
   #include <lua.h>
   #include <lauxlib.h>
   #include <lualib.h>
}


#define LUA_OUTPUTPORT_T "OutputPort"   


namespace SRI{

	class OutputPort;

	namespace LuaOutputPortApi{

		Logger g_tLog("OutputPortApi", SRI::LOG_DEBUG);

		int iCreateOutputPort(lua_State* L, Ref<OutputPort> port);

		/** Expects a LuaOutputPort as first(self) parameter and a string as message
		* It returns an error code (0== SRI_OK in case of success)*/
		int iSend(lua_State* L);

		int iCheckOutputPort(lua_State* L, int idx);
		Ref<OutputPort> tGetOutputPort(lua_State* L, int idx);

		static const struct luaL_reg OutputPortObjApi[] = {
			{"send", iSend},
			{NULL, NULL}
		};

		static const struct luaL_reg OutputPortApi[] = {
			{NULL, NULL}
		};
	}
}

extern "C" {
	LUA_PACKAGE_API int luaopen_LuaOutputPort(lua_State* L);
}



#endif