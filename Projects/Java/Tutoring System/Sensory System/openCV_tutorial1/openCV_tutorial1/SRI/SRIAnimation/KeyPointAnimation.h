#ifndef SRI_KEYPOINT_ANIMATION_H
#define SRI_KEYPOINT_ANIMATION_H


#include "SRI/SRIAnimation/Animation.h"
#include "SRI/SRIAnimation/KeyPointSequence.h"
#include "SRI/Logger/Logger.h"

namespace SRI{


INST_SRI_ANIMATION_TEMPL SRI::Map<SRI::String, Ref<KeyPointSequence>>;

class SRI_ANIMATION_API KeyPointAnimation: public Animation{

private:
	SRI::Logger m_tLog;

protected:
	//For every statoutput there is a sequence
	SRI::Map<SRI::String, Ref<KeyPointSequence>> m_mKeySequences;

	int iAddKeyPointSequence(Ref<KeyPointSequence> k);

public:
	KeyPointAnimation(SRI::String name);
	virtual ~KeyPointAnimation();
	KeyPointAnimation(const KeyPointAnimation& c);
	KeyPointAnimation& operator=(const KeyPointAnimation& c);

	Component* ptClone() const;

	virtual void vInit();
	virtual bool bHasMoreSteps(SRI::TimeStamp t);
	virtual void vTimedStep(SRI::TimeStamp t);

};

}

#endif


