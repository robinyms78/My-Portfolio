#ifndef SRI_DEMOCOMPONENT_H
#define SRI_DEMOCOMPONENT_H

#include "SRI/SRIEngine/SRIPlugin.h"
#include "SRI/SRIEngine/Component.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/SRIPlugin.h"

namespace SRI{

class SRI_PLUGIN_API DemoComponent: public Component{

private:
	int m_iDemoInt;
	Logger m_tLog;
public:
	DemoComponent(SRI::String name);
	virtual ~DemoComponent();
	DemoComponent(const DemoComponent& c);
	DemoComponent& operator=(const DemoComponent& c);

	int iGetStepsLeft();

	virtual Component* ptClone();

	virtual void vInit();
	virtual void vFinalize();
	virtual bool bHasMoreSteps();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();

};


}

#endif