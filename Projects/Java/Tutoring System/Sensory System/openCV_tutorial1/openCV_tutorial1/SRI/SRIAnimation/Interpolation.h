#ifndef SRI_INTERPOLATION_H
#define SRI_INTERPOLATION_H

#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/SRIUtil/Serializable.h"
#include "SRI/SRIEmbodiment/ActuatorState.h"
#include "SRI/SRIUtil/SRITime.h"


namespace SRI{

class KeyPoint;

class SRI_ANIMATION_API Interpolation: public Serializable{
	friend class KeyPoint;
private:

protected:
	SRI::TimeStamp m_tEndTime;
	SRI::String m_szInterpolationType;
	
	SRI::Ref<SRI::ActuatorState> m_ptStartState;
	SRI::Ref<SRI::ActuatorState> m_ptEndState;

	virtual void vSetInterpolationType(SRI::String type);

	SRI::KeyPoint* m_ptParentKey;

	void vSetParentKeyPoint(SRI::KeyPoint* key);

public:
	Interpolation();
	virtual ~Interpolation();

	Interpolation(const Interpolation& c);
	Interpolation& operator=(const Interpolation& c);

	/** Used by KeyPoint to update references */
	virtual void vSetEndTime(SRI::TimeStamp endTime);
	virtual void vSetStartState(SRI::Ref<SRI::ActuatorState> startState);
	virtual void vSetEndState(SRI::Ref<SRI::ActuatorState> endState);
	
	virtual SRI::Ref<ActuatorState> ptGetActuatorState(TimeStamp time);
	virtual SRI::String szGetInterpolationType() const;
	
	//=========== from Cloneable interface ========================
	virtual Interpolation* ptClone() const;

	//=========== from serializable interface =====================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;

};

}


#endif