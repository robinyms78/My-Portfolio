

#ifndef DEMO_REACTIVE_COMPONENT_FACTORY_H
#define DEMO_REACTIVE_COMPONENT_FACTORY_H

#include "SRI/SRIEngine/SRIPlugin.h"
#include "SRI/SRIEngine/ComponentFactory.h"
#include "SRI/Logger/Logger.h"


namespace SRI{

/** This test class demonstrates how components are developed within the SRI architecture.
* The architecture requires the developer to provide a factory and a class defenition for a new module.
* The factory is stored in a global registry. An engine object has access to the global factory and
* uses the createComponent method to create instances for a SRI application*/
class SRI_PLUGIN_API DemoReactiveComponentFactory: public ComponentFactory{
private:
	Logger m_tLog;
public:
	DemoReactiveComponentFactory(SRI::String name, SRI::String config = "");
	virtual ~DemoReactiveComponentFactory();

	/** Overwrite the createComponent method as given by the ComponentFactory class*/
	virtual SRI::Ref<SRI::Component> ptCreateComponent(SRI::String name, SRI::String config = "");
};

}// end namespace
#endif
