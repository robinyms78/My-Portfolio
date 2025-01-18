#ifndef SRI_PORTDEFINITION_H
#define SRI_PORTDEFINITION_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/Serializable.h"
#include "SRI/SRIEngine/Definition.h"

namespace SRI{

class SRI_E_API PortDefinition: public SRI::Definition{

public:
	typedef enum{
		NO_DIRECTION = -1,
		INPUT = 0,
		OUTPUT = 1
	}tPortDirection;

	static SRI::String szDirectionToString(tPortDirection dir);
	static tPortDirection eDirectionFromString(SRI::String dir);

private:
	SRI::String m_szPortDataType;
	tPortDirection m_ePortDirection;

public:
	PortDefinition();
	PortDefinition(SRI::String name, SRI::String portDataType, tPortDirection direction = PortDefinition::NO_DIRECTION);
	virtual ~PortDefinition();
	PortDefinition(const PortDefinition& c);
	PortDefinition& operator=(const PortDefinition& c);

	virtual bool operator==(const PortDefinition& c) const;
	virtual bool operator!=(const PortDefinition& c) const;
	
	virtual Definition* ptClone() const;

	void vSetPortDataType(SRI::String type);
	SRI::String szGetPortDataType() const;
	tPortDirection eGetPortDirection() const;

	//================ Interface from Serializable ====================================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;

};

}

#endif