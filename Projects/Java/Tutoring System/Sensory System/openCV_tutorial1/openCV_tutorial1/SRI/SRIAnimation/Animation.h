#ifndef SRI_ANIMATION_H
#define SRI_ANIMATION_H

#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/SRIEngine/ReactiveComponent.h"

#include "SRI/SRIEmbodiment/Embodiment.h"
#include "SRI/SRIUtil/SRITime.h"
#include "SRI/SRIEngine/ComponentDefinition.h"
#include "SRI/SRIAnimation/AnimationDefinition.h"

namespace SRI{




/** An animation defines output ports on which the values for the
* actuators are send. 
*/
class SRI_ANIMATION_API Animation : public ReactiveComponent{
	friend class AnimationEngine;

private:
	TimeStamp m_tStepTime;

protected:
	SRI::String m_szEmbodimentType;
	virtual void vSetEmbodimentType(SRI::String embodimentType);

	SRI::List<PortMapping> m_lPortMappings;

	void vSetOutPortMapping(SRI::String outPortName, SRI::String targetComponent, SRI::String targetPort);
	void vSetInPortMapping(SRI::String inPortName, SRI::String sourceComponent, SRI::String sourcePort);
	void vSetPortMapping(PortMapping m);

	void vRemovePortMapping(PortMapping m);
	void vRemoveOutPortMapping(SRI::String outPortName, SRI::String targetComponent, SRI::String targetPort);
	void vRemoveInPortMapping(SRI::String inPortName, SRI::String sourceComponent, SRI::String sourcePort);
	void vRemoveAllPortMappings();

	/** returns a reference to the timestamp last received over the TimeInput port */
	TimeStamp& tGetStepTime();

public:
	Animation(SRI::String name);
	~Animation();
	Animation(const Animation &c);
	Animation& operator=(const Animation&c);

	virtual Component* ptClone() const;

	/** \returns a list of port mappings*/
	virtual SRI::List<SRI::PortMapping> tGetPortMappings();
	virtual SRI::String szGetEmbodimentType() const;

	virtual bool bHasMoreSteps(SRI::TimeStamp t);
	virtual void vTimedStep(SRI::TimeStamp t);

	virtual SRI::Ref<SRI::Definition> ptGetDefinition() const;
	
	virtual void vStep();
	virtual bool bHasMoreSteps();
};
 
}// end namespace
 
#endif
 
 
   
 
    
 //---------------------------------------------------------------------------


