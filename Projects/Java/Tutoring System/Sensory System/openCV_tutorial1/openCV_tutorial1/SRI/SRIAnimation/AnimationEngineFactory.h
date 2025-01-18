#ifndef SRI_ANIMATION_ENGINE_FACTORY_H
#define SRI_ANIMATION_ENGINE_FACTORY_H

#include "SRI/SRIGlobals.h"
#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/SRIEngine/ComponentFactory.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

class SRI_ANIMATION_API AnimationEngineFactory: public SRI::ComponentFactory{

private:
	Logger m_tLog;

public:
	AnimationEngineFactory(SRI::String name, SRI::String config = "");
	virtual ~AnimationEngineFactory();

	AnimationEngineFactory(const AnimationEngineFactory& c);
	AnimationEngineFactory& operator=(const AnimationEngineFactory& c);

	virtual SRI::Ref<SRI::Component> ptCreateComponent(SRI::String name, SRI::String config = "");

};


}

#endif