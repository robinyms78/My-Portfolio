#ifndef SRI_DEFINITION_H
#define SRI_DEFINITION_H

/** A definition holds a textual representation of a software component */

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIUtil/SRIString.h"

namespace SRI{

class SRI_E_API Definition{

private:

protected:
	SRI::String m_szName;
	SRI::String m_szDefType;
	SRI::String m_szConfig;

	/** Definition type should be set from within the class definition */
	virtual void vSetDefinitionType(SRI::String type);

public:
	Definition();
	Definition(SRI::String name, SRI::String defType, SRI::String config);
	Definition(const Definition& c);
	Definition& operator=(const Definition& c);
	virtual ~Definition();

	bool operator==(const Definition& c) const;
	bool operator!=(const Definition& c) const;

	virtual void vSetName(SRI::String name);
	virtual void vSetConfig(SRI::String config);
	

	virtual SRI::String szGetDefinitionType() const;
	virtual SRI::String szGetName() const;
	virtual SRI::String szGetConfig() const;

	virtual Definition* ptClone() const;

	//================ Interface from Serializable ====================================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual const char* szGetObjType() const;

};


}



#endif