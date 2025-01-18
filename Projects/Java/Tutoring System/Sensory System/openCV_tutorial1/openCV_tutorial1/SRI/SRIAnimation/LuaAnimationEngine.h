#ifndef SRI_LUA_ANIMATION_ENGINE_H
#define SRI_LUA_ANIMATION_ENGINE_H

#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/Logger/Logger.h"

#ifdef SRI_USE_LUA

#include "SRI/SRIExtensions/LuaPointerHandle.h"
extern "C"
{
   #include <lua.h>
   #include <lauxlib.h>
   #include <lualib.h>
}

#define LUA_ANIMATION_ENGINE_T "AnimationEngine"

namespace SRI{

class AnimationEngine;

namespace LuaAnimation{



/** call AM:play(animName)  
*   play(AM, animName)
*/
int iPlayAnimation(lua_State* L);
int iSetEmbodiment(lua_State* L);
int iSetEmbodimentDef(lua_State* L);
int iCloseEmbodiment(lua_State* L);
int iLoadAnimation(lua_State* L);
int iCloseAnimation(lua_State* L);
int iStopAnimation(lua_State* L);
int iPauseAnimation(lua_State* L);

static const struct luaL_reg AnimationEngineApi[] = {
	{"loadAnimation", iLoadAnimation},
	{"playAnimation", iPlayAnimation},
	{"stopAnimation", iStopAnimation},
	{"pauseAnimation", iPauseAnimation},
	{"closeAnimation", iCloseAnimation},
	{"setEmbodiment", iSetEmbodiment},
	{"setEmbodimentDef", iSetEmbodimentDef},
	{"closeEmbodiment", iCloseEmbodiment},
	{NULL, NULL} /*sentinel*/
};

//============== Helper function for Lua object ==================================

static Logger g_tLog("LuaComponentApi", LOG_DEBUG);

void vSetGlobalAnimationEngine(lua_State* L, SRI::AnimationEngine* ae, bool isLuaHandled);
/** \returns the number of objects left on stack (should be 1) */
int iCreateLuaAnimationEngineStub(lua_State* L);
/** \returns SRI error code */
int iFillAnimationEngineStub(lua_State* L, AnimationEngine* ae, bool isLuaHandled);
SRI::AnimationEngine* ptGetAninmationEngine(lua_State* L, int idx);
SRI::LuaPointerHandle<SRI::AnimationEngine>* ptGetAnimationEngineHandle(lua_State* L, int idx);

}// end animation namespace


}// end SRI namespace

extern "C" {
	SRI_ANIMATION_API int luaopen_LuaAnimationEngine(lua_State* L);
}

#endif  // use of lua

#endif