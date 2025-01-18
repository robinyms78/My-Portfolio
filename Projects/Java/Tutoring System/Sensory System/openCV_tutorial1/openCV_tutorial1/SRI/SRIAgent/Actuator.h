#ifndef SRI_ACTUATOR_H
#define SRI_ACTUATOR_H

#include "SRI/SRIAgent/SRIAgentLib.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIAgent/ActuatorState.h"
#include "SRI/SRIAgent/ActuatorDefinition.h"
#include "SRI/SRIUtil/SRIRef.h"

namespace SRI{

INST_AGENT_TEMPL Ref<ActuatorState>; 

class AGENT_API Actuator: public ReactiveComponent{

private:
	

protected:
	Ref<ActuatorState> m_ptState;
	//ActuatorDefinition m_tActuatorDefinition;
	
public:
	Actuator(SRI::String name);
	virtual ~Actuator();

	/** Makes only flat copy */
	Actuator(const Actuator& c);
	/** Only flat copy */
	Actuator& operator=(const Actuator& c);

	virtual void vSetActuationType(SRI::String actuationType);

	virtual void vSetState(Ref<ActuatorState> val);
	virtual Ref<ActuatorState> ptGetState();

	virtual bool operator==(const Actuator& c);

	virtual SRI::String szGetStateType() const;
};



}// end namespace


#endif