#ifndef SRI_REACTIVE_COMPONENT_FACTORY_H
#define SRI_REACTIVE_COMPONENT_FACTORY_H

#include "ComponentFactory.h"
#include "Logger.h"

namespace SRI{

class SRI_E_API ReactiveComponentFactory : public ComponentFactory{
	friend class SRIRegistry;

private:
	Logger m_tLog;

protected:

public:
	ReactiveComponentFactory(SRI::String config = "");
	virtual ~ReactiveComponentFactory();

	virtual Component* ptCreateComponent(SRI::String name, SRI::String config = "");
};


} // end namespace sri


#endif