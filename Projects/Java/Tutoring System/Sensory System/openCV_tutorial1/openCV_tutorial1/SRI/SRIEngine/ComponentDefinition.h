#ifndef SRI_COMPONENT_DEFINITION_H
#define SRI_COMPONENT_DEFINITION_H


#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIEngine/Definition.h"
#include "SRI/SRIEngine/PortDefinition.h"

namespace SRI{

class ComponentDefinition;


INST_SRI_E_TEMPL SRI::Map<SRI::String, PortDefinition>;
INST_SRI_E_TEMPL SRI::Map<SRI::String, ComponentDefinition>;
INST_SRI_E_TEMPL SRI::Map<SRI::String, SRI::Ref<ComponentDefinition>>;

class SRI_E_API ComponentDefinition: public SRI::Definition{

protected:
	SRI::Map<SRI::String, PortDefinition> m_mInputPorts;
	SRI::Map<SRI::String, PortDefinition> m_mOutputPorts;

	SRI::Map<SRI::String, SRI::Ref<ComponentDefinition>> m_mChildren;
	SRI::String m_szEngineName; //indicates if component is attached to an engine
	SRI::String m_szComponentName;  // the base name property is used for the fully qualified name. This holds the unqualified name
	SRI::String m_szComponentType; //holds the type of the component

public:
	ComponentDefinition();
	/** Assumes that component name is the same as full qualified name */
	ComponentDefinition( SRI::String name, SRI::String type, SRI::String config);
	/** Allows to give individual component name and fully qualified name */
	ComponentDefinition(SRI::String componentName, SRI::String fullName, SRI::String type, SRI::String config);
	virtual ~ComponentDefinition();
	ComponentDefinition(const ComponentDefinition& c);
	ComponentDefinition& operator=(const ComponentDefinition& c);
	virtual bool operator==(const ComponentDefinition& c);
	virtual bool operator!=(const ComponentDefinition& c);

	virtual void vSetComponentName(SRI::String compName);
	virtual void vSetEngineName(SRI::String engineName);
	virtual void vSetComponentType(SRI::String compType);

	int iAddInputPortDefinition(const PortDefinition& c);
	int iAddOutputPortDefinition(const PortDefinition& c);

	int iRemoveInputPortDefinition(const SRI::String &name);
	int iRemoveOutputPortDefinition(const SRI::String &name);

	virtual SRI::String szGetComponentName() const;
	virtual SRI::String szGetEngineName() const;
	virtual SRI::String szGetComponentType() const;

	SRI::Map<SRI::String, PortDefinition> tGetInputPortDefinitions();
	SRI::Map<SRI::String, PortDefinition> tGetOutputPortDefinitions();

	
	/** Inserts the reference as a child of the current definition */
	virtual int iAddChildDefinition(SRI::Ref<ComponentDefinition> def);
	virtual void vRemoveChildDefinition(SRI::String name);
	virtual void vClearChildren();

	virtual SRI::Definition* ptClone() const;


	//================ Interface from Serializable ====================================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;
};

}


#endif