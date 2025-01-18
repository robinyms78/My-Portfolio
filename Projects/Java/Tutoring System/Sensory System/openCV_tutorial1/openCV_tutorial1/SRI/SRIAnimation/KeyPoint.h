#ifndef SRI_KEYPOINT_H
#define SRI_KEYPOINT_H

#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/SRIEmbodiment/ActuatorState.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIAnimation/Interpolation.h"
#include "SRI/SRIUtil/SRITime.h"
#include "SRI/Logger/Logger.h"

//------------------------------------------------------------------------------

namespace SRI{

class KeyPoint;

INST_SRI_ANIMATION_TEMPL SRI::Ref<SRI::KeyPoint>;
INST_SRI_ANIMATION_TEMPL Ref<Interpolation>;

/** A KeyPoint defines an actuator state for a given interval. The time is 
* always relative to a KeyPointAnimation. That is, zero is
* when the KeyPointAnimation starts. A time of t= 3000 (3 second) would define the KeyPoint 
* three seconds after the KeyPointAnimation has started.  
*
*/
class SRI_ANIMATION_API KeyPoint {

friend class KeyPointSequence;

private: 
	
	SRI::TimeStamp m_tTime;
	Ref<KeyPoint> m_ptSelfRef;
	SRI::String m_szId;
	SRI::Logger m_tLog;
	
	/** Function is called by KeyPoint sequence to give it a unique ID wihtin the sequence */

protected:
	Ref<Interpolation> m_ptInterpolation;
	Ref<KeyPoint> m_ptNextKeyPoint;
	Ref<KeyPoint> m_ptPreviousKeyPoint;
	void vSetId(SRI::String id);
	SRI::Ref<ActuatorState> m_ptActuatorState; 

 public:

	KeyPoint();
	KeyPoint(SRI::TimeStamp time, SRI::Ref<ActuatorState> state = SRI::Ref<ActuatorState>());
	virtual ~KeyPoint();

	KeyPoint(const KeyPoint& c);//copy ctor
	KeyPoint& operator=(const KeyPoint& c);
	
	virtual bool operator==(const KeyPoint& c) const;
	virtual bool operator!=(const KeyPoint& c) const;
	virtual SRI::String szGetStateType() const;

/**
	* This fucntion get the ID for the state, normally in numeric form but it can be set as any alpha numeric as well.
	*  
	* \Remarks
	* \see 
	* \param void
	* \returns The ID of the state
	*/
	virtual SRI::String szGetId();

/**
	* This fucntion get the time that is set for the keypoint.
	*  
	* \Remarks
	* \see 
	* \param void
	* \returns The timing of the keypoint
	*/
	virtual SRI::TimeStamp tGetTime();
		
/**
	* This fucntion set the time that is set for the keypoint.
	*  
	* \Remarks
	* \see 
	* \param The timing for the Keypoint
	* \returns void
	*/
	virtual void vSetTime(SRI::TimeStamp time);

/**
	* This fucntion get the actuator state(eg.RoombaState) that is set for the keypoint.
	*  t == 0 returns the state at keypoint
	* \Remarks
	* \see 
	* \param void
	* \returns The Keypoint's actuator state
	*/
	virtual Ref<ActuatorState> ptGetActuatorState(SRI::TimeStamp time);
	/** Retruns the state that is stored with the keyPoint (at time 0) */
	virtual Ref<ActuatorState> ptGetKeyActuatorState();
	
/**
	* This fucntion set the actuator state(eg.RoombaState) that is set for the keypoint.
	*  
	* \Remarks
	* \see 
	* \param The Keypoint's actuator state
	* \returns Void
	*/
	virtual void vSetActuatorState(SRI::Ref<ActuatorState> curr);
	virtual int iSetInterpolation(Ref<Interpolation> interpolation);
	virtual Ref<Interpolation> ptGetInterpolation();

  /**
	* This fucntion get the next actuator state(eg.RoombaState) that is set for the keypoint.
	*  A NULL means it is the ending keypoint
	* \Remarks
	* \see 
	* \param Void
	* \returns The Keypoint's next actuator state
	*/
	virtual Ref<KeyPoint> ptGetNextKeyPoint();

 /**
	* This fucntion get the next actuator state(eg.RoombaState)  for the keypoint.
	*   A NULL means it is the ending keypoint
	* \Remarks
	* \see 
	* \param The Keypoint's next actuator state
	* \returns Void
	*/
	virtual void vSetNextKeyPoint(Ref<KeyPoint> next);
 
  /**
	* This fucntion get the previous actuator state(eg.RoombaState) that is set for the keypoint.
	*  A NULL means it is the starting keypoint
	* \Remarks
	* \see 
	* \param Void
	* \returns The Keypoint's previous actuator state
	*/
	virtual Ref<KeyPoint> ptGetPrevKeyPoint();

 /**
	* This fucntion get the previous actuator state(eg.RoombaState)  for the keypoint.
	*   A NULL means it is the starting keypoint
	* \Remarks
	* \see 
	* \param The Keypoint's previous actuator state
	* \returns Void
	*/
	virtual void vSetPrevKeyPoint(Ref<KeyPoint> prev);

	

	/** Creates a unique random ID*/
	static SRI::String szCreateId();

	//================ Interface Cloneable ============================================
	virtual KeyPoint* ptClone() const;

	//================ Interface from Serializable ====================================
	static const char* szGetClassType();
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;


};
 

}
 
#endif 
 
 
   
 
    
 //---------------------------------------------------------------------------


