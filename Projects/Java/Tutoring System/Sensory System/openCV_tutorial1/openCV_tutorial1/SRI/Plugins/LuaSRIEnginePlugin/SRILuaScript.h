#ifndef SRI_LUA_SCRIPT_H
#define SRI_LUA_SCRIPT_H

#include "SRI/SRIEngine/Serializable.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIEngine/SRIEnginePlugin.h"

namespace SRI{

class SRI_PLUGIN_API LuaScript: public Serializable{

private:

protected:
	SRI::String m_szScript;

public:
	LuaScript(SRI::String script = "");
	virtual ~LuaScript();

	LuaScript(const LuaScript& c);
	LuaScript& operator=(const LuaScript& c);

	void vSetScript(SRI::String script);
	SRI::String szGetScript();

	LuaScript* ptClone() const;

	// ========  Interface from Serializable  ==================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	/** This returns a class type for serialization */
	virtual const char* szGetObjType() const;

	static const char* szGetClassType();

};

}

#endif


