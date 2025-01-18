#ifndef SRI_ACTUATOR_STATE_H
#define SRI_ACTUATOR_STATE_H

#include "SRI/SRIAgent/SRIAgentLib.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/Serializable.h"

namespace SRI{

class ActuatorState;

INST_AGENT_TEMPL SRI::Ref<SRI::ActuatorState>;

/** An ActuatorState defines the value of an actuator over a period of time
* starting from 0. 
*/
class AGENT_API ActuatorState: public Serializable{

protected:
	void* m_ptValue;
	SRI::String m_szStateType;

	void vSetStateType(SRI::String stateType);

public:
	ActuatorState();
	virtual ~ActuatorState();

	ActuatorState(const ActuatorState& c);
	virtual ActuatorState& operator=(const ActuatorState& c);
	
	virtual bool operator==(const ActuatorState& c);

	virtual ActuatorState* ptClone() const;

	/** This retuns the state type for type checking with the actuators */
	virtual SRI::String szGetStateType() const;

	//=========== from serializable interface =====================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	/** This returns a class type for serialization */
	virtual const char* szGetObjType() const;

};



}// end namespace


#endif