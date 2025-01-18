#ifndef SRI_SENSOR_DEFINITION_H
#define SRI_SENSOR_DEFINITION_H

#include "SRI/SRIEngine/ComponentDefinition.h"
#include "SRI/SRIAgent/SRIAgentLib.h"
#include "SRI/SRIUtil/SRIString.h"

namespace SRI{

class AGENT_API SensorDefinition: public SRI::ComponentDefinition{
private:
	SRI::String m_szSensingType;


public:
	SensorDefinition();
	SensorDefinition(SRI::String name, SRI::String type, SRI::String config);
	SensorDefinition(SRI::String name, SRI::String type, SRI::String config, SRI::String sensingType);
	virtual ~SensorDefinition();
	SensorDefinition(const SensorDefinition& c);
	SensorDefinition& operator=(const SensorDefinition& c);
	virtual bool operator==(const SensorDefinition& c);

	
	virtual void vSetSensingType(SRI::String sensType);
	virtual SRI::String szGetSensingType();

	SRI::Definition* ptClone() const;

	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;
};

}


#endif