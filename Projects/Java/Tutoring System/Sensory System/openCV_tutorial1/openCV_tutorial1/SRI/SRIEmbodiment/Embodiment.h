#ifndef SRI_EMBODIMENT_H
#define SRI_EMBODIMENT_H

#include "SRI/SRIEmbodiment/SRIEmbodimentLib.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEmbodiment/Actuator.h"
#include "SRI/SRIEmbodiment/Sensor.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/SRIEngineHandle.h"
#include "SRI/SRIEmbodiment/EmbodimentDefinition.h"
#include "SRI/SRIEngine/ReactiveComponent.h"

namespace SRI{

INST_EMBODIMENT_TEMPL SRI::Map<SRI::String, SRI::Ref<SRI::Actuator>>;
INST_EMBODIMENT_TEMPL SRI::Map<SRI::String, SRI::Ref<SRI::Sensor>>;

class EMBODIMENT_API Embodiment: public ReactiveComponent{

private:
	SRI::Map<SRI::String, SRI::Ref<SRI::Actuator>> m_mActuators;
	SRI::Map<SRI::String, SRI::Ref<SRI::Sensor>> m_mSensors;

	
	Logger m_tLog;
	
	/** Load the components to an engine */
	virtual int iLoadActuators();
	virtual int iLoadSensors();

	virtual void vCloseActuators();
	virtual void vCloseSensors();

	virtual void vSetEmbodimentDefinition(const EmbodimentDefinition* c);

protected:
	Ref<EngineHandle> m_ptEngineHandle;


	SRI::String m_szEmbodimentType;

	/** Important for comparisons if embodiments are of same type and accept similar animations */
	void vSetEmbodimentType(SRI::String type);
	
	/** The actuator is added to the actuators list and automatically
	* added as a child of the embodiment */
	int iAddActuator(Ref<Actuator> actuator);
	/** The sensor is added to the sensors list and added to the 
	* list of children */
	int iAddSensor(Ref<Sensor> sensor);

public:
	Embodiment(SRI::String name);
	virtual ~Embodiment();

	Embodiment(const Embodiment& c);
	Embodiment& operator=(const Embodiment& c);

	/** Overwrite to keep definitions of actuators uptodate */
	virtual int iSetNameSpace(SRI::String name);


	SRI::Map<SRI::String, SRI::Ref<SRI::Actuator>>& tGetActuators();
	SRI::Map<SRI::String, SRI::Ref<SRI::Sensor>>& tGetSensors();

	virtual SRI::Ref<SRI::Actuator> ptGetActuator(SRI::String name);
	virtual SRI::Ref<SRI::Sensor> ptGetSensor(SRI::String name);

	virtual int iLoadEmbodimentDefinition(const SRI::String config);
	//void vSetVector(const EmbodimentVector& vec);
	//EmbodimentVector* ptCreateVector();

	// From component interface
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();
};



}// end namespace


#endif
