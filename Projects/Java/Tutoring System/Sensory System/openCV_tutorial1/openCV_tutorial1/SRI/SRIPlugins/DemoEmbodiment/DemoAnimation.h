#ifndef DEMO_ANIMATION_H
#define DEMO_ANIMATION_H

#include "SRI/SRIEngine/SRIRegistryPlugin.h"
#include "SRI/SRIAnimation/Animation.h"
#include "SRI/Logger/Logger.h"

class SRI_PLUGIN_API DemoAnimation: public SRI::Animation{

private:
	SRI::Logger m_tLog;

public:
	DemoAnimation(SRI::String name);
	virtual ~DemoAnimation();

	DemoAnimation(const DemoAnimation& c);
	DemoAnimation& operator=(const DemoAnimation& c);

	virtual SRI::Component* ptClone() const;

	virtual bool bHasMoreSteps(SRI::TimeStamp t);
	virtual void vTimedStep(SRI::TimeStamp t);

};



#endif