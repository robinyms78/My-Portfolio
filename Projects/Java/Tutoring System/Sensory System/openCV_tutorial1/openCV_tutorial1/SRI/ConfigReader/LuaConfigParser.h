#ifndef SRI_LUA_CONFIG_PARSER_H
#define SRI_LUA_CONFIG_PARSER_H

#ifdef SRI_USE_LUA	

#include "SRI/ConfigReader/ConfigParser.h"
#include "SRI/Logger/Logger.h"
#include "SRI/LuaEngine/LuaEngine.h"

namespace SRI{

class LuaConfigParser: public ConfigParser{

private:
	Logger m_tLog;
	LuaEngine m_tLua;

protected:
	/**calls lua parsePath and leaves the result on top of stack.
	* \returns error code if function fails */
	int iParsePath(SRI::String configPath);
	void vLogLuaError(lua_State* L, const char* fmt, ...);

public:
	LuaConfigParser();
	~LuaConfigParser();
	LuaConfigParser(const LuaConfigParser& c);
	LuaConfigParser operator=(const LuaConfigParser& c);

	virtual ConfigParser* ptClone();
	virtual int iReadString(SRI::String config);
	virtual int iReadFile(SRI::String fileName);

	virtual SRI::String szEvalQuery(const SRI::String& query);

	virtual bool bHasParameter(const SRI::String& configPath);
	//virtual int iGetConfigNodes(const SRI::String& configPath, ConfigNode& node);

	virtual bool bGetBoolValue(const SRI::String& configPath);
	virtual int iGetIntValue(const SRI::String& configPath);
	virtual double dGetDoubleValue(const SRI::String& configPath);
	virtual SRI::String szGetStringValue(const SRI::String& configPath);
	virtual SRI::Ref<SRI::ConfigNode> ptGetNode(const SRI::String& configPath);
	virtual SRI::Ref<SRI::ConfigNodeSet> ptGetNodeSet(const SRI::String& configPath);
};

}


#endif



#endif