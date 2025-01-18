#ifndef LUA_SRI_ENGINE_H
#define LUA_SRI_ENGINE_H

#include "SRI/LuaSRIEngine/LuaSRIEngineLib.h"

#include "SRI/SRIEngine/SRIEngine.h"
#include "lua.hpp"
#include "SRI/SRIExtensions/LuaPointerHandle.h"


#define LUA_SRIENGINE_T "LuaSRIEngine"

namespace SRI{

/** The LuaSRIEngine is a wrapper that exposes the SRIEnginge functionality to LUA
*/
 namespace LuaSRIEngine{

//=============== Helper functions ===========================================
//SRI::Logger g_SRILuaLog("SRILuaLog", SRI::LOG_DEBUG);


/** Function creates a Lua table[class] of type "SRIEngine" and leaves it on the stack
* \returns SRI_OK in case of success; otherwise an error code. Nothing is left on the
* stack in case of error
*/
LUA_SRIENGINE_API int iCreateLuaSRIEngineStub(lua_State* L);

/** assumes that the table where to register is already on the stack*/
LUA_SRIENGINE_API int iSetSRIEngine(lua_State* L, SRI::SRIEngine* engine, bool isLuaHandled);

/** Function returns the Pointer handle as it is associated in Lua.
*/
LUA_SRIENGINE_API SRI::LuaPointerHandle<SRI::SRIEngine>* ptGetEngineHandle(lua_State* L, int idx);


/** Checks if there is a SRIEngien type at the given index. 
* \returns SRI_OK or an error code
*/
LUA_SRIENGINE_API int iCheckEngine(lua_State* L, int index);

/** Checks if there is an SRIEngine object at the given index and returns the reference.
* \returns In case of error it returns NULL and logs an error code.
*/
LUA_SRIENGINE_API SRI::SRIEngine* ptGetEngine(lua_State* L, int index);

/** Sets the global SRI.Engine field */
LUA_SRIENGINE_API int iRegisterGlobalEngine(lua_State* L, SRI::SRIEngine* engine);

//=============== SRI Interface ===============================================
/** Create a new lua managed engine. It expects a name as a parameter */
LUA_SRIENGINE_API int iCreateSRIEngine(lua_State* L);


//=============== Engine interface ============================================
int iStopEngine(lua_State* L);
int iInitEngine(lua_State* L);
int iRunEngine(lua_State* L);
int iStepEngine(lua_State* L);
int iFinalizeEngine(lua_State* L);


int iCreateComponent(lua_State* L);
int iRemoveComponent(lua_State* L);

int iReleaseEngine(lua_State* L);

static const struct luaL_reg luaSRIApi[] = {
	{"createEngine", iCreateSRIEngine},
	{NULL, NULL} /*sentinel*/
};


static const struct luaL_reg luaSRIEngineApi[] = {
	{"stopEngine", iStopEngine},
	{"initEngine", iInitEngine},
	{"runEngine", iRunEngine},
	{"stepEngine", iStepEngine},
	{"createComponent", iCreateComponent},
	{"removeComponent", iRemoveComponent},
	{NULL, NULL} /*sentinel*/
};

} // end LUASRIEngine namespace

}// end namespace SRI



#endif