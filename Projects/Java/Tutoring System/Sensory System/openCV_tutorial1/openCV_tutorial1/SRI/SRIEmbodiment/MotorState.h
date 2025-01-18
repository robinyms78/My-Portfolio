#ifndef SRI_POSITION_SERVO_STATE_H
#define SRI_POSITION_SERVO_STATE_H

#include "SRI/SRIEmbodiment/SRIEmbodimentLib.h"
#include "SRI/SRIEmbodiment/ActuatorState.h"

#define DOUBLE_ERROR_MARGIN 0.000001

namespace SRI{

class EMBODIMENT_API MotorState: public ActuatorState{

private:

protected:
	double m_dPosition;

public:

	MotorState();
	MotorState(double pos);
	virtual ~MotorState();

	MotorState(const MotorState& c);
	MotorState& operator=(const MotorState& c);
	MotorState& operator=(double pos);
	bool operator==(const MotorState& c);
	bool operator==(double pos);
	bool operator!=(const MotorState& c);
	bool operator!=(double pos);
	operator double() const; // cast class to double

	//=========== from Cloneable interface ========================
	virtual ActuatorState* ptClone() const;

	//=========== from serializable interface =====================

	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;

	double dGetPosition() const;
	void vSetPosition(double pos);

};

}

#endif
