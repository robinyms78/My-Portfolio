#ifndef LUA_COMPONENT_H
#define LUA_COMPONENT_H


#include "SRI/LuaComponent/LuaComponentLib.h"
#include "SRI/SRIEngine/SRIPlugin.h"
#include "SRI/SRIExtensions/LuaPointerHandle.h"
#include "SRI/SRIEngine/ReactiveComponent.h"


extern "C"
{
   #include <lua.h>
   #include <lauxlib.h>
   #include <lualib.h>
}

#define LUA_COMPONENT_T "Component"   // typename of a component within Lua
#define LUA_INPUTPORT_T "InputPort"  
#define LUA_OUTPUTPORT_T "OutputPort"

#define ID_SIZE 80

/** Goal: 
* myComponent = SRI.createComponent("MyComponent");
*
* function myComponent:step() 
*    -- self:super():step(); TODO who calls the base class??
* end
* 
* // in C
* LuaComponent c = getPointer(LUA);   // It must exist
*
* c->Step();
*
*   //myComponent = Util.createClass("MyComponent"); 
*   //Util.inherit(myComponent, SRI.createComponent); 
*
**/ 


namespace SRI{

class LuaEngine;

/** This class implements the component interface and calls
 * the functions as defined in Lua 
 * A lua component might be generated using a C++ factory or a Lua factory
 */
class SRI_PLUGIN_API LuaComponent: public SRI::ReactiveComponent{ 

private:
	LuaEngine* m_ptLua;
	//lua_State* m_ptLuaState; //convenience access pointer (managed by LuaEngine class)

	Logger m_tLog;
	SRI::String m_szLuaRegId;
	SRI::String m_szLuaSrc;   // encodes lua src: if starting with @its filename, otherwise it is src

	int iCallLuaExtension(const char* fncName);

	/** assumes that the definition function is already on the stack*/
	int iCallLuaComponentDefinition();

	/** After executing a lua script, this function binds the result to this object*/
	int iBindLuaComponent();

	int iLoadLibraries();

	int iCreateLuaTable();

protected:
	/** This function is called when a component gets added to an engine. */
	virtual int iSetEngineHandle(Ref<EngineHandle> handle);
	


public:
	LuaComponent(SRI::String name);
	virtual ~LuaComponent();

	/** Be careful with using the copy. The LuaEngine is NOT copied. The lua src need to be evaluated again.
	*/
	LuaComponent(const LuaComponent& c);
	LuaComponent& operator=(const LuaComponent& c);

	SRI::String szGetLuaSrc() const;

	/** Delegates handling of an associated lua_State to the LuaEngine
	* All Lua objects have to be reset manually in the given new lua_state.
	*/
	virtual void vSetLuaState(lua_State* engine, bool isExternallyManaged);

	/** This function assumes that the lua component table is ontop of the stack.
	* It sets the lua table for the c++ object so that the lua functions can be found
	* when calling object functions.
	*/
	int iAssociateLuaTable();

	/** Sets the LuaRegistry table entry of current ID to nil*/
	int iBreakLuaTableAssociation();
	
	/** These functions assume to receive a table witht the component functions */
	int iLoadComponentScript(SRI::String script);
	int iLoadComponentScriptFile(SRI::String fileName);

	lua_State* ptGetLuaState();
	LuaEngine* ptGetLuaEngine();

	virtual Component* ptClone() const;
	/** Creates a luaobject to represent a port. It leaves the object on the stack
	* If there is an error it leaves nothing on the stack and returns an error code*/
	int iCreateLuaOutputPort(lua_State* L, SRI::String name);
	int iCreateLuaInputPort(lua_State* L, SRI::String name);

	virtual void vInit();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();
	virtual bool bHasMoreSteps();
	virtual void vFinalize();
};



}



namespace SRI{
	namespace LuaComponentApi{

	static Logger g_tLog("LuaComponentApi", LOG_DEBUG);


/** This function checks if at the given index a valid LuaComponent table is stored.
* If the table is valid it returns a pointer to the C++ type; otherwise NULL.
* The function calls Lua error ungracefully in case of error */
SRI::LuaComponent* ptGetComponent(lua_State* L, int idx);

/** Function returns the Pointer handle as it is associated in Lua.
*/
LuaPointerHandle<SRI::LuaComponent>* ptGetComponentHandle(lua_State* L, int idx);

/** This function also checks if at the given index a valid component is stored.
* However, in case the type is not valid, it returns an error code without 
* calling lua_error */
int iCheckComponent(lua_State* L, int idx);

/** A helper function to initialize the lua data structure
* This function requires that the table that holds the lua version of a component is on top of the stack.
* The parameter isLuaHandled controls if the C++ component is memory controlled by lua or not.
*/
int iSetComponent(lua_State* L, SRI::LuaComponent* c, bool isLuaHandled);

/** Helper function to just create a table to hold the luaComponet.
* */
int iCreateComponentTable(lua_State* L);


/** This function is the __gc() function in the meta table for the udata*/
int iReleaseComponent(lua_State* L);


// Component functions
int iInit(lua_State* L);
int iStep(lua_State* L);
int iPreStep(lua_State* L);
int iPostStep(lua_State* L);
int iHasMoreSteps(lua_State* L);
int iSetName(lua_State* L);
int iSetComponentType(lua_State* L);

/** The function expects a valid luaComponent as first parameter, name and type as second and third.
* It returns 0 on success or an error code and an error message otherwise
* iCreateOutputPort(component: luaComponent, name:string, type:string) -> number
*/
int iCreateOutputPort(lua_State* L);
/** The function expects a valid luaComponent as first parameter, name and type as second and third.
* It returns 0 on success or an error code and an error message otherwise
* iCreateInputPort(component: luaComponent, name:string, type:string) -> number
*/
int iCreateInputPort(lua_State* L);



//SRI interface
int iCreateComponent(lua_State* L);

//Port helper functions
int iCheckLuaInputPort(lua_State* L, int idx);
Ref<InputPort> tGetInputPort(lua_State* L, int idx);
int iCheckLuaOutputPort(lua_State* L, int idx);
Ref<OutputPort> tGetOutputPort(lua_State* L, int idx);


//Port Interface functions
int iReceive(lua_State* L);
/** Expects a LuaOutputPort as first(self) parameter and a string as message
* It returns an error code (0== SRI_OK in case of success)*/
int iSend(lua_State* L);

int iGetOutputPort(lua_State* L);
int iGetInputPort(lua_State* L);
int iIgnorePortTableAssign(lua_State* L);


static const struct luaL_reg ComponentObjApi[] = {
  {"init", iInit},
  {"step", iStep},
  {"preStep", iPreStep},
  {"postStep", iPostStep},
  {"hasMoreSteps", iHasMoreSteps},
  {"createOutputPort", iCreateOutputPort},
  {"createInputPort", iCreateInputPort},
  {"setName", iSetName},
  {"setComponentType", iSetComponentType},
  {NULL, NULL}
};


static const struct luaL_reg ComponentApi[] = {
  {"createComponent", iCreateComponent},
  {NULL, NULL} /*sentinel*/
};

static const struct luaL_reg OutputPortObjApi[] = {
	{"send", iSend},
	{NULL, NULL}
};

static const struct luaL_reg InputPortObjApi[] = {
	{"receive", iReceive},
	{NULL, NULL}
};


} // end namespace LuaComponent

}//namespace SRI

extern "C" {
	LUA_PACKAGE_API int luaopen_LuaComponentApi(lua_State* L);
}




#endif
