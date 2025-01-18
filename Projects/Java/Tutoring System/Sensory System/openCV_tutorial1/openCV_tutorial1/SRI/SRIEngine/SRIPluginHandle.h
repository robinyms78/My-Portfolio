#ifndef SRI_PLUGIN_HANDLE
#define SRI_PLUGIN_HANDLE


#include "SRI/Logger/Logger.h"
#include "SRI/SRIGlobals.h"
#include "SRI/SRIEngine/SRIPlugin.h"
#include "SRI/SRIEngine/LibHandle.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/ConfigReader/ConfigNode.h"

namespace SRI{

INST_SRI_E_TEMPL SRI::Ref<LibHandle>;

/** Main class that keeps track of open handles to plugins*/
class SRI_E_API SRIPluginHandle{

private:
	Logger m_tLog;

protected:	
	Ref<LibHandle> m_ptLibHandle;

	SRI::String m_szFilePath;
	SRI::String m_szPluginName;
	SRI::String m_szConfig;

	SRI::String m_szInitFuncName;
	SRI::String m_szFreeFuncName;
	SRI::String m_szPluginExtension;


	SRIPluginHandle(const SRIPluginHandle& c);
	SRIPluginHandle operator=(const SRIPluginHandle& c);


	virtual int iInitPlugin();
	virtual void vFinalizePlugin();
	virtual int iLoadLibrary(SRI::String pluginName, SRI::String filePath, SRI::String config);


public:

	SRIPluginHandle();
	virtual ~SRIPluginHandle();
	bool operator==(const SRIPluginHandle& c);

	virtual SRIPluginHandle* ptClone();
	HMODULE hGetHandle();
	virtual void vCloseLibrary();
};

} // end namespace SRI

#endif // SRI_PLUGIN_HANDLE

