#ifndef SRI_XML_CONFIG_NODE_H
#define SRI_XML_CONFIG_NODE_H


#include "SRI/ConfigReader/ConfigNode.h"
#include "xpath_processor.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

INST_CR_TEMPL Ref<TiXmlNode>;

class CR_API XmlConfigNode : public ConfigNode{

private:
	
	Ref<TiXmlNode> m_ptXmlNode;
	Logger m_tLog;

protected:
	Ref<TiXmlNode> ptGetTiXmlNode();

public:
	XmlConfigNode();
	/**By default the XML tree holds the memory. Therefore this memory is not managed.*/
	XmlConfigNode(TiXmlNode *node);
	XmlConfigNode(SRI::Ref<TiXmlNode> node);
	XmlConfigNode(SRI::String xmlText);
	virtual ~XmlConfigNode();

	XmlConfigNode(const XmlConfigNode& c);
	XmlConfigNode& operator=(const XmlConfigNode& c);

	virtual ConfigNode* ptClone() const;

	virtual SRI::String szGetValue() const;
	virtual SRI::Ref<ConfigNode> ptGetFirstChild(SRI::String value="");
	virtual SRI::Ref<ConfigNode> ptIterateChildren(SRI::String value="", Ref<ConfigNode> previous=Ref<ConfigNode>());

	/** Appends the a copy of the given child and returns a pointer to the copy. */
	virtual int iAppendChild(Ref<ConfigNode>& node);
	/** Inserts a copy of the node after the specified child and returns a pointer to the copy. If the child is NULL it will be inserted as first element*/
	virtual int iInsertChild(Ref<ConfigNode>& node, Ref<ConfigNode> prev = Ref<ConfigNode>((ConfigNode*)NULL));

	/** Removes the given child and returns a reference to it if successful*/
	virtual int iRemoveChild(Ref<ConfigNode>& node);

	virtual int iSetAttribute(SRI::String attribute, SRI::String value);

	virtual SRI::String szGetNodeType() const;

	virtual SRI::String szGetTextChild();
	virtual double dGetDoubleAttribute(SRI::String attribName);
	virtual int iGetIntAttribute(SRI::String attribName);
	virtual SRI::String szGetStringAttribute(SRI::String attribName);

	virtual SRI::String szGetXmlString();
	virtual bool bHasAttribute(SRI::String attribName);
};

} // end namespace

#endif