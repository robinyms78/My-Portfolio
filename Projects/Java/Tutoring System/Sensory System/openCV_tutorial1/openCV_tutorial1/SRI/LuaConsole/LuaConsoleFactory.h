#ifndef LUA_CONSOLE_FACTORY_H
#define LUA_CONSOLE_FACTORY_H

#include "SRI/SRIEngine/SRIPlugin.h"
#include "SRI/SRIEngine/ComponentFactory.h"
#include "SRI/LuaConsole/LuaConsole.h"

namespace SRI{

class SRI_PLUGIN_API LuaConsoleFactory: public ComponentFactory{

private:
	Logger m_tLog;

public:
	LuaConsoleFactory(SRI::String name, SRI::String config = "");
	virtual ~LuaConsoleFactory();

	virtual SRI::Ref<SRI::Component> ptCreateComponent(SRI::String name, SRI::String config = "");

};

}

#endif