
#ifndef SRI_REGISTRY_FACTORY_PLUGIN_LOADER
#define SRI_REGISTRY_FACTORY_PLUGIN_LOADER

#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/SRIRegistryPluginHandle.h"


namespace SRI{

INST_SRI_E_TEMPL SRI::Map<SRI::String, SRI::RegistryPluginHandle*>;
INST_SRI_E_TEMPL SRI::MapIterator<SRI::String, SRI::RegistryPluginHandle*>;


/** This class is a helper class for the Registry. It manages locally the lifetime of plugins*/
class SRI_E_API RegistryPluginLoader{

private:
	Logger m_tLog;
	SRI::Map<SRI::String, RegistryPluginHandle*> m_mPlugins;
	Ref<SRIRegistry> m_ptRegistry;

	SRI::String m_szConfig;

	virtual int iGetRegistry(SRI::String config);

	virtual int iRegisterFactories(RegistryPluginHandle* plug);
	virtual int iUnregisterFactories(RegistryPluginHandle* plug);

public:
	RegistryPluginLoader(SRI::String config = "");
	virtual ~RegistryPluginLoader();
	RegistryPluginLoader(const RegistryPluginLoader& c);
	RegistryPluginLoader& operator=(const RegistryPluginLoader& c);


	virtual int iLoadPlugin(SRI::String pluginName, SRI::String filePath = "",  SRI::String config = "");
	/** Unregisters a plugin from the plugin list (also see vReleasePlugin())*/
	virtual void vClosePlugin(SRI::String pluginName);

	//// The entire plugin is given as a script file
	//virtual int iLoadLuaPlugin(SRI::String pluginName, SRI::String filePath = "",  SRI::String config = "");

	/** Unregisteres the plugin; calls ReleasePlugin and closes the enclosing library */
	virtual void vReleasePlugin(SRI::String pluginName);
	virtual void vFinalizeAllPlugins();

};


}


#endif