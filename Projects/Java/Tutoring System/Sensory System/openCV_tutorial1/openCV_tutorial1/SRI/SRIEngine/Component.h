#ifndef SRI_COMPONENT_H
#define SRI_COMPONENT_H

#include "SRI/SRIGlobals.h"
#include "SRI/SRIEngine/ComponentDefinition.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/Cloneable.h"
#include "SRI/SRIEngine/SRIEngineHandle.h"


namespace SRI{

class SRIEngine;
class Component;


INST_SRI_E_TEMPL SRI::Map<SRI::String, SRI::Ref<SRI::Component>>;
INST_SRI_E_TEMPL SRI::Ref<Component>;
INST_SRI_E_TEMPL SRI::MapIterator<SRI::String, SRI::Ref<SRI::Component>>;
INST_SRI_E_TEMPL SRI::Ref<EngineHandle>;
INST_SRI_E_TEMPL SRI::Ref<Definition>;

typedef enum{
	SRI_FAILED = -1,
	SRI_STOPPED = 0,
	SRI_RUNNING = 1,
	SRI_INITIALIZED = 2,
	SRI_PAUSED = 3,
	SRI_FINALIZED = 4
} ComponentStatus;



/** The Component class is the most general interface to components
* in the SRI reactive system framework.
*/
class SRI_E_API Component: public SRI::Cloneable{
	friend class SRIEngine;  // sets the ID of the component
	friend class SRIEngineStub;
	friend class ComponentServer; 


private:
	Component(); // no default constructor available
	

	void vCloneChildren(const Component& c);
		

protected:
	SRI::Ref<Component> m_ptSelfRef;
	Logger m_tLog;
		
	SRI::Ref<EngineHandle> m_ptEngineHandle;

	/** This function is called by the engine after the initialization of the component*/
	virtual void vSetId(SRI::String id); 
	virtual int iSetNameSpace(SRI::String name);

	SRI::String m_szID;
	SRI::String m_szComponentType;
	SRI::String m_szName; // a human readable name for the component
	SRI::String m_szNameSpace;

	ComponentStatus m_eStatus;

	SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mChildComponents;
	SRI::Ref<SRI::Component> m_ptParent;

	SRI::Ref<Definition> m_ptComponentDefinition;

	/** Creates a copy and sets the copy*/
	virtual void vSetDefinition(const Definition* def);
	/** Sets the definition directly */
	virtual void vSetDefinition(SRI::Ref<Definition> ptDef);
	
	/** Convenience helper function to step children */
	virtual void vInitChildren();
	virtual void vStepChildren();
	virtual void vPreStepChildren();
	virtual void vPostStepChildren();
	virtual void vFinalizeChildren();

public:
	//constructors & destructors
	Component(SRI::String name);
	virtual ~Component();

	/** A copy is not added to an engine automatically*
	* The EngineHandle pointer remains unchanged. */
	Component(const Component& c);
	Component& operator=(const Component& c);


	bool operator==(const Component& c);

	virtual Ref<EngineHandle> ptGetEngineHandle();
	virtual int iSetEngineHandle(Ref<EngineHandle> handle);

	/** Sets a new parent. If the parent is valid, the given component changes its
	* namespace and is automatically added to the engine embedded loop.
	* In case the given new parent is NULL (or invalid) and the component has been
	* child, the component is automatically removed from the embedded loop. */
	virtual int iSetParent(Ref<Component> newParent);
	virtual int iAddChild(Ref<Component> comp);
	virtual Ref<Component> ptGetChild(SRI::String name);
	virtual Ref<Component> ptGetParent();
	virtual SRI::Map<SRI::String, SRI::Ref<SRI::Component>>& tGetChildComponents();
	virtual bool bHasChild(SRI::String name);
	/** returns reference to removed child. Child keeps its children*/
	virtual Ref<Component> ptRemoveChild(SRI::String name);
	virtual Ref<Component> ptRemoveChild(Ref<Component> comp);
	virtual void vDeleteAllChildren();

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
	/** By default the children are not stepped. to step children in derived classes use stepChildren() functions*/
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();

	
};

} // end namepspace

#endif SRI_COMPONENT_H

