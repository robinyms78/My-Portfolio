#ifndef SRI_EMBODIMENT_DEFINITION_H
#define SRI_EMBODIMENT_DEFINITION_H

#include "SRI/SRI.h"
#include "SRI/SRIAgent/SRIAgentLib.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIUtil/SRIString.h"
//#include "SRI/SRIEngine/ComponentDefinition.h"
#include "SRI/SRIAgent/ActuatorDefinition.h"
#include "SRI/SRIAgent/SensorDefinition.h"


namespace SRI{

//INST_SRI_E_TEMPL SRI::Map<SRI::String, PortDefinition>;
//INST_AGENT_TEMPL SRI::Map<SRI::String, ComponentDefinition>;
//INST_SRI_E_TEMPL SRI::Map<SRI::String, SRI::Ref<ComponentDefinition>>;

INST_AGENT_TEMPL SRI::Map<SRI::String, ActuatorDefinition>;
INST_AGENT_TEMPL SRI::Map<SRI::String, SensorDefinition>;

class AGENT_API EmbodimentDefinition: public ComponentDefinition{

private:
	SRI::String m_szEmbType;

	SRI::Map<SRI::String, ActuatorDefinition> m_mActuatorDefinitions;
	SRI::Map<SRI::String, SensorDefinition> m_mSensorDefinitions;
	
	/** Hide the option to change component type */
	virtual void vSetComponentType(SRI::String type);

public:
	EmbodimentDefinition();
	EmbodimentDefinition(SRI::String embName, SRI::String embType, SRI::String config);
	virtual ~EmbodimentDefinition();
	EmbodimentDefinition(const EmbodimentDefinition& c);
	EmbodimentDefinition& operator=(const EmbodimentDefinition& c);

	virtual bool operator==(const EmbodimentDefinition& c) const;
	virtual bool operator!=(const EmbodimentDefinition& c) const;

	virtual EmbodimentDefinition* ptClone() const;

	SRI::Map<SRI::String, ActuatorDefinition> tGetActuatorDefinitions();
	SRI::Map<SRI::String, SensorDefinition> tGetSensorDefinitions();

	int iAddActuatorDefinition(ActuatorDefinition actDef);
	int iAddSensorDefinition(SensorDefinition sensDef);

	void vClearActuatorDefinitions();
	void vClearSensorDefinitions();
	int iRemoveActuatorDefnition(SRI::String name);
	int iRemoveSensorDefinition(SRI::String name);

	void vSetEmbodimentName(SRI::String name);
	void vSetEmbodimentType(SRI::String type);

	SRI::String szGetEmbodimentName() const;
	SRI::String szGetEmbodimentType() const;




	//================ Interface from Serializable ====================================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;
};

}

#endif