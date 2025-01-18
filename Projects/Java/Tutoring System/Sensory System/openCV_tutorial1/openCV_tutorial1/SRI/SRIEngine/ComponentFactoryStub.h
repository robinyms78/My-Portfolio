#ifndef SRI_COMPONENT_FACTORY_STUB_H
#define SRI_COMPONENT_FACTORY_STUB_H


#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIEngine/ComponentFactory.h"
#include "SRI/SRIEngine/StubTemplate.h"


namespace SRI{

class Component;

/// A ComponentFactoryStub is a local (to the engine/registry) representation of a remote ComponentFactory
/** ComponentFactoryStubs provide allow the engine/registry to access the services of a 
	remotely running ComponentFactory. When ptCreateComponent is called, the stub communicates
	with its associated ComponentFactoryServer, receives the port number of the newly created
	ComponentServer/ReactiveComponentServer, creates a new ComponentStub/ReactiveComponent stub that
	connects to the newly created servers, and returns the ComponentStub/ReactiveComponent stub to
	the caller of ptCreateComponent.
*/ 

class SRI_E_API ComponentFactoryStub: public ComponentFactory{
	friend class SRIRegistry;

private:
	Logger m_tLog;
	StubTemplate* m_ptStubTemplate;
	SRI::String m_szPeerIp;

	int szCallFunction(SRI::String funcName, const std::vector<SRI::String>& args, Ref<SRI::String> retstring) const;


protected:
	

public:
	ComponentFactoryStub(const ComponentFactoryStub& c);
	ComponentFactoryStub& operator=(const ComponentFactoryStub& c);
	ComponentFactoryStub(SRI::String factName, SRI::String ip, int portNo, SRI::String config = ""); 
	~ComponentFactoryStub();


	SRI::Ref<Component> ptCreateComponent(SRI::String name, SRI::String configFileName = "");
	virtual void vSetComponentType(SRI::String typeId);
	
	//TODO: calling logger in const
	virtual int iSetName(SRI::String name);
	virtual SRI::String szGetName() const;
	virtual SRI::String szGetComponentType() const;
	virtual SRI::String szGetConfig() const;
	//returns handle in same address space. is ok because the registry is a singleton across the entire system
	//so not overridden
	//virtual SRI::RegistryHandle* ptGetRegistryHandle() const;


	virtual ComponentDefinition tGetComponentDefinition(SRI::String config); // holds a definition (contract) of what type of components will be produced
	//***END ComponentFactory


	///Sends shutdown signal to remote server
	void vShutdownRemote();

};


} // end namespace sri


#endif
