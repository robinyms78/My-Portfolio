

#ifndef SRI_COMPONENT_STUB_H
#define SRI_COMPONENT_STUB_H

#include "SRI/SRIEngine/Component.h"
#include <sstream>
#include <vector>
#include "SRI/SRIEngine/StubTemplate.h"

namespace SRI{

/// A ComponentStub is a local (to the engine/registry) representation of a remote Component
/** ComponentStubs provide allow the engine/registry to access the services of a 
	remotely running Component. When the ComponentStub is deleted, the memory of the
	remote Component is automatically reclaimed.
*/ 

class SRI_E_API ComponentStub : public Component{
	friend class SRIEngine; //sets the ID of the module

private:
	StubTemplate* m_ptStubTemplate;
	int szCallFunction(SRI::String funcName, const std::vector<SRI::String>& args, Ref<SRI::String> retstring) const;
	int szCallFunction(SRI::String funcName, Ref<SRI::String> retstring) const;

	SRI::String m_szCachedName; //name of the component

protected:

	
	//SRI::Ref<EngineHandle> m_ptEngineHandle;

	/** This function is called by the engine after the initialization of the component*/
	virtual void vSetId(SRI::String id); 
	virtual int iSetNameSpace(SRI::String name);

	Logger m_tLog;

/*
	SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mChildComponents;
	SRI::Ref<SRI::Component> m_ptParent;

	SRI::Ref<ComponentDefinition> m_ptComponentDefinition;*/

	SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mParentServers; //keeps parent servers alive

	/** Creates a copy and sets the copy*/
	virtual void vSetDefinition(const Definition* def);
	/** Sets the definition directly */
	virtual void vSetDefinition(SRI::Ref<Definition> ptDef);

public:
	ComponentStub(SRI::String name, SRI::String ip, int portNo);
	virtual ~ComponentStub();

	ComponentStub(const ComponentStub& c);
	ComponentStub& operator=(const ComponentStub& c);

	SRI::String szGetPeerIp() const; //TODO: think of refactoring stubs
	int iGetPeerPort() const;

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

	virtual Component* ptClone() const;
	virtual ComponentStatus eGetStatus() const;
	virtual void vSetStatus(ComponentStatus status);
	virtual SRI::Ref<Definition> ptGetDefinition() const;

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

	void vShutdownRemote();

};

} // end namespace


#endif SRI_COMPONENT_STUB_H