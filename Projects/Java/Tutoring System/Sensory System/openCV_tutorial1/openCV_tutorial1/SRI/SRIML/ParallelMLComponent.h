#ifndef SRI_SRIML_PARALLELMLCOMPONENT_H
#define SRI_SRIML_PARALLELMLCOMPONENT_H

#include "SRI/SRIML/MLComponent.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

class ParallelMLComponent : public MLComponent{
	
private:
	ParallelMLComponent(); // no default constructor available
	Logger m_tLog;

protected:

	
	

public:
	//constructors & destructors

	ParallelMLComponent(SRI::String name);
	virtual ~ParallelMLComponent();
	ParallelMLComponent(const ParallelMLComponent& c);
	

	bool operator==(const ParallelMLComponent& c); 
	ParallelMLComponent& operator=(const ParallelMLComponent& c);

	Component* ptClone() const; 
	
	void vInit();
	void vFinalize();
	bool bHasMoreSteps();
	void vStep();
	void vPreStep();
	void vPostStep();

			
};

} // end namepspace

#endif SRI_SRIML_PARALLELMLCOMPONENT_H

