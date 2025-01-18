#ifndef SRI_REGISTRY_PLUGIN_HANDLE
#define SRI_REGISTRY_PLUGIN_HANDLE


#include "SRI/SRIEngine/SRIPluginHandle.h"
#include "SRI/SRIEngine/SRIRegistryPlugin.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/SRIRegistry.h"
#include "SRI/SRIEngine/SRIRegistryHandle.h"

namespace SRI{

INST_SRI_E_TEMPL SRI::Ref<SRI::ComponentFactory>;

class SRI_E_API RegistryPluginHandle: public SRIPluginHandle{

private:
	Logger m_tLog;

	SRIRegistryPluginInitFnc m_Init_cb;
	SRIRegistryPluginFreeFnc m_Free_cb;
	FactoryMap* m_pmFactories;
	RegistryHandle m_tRegistryHandle;
	FactoryMap m_mFactories;

protected:
	/** After copy the Plugin needs to bee initialized with a new Registry
	* plugin needs to be added to the plugin list etc.*/
	RegistryPluginHandle(const RegistryPluginHandle& c);
	RegistryPluginHandle operator=(const RegistryPluginHandle& c);

	SRI::String m_szFactoryMapName;
	SRI::Ref<SRI::ComponentFactory> m_ptEmptyFactory;
	SRI::FactoryMap m_mEmptyMap;

public:
	RegistryPluginHandle();
	virtual ~RegistryPluginHandle();
	
	virtual SRIPluginHandle* ptClone();

	virtual int iLoadLibrary( SRI::String pluginName, SRI::String filePath = "",SRI::String config="");
	virtual int iInitPlugin(SRI::RegistryHandle registryHandle);
	virtual void vFinalizePlugin();

	virtual SRI::Ref<SRI::ComponentFactory> ptGetFactoryByName(const SRI::String name);
	virtual SRI::FactoryMap& mGetFactories();

	virtual SRI::String szGetName();

};



} //end namespace



#endif