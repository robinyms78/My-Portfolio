#ifndef SRI_REACTIVE_COMPONENT_STUB_H
#define SRI_REACTIVE_COMPONENT_STUB_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIEngine/StubTemplate.h"

namespace SRI{

/// A ReactiveComponentStub is a local (to the engine/registry) representation of a remote ReactiveComponent
/** ReactiveComponentStubs provide allow the engine/registry to access the services of a 
	remotely running ReactiveComponent. When the ReactiveComponentStub is deleted, the memory of the
	remote ReactiveComponent is automatically reclaimed.
*/ 

class SRI_E_API ReactiveComponentStub: public ReactiveComponent {
	
	friend class SRIEngine; //sets the ID of the module
							

private:
	StubTemplate* m_ptStubTemplate;
	Logger m_tLog;

	int szCallFunction(SRI::String funcName, const std::vector<SRI::String>& args, Ref<SRI::String> retstring) const;
	int szCallFunction(SRI::String funcName, Ref<SRI::String> retstring) const;
	//int szCallFunction(SRI::String funcName, std::vector<SRI::String>* args) const;

	/** Creates a copy and sets the copy*/
	virtual void vSetDefinition(const Definition* def);
	/** Sets the definition directly */
	virtual void vSetDefinition(SRI::Ref<Definition> ptDef);
	

	//used by SRIEngine when connecting ports
	int iListenForConnection();
	int iFinaliseConnection(const SRI::String& inport);
	int iConnectForConnection(const SRI::String& outport, const SRI::String& ip, int listenPort);

protected:
	virtual int iSetNameSpace(SRI::String name);
	virtual void vSetId(SRI::String id); 
	
public:
	
	ReactiveComponentStub(SRI::String name, SRI::String ip, int portNo);
	virtual ~ReactiveComponentStub();

	ReactiveComponentStub(const ReactiveComponentStub& c);
	ReactiveComponentStub& operator=(const ReactiveComponentStub& c);


	
	SRI::String szGetPeerIp() const; //TODO: think of refactoring stubs
	int iGetPeerPort() const;
	
	virtual Component* ptClone() const;

	int iAddRemoteOutputConnection(const SRI::String& outport, const SRI::String& inport, int listenPort);
	int iAddRemoteInputConnection(const SRI::String& inport, const SRI::String& outport, int listenPort);

	//Exposed functions
	//BEGIN from ReactiveComponent
	virtual int iCreateOutputPort(SRI::String name, SRI::String type);
	virtual int iCreateInputPort(SRI::String name, SRI::String type);

	virtual void vRemoveOutputPort(SRI::String name);
	virtual void vRemoveInputPort(SRI::String name);

	virtual bool bHasInputPort(const SRI::String& inport);
	virtual bool bHasOutputPort(const SRI::String& outport);

	virtual SRI::String szGetOutputPortAddress(const SRI::String& outport);
	virtual SRI::String szGetInputPortAddress(const SRI::String& inport);
	
	/** Adds connection object to the specified output port*/
	virtual int iAddOutputConnection(const SRI::String& outport, Ref<Connection> connection);
	/** Adds connection object to the specified input port*/
	virtual int iAddInputConnection(const SRI::String& inport, Ref<Connection> connection);

	virtual int iRemoveOutputConnection(const SRI::String& outport, const SRI::String& inport);
	virtual int iRemoveInputConnection(const SRI::String& inport, const SRI::String& outport);

	//TODO: consider deprecating, given above two functions? how to implement remotely?
	virtual int iRemoveOutputConnection(const SRI::String& outport, Ref<Connection> connection);
	virtual int iRemoveInputConnection(const SRI::String& inport, Ref<Connection> connection);

	

	/** Returns a list of ports in the format: Name, Type*/
	virtual SRI::Map<SRI::String, SRI::String> mGetInputPortList();
	virtual SRI::Map<SRI::String, SRI::String> mGetOutputPortList();

	/** Retruns a list of ports encoded in an xml string */
	virtual SRI::String szGetInputPorts();
	/** Retruns a list of ports encoded in an xml string */
	virtual SRI::String szGetOutputPorts();

	// =================== Private Port =============================================================
	virtual int iCreatePrivateOutputPort(SRI::String name, SRI::String type);
	virtual int iCreatePrivateInputPort(SRI::String name, SRI::String type);

	virtual void vRemovePrivateOutputPort(SRI::String name);
	virtual void vRemovePrivateInputPort(SRI::String name);

	//END from ReactiveComponent
	
	//Begin from Component
	bool operator==(const Component& c);

	virtual int iSetEngineHandle(Ref<EngineHandle> handle); //engine should be started with ip add if required =)
	virtual Ref<EngineHandle> ptGetEngineHandle();

	virtual int iSetParent(Ref<Component> newParent);
	virtual int iAddChild(Ref<Component> comp);
	virtual Ref<Component> ptGetChild(SRI::String name);
	virtual Ref<Component> ptGetParent();
	virtual bool bHasChild(SRI::String name);
	/** returns reference to removed child. Child keeps its children*/
	virtual Ref<Component> ptRemoveChild(SRI::String name);
	virtual Ref<Component> ptRemoveChild(Ref<Component> comp);

	virtual SRI::String szGetID() const;
	/** returns a descriptive label of the type of component */
	virtual SRI::String szGetComponentType() const;
	/** \returns returns fully qualified name including namespace */
	virtual SRI::String szGetName() const;
	/** \returns returns only the current namespace */
	virtual SRI::String szGetNameSpace() const;
	/** \returns returns just the name of the component without the namespace */
	virtual SRI::String szGetComponentName() const;
	/** The function sets the fully qualified name of the component. The name is parsed
	* to seperate namespace from component name and sets both values accordingly*/
	virtual int iSetName(SRI::String name);

	/** Components should ALWYAS set their type in the constructor. The type string should match the
	* type string that is given by the factory. The Factory can set the type
	* of the component during construction if a configuration deserves a specific type name. */
	virtual int iSetComponentType(SRI::String type);

	
	virtual ComponentStatus eGetStatus() const;
	virtual void vSetStatus(ComponentStatus status);
	virtual SRI::Ref<Definition> ptGetDefinition() const;
	virtual SRI::String szGetDefinition() const;

	/** A component overwriting this function must call the base class implementation 
	* Baseclass implementation sets the status of the component to "INITIALIZED" and makes sure that all 
	* children initialize. (if this behaviour is not desired for children, the component can simply
	* maintain its own list of component children)
	*/
	virtual void vInit();
	/** A component overwriting this function must call the base class implementation.
	* Baseclass implementation sets the status of the component to "STOPPED" and makes sure that all 
	* children finalize.   (if this behaviour is not desired for children, the component can simply
	* maintain its own list of component children)
	*/
	virtual void vFinalize();
	virtual bool bHasMoreSteps();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();

	//END from Component
	void vShutdownRemote();
	

	

private:

	
};



//extern SRI_E_API int nReactiveComponent;
//SRI_E_API int fnReactiveComponent(void);


} // end namespace



#endif
