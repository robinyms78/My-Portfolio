#ifndef SRI_LUA_ENGINE_H
#define SRI_LUA_ENGINE_H

//#include "lua.hpp"

#include "SRI/LuaEngine/LuaEngineLib.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIString.h"

struct lua_State;

namespace SRI{

class SRIEngine;



class LE_API LuaEngine{

private:
	Logger m_tLog;
	lua_State* m_ptLua;;
	bool m_bIsExternallyManaged;

	LuaEngine(const LuaEngine& c);
	LuaEngine& operator=(const LuaEngine& c);


public:
	LuaEngine();
	virtual ~LuaEngine();

	lua_State* ptGetState();
	/** With this function the luaStack can be set. If the isExternallyManaged flag is true,
	* the engine won't clsoe the state when the engine is destroyed
	*/
	void vSetLuaState(lua_State* state, bool isExternallyManaged);

	/** Runs the given script. It returns an error message and pops all results 
	* from the stack to maintain stacksize */
	virtual int iRunScript(SRI::String script);
	virtual int iRunScriptFile(SRI::String fileName);

	/** Executes the script. It expects that nargs parameters have been pushed to the stack
	* The number of return parameters is adjusted to nResults */
	virtual int iExecuteScript(SRI::String script, int nArgs, int nResults);

	/** This is a convenience function to log lua errors using the global SRI logger system.
	* When a lua_pcall encounters an error it pushes an error message on the stack.
	* This function logs this error message and pops it from the stack*/
	void vLogLuaCallError(const char* pszFormat, ...);

	/** removes the item at given stack pos*/
	int iLuaRemove(int idx);
	
	bool bGetAsBool(int idx);
	double dGetAsNumber(int idx);
	SRI::String szGetAsString(int idx);


};


}// End namespace

#endif
