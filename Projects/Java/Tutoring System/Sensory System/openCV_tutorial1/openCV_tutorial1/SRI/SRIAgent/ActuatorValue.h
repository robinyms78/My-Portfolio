#ifndef SRI_ACTUATOR_VALUE_H
#define SRI_ACTUATOR_VALUE_H

#include "SRIAgentLib.h"
#include "ReactiveComponent.h"


namespace SRI{

class AGENT_API ActuatorValue{

protected:
	void* m_ptValue;

public:
	ActuatorValue();
	virtual ~ActuatorValue();

	ActuatorValue(const ActuatorValue& c);
	virtual ActuatorValue& operator=(const ActuatorValue& c);
	
	virtual bool operator==(const ActuatorValue& c);
};



}// end namespace


#endif