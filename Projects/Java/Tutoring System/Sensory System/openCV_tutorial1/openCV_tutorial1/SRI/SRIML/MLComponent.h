#ifndef SRI_SRIML_MLCOMPONENT_H
#define SRI_SRIML_MLCOMPONENT_H


#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIList.h"

#include "SRI/SRIEngine/Component.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

class MLComponent : public Component{
	
private:
	MLComponent(); // no default constructor available
	Logger m_tLog;


	

protected:


	SRI::List<SRI::Ref<Component>> m_ComponentList; 
	virtual MLComponent& operator=(const MLComponent& c);
	

public:
	//constructors & destructors
	MLComponent(SRI::String name);
	virtual ~MLComponent();
	MLComponent(const MLComponent& c);
	

	virtual bool operator==(const MLComponent& c); 

	virtual Component* ptClone() const; 
	ComponentStatus eGetStatus() const;
	

	virtual void vInit();
	virtual void vFinalize();
	virtual bool bHasMoreSteps();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();

	virtual void vAddComponent(SRI::Ref<Component>  c); 
		
};

} // end namepspace

#endif SRI_SRIML_MLCOMPONENT_H

