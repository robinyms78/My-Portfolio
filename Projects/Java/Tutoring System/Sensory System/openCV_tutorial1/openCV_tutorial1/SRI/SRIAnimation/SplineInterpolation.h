#ifndef SRI_SPLINE_INTERPOLATION_H
#define SRI_SPLINE_INTERPOLATION_H

#include "SRI/SRIAnimation/DoubleInterpolation.h"


namespace SRI{



class SRI_ANIMATION_API SplineInterpolation: public DoubleInterpolation{
	
private:

protected:
	double m_dTimeC1;
	double m_dTimeC2;
	double m_dValC1;
	double m_dValC2;

public:
	SplineInterpolation();
	virtual ~SplineInterpolation();

	SplineInterpolation(const SplineInterpolation& c);
	SplineInterpolation& operator=(const SplineInterpolation& c);

	double dGetValue(double time);

	//=========== from Cloneable interface ========================
	virtual Interpolation* ptClone() const;

	//=========== from serializable interface =====================

	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;

};

}


#endif