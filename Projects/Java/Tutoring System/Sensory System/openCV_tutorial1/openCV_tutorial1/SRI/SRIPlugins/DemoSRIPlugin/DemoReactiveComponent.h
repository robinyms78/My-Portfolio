#ifndef SRI_DEMOCOMPONENT_H
#define SRI_DEMOCOMPONENT_H

#include "SRI/SRIEngine/SRIPlugin.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

class SRI_PLUGIN_API DemoReactiveComponent: public ReactiveComponent{

private:
	int m_iDemoInt;
	Logger m_tLog;

public:
	DemoReactiveComponent(SRI::String name);
	virtual ~DemoReactiveComponent();

	virtual void vInit();
	virtual void vFinalize();
	virtual bool bHasMoreSteps();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();

};


}

#endif