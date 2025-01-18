#ifndef SRI_REGISTRY_H
#define SRI_REGISTRY_H

#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIGlobals.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/ComponentFactory.h"

//#include "RegistryServiceHandler.h"

namespace Poco {

	class Thread;

	namespace XML {
		class Document;
	}

	namespace Net{
		class ServerSocket;
		class StreamSocket;
		class SocketReactor;

	
	}
}

namespace SRI{

//template <class ServiceHandler> class RegistrySocketAcceptor;

class OutputPort;
class InputPort;
class Component;
class SRIRegistry;


// create an instance for dll export
INST_SRI_E_TEMPL SRI::Map<SRI::String, Ref<SRI::ComponentFactory>>;
INST_SRI_E_TEMPL SRI::MapIterator<SRI::String, Ref<SRI::ComponentFactory>>;
//INST_SRI_E_TEMPL SRI::Map<SRI::String, SRIEngine*>;
//INST_SRI_E_TEMPL SRI::MapIterator<SRI::String, SRIEngine*>;
INST_SRI_E_TEMPL SRI::Ptr<SRI::SRIRegistry>;
INST_SRI_E_TEMPL SRI::Ref<SRI::SRIRegistry>;


/** The component registry is implemented as a singelton and accessible for all
* components in the SRI architecture
* Plugins can be loaded from DLL.
* The plugins must provide the InitSRIPlugin() and FreeSRIPlugin() functions.
* 
* The lifespan of factories is modeled independent from the lifespan of the registry.
* That means that factories can be services that register or unregister at a registry.
* The base implementation of a factory requires to unregister from a registry.
*
* A registry is global for a namespace. Multiple engines of a namespace can
* use the same registry. 
*/
class  SRI_E_API SRIRegistry{
	friend class SRIEngine; // so that the engine can call the createId function
	friend class SRIEngineStub;
	friend class SRIRegistryServer; //access to szCreateComponentID()


private:
#ifdef SRI_THREADSAFE
	HANDLE m_hRegistryMutex;
#endif


protected:
	SRIRegistry();
	SRIRegistry(const SRIRegistry& c);
	SRIRegistry& operator=(const SRIRegistry& c);

	static Logger m_tLog;

	static Ref<SRIRegistry> m_ptInstance;
	//static Ref<SRIRegistry> m_tBaseRef;

	static int m_iIdNum;

	static bool m_bIsRemote;
	static SRI::String m_szIp; //ip of real registry
	static int m_iPort;

	SRI::Map<SRI::String, Ref<ComponentFactory>> m_mComponentFactories;
	//SRI::Map<SRI::String, SRIEngine*> m_mEngines;
	
	/** This function is used internally to assign an ID to a new component.*/
	virtual SRI::String szCreateComponentID();

public:
	//static SRIRegistry* ptGetInstance();
	static Ref<SRIRegistry> ptGetInstance();
	static int m_iRefCount;

	virtual ~SRIRegistry();


	/** The function registers a component with the registry.
	* The base class of the factory makes sure that it is unregistered in the destructor.
	* The memory is managed by smart references. All factories that are present when the factory goes out 
	* of scope are deleted. 
	*/
	virtual int iRegisterComponentFactory(Ref<ComponentFactory> c);
	/** Removes the given factory from the list of available factories*/
	virtual int iUnregisterComponentFactory(Ref<ComponentFactory> c);
	virtual int iUnregisterComponentFactory(SRI::String name);
	/** Thin unregisters and delets all factories*/
	virtual void vUnregisterAllComponentFactories();
	virtual bool bIsRegistered(Ref<ComponentFactory> c);
	virtual bool bIsRegistered(SRI::String name);
	/** returns the number of factories that could produce the given type */
	virtual int iFactoriesWithType(SRI::String type);


	virtual SRI::Map<SRI::String, Ref<ComponentFactory>>& tGetComponentFactories();

	/**
	* \param typeId Type of ComponentFactory
	* \param selectionCriteria
	* \returns A reference to the ComponentFactory registerd with the given typeId if it exists, otherwise NULL
	*/
	virtual Ref<ComponentFactory> ptGetComponentFactory(SRI::String typeId, SRI::String selectionCriteria = "");
	virtual Ref<ComponentFactory> ptGetComponentFactoryByName(SRI::String name);

	//virtual int iRegisterEngine(SRIEngine* engine);
	//virtual int iUnregisterEngine(SRIEngine* engine);
	//SRIEngine* ptGetEngine(SRI::String name);

	static void vMakeRemote(const SRI::String& ip, int port); 
};





//
//
//template<> class SRIRef<SRI::SRIRegistry> {
//private:
//	SRI::SRIRegistry* m_ptRegistry;
//public:
//	SRIRef(): m_ptRegistry(NULL){};
//	
//	SRIRef(SRI::SRIRegistry* reg): m_ptRegistry(reg){};
//	
//	virtual ~SRIRef(){
//		if (m_ptRegistry != NULL){
//			SRI::SRIRegistry::vReleaseInstance();
//		}
//	}
//
//	SRIRegistry& operator*(){
//		return *m_ptRegistry;
//	}
//
//	SRIRegistry* operator->(){
//		return m_ptRegistry;
//	}
//
//	bool operator==(const SRIRef<SRIRegistry>& c){
//		return m_ptRegistry == c.m_ptRegistry;
//	}
//
//	bool operator !=(const SRIRef<SRIRegistry>& c){
//		return !(*this == c);
//	}
//
//	bool isValid() const{
//		return (m_ptRegistry != NULL);
//	}
//
//};





} // end namespace 
#endif