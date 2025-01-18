#ifndef SRI_XML_NODE_SET_H
#define SRI_XML_NODE_SET_H

#include "SRI/ConfigReader/ConfigNodeSet.h"
#include "xpath_processor.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

INST_CR_TEMPL SRI::Ref<TinyXPath::xpath_processor>;

class CR_API XmlConfigNodeSet : public ConfigNodeSet{

private:
	SRI::Ref<TinyXPath::xpath_processor> m_ptXPath;
	Logger m_tLog;

public:
	XmlConfigNodeSet();
	XmlConfigNodeSet(const TiXmlNode *XNp_source_tree, const char *cp_xpath_exp);
	XmlConfigNodeSet(SRI::Ref<TinyXPath::xpath_processor> pathProcessor,  int nodeSetSize);
	virtual ~XmlConfigNodeSet();

	XmlConfigNodeSet(const XmlConfigNodeSet& c);
	XmlConfigNodeSet& operator=(const XmlConfigNodeSet& c);

	virtual SRI::Ref<ConfigNode> ptGetNode(int pos);

};

} // end namespace




#endif

