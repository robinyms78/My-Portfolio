#ifndef SRI_CONFIG_NODE_H
#define SRI_CONFIG_NODE_H

#include "SRI/ConfigReader/ConfigReaderLib.h"
#include "SRI/SRIUtil/SRIString.h"

namespace SRI{

class CR_API ConfigNode{

private:

public:
	ConfigNode();
	virtual ~ConfigNode();

	ConfigNode(const ConfigNode& c);
	ConfigNode& operator=(const ConfigNode& c);

	virtual ConfigNode* ptClone() const;

	/** Returns the value of the node. Depending on the type this might have different
	* meaning. For elements it is the node name. For text elements it is the value of
	* the text*/
	virtual SRI::String szGetValue() const;
	/** If empty string is given, this function returns the first child */
	virtual SRI::Ref<ConfigNode> ptGetFirstChild(SRI::String value = "");
	/** If the node has a text child this function returns its value. Otherwise
	* it returns "" */
	virtual SRI::String szGetTextChild();
	virtual SRI::Ref<ConfigNode> ptIterateChildren(SRI::String value = "", Ref<ConfigNode> previous = Ref<ConfigNode>());

	/** The node is given by reference, because the pointer might be modified for memory optimization */
	virtual int iAppendChild(Ref<ConfigNode>& node);
	/** Inserts the node after the specified child */
	virtual int iInsertChild(Ref<ConfigNode>& node, Ref<ConfigNode> prev);
	
	/** Removes the given child. The node reference receives a copy of the removed element*/
	virtual int iRemoveChild(Ref<ConfigNode>& node);	
	
	virtual int iSetAttribute(SRI::String attribute, SRI::String value);
	
	/** \returns "ConfigNode" for base class and "LuaNode" or "XmlNode" according to implementation */
	virtual SRI::String szGetNodeType() const;

	virtual double dGetDoubleAttribute(SRI::String attribName);
	virtual int iGetIntAttribute(SRI::String attribName);
	virtual SRI::String szGetStringAttribute(SRI::String attribName);
	virtual SRI::String szGetXmlString();
	virtual bool bHasAttribute(SRI::String attribName);

};


} // end namespace

#endif