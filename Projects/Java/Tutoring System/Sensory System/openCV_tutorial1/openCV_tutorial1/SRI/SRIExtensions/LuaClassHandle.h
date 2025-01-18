
#ifndef LUA_CLASSHANDLE_H
#define LUA_CLASSHANDLE_H

#include "SRI/SRIExtensions/SRILuaUtil.h"
#include "SRI/SRIExtensions/LuaPointerHandle.h"


#define LUA_CLASSHANDLE_DEF(TYPE) \
	int iCreate ## TYPE ## Stub(lua_State* L); \
	int iFill ## TYPE ## Stub(lua_State* L, TYPE* obj, bool isLuaHandled); \
	SRI::LuaPointerHandle<TYPE>* ptGetHandle(lua_State* L, int idx); \
	int iCheck ## TYPE (lua_State* L, int index); \
	TYPE* ptGet ## TYPE (lua_State* L, int index); \
	/**int iCreate ## TYPE ## Obj(lua_State* L);*/ \
	int iRelease ## TYPE (lua_State* L); \
	int iCreate ## TYPE ## MetaTable(lua_State* L);\



#define LUA_CLASSHANDLE_IMP(TYPE, OBJ_API) \
	/** returns the number of objects left on stack */ \
	int iCreate ## TYPE ## Stub(lua_State* L){ \
		if( L == NULL){ \
			LuaUtil::g_Log.error("Unable to create" #TYPE " stub: Lua is NULL"); \
			return SRI::SRI_ERR_NULL; \
		}\
		\
		lua_getglobal(L, "Util");\
		if(lua_isnil(L, -1)){ \
			LuaUtil::g_Log.error("Unable to create " #TYPE " stub: Util not loaded"); \
			lua_pop(L,1); \
			return luaL_error(L,"Unable to find Util table"); \
		}\
		\
		lua_getfield(L, -1, "createClass");\
		if(lua_isnil(L,-1)){\
			LuaUtil::g_Log.error("Unable to create " #TYPE " Stub: Util.createClass() method not found");\
			lua_pop(L,1); \
			return luaL_error(L,"Unable to find createClass function");\
		}\
		\
		lua_pushstring(L, #TYPE);\
		int res = lua_pcall(L,1,1, NULL);\
		if(res != 0){\
		SRI::vLogLuaError(L, LuaUtil::g_Log, "Unable to create " #TYPE " Stub: createClass failed:");\
			lua_pop(L, 1);\
			return luaL_error(L,"Unable to create " #TYPE " Stub: createClass failed:");\
		}\
		lua_remove(L, -2); /**  remove the Util class from the stack */ \
		\
		if(!lua_istable(L, -1)){ \
		LuaUtil::g_Log.error("Unable to create " #TYPE " stub: Util.createClass() failed"); \
			return luaL_error(L,"Unable to create table: createClass() failed"); \
		} \
		/** add functions to Engine table */\
		if(OBJ_API != NULL){\
			luaL_register(L, NULL, OBJ_API);\
		}\
		\
		return 1;\
	}\
	\
	\
	\
	/** assumes that the table where to register is already on the stack*/\
	int iFill ## TYPE ## Stub(lua_State* L, TYPE * obj, bool isLuaHandled){\
		if( (L== NULL) || (obj == NULL)){\
			LuaUtil::g_Log.error("Unable to set " #TYPE " in Lua environment: Got NULL pointer");\
			return SRI::SRI_ERR_NULL;\
		}\
		\
		if(!lua_istable(L, -1)){\
			LuaUtil::g_Log.error(#TYPE "  table expected as first parameter");\
			return SRI::SRI_ERR_TYPE;\
		}\
		\
		\
		SRI::LuaPointerHandle<TYPE>* ptHandle = NULL;\
		\
		lua_getfield(L, -1, "__obj_ptr");\
		if(lua_isuserdata(L, -1)){\
			ptHandle = (SRI::LuaPointerHandle<TYPE>*)luaL_checkudata(L, -1,#TYPE);\
			\
			if(ptHandle != NULL){ \
				ptHandle->vReleaseHandle();     \
			} \
		}\
		\
		if(ptHandle == NULL){\
			lua_pop(L, 1); /**  pop the nil result */\
			SRI::LuaPointerHandle<TYPE> handle;  /**  dummy to initialize data struct size */\
			ptHandle =  (SRI::LuaPointerHandle<TYPE>*) lua_newuserdata(L, sizeof(handle));\
			memcpy(ptHandle, &handle, sizeof(handle));\
			\
			/** Set meta table for UDATA object */\
			luaL_getmetatable(L, #TYPE);\
			lua_setmetatable(L, -2);\
		}\
		\
		if(ptHandle != NULL){\
			ptHandle->vSetPointer(obj, isLuaHandled);\
		}\
		\
		lua_setfield(L, -2, "__obj_ptr");\
		\
		return SRI::SRI_OK;\
	}\
	/** Function returns the Pointer handle as it is associated in Lua.	*/\
	\
	SRI::LuaPointerHandle<TYPE>* ptGetHandle(lua_State* L, int idx){\
		if(L == NULL){\
			LuaUtil::g_Log.error("Unable to get " #TYPE ": Lua is NULL");\
			return NULL;\
		}\
		\
		if(!lua_istable(L, idx)){\
			LuaUtil::g_Log.error("Expected " #TYPE " table at stack index %d",idx);\
			/** luaL_error(L,"Expected component table"); */\
			return NULL;\
		}\
		\
		int tablePos = idx;\
		if(idx < 0){\
			tablePos = lua_gettop(L) + 1 + idx;\
		}\
		\
		lua_getfield(L, idx, "hasType");  /** function */ \
		if(!lua_isfunction(L, -1)){ \
			LuaUtil::g_Log.error("Type error: Expected " #TYPE ", which should have a hasType() function");\
			lua_pop(L, 1); /**  pop nil */ \
			return NULL;\
		}\
		\
		lua_pushvalue(L, tablePos); /** create a duplicate on the stack for the self pointer*/ \
		lua_pushstring(L, #TYPE);\
		int res = lua_pcall(L, 2, 1, NULL);\
		if(res != NULL){\
			SRI::vLogLuaError(L, LuaUtil::g_Log, "Unable to call hasType function. Didn't get a " #TYPE " type at index %d", idx);\
			lua_pop(L, lua_gettop(L) - tablePos);\
			return NULL;\
		}\
		bool isOfComponentType = (lua_toboolean(L, -1) != 0);\
		lua_pop(L, 1); /**  remove the bool from stack */ \
		\
		if(!isOfComponentType){\
			LuaUtil::g_Log.error("Expected " #TYPE " table at index %d", idx);\
			return NULL;\
		}\
		\
		lua_getfield(L, tablePos, "__obj_ptr");\
		if (lua_isnil(L, -1)){\
			LuaUtil::g_Log.error("No " #TYPE " class is associated");\
			lua_pop(L, 1);\
			return NULL;\
		}\
		\
		LuaPointerHandle<TYPE>* handle = \
		(LuaPointerHandle<TYPE>*) luaL_checkudata(L, -1,#TYPE);\
		lua_pop(L,1); /** pop the udata from stack; */ \
		return handle;\
	}\
	\
	\
	/** Checks if there is a SRIEngien type at the given index. \
	* \returns SRI_OK or an error code\
	*/\
	int iCheck ## TYPE (lua_State* L, int index){\
		if(!lua_istable(L, index)){\
			LuaUtil::g_Log.error("No  " #TYPE "  stored at stack index[%d]", index);\
			return SRI::SRI_ERR_TYPE;\
		}\
		\
		SRI::LuaPointerHandle<TYPE>* handle = ptGetHandle(L, index);\
		if((handle != NULL) && (handle->ptGetObj() != NULL)){\
			return SRI::SRI_OK;\
		}else{\
			return SRI::SRI_ERR_NULL;\
		}\
	}\
	\
	/** Checks if there is an class object at the given index and returns the reference.\
	* \returns In case of error it returns NULL and logs an error code.\
	*/\
	TYPE * ptGet ## TYPE (lua_State* L, int index){\
		SRI::LuaPointerHandle<TYPE>* handle = ptGetHandle(L, index);\
		if((handle != NULL) && (handle->ptGetObj() != NULL)){\
			return handle->ptGetObj();\
		}else{\
			return NULL;\
		}\
	}\
	\
	/** int iCreate ## TYPE ## Obj(lua_State* L){\
		const char* name = luaL_checkstring(L, 1);\
		int stackSize = lua_gettop(L);\
		\
		TYPE * obj = new TYPE (name);\
		if(obj == NULL){\
			return SRI::SRI_ERR_NULL;\
		}\
		\
		int res = iCreate ## TYPE ## Stub(L);\
		if(res != 1){  /**  didn't leave one on stack *//** \
			delete obj;\
			lua_pop(L, lua_gettop(L) - stackSize);\
			luaL_error(L, "Unable to create engine table");\
		}\
		\
		res = iFill ## TYPE ## Stub(L, obj, true);\
		if(res != SRI::SRI_OK){\
			delete obj;\
			lua_pop(L, lua_gettop(L) - stackSize);\
			luaL_error(L, "Unable to assign  " #TYPE "  table");\
		}\
		\
		return 1;\
	} */\
	\
	int iRelease ## TYPE (lua_State* L){\
		LuaPointerHandle<TYPE>* h = (LuaPointerHandle<TYPE>*)luaL_checkudata(L, -1, #TYPE);\
		\
		if(h != NULL){\
			h->vReleaseHandle();\
		}\
		return 0;\
	}\
	\
	int iCreate ## TYPE ## MetaTable(lua_State* L){\
		luaL_newmetatable(L, #TYPE); /** meta tbale for udata object */\
		lua_pushcfunction(L, iRelease ## TYPE );\
		lua_setfield(L, -2, "__gc");\
		lua_pop(L, 1); \
		return 0;\
	}\






#endif

