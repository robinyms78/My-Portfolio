#ifndef SRI_DEMO_ACTUATOR_H
#define SRI_DEMO_ACTUATOR_H

#include "SRI/SRIEngine/SRIRegistryPlugin.h"
#include "SRI/SRIEmbodiment/Actuator.h"
#include "SRI/Logger/Logger.h"

class SRI_PLUGIN_API DemoActuator: public SRI::Actuator{

private:
	SRI::Logger m_tLog;


public:
	DemoActuator(SRI::String name);
	virtual ~DemoActuator();

	DemoActuator(const DemoActuator& c);
	DemoActuator& operator=(const DemoActuator& c);

	virtual SRI::Component* ptClone() const;

	virtual bool bHasMoreSteps();
	virtual void vStep();

};


#endif