#ifndef DEMO_ANIMATION_FACTORY_H
#define DEMO_ANIMATION_FACTORY_H

#include "SRI/SRIEngine/SRIRegistryPlugin.h"
#include "SRI/SRIEngine/ComponentFactory.h"

class SRI_PLUGIN_API DemoAnimationFactory: public SRI::ComponentFactory{

private:


public:
	DemoAnimationFactory(SRI::String name, SRI::String config="");
	DemoAnimationFactory(const DemoAnimationFactory& c);
	DemoAnimationFactory& operator=(const DemoAnimationFactory& c);
	virtual ~DemoAnimationFactory();

	virtual SRI::Ref<SRI::Component> ptCreateComponent(SRI::String name, SRI::String config = "");

};


#endif