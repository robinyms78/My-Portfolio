#ifndef SRI_SERIALIZABLE_H
#define SRI_SERIALIZABLE_H

#include "SRI/SRIEngine/Cloneable.h"
#include "SRI/SRIUtil/SRIString.h"


namespace SRI{

class Serializable: public SRI::Cloneable{

public:
	virtual SRI::String szToString() const = 0;
	virtual int iFromString(SRI::String data) = 0;
	/** Returns a string identifying the object type that is serialized */
	virtual const char* szGetObjType() const = 0;
};

}

#endif