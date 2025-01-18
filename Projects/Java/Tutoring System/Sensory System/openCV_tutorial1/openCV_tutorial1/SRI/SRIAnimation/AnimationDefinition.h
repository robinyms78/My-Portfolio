#ifndef SRI_ANIMATION_DEFINITION_H
#define SRI_ANIMATION_DEFINITION_H

#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/SRIEngine/ComponentDefinition.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIList.h"
#include "SRI/SRIEngine/PortMapping.h"

namespace SRI{

INST_SRI_ANIMATION_TEMPL SRI::List<SRI::PortMapping>;

class SRI_ANIMATION_API AnimationDefinition: public SRI::ComponentDefinition{

protected:
	SRI::List<PortMapping> m_lPortMappings;

public:
	AnimationDefinition();
	AnimationDefinition(SRI::String name, SRI::String type, SRI::String config);

	virtual ~AnimationDefinition();
	AnimationDefinition(const AnimationDefinition& c);
	AnimationDefinition& operator=(const AnimationDefinition& c);
	virtual bool operator==(const AnimationDefinition& c);

	virtual void vSetName(SRI::String name);
	virtual void vSetActuatorType(SRI::String type);
	virtual void vSetConfig(SRI::String config);
	virtual void vSetPortMappings(SRI::List<PortMapping> t);

	virtual SRI::String szGetComponentType();
	virtual SRI::String szGetName();
	virtual SRI::String szGetConfig();
	virtual SRI::List<PortMapping> tGetPortMappings();

	virtual SRI::Definition* ptClone() const;

	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;
};

}


#endif