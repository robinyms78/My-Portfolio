
#ifndef SRI_ENGINE_PLUGIN_HANDLE_H
#define SRI_ENGINE_PLUGIN_HANDLE_H

#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/Component.h"
#include "SRI/SRIEngine/SRIEngine.h"
#include "SRI/SRIEngine/SRIPluginHandle.h"
#include "SRI/SRIEngine/SRIEnginePlugin.h"

namespace SRI{


class SRIEngine;

class SRI_E_API SRIEnginePluginHandle: public SRIPluginHandle{

private:
	Logger m_tLog;	
	SRI::Ref<SRI::SRIEngine> m_ptEngine;

protected:
	SRIEnginePluginInitFnc m_Init_cb;
	SRIEnginePluginFreeFnc m_Free_cb;

	/** After copy the Plugin needs to bee initialized with a new engine*/
	SRIEnginePluginHandle(const SRIEnginePluginHandle& c);
	SRIEnginePluginHandle operator=(const SRIEnginePluginHandle& c);

public:

	SRIEnginePluginHandle();
	virtual ~SRIEnginePluginHandle();

	virtual SRIPluginHandle* ptClone();

	int iLoadLibrary(SRI::String pluginName, SRI::String pluginPath, SRI::String config);
	/** Calls the init function as defined in the DLL */
	int iInitPlugin(SRI::Ref<SRI::SRIEngine> engine);

	/** Class the finalize function as defined in the loaded DLL*/
	void vFinalizePlugin();

};

} // end namespace SRI

#endif