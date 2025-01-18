
#ifndef SRI_DEMO_EMBODIMENT_FACTORY_H
#define SRI_DEMO_EMBODIMENT_FACTORY_H

#include "SRI/SRIEngine/SRIRegistryPlugin.h"
#include "SRI/SRIEngine/ComponentFactory.h"


class SRI_PLUGIN_API DemoEmbodimentFactory: public SRI::ComponentFactory{

private:

public:
	DemoEmbodimentFactory(SRI::String factName, SRI::String config = "");
	virtual ~DemoEmbodimentFactory();

	DemoEmbodimentFactory(const DemoEmbodimentFactory& c);
	DemoEmbodimentFactory& operator=(const DemoEmbodimentFactory& c);
	
	virtual SRI::Ref<SRI::Component> ptCreateComponent(SRI::String name, SRI::String config = "");
	
};




#endif