#ifndef SRI_MOTOR_KEYPOINT_H
#define SRI_MOTOR_KEYPOINT_H

#include "SRI/SRIAnimation/KeyPoint.h"
#include "SRI/SRIEmbodiment/MotorState.h"
#include "SRI/SRIAnimation/DoubleInterpolation.h"

namespace SRI{

class SRI_ANIMATION_API MotorKeyPoint: public KeyPoint{

private:

protected:

public:
	MotorKeyPoint();
	MotorKeyPoint(TimeStamp time);
	virtual ~MotorKeyPoint();

	MotorKeyPoint(const MotorKeyPoint& c);
	MotorKeyPoint& operator=(const MotorKeyPoint& c);

	virtual KeyPoint* ptClone() const;

	virtual Ref<ActuatorState> ptGetActuatorState(SRI::TimeStamp time);

	//================ Interface from Serializable ====================================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;
};

}


#endif