#ifndef SRI_COMPONENT_FACTORY_H
#define SRI_COMPONENT_FACTORY_H

#include "SRI/SRIGlobals.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/ComponentDefinition.h"

namespace SRI{

class Component;
class RegistryHandle;
class SRIRegistry;
class SRIRegistryStub;

//INST_SRI_E_TEMPL SRI::Ref<SRI::SRIRegistry>;

/** The componentFacotry is modeled as an independent service. They can 
* be instantiated independently and registered at a registry. For now,
* a factory can only be registered at one registry at a time. 
*/


class SRI_E_API ComponentFactory{
	friend class SRI::RegistryHandle;
	friend class SRI::SRIRegistry;
	friend class SRI::SRIRegistryStub;

private:

	Logger m_tLog;


protected:
	SRI::String m_szComponentType;
	SRI::String m_szName;
	SRI::String m_szConfig;

	

	//Soon be replaced by RegistryHandle
	//SRI::Ref<SRIRegistry> m_ptSRIRegistry;   // Initialized with global registry (not possible to register at multiple registries)
	RegistryHandle* m_ptRegistryHandle;
	//TODO: better solution that uses Refs?
	
	int iSetRegistryHandle(const RegistryHandle* handle);

public:
	ComponentFactory(const ComponentFactory& c);
	ComponentFactory& operator=(const ComponentFactory& c);
	ComponentFactory(SRI::String factName, SRI::String config = "");
	virtual ~ComponentFactory();

	virtual SRI::Ref<SRI::Component> ptCreateComponent(SRI::String name, SRI::String config = "");

	/** sets the type of the components are being produced */
	virtual void vSetComponentType(SRI::String type);
	virtual void vSetConfig(SRI::String config);
	
	virtual int iSetName(SRI::String name);
	virtual SRI::String szGetName() const;
	virtual SRI::String szGetComponentType() const;
	virtual SRI::String szGetConfig() const;
	virtual SRI::RegistryHandle* ptGetRegistryHandle() const;


	virtual ComponentDefinition tGetComponentDefinition(SRI::String config); // holds a definition (contract) of what type of components will be produced
};


} // end namespace sri


#endif SRI_COMPONENT_FACTORY_H
