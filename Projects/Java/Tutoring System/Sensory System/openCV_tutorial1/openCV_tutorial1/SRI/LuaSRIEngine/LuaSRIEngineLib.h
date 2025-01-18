#ifndef LUA_SRI_ENGINE_LIB_H
#define LUA_SRI_ENGINE_LIB_H

#ifdef LUASRIENGINE_EXPORTS
#define LUA_SRIENGINE_API __declspec(dllexport)
#else
#define LUA_SRIENGINE_API __declspec(dllimport)
#endif

#include "SRI/Logger/Logger.h"
#include "lua.hpp"

namespace SRI{

	namespace LuaSRIEngine{
	
		//extern SRI::Logger g_SRILuaLog;

	}// end LuaSRIEngine namespace
}


extern "C" {
	LUA_SRIENGINE_API int luaopen_LuaSRIEngine(lua_State* L);
}


#endif