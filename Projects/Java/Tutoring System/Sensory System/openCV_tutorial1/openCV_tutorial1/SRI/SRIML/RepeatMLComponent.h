#ifndef SRI_SRIML_REPEATMLCOMPONENT_H
#define SRI_SRIML_REPEATMLCOMPONENT_H


#include "SRI/SRIML/MLComponent.h"
#include "SRI/SRIML/SequentialMLComponent.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

class RepeatMLComponent : public MLComponent{
	
private:
	RepeatMLComponent(); // no default constructor available
	Logger m_tLog;
	SequentialMLComponent m_SequentialComponent;
	int m_iNumRepeats;

public:
	//constructors & destructors
	RepeatMLComponent(SRI::String name, int numRepeats);
	virtual ~RepeatMLComponent();
	RepeatMLComponent(const RepeatMLComponent& c);
	
	RepeatMLComponent& operator=(const RepeatMLComponent& c);
	bool operator==(const RepeatMLComponent& c); 

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

#endif SRI_SRIML_REPEATMLCOMPONENT_H

