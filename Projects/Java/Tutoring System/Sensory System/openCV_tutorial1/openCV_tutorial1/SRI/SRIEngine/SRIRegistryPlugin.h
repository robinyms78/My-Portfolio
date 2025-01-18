
#ifndef SRI_REGISTRY_PLUGIN_H
#define SRI_REGISTRY_PLUGIN_H

#include "SRI/SRIEngine/SRIPlugin.h"

#define SRI_REGISTRY_PLUGIN_INIT_FNC_NAME "InitSRIRegistryPlugin"
#define SRI_REGISTRY_PLUGIN_FREE_FNC_NAME "FreeSRIRegistryPlugin"
#define SRI_REGISTRY_PLUGIN_FACTORY_DATA_NAME "Factories"
#define SRI_REGISTRY_PLUGIN_EXTENSION ".dll"

#include "SRI/SRIGlobals.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIEngine/ComponentFactory.h"
#include "SRI/SRIEngine/SRIRegistry.h"
#include "SRI/SRIEngine/SRIRegistryHandle.h"

namespace SRI{

class SRIRegistry;


typedef SRI::Map<SRI::String,SRI::Ref<SRI::ComponentFactory>> FactoryMap;
typedef SRI::MapIterator<SRI::String,SRI::Ref<SRI::ComponentFactory>> FactoryMapIterator;
typedef SRI::ConstMapIterator<SRI::String,SRI::Ref<SRI::ComponentFactory>> ConstFactoryMapIterator;


typedef int (*SRIRegistryPluginInitFnc)(SRI::RegistryHandle registryHandle, SRI::String pluginPath, SRI::String config);
typedef void (*SRIRegistryPluginFreeFnc)(SRI::RegistryHandle registryHandle, SRI::String pluginPath, SRI::String config);


// OLD Interface below
//
///** The plugin may register component factories. The plugin keeps a reference to the factories and unregisters them
//* when they are not needed any more */
//
//typedef int (*SRIRegistryPluginInitFnc)(SRI::Ref<SRI::SRIRegistry> registry, SRI::String pluginName, SRI::String pluginPath, SRI::String config);
//typedef void (*SRIRegistryPluginFreeFnc)(SRI::Ref<SRI::SRIRegistry> registry, SRI::String pluginName, SRI::String pluginPath, SRI::String config);
//
//TODO: the above functionality may be changed with the introduction of ComponentPlugins


}



#endif
