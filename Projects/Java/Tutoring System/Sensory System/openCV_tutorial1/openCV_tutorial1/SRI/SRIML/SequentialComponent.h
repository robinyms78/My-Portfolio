#ifndef SRI_SRIML_SEQUENTIALCOMPONENT_H
#define SRI_SRIML_SEQUENTIALCOMPONENT_H


#include "SRIEngineLib.h"
#include "SRI_String.h"
#include "SRI_List.h"

#include "Component.h"
#include "Logger.h"

namespace SRI{

class SequentialComponent : public Component{
	
private:
	SequentialComponent(); // no default constructor available
	Logger m_tLog;


	

protected:


	SRI::List<Component *> m_ComponentList; 
	SRI::ListIterator<Component *> m_liCurrentComponent;
	int m_iIndexPos; 
	SequentialComponent& operator=(const SequentialComponent& c);
	

public:
	//constructors & destructors
	SequentialComponent(SRI::String name);
	virtual ~SequentialComponent();
	SequentialComponent(const SequentialComponent& c);
	

	bool operator==(const SequentialComponent& c); 

	Component* ptClone() const; 
	ComponentStatus eGetStatus() const;
	

	void vInit();
	void vFinalize();
	bool bHasMoreSteps();
	void vStep();
	void vPreStep();
	void vPostStep();

	void iAddComponent(Component * c); //takes over the memory of the component
		
};

} // end namepspace

#endif SRI_SRIML_SEQUENTIALCOMPONENT_H

