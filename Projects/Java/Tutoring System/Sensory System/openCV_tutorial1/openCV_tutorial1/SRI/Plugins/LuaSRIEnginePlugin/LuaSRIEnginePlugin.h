#ifndef LUA_SRI_ENGINE_PLUGIN_H
#define LUA_SRI_ENGINE_PLUGIN_H

#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/SRIEngine.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIEngine/SRIEnginePlugin.h"
#include "SRI/LuaEngine/LuaEngine.h"
#include "SRI/SRIEngine/InputPort.h"


extern "C"
{
   #include <lua.h>
   #include <lauxlib.h>
   #include <lualib.h>
}


namespace SRI{

class EngineHandle;

INST_TEMPLATE SRI::Ref<InputPort>;

/** This class implements the component interface and calls
 * the functions as defined in Lua 
 * A lua component might be generated using a C++ factory or a Lua factory
 */
class SRI_PLUGIN_API LuaSRIEnginePlugin: public SRI::ReactiveComponent{ 

private:
	LuaEngine* m_ptLua;
	//lua_State* m_ptLuaState; //convenience access pointer (managed by LuaEngine class)
	SRI::Ref<InputPort> m_ptCommandInputPort; 
	Logger m_tLog;
	SRI::Ref<SRI::SRIEngine> m_ptEngine;
	
	void vInitLua();

protected:
	///** This function is called when a component gets added to an engine. */
	//virtual int iSetEngineHandle(Ref<EngineHandle> handle);

public:
	LuaSRIEnginePlugin(SRI::String name, SRI::Ref<SRIEngine> engine = SRI::Ref<SRI::SRIEngine>((SRIEngine*)NULL));
	virtual ~LuaSRIEnginePlugin();

	virtual void vSetLuaState(lua_State* engine, bool isExternallyManaged);
	LuaEngine* ptGetLuaEngine();
	
	int iRunScript(SRI::String script);
	int iRunScriptFile(SRI::String fileName);

	virtual void vInit();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();
	virtual bool bHasMoreSteps();
	virtual void vFinalize();
};



}



#endif