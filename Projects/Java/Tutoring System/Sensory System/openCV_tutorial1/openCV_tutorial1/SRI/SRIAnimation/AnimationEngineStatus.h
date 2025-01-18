#ifndef SRI_ANIMATION_ENGINE_STATUS_H
#define SRI_ANIMATION_ENGINE_STATUS_H

#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/SRIUtil/Serializable.h"

namespace SRI{

class SRI_ANIMATION_API AnimationEngineStatus: public Serializable{

private:
	SRI::String m_szEventType;
	SRI::String m_szAnimName;
	SRI::String m_szStatusValue;

public:
	AnimationEngineStatus();
	AnimationEngineStatus(SRI::String eventType, SRI::String statusValue, SRI::String animName = "");
	virtual ~AnimationEngineStatus();

	AnimationEngineStatus(const AnimationEngineStatus& c);
	AnimationEngineStatus& operator=(const AnimationEngineStatus& c);
	bool operator==(const AnimationEngineStatus& c) const;
	bool operator!=(const AnimationEngineStatus& c) const;

	Serializable* ptClone() const;

	SRI::String szGetEventType() const;
	SRI::String szGetStatusValue() const;
	SRI::String szGetAnimName() const;

	void vSetEventType(SRI::String eventType);
	void vSetStatusValue(SRI::String statusValue);
	void vSetAnimName(SRI::String animName);


	// ========= Serializable interface ========================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	/** Returns a string identifying the object type that is serialized */
	virtual const char* szGetObjType() const;
	static const char* szGetClassType();
};


}

#endif