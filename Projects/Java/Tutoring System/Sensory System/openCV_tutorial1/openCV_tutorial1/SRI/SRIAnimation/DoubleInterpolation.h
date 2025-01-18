#ifndef SRI_DOUBLE_INTERPOLATION_H
#define SRI_DOUBLE_INTERPOLATION_H

#include "SRI/SRIAnimation/Interpolation.h"



namespace SRI{

/** Double interpolations work on one-dimensional real numbers.
* They return a double value for a given time */
class SRI_ANIMATION_API DoubleInterpolation: public Interpolation{
	
private:

protected:
	

public:
	DoubleInterpolation();
	virtual ~DoubleInterpolation();

	DoubleInterpolation(const DoubleInterpolation& c);
	DoubleInterpolation& operator=(const DoubleInterpolation& c);

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