#ifndef SRI_SRIML_SEQUENTIALMLCOMPONENT_H
#define SRI_SRIML_SEQUENTIALMLCOMPONENT_H

#include "SRI/SRIML/MLComponent.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

class SequentialMLComponent : public MLComponent{
	
private:
	SequentialMLComponent(); // no default constructor available
	Logger m_tLog;


	

protected:

	SRI::ListIterator<Ref<Component>> m_liCurrentComponent;
	int m_iIndexPos; 
	
	

public:
	//constructors & destructors
	SequentialMLComponent(SRI::String name);
	virtual ~SequentialMLComponent();
	SequentialMLComponent(const SequentialMLComponent& c);
	
	SequentialMLComponent& operator=(const SequentialMLComponent& c);
	bool operator==(const SequentialMLComponent& c); 

	Component* ptClone() const; 
	
	void vInit();
	void vFinalize();
	bool bHasMoreSteps();
	void vStep();
	void vPreStep();
	void vPostStep();

			
};

} // end namepspace

#endif SRI_SRIML_SEQUENTIALMLCOMPONENT_H

