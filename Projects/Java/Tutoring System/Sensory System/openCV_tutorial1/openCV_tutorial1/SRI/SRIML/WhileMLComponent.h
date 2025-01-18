#ifndef SRI_SRIML_WHILEMLCOMPONENT_H
#define SRI_SRIML_WHILEMLCOMPONENT_H


#include "SRI/SRIML/MLComponent.h"
#include "SRI/SRIML/SequentialMLComponent.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIString.h"

namespace SRI{

class WhileMLComponent : public MLComponent{
	
private:
	WhileMLComponent(); // no default constructor available
	Logger m_tLog;
	SequentialMLComponent m_SequentialComponent;
	SRI::String m_szCondition;

public:
	//constructors & destructors
	WhileMLComponent(SRI::String name, SRI::String condition);
	virtual ~WhileMLComponent();
	WhileMLComponent(const WhileMLComponent& c);
	
	WhileMLComponent& operator=(const WhileMLComponent& c);
	bool operator==(const WhileMLComponent& c); 

	Component* ptClone() const; 
	
	void vInit();
	void vFinalize();
	bool bHasMoreSteps();
	void vStep();
	void vPreStep();
	void vPostStep();
	
	void vAddComponent(Component * c);

			
};

} // end namepspace

#endif SRI_SRIML_WHILEMLCOMPONENT_H

