#ifndef SRI_AGENT_H
#define SRI_AGENT_H


#include "SRI/SRIAgent/SRIAgentLib.h"
#include "SRI/SRIEngine/ReactiveComponent.h"

namespace SRI{

class AGENT_API Agent: public SRI::ReactiveComponent{

public:
	Agent(SRI::String name);
	virtual ~Agent();

	Agent(const Agent& c);
	Agent& operator=(const Agent& c);

};

} //end namespace

#endif