#ifndef LUA_COMPONENT_FACTORY
#define LUA_COMPONENT_FACTORY


#include "SRI/LuaComponent/LuaComponentLib.h"
#include "SRI/SRIEngine/SRIPlugin.h"
#include "SRI/SRIEngine/ComponentFactory.h"
#include "SRI/SRIExtensions/LuaPointerHandle.h"
#include "SRI/Logger/Logger.h"
#include  "LuaEngine.h"

extern "C"
{
   #include <lua.h>
   #include <lauxlib.h>
   #include <lualib.h>
}

namespace SRI{


#define LUA_COMPONENTFACTORY_T "LuaComponentFactory"

class SRI_PLUGIN_API LuaComponentFactory: public ComponentFactory{

private:
	Logger m_tLog;
	LuaEngine* m_ptLua;

	SRI::String m_szLuaObjId;
	
	SRI::String m_szLuaSrc;   // encodes lua src: if starting with @its filename, otherwise it is src

	/** This function is a helper function to load a factory from lua code. It assumes that
	* the lua code is as a function on top of the stack */
	int iEvalFactoryScript();

	/** After executing a lua script, this function binds the result to this object*/
	int iBindLuaFactory();
	int iLoadLibraries();
	int iCreateLuaTable();

public:
	LuaComponentFactory(SRI::String name, SRI::String config = "");
	virtual ~LuaComponentFactory();
	LuaComponentFactory(const LuaComponentFactory& c);
	LuaComponentFactory& operator=(const LuaComponentFactory& c);

	void vSetLuaObjId(SRI::String objId);
	SRI::String szGetLuaObjId();

	int iLoadFactoryScript(SRI::String script);
	int iLoadFactoryScriptFile(SRI::String fileName);

	void vSetLuaState(lua_State* state, bool isExternallyManaged);

	/** This function assumes that the lua component table is ontop of the stack.
	* It sets the lua table for the c++ object so that the lua functions can be found
	* when calling object functions.
	*/
	int iAssociateLuaTable();
		
	/** Sets the LuaRegistry table entry of current ID to nil*/
	int iBreakLuaTableAssociation();

	lua_State* ptGetLuaState();
	LuaEngine* ptGetLuaEngine();

	virtual SRI::Ref<SRI::Component> ptCreateComponent(SRI::String name, SRI::String config = "");
};

} // end namespace SRI



namespace SRI{
	namespace LuaComponentFactoryApi{

	static Logger g_tLog("LuaComponentApi", LOG_DEBUG);



//ComponentFacotry Object API
int iSetComponentType(lua_State* L);

int iSetName(lua_State* L);

//SRI interface
int iCreateComponentFactory(lua_State* L);

/** Helper function to just create a table to hold the luaComponet.*/
int iCreateComponentFactoryTable(lua_State* L);


//Helper functions
int iCheckComponentFactory(lua_State* L, int idx);
SRI::LuaComponentFactory* ptGetComponentFactory(lua_State* L, int idx);
/** Function returns the Pointer handle as it is associated in Lua.
*/
LuaPointerHandle<SRI::LuaComponentFactory>* ptGetComponentFactoryHandle(lua_State* L, int idx);
/** This function is the __gc() function in the meta table for the udata*/
int iReleaseComponentFactory(lua_State* L);


int iSetComponentFactory(lua_State* L, SRI::LuaComponentFactory* c, bool isLuaHandled);



static const struct luaL_reg ComponentFactroyApi[] = {
  {"createComponentFactory", iCreateComponentFactory},
  {NULL, NULL}
};



static const struct luaL_reg ComponentFactroyObjApi[] = {
	{"setComponentType", iSetComponentType},
	{"setName", iSetName},
	{NULL, NULL}
};


} // end namespace LuaComponentFactory

}//namespace SRI



extern "C" {
	LUA_PACKAGE_API int luaopen_LuaComponentFactoryApi(lua_State* L);
}




#endif