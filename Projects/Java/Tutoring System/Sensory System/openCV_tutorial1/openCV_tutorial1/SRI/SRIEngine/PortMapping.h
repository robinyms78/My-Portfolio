#ifndef SRI_PORT_MAPPING_H
#define SRI_PORT_MAPPING_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIUtil/SRIString.h"

namespace SRI{

class SRI_E_API PortMapping{

protected:
	SRI::String m_szSourceComponentName;
	SRI::String m_szSourceComponentType;
	SRI::String m_szSourcePortName;
	SRI::String m_szTargetComponentName;
	SRI::String m_szTargetComponentType;
	SRI::String m_szTargetPortName;

public:
	PortMapping();
	PortMapping(SRI::String srcCompName, SRI::String srcPortName, SRI::String targetCompName, SRI::String targetPortName);
	PortMapping(SRI::String srcCompName, SRI::String srcCompType, SRI::String srcPortName, SRI::String targetCompName, SRI::String targetCompType, SRI::String targetPortName);
	virtual ~PortMapping();

	PortMapping(const PortMapping& c);
	PortMapping& operator=(const PortMapping& c);

	bool operator==(const PortMapping& c) const;
	bool operator!=(const PortMapping& c) const;

	virtual SRI::String szGetSourceComponentName() const;
	virtual SRI::String szGetTargetComponentName() const;
	virtual SRI::String szGetSourcePortName() const;
	virtual SRI::String szGetTargetPortName() const;
	virtual SRI::String szGetSourceComponentType() const;
	virtual SRI::String szGetTargetComponentType() const;

	virtual void vSetSourceComponentName(SRI::String name);
	virtual void vSetTargetComponentName(SRI::String name);
	virtual void vSetSourcePortName(SRI::String name);
	virtual void vSetTargetPortName(SRI::String name);
	virtual void vSetSourceComponentType(SRI::String type);
	virtual void vSetTargetComponentType(SRI::String type);

	virtual PortMapping* ptClone() const;

	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;
};

}




#endif

