
#ifndef SRI_DEMO_EMBODIMENT_H
#define SRI_DEMO_EMBODIMENT_H

#include "SRI/SRIEngine/SRIRegistryPlugin.h"
#include "SRI/SRIEmbodiment/Embodiment.h"
#include "SRI/Logger/Logger.h"

class SRI_PLUGIN_API DemoEmbodiment: public SRI::Embodiment{

private:
	SRI::Logger m_tLog;

public:
	DemoEmbodiment(SRI::String name);
	virtual ~DemoEmbodiment();

	DemoEmbodiment(const DemoEmbodiment& c);
	DemoEmbodiment& operator=(const DemoEmbodiment& c);

	virtual void vInit();
	virtual void vStep();

};




#endif





