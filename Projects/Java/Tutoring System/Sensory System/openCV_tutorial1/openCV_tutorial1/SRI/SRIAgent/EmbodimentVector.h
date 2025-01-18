#ifndef SRI_EMBODIMENT_VECTOR_H
#define SRI_EMBODIMENT_VECTOR_H

#include "SRIAgentLib.h"
#include "SRI_String.h"
#include "ActuatorState.h"
#include "SRI_Map.h"


namespace SRI{

INST_AGENT_TEMPL SRI::Map<SRI::String, SRI::ActuatorState>;

class Embodiment;

/** An embodimentvector contains the posture of a robot at a given time.
* The dimensions of the vector specify the actuators of the robot.
* The values are control signals that are passed to the actuators.
*/
class AGENT_API EmbodimentVector{

private:
	SRI::Map<SRI::String, ActuatorState> m_mValues;

public:
	EmbodimentVector(SRI::Embodiment* emb);
	virtual ~EmbodimentVector();
		

};



}// end namespace


#endif