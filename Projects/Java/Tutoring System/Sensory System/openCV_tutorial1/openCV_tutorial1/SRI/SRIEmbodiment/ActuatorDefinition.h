#ifndef SRI_ACTUATOR_DEFINITION_H
#define SRI_ACTUATOR_DEFINITION_H

#include "SRI/SRIEngine/ComponentDefinition.h"
#include "SRI/SRIEmbodiment/SRIEmbodimentLib.h"
#include "SRI/SRIUtil/SRIString.h"


namespace SRI{


class EMBODIMENT_API ActuatorDefinition: public SRI::ComponentDefinition{

protected:
	SRI::String m_szActuationType;

public:
	ActuatorDefinition();
	ActuatorDefinition(SRI::String name, SRI::String type, SRI::String config);
	ActuatorDefinition(SRI::String name, SRI::String type, SRI::String config, SRI::String actuationType);
	virtual ~ActuatorDefinition();
	ActuatorDefinition(const ActuatorDefinition& c);
	ActuatorDefinition& operator=(const ActuatorDefinition& c);
	virtual bool operator==(const ActuatorDefinition& c);

	virtual void vSetActuationType(SRI::String actType);

	virtual SRI::String szGetActuationType();

	SRI::Definition* ptClone() const;

	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;
};

}


#endif
