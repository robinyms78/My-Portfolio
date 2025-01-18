#ifndef SRI_ANIMATION_HANDLE_H
#define SRI_ANIMATION_HANDLE_H

#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/Component.h"
#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/SRIAnimation/Animation.h"
#include "SRI/SRIUtil/SRITime.h"

namespace SRI{

class AnimationHandle{

private:
	SRI::TimeStamp m_tCurrentTime;
	Ref<SRI::Component> m_ptAnimation;
	SRI::List<SRI::PortMapping> m_lPortMappings;

public:
	AnimationHandle();
	AnimationHandle(Ref<SRI::Component> animation);

	virtual ~AnimationHandle();
	AnimationHandle(const AnimationHandle& c);

	AnimationHandle& operator=(const AnimationHandle& c);
	virtual bool operator==(const AnimationHandle& c) const;

	void vSetCurrentTime(const TimeStamp& t);
	void vSetAnimation(Ref<SRI::Component> animation);
	void vSetPortMappings(const SRI::List<SRI::PortMapping>& portMappings); 

	TimeStamp tGetCurrentTime() const;
	Ref<SRI::Component>& ptGetAnimation();
	SRI::List<SRI::PortMapping>& tGetPortMappings();	

};


} // end namespace



#endif