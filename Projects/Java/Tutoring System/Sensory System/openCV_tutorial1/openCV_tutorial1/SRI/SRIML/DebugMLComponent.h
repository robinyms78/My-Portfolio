#ifndef SRI_SRIML_DEBUGMLCOMPONENT_H
#define SRI_SRIML_DEBUGMLCOMPONENT_H


#include "SRI/SRIML/MLComponent.h"
#include "SRI/SRIML/SequentialMLComponent.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIString.h"

namespace SRI{

class DebugMLComponent : public MLComponent{
	
private:
	DebugMLComponent(); // no default constructor available
	Logger m_tLog;
	SRI::String m_szDebugMessage;
	bool m_bHasPrinted;

	void vAddComponent(Ref<Component>  c); //hide this method

public:
	//constructors & destructors
	DebugMLComponent(SRI::String name, SRI::String message);
	virtual ~DebugMLComponent();
	DebugMLComponent(const DebugMLComponent& c);
	
	DebugMLComponent& operator=(const DebugMLComponent& c);
	bool operator==(const DebugMLComponent& c); 

	Component* ptClone() const; 
	
	void vInit();
	void vFinalize();
	bool bHasMoreSteps();
	void vStep();
	void vPreStep();
	void vPostStep();

			
};

} // end namepspace

#endif SRI_SRIML_DEBUGMLCOMPONENT_H

