#ifndef LUA_PLUGINLOADER_H
#define LUA_PLUGINLOADER_H

#include "SRI/LuaSRIEngine/LuaSRIEngineLib.h"

#include "SRI/SRIEngine/SRIEngine.h"
#include "lua.hpp"
#include "SRI/SRIExtensions/LuaClassHandle.h"
#include "SRI/SRIEngine/SRIRegistryPluginLoader.h"




namespace SRI{

/** The LuaSRIEngine is a wrapper that exposes the SRIEnginge functionality to LUA
*/
namespace LuaPluginLoader{


	int iLoadPlugin(lua_State* L);


	static const struct luaL_reg luaPluginLoaderApi[] = {
		{"loadPlugin", iLoadPlugin},
		{NULL, NULL} /*sentinel*/
	};


	LUA_CLASSHANDLE_DEF(RegistryPluginLoader)


	LUA_SRIENGINE_API int iCreateRegistryPluginLoader(lua_State* L);
	
	static const struct luaL_reg SRIPluginLoaderApi[] = {
		{"createRegistryPluginLoader", iCreateRegistryPluginLoader},
		{NULL, NULL} /*sentinel*/
	};

	}// end LuaPluginLoader namespace
}// end sri namespace

extern "C" {
	LUA_SRIENGINE_API int luaopen_RegistryPluginLoader(lua_State* L);
}



#endif