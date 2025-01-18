

#ifndef SRI_ENGINE_STUB_H
#define SRI_ENGINE_STUB_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIEngine/SRIEngine.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIEngine/StubTemplate.h"

namespace Poco {
	class ThreadPool;
}


namespace SRI{

class Component;
class SRIEnginePluginHandle;
class InputPort;
class OutputPort;
class EngineHandle;

// storage labels:
//    simulation
//    engine
//    embedded

/** The engine takes owenership of the components under its control
* The engine has two loops. One is called the simulation loop and the other the engine loop.
* The two loops are identical in that they host and run components.
* A component name must be unique for the whole engine (all loops).
* There is an ordering in execution of the two loops. vPreStep() and vStep() of the
* engine loop components are executed BEFORE the simulation loop (preStep, Step, postStep).
* The vPostStep() method of the engine loop components is executed afterwards.
* There is no ordering in execution of the modulues within one loop. Due to this ordering, engine loop components
* enclose the simulation loop and can provide control functionality (GUI, Console, etc.)
* Usually, engine loop components are added and removed by SRIEnginePlugins.
* Simulation loop components are created through factories that are accessed through the registry.
*/
class SRI_E_API SRIEngineStub : public SRIEngine {
	friend class SRI::EngineHandle;
	
private:
	Ref<SRIRegistry> m_ptSRIRegistry;
	Ref<LoggerManager> m_ptLoggerManager;

	Ref<SRIEngine> m_ptSelfRef;

	Ref<StubTemplate> m_ptStubTemplate;

	Poco::ThreadPool *m_ptThreadPool;


	Logger m_tLog;
	bool m_bIsRunning;

	/** Engine plugins are libraries that are loaded on runtime. 
	* There are two functions called from the lirbary:
	* 1) InitSRIEnginePlugin(SRI::SRIEngine* engine, SRI::String name, SRI::String pluginPath, SRI::String config)
	* 2) FreeSRIEnginePlugin(SRI::SRIEngine* engine, SRI::String pluginName, SRI::String pluginPath, SRI::String config);
	* On load, a plugin does whatever it needs to do on the engine: including adding components to the engineloop.
	* On close, a plugin removes whatever it has done and removes the components that it had added. (Plugins need to be 
	* released before the components of the two SRIEngine loops are released. 
	*/
	SRI::Map<SRI::String, SRI::SRIEnginePluginHandle*> m_mSRIEnginePlugins;
	SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mEngineLoopComponents;
	SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mSimulationLoopComponents;
	SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mEmbeddedComponents;  // holds references to all components that are children

	
	//these components in these maps facilitate:
	//1. creating connections between component. the enginestub will check if the components
	//	are both local (using dynamic casting) and will handle the creation of the connection;
	//	otherwise, it will pass the connect request to the main engine
	// anything else???
		

	//TODO: what should these functions do?
	SRIEngineStub(const SRIEngineStub& c);
	SRIEngineStub operator=(const SRIEngineStub& c);

	SRI::String m_szName;


	//TODO: what should these functions do? to make virtual and override?
	/** This function frees all components registered in the engine loop*/
	void vDeleteAllEngineComponents();
	/** This function frees all components registered in the simulation loop*/
	void vDeleteAllSimulationComponents();
	
	/** Frees all loaded plugins. The FreeSRIEnginePlugin function is called and the library is closed. */
	///At present enginestubs don't have plugins loaded, so this shouldn't remove anything
	void vReleaseAllPlugins();
	
	/** Function called Component (through EngineHandle) */
	void vRemoveComponent(SRI::String compName);

	DWORD m_iEngineProcessId;
	

public:
	SRIEngineStub(SRI::String ip, int portNo, SRI::String name="SRIEngineStub");
	virtual ~SRIEngineStub();

	//TODO: how to implement
	//bool operator==(const SRIEngine& e);

	/**
	* This method creates a component and assigns the given name to identify it in the application.
	* The name must be unique.
	* \returns 0 on success, otherwise an error code reflected by a negative number
	*/

	
	virtual int iConnect(SRI::String sender, SRI::String outport, SRI::String receiver, SRI::String inport);

	virtual int iDisconnect(SRI::String sender, SRI::String outport, SRI::String receiver, SRI::String inport);


	/** Initalizes all simulation loop components */
	virtual void vInitSimulationLoop();
	/** Performs a single step of all components*/
	virtual void vStepSimulationLoop();
	

	/** Engine loop convenience fucntions */
	virtual void vInitEngineLoop();
	virtual void vPreStepEngineLoop();
	virtual void vStepEngineLoop();
	virtual void vPostStepEngineLoop();
	

	
	// Main functions to control the engine. They handle engineloop as well as simulation loop components 
	/** Initializes all components. First of the engine loop, then of the simulation loop. */
	virtual void vInit();
	/** Steps all components. First preStep and Step of engine loop are executed. Then preStep, Step postStep of
	* simulation loop. At last postStep of engine loop components are executed.*/
	virtual void vStep();
	/** Encloses the vStep() function in a while loop. The loop stops if vStop() is called (For example by one of the
	* engine loop components. This allows to react on events such as closing of control window.*/
	virtual void vRun();
	/** Sets a flag that is evaluated by the vRun() method before it enters a Step(). The vRun() method returns. A stopped
	* engine can be restarted by calling vRun() again.*/
	virtual void vStop();
	/** Calls the finalize function on all components (engine and simulation loop) */
	virtual void vFinalize();

	/** This function is called by the destructor and frees all components and plugins*/
	void vReleaseAll();

	void vFinalizeAllSimulationComponents();
	void vFinalizeAllEngineComponents();

	//TODO: can remote engines have plugins?

	/*virtual int iLoadEnginePlugin(SRI::String pluginName, SRI::String pluginPath = "", SRI::String config = "");
	virtual void vReleaseEnginePlugin(SRI::String pluginName);*/
	//virtual int iCreateRemoteComponent(int portNo, SRI::String typeId, SRI::String name, SRI::String config = "");

	//==================== Paramter component access ===========================================================
	/** This function searches the registry for a component factory with given type. If found
	* it creates a component with given name and adds it to the specified loop within the engine. The two supported labels
	* are currently "engine" and "simulation". By default it will choose the simulation loop*/
	virtual int iCreateComponent(SRI::String typeId, SRI::String name, SRI::String config = "", SRI::String loopLabel = "simulation", SRI::String selectionCriteria = ""); // using a string as an identifier (futur extensions might include regular expressions)
	/** This function takes an existing component and adds it to the engine. The engine will take over
	* and release the memory when it is no longer needed. The component is added to the simulation loop
	* and can be stepped. When the adding fails, the component is released immediately*/
	virtual int iAddComponent(Component* comp, SRI::String loopLabel = "simulation");
	/** Used to remove and delete a component associated with the engine. It will search for the component in the specified loop.
	*   A "*" string will trigger to search through all loops and delete all components wiht the given name.*/
	virtual void vDeleteComponent(SRI::String name, SRI::String loopLabel = "*");
	/** Breaks the association of the component with the engine. The component is neither finalized, nor deleted.
	* The caller takes over the responsibility to release the component. */
	virtual void vRemoveComponent(Component* comp, SRI::String loopLabel = "*");
	/** \returns the component with the given name from the simulation loop. NULL if none is found. A "*" value 
	* will search through both loops.*/
	virtual Ref<Component> ptGetComponent(SRI::String name, SRI::String loopLabel = "simulation");

	virtual bool bHasComponent(SRI::String name, SRI::String loopLabel = "simulation");
	/** This function checks for pointer equality if a component is already existing */
	virtual bool bHasComponent(Component* comp);
	virtual SRI::String szGetLoopLabel(SRI::String name);
	virtual SRI::String szGetLoopLabel(Component* comp);

	//==================== Simulation components ===========================================================
	/** This function searches the registry for a component factory with given type. If found
	* it creates a component with given name and adds it to the engines simulation loop*/
	virtual int iCreateSimComponent(SRI::String typeId, SRI::String name, SRI::String config = "");
	/** Adds the ref to the engine if valid*/
	virtual int iAddSimComponent(SRI::Ref<SRI::Component> comp);
	/** This function takes an existing component and adds it to the engine. The engine will take over
	* and release the memory when it is no longer needed. The component is added to the simulation loop
	* and can be stepped. When the adding fails, the component is released immediately*/
	virtual int iAddSimComponent(Component* comp);
	/** Used to remove and delete a component associated with the engien.*/
	virtual void vDeleteSimComponent(SRI::String name);
	/** Breaks the association of the component with the engine. The component is neither finalized, nor deleted.
	* The caller takes over the responsibility to release the component. */
	virtual void vRemoveSimComponent(Component* comp);
	/** \returns the component with the given name from the simulation loop. NULL if none is found.*/
	virtual Ref<Component> ptGetSimComponent(SRI::String name);

	//==================== Engine Components ===========================================================
	/** Functions for engine loop components are usually accessed by SRIEngineLoop plugins. They behave like
	* the simulation loop counterparts but target the engine loop instead of the simulation loop.*/
	virtual int iCreateEngineComponent(SRI::String typeId, SRI::String name, SRI::String config = "");
	virtual int iAddEngineComponent(SRI::Ref<SRI::Component> comp);
	virtual int iAddEngineComponent(Component* comp);
	/** The remove functions just remove the component without releasing the memory */
	virtual void vRemoveEngineComponent(Component* comp);
	virtual void vDeleteEngineComponent(SRI::String name);
	virtual Ref<Component> ptGetEngineComponent(SRI::String name);


	/** This function changes the name of a component. It returns and
	* error code if a component with oldName could not be found or if
	* the new name is already in use in the engine*/
	virtual int iChangeName(SRI::String oldName, SRI::String newName);

	//==================== Embedded functionality ===========================================================
	virtual int iAddEmbeddedComponent(SRI::Ref<SRI::Component> comp);
	/** The memory of the component is taken over*/
	virtual int iAddEmbeddedComponent(Component* comp);
	virtual int iCreateEmbeddedComponent(SRI::String typeId, SRI::String name, SRI::String config = "");
	/** The caller takes over the responsibility to release the memory*/
	virtual void vRemoveEmbeddedComponent(Component* comp);
	virtual void vDeleteEmbeddedComponent(SRI::String name);
	virtual Ref<Component> ptGetEmbeddedComponent(SRI::String name);


	//==================== Convenience functions ===========================================================
	/** Convenience access functions to target individual components of the simulation loop*/
	virtual void vInitComponent(SRI::String name);
	virtual void vFinalizeComponent(SRI::String name);
	virtual void vStopComponent(SRI::String name);
	virtual void vPauseComponent(SRI::String name);

	SRI::String szGetName() const;
	void vSetName(SRI::String name);

	//Convenience access functions
	/** The Engine requests a handle to the registry when it is created and releases it when it 
	* goes out of scope. During the lifetime of the engine the handle is stays valid*/
	//SRIRegistry* ptGetSRIRegistry();
	Ref<LoggerManager> ptGetLoggerManager();
	Ref<SRIRegistry> ptGetSRIRegistry();

	int szCallFunction(SRI::String funcName, const std::vector<SRI::String>& args, Ref<SRI::String> retstring) const;
	//int szCallFunction(SRI::String funcName, const std::vector<SRI::String>& args) const;
	void vShutdownRemote();

};


}// end namespace




#endif SRI_ENGINE_STUB_H
