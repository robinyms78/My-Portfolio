

#include "SRI.h"
#include "SRIRegistryPlugin.h"


BOOL APIENTRY DllMain( HMODULE hModule,
					   DWORD  ul_reason_for_call,
					   LPVOID lpReserved
					 )
{
	switch (ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
	case DLL_THREAD_ATTACH:
	case DLL_THREAD_DETACH:
	case DLL_PROCESS_DETACH:
		break;
	}
	return TRUE;
}


SRI::Logger logger("Camera", SRI::LOG_DEBUG);

SRI_PLUGIN_API SRI::FactoryMap Factories;


SRI_PLUGIN_API int InitSRIRegistryPlugin(SRI::RegistryHandle registryHandle, SRI::String pluginPath, SRI::String config){
	int res = SRI::SRI_OK;
	//Factories.clear();
	//Factories["DemoReactiveComponentFactory"] = SRI::Ref<SRI::ComponentFactory>(new SRI::DemoReactiveComponentFactory());
	logger.debug("Plugin was loaded\n");
	return res;
}



SRI_PLUGIN_API void FreeSRIRegistryPlugin(SRI::RegistryHandle registryHandle, SRI::String pluginPath, SRI::String config){

	logger.debug("Plugin was released\n");
}
