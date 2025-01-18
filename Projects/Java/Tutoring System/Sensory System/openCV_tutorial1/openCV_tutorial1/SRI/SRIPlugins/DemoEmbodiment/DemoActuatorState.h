#ifndef DEMO_ACTUATOR_STATE_H
#define DEMO_ACTUATOR_STATE_H

#include "SRI/SRIEngine/SRIRegistryPlugin.h"
#include "SRI/SRIEmbodiment/ActuatorState.h"


class SRI_PLUGIN_API DemoActuatorState: public SRI::ActuatorState{

private:
	SRI::String m_szDemoState; // for illustration just a string

public:
	DemoActuatorState();
	DemoActuatorState(SRI::String state);
	virtual ~DemoActuatorState();

	DemoActuatorState(const DemoActuatorState& c);
	virtual DemoActuatorState& operator=(const DemoActuatorState& c);
	
	virtual bool operator==(const DemoActuatorState& c);

	virtual ActuatorState* ptClone() const;

	SRI::String szGetStateValue() const;
	void vSetStateValue(SRI::String value);

	/** This retuns the state type for type checking with the actuators */
	virtual SRI::String szGetStateType() const;

	//=========== from serializable interface =====================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	/** This returns a class type for serialization */
	virtual const char* szGetObjType() const;

};



#endif


