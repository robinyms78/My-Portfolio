#ifndef SRI_CLONEABLE_H
#define SRI_CLONEABLE_H

#include "SRI/SRIEngine/SRIEngineLib.h"

namespace SRI{

class Cloneable{

	
	virtual Cloneable *ptClone() const = 0;
};

}

#endif