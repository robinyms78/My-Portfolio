#ifndef LUA_CONSOLE_PLUGIN_H
#define LUA_CONSOLE_PLUGIN_H

#include "SRIRegistryPlugin.h"
#include "Logger.h"

#include "LuaConsoleFactory.h"


namespace LuaConsolePlugin{

//
extern "C" SRI_PLUGIN_API int InitSRIRegistryPlugin(SRI::Ref<SRI::SRIRegistry> registry, SRI::String pluginName, SRI::String pluginPath, SRI::String config);

//SRI_PLUGIN_API 
extern "C"  SRI_PLUGIN_API void FreeSRIRegistryPlugin(SRI::Ref<SRI::SRIRegistry> registry, SRI::String pluginName, SRI::String pluginPath, SRI::String config);

} // end namespace

#endif