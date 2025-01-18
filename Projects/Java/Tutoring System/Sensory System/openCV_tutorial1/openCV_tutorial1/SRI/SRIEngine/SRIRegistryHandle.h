#ifndef SRI_REGISTRY_HANDLE_H
#define SRI_REGISTRY_HANDLE_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIPtr.h"

namespace SRI{

class SRIRegistry;
	
INST_SRI_E_TEMPL SRI::Ptr<SRI::SRIRegistry>;
INST_SRI_E_TEMPL SRI::Ref<SRI::SRIRegistry>;

class SRI_E_API RegistryHandle{
	friend class SRI::SRIRegistry;

private:
	Logger m_tLog;
	Ref<SRIRegistry> m_ptRegistry;
	SRI::String m_szConfig;

	int iGetRegistry(SRI::String config);

public:
	RegistryHandle(SRI::String config = "");
	RegistryHandle(Ref<SRIRegistry> registry);
	virtual ~RegistryHandle();
	RegistryHandle(const RegistryHandle& c);
	RegistryHandle& operator=(const RegistryHandle&c);

	virtual bool bIsValid();
	virtual int iUnregisterComponentFactory(SRI::String name);
	virtual bool bIsRegistered(SRI::String name);
	
};

}


#endif