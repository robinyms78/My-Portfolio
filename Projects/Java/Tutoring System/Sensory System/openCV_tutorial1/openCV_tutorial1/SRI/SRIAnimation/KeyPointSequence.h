#ifndef SRI_KEYPOINT_SEQUENCE_H
#define SRI_KEYPOINT_SEQUENCE_H

#include "SRI/SRIAnimation/SRIAnimationLib.h"
//#pragma warning(disable: 4251)
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/Serializable.h"
#include "SRI/SRIAnimation/KeyPoint.h"


/**
	* This is a Keypoint Sequence contains a list of keypoints that will be needed for animation
	* Keypoints can be added or remove from the list and the whole list can be extracted and used for animation purpose.
	* \Remarks
	* \see 
	* \param 
	* \returns 
	* \date 2012-01-06 
	* \author Chin
	*/
//------------------------------------------------------------------------------

namespace SRI{


/** KeyPointSequences are a container to hold keyPoints. Wheras KeyPoints define an order
* through a linked list, KeyPointSequences add access using time values. Every KeyPoint has
* a time at which it defines the state of the actuator. For a sequences, this time must be
* greater than zero. That means that the first KeyPoint can earliest be at time zero (no
* timewarp backwards in time is allowed). However, the first KeyPoint can also only start
* at time t = 3000 (3 seconds). 
* On construction of the KeyPointSequences it has to be made sure that at one given time
* only one KeyPoint is defined. 
*/
class SRI_ANIMATION_API KeyPointSequence {

private:
	static int m_iKeyPointIdCount;

	SRI::Logger m_tLog;
	Ref<KeyPoint> m_ptFirstKey;
	Ref<KeyPoint> m_ptLastKey;

	SRI::String m_szStateType; // only keypoints with same type should be added
	SRI::String m_szName;

protected:
	virtual SRI::String szCreateKeyPointId();

public:
	KeyPointSequence(SRI::String name, SRI::String stateType);
	virtual ~KeyPointSequence (void);
	KeyPointSequence(const KeyPointSequence& c);//copy ctor
	KeyPointSequence& operator=(const KeyPointSequence& c);

	/**
	* This fucntion get the Keypoint that is the last to occur before the given time.
	* 
	* \Remarks
	* \see 
	* \param the timing for the keypoint
	* \returns Keypoint pointer
	*/
	Ref<KeyPoint> ptGetKeyPoint(SRI::TimeStamp time);


	/**
	* This function add new Keypoint into the Keypoint sequence list. 
	* 
	* \Remarks
	* \see 
	* \param pointer of the new keypoint to be added
	* \returns 0 for success, -1 for error
	*/
	int iInsertKeyPoint(Ref<KeyPoint> key);


	/**
	* This function remove Keypoint from the Keypoint sequence list. 
	* user need to input the pointer oft he keypoint to be removed
	* \Remarks
	* \see 
	* \param pointer of the keypoint tobe remved
	* \returns 0 for success, -1 for error
	*/
	int iRemoveKeyPoint(Ref<KeyPoint> kp);

	/** returns true if the given keypoint is a memeber of the sequence*/
	bool bIsInSequence(Ref<KeyPoint> kp);

	Ref<KeyPoint> ptGetFirst() const;
	Ref<KeyPoint> ptGetLast() const;

	/** KeyPoints are organized in a linked list, which defines an order over the KeyPoints.
	* This function returns a key given its index position in the list 1st, 2nd, 3rd irrespective
	* of the time of the KeyPoint. The index starts at 0.*/
	Ref<KeyPoint> ptGetKeyAtIndex(int index) const;

	virtual bool bIsEmpty() const; 

	/** Returns the start time of the keyPoint sequence. A valid value is greater than zero.
	* If the sequence is empty -1 is returned. */
	virtual SRI::TimeStamp tGetStartTime() const;

	/** Returns the time difference between the last and the first keyPoint. If the sequence is empty it
	* returns 0. */
	virtual TimeStamp tGetDuration() const;

	virtual TimeStamp tGetEndTime() const;

	/** Retruns the number of keyPoints in this sequence */
	virtual int iGetSize() const; 


	virtual SRI::String szGetStateType() const;
	virtual SRI::String szGetName() const;

	//================ Interface Cloneable ============================================
	virtual KeyPointSequence* ptClone() const;

	//================ Interface from Serializable ====================================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;
	static const char* szGetClassType();
};





}

#endif