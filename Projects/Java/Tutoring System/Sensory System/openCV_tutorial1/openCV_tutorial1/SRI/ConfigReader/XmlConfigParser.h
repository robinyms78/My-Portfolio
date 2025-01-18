#ifndef SRI_XML_CONFIG_PARSER_H
#define SRI_XML_CONFIG_PARSER_H

#include "SRI/ConfigReader/ConfigParser.h"
#include "SRI/Logger/Logger.h"
#include "xpath_processor.h"

namespace SRI{

class XmlConfigParser: public ConfigParser{

private:
	Logger m_tLog;
	TiXmlDocument m_tDoc;

public:
	XmlConfigParser();
	~XmlConfigParser();
	XmlConfigParser(const XmlConfigParser& c);
	XmlConfigParser operator=(const XmlConfigParser& c);

	virtual ConfigParser* ptClone();
	virtual int iReadString(SRI::String config);
	virtual int iReadFile(SRI::String fileName);

	virtual SRI::String szEvalQuery(const SRI::String& query);

	virtual bool bHasParameter(const SRI::String& configPath);
	//virtual int iGetConfigNodes(const SRI::String& configPath, ConfigNode& node);

	virtual bool bGetBoolValue(const SRI::String& configPath);
	virtual int iGetIntValue(const SRI::String& configPath);
	virtual double dGetDoubleValue(const SRI::String& configPath);
	virtual SRI::String szGetStringValue(const SRI::String& configPath);

	virtual SRI::Ref<SRI::ConfigNode> ptGetNode(const SRI::String& configPath);
	virtual SRI::Ref<SRI::ConfigNodeSet> ptGetNodeSet(const SRI::String& configPath);
};

}






#endif