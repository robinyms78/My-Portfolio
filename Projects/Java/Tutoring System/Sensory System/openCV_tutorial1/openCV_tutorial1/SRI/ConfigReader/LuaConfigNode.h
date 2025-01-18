#ifndef SRI_LUA_CONFIG_NODE_H
#define SRI_LUA_CONFIG_NODE_H

#include "SRI/ConfigReader/ConfigNode.h"

namespace SRI{

/** TODO:: Implement conversion between XML and Lua node implementation */

class LuaConfigNode : public ConfigNode{

private:

public:
	LuaConfigNode();
	virtual ~LuaConfigNode();

	LuaConfigNode(const ConfigNode& c);
	LuaConfigNode& operator=(const ConfigNode& c);
	/** Inserts the child at the end of the list */
	virtual int iAppendChild(Ref<ConfigNode> node);
	/** Inserts the node after the specified child */
	virtual int iInsertChild(Ref<ConfigNode>& node, Ref<ConfigNode> prev);

	/** Removes the given child and returns a reference to it if successful*/
	virtual int iRemoveChild(Ref<ConfigNode>& node);

	virtual int iSetAttribute(SRI::String attribute, SRI::String value);
	virtual SRI::String szGetNodeType() const;

};

} // end namespace

#endif