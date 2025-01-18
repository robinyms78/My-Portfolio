#ifndef SRI_LINEAR_INTERPOLATION_H
#define SRI_LINEAR_INTERPOLATION_H

#include "SRI/SRIAnimation/DoubleInterpolation.h"


namespace SRI{



class SRI_ANIMATION_API LinearInterpolation: public DoubleInterpolation{
	
private:

protected:
	

public:
	LinearInterpolation();
	virtual ~LinearInterpolation();

	LinearInterpolation(const LinearInterpolation& c);
	LinearInterpolation& operator=(const LinearInterpolation& c);

	double dGetValue(SRI::TimeStamp time);

	//=========== from Cloneable interface ========================
	virtual Interpolation* ptClone() const;

	//=========== from serializable interface =====================

	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;

};

}


#endif