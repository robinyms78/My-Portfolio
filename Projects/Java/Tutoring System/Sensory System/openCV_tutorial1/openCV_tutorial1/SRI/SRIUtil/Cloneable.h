#ifndef SRI_CLONEABLE_H
#define SRI_CLONEABLE_H

#include "SRI/SRIUtil/SRIUtilLib.h"

namespace SRI{


/** base class implementation provided in order to have virtual destructor
* that calls derived destructors */

class SRIUTIL_API Cloneable{

public:
	Cloneable();
	virtual ~Cloneable();
	
	virtual Cloneable *ptClone() const = 0;
};

}

#endif