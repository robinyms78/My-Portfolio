#ifndef SRI_LUA_SCRIPT_H
#define SRI_LUA_SCRIPT_H

#ifdef SRI_USE_LUA

#include "SRI/SRIExtensions/SRIExtensionsLib.h"
#include "SRI/SRIUtil/Serializable.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/Logger/Logger.h"

namespace SRI{



class SRI_EXT_API LuaScript: public Serializable{

private:
	Logger m_tLog;

protected:
	SRI::String m_szScript;

public:
	LuaScript(SRI::String script = "");
	virtual ~LuaScript();

	LuaScript(const LuaScript& c);
	LuaScript& operator=(const LuaScript& c);

	void vSetScript(SRI::String script);
	SRI::String szGetScript();

	virtual SRI::Serializable* ptClone() const;

	// ========  Interface from Serializable  ==================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	/** This returns a class type for serialization */
	virtual const char* szGetObjType() const;

	static const char* szGetClassType();

};


}

#endif

#endif


