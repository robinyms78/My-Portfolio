//#include "RegistryServiceHandler.h"
//
//	SRIRegistry();
//	SRIRegistry(const SRIRegistry& c);
//	SRIRegistry& operator=(const SRIRegistry& c);
//
//	static Logger m_tLog;
//
//	static Ref<SRIRegistry> m_ptInstance;
//	//static Ref<SRIRegistry> m_tBaseRef;
//
//	static int m_iIdNum;
//
//	static bool m_bIsRemote;
//	static SRI::String m_szIp; //ip of real registry
//	static int m_iPort;
//
//	SRI::Map<SRI::String, Ref<ComponentFactory>> m_mComponentFactories;
//	//SRI::Map<SRI::String, SRIEngine*> m_mEngines;
//	
//	/** This function is used internally to assign an ID to a new component.*/
//	SRI::String szCreateComponentID();
//
//public:
//	//static SRIRegistry* ptGetInstance();
//	static Ref<SRIRegistry> ptGetInstance();
//	static int m_iRefCount;
//
//	virtual ~SRIRegistry();
//
//	/** The function registers a component with the registry. 
//	* The base class of the factory makes sure that it is unregistered in the destructor.
//	* The memory is managed by smart references. All factories that are present when the factory goes out 
//	* of scope are deleted. 
//	*/
//	virtual int iRegisterComponentFactory(Ref<ComponentFactory> c);
//ADD TO MYSELF FIRST, THEN REGISTER A FACTORY STUB WITH THE MAIN REGISTRY
//	/** Removes the given factory from the list of available factories*/
//	virtual int iUnregisterComponentFactory(Ref<ComponentFactory> c);
//ASSUMES THAT I WILL NEVER SEE STUBS, REASONABLE ASSUMPTION
//	virtual int iUnregisterComponentFactory(SRI::String name);
// sends the command to shutdown if local is stub, otherwise shuts down and informs the boss
//	/** Thin unregisters and delets all factories*/
//	virtual void vUnregisterAllComponentFactories();
//same as above
//checks main, easier to reason
//	virtual bool bIsRegistered(Ref<ComponentFactory> c);
//	virtual bool bIsRegistered(SRI::String name);
//	/** returns the number of factories that could produce the given type */
// simply send to main registry because main registry has overview knowledge
//	virtual int iFactoriesWithType(SRI::String type);
//
//
//	virtual SRI::Map<SRI::String, Ref<ComponentFactory>>& tGetComponentFactories();
//
//	/**
//	* \param typeId Type of ComponentFactory
//	* \returns A reference to the ComponentFactory registerd with the given typeId if it exists, otherwise NULL
//	*/
// if local returns me
// otherwise, connects or directly, or uses relay?
//	virtual Ref<ComponentFactory> ptGetComponentFactory(SRI::String typeId, SRI::String selectionCriteria = "");
//	virtual Ref<ComponentFactory> ptGetComponentFactoryByName(SRI::String name);
//
//	//virtual int iRegisterEngine(SRIEngine* engine);
//	//virtual int iUnregisterEngine(SRIEngine* engine);
//	//SRIEngine* ptGetEngine(SRI::String name);
//
//	static void vMakeRemote(const SRI::String& ip, int port); 
//};
//
//
//
//
//
////
////
////template<> class SRIRef<SRI::SRIRegistry> {
////private:
////	SRI::SRIRegistry* m_ptRegistry;
////public:
////	SRIRef(): m_ptRegistry(NULL){};
////	
////	SRIRef(SRI::SRIRegistry* reg): m_ptRegistry(reg){};
////	
////	virtual ~SRIRef(){
////		if (m_ptRegistry != NULL){
////			SRI::SRIRegistry::vReleaseInstance();
////		}
////	}
////
////	SRIRegistry& operator*(){
////		return *m_ptRegistry;
////	}
////
////	SRIRegistry* operator->(){
////		return m_ptRegistry;
////	}
////
////	bool operator==(const SRIRef<SRIRegistry>& c){
////		return m_ptRegistry == c.m_ptRegistry;
////	}
////
////	bool operator !=(const SRIRef<SRIRegistry>& c){
////		return !(*this == c);
////	}
////
////	bool isValid() const{
////		return (m_ptRegistry != NULL);
////	}
////
////};
//
//
//
//
//
//} // end namespace 
//#endif




#ifndef SRI_REGISTRY_STUB_H
#define SRI_REGISTRY_STUB_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/StubTemplate.h"
#include "SRI/SRIEngine/SRIRegistry.h"

namespace SRI{

class ComponentFactory;

/// An SRIRegistryStub represents of the remote SRIRegistry, allowing remote Components and ComponentFactories access to the services of the central registry.
/** SRIRegistryStubs are identical in functionality to an SRIRegistry, save for two important 
	differences:
	<ol>
	<li>An SRIRegistry maintains at all times a complete record of and access to all available ComponentFactories (local or remote); SRIRegistryStubs only maintain a record</li>
	<li></li>
	</ol>
*/ 

class SRI_E_API SRIRegistryStub: public SRIRegistry {

friend class SRIRegistry;
	
private:
	Logger m_tLog;
	StubTemplate* m_ptStubTemplate;
	SRI::String m_szPeerIp;
	int m_iPortNo;
	

	SRIRegistryStub(const SRI::String& ip, int port);
	//SRIRegistry(const SRIRegistry& c); //TODO do copy and assignment make sense?
	//SRIRegistry& operator=(const SRIRegistry& c);

	//static Ptr<SRIRegistry> m_ptInstance;
	//static Ref<SRIRegistry> m_tBaseRef;

	//static int m_iIdNum;





protected:
	virtual SRI::String szCreateComponentID();

public:

	//static Ref<SRIRegistry> ptGetInstance();
	//static int m_iRefCount;


	virtual ~SRIRegistryStub();

	/** The function registers a component with the registry. 
	* The base class of the factory makes sure that it is unregistered in the destructor.
	* The memory is NOT taken over. All factories that are present when the factory goes out 
	* of scope are deleted. 
	*/
	virtual int iRegisterComponentFactory(Ref<ComponentFactory> c, int port);
	/** Removes the given factory from the list of available factories*/
	virtual int iUnregisterComponentFactory(Ref<ComponentFactory> c);
	virtual int iUnregisterComponentFactory(SRI::String name);
	/** Thin unregisters and delets all local factories*/
	//current does the same thing as the superclass version, so not overridden
	//virtual void vUnregisterAllComponentFactories();
	virtual bool bIsRegistered(Ref<ComponentFactory> c);
	virtual bool bIsRegistered(SRI::String name);
	virtual int iFactoriesWithType(SRI::String type);

	//this currently returns only the local set of ComponentFactories; no need to override
	//virtual SRI::Map<SRI::String, ComponentFactory*>& tGetComponentFactories();

	/**
	* \param typeId 
	* \param selectionCriteria
	* \returns The component registerd with the given name if exists, otherwise NULL
	*/
	virtual Ref<ComponentFactory> ptGetComponentFactory(SRI::String typeId, SRI::String selectionCriteria = "");
	/**
	* \param name Name of the component as given in the registry
	* \returns The component registerd with the given name if exists, otherwise NULL
	*/
	virtual Ref<ComponentFactory> ptGetComponentFactoryByName(SRI::String name);

	//virtual int iRegisterEngine(SRIEngine* engine);
	//virtual int iUnregisterEngine(SRIEngine* engine);
	//SRIEngine* ptGetEngine(SRI::String name);

};


} // end namespace sri


#endif SRI_REGISTRY_STUB_H