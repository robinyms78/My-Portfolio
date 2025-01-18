#ifndef CONFIG_PARSER_H 
#define CONFIG_PARSER_H

#include "SRI/SRIUtil/SRIString.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/ConfigReader/ConfigNodeSet.h"
#include "SRI/SRIUtil/SRIRef.h"

namespace SRI{

/** The ConfigParser supports reading configuration using a configPath
* The configPath has a similar syntax as XPath
*/
class ConfigParser{

private:

protected: 
	SRI::String m_szConfig;
	bool m_bHoldsFile;

public:

	ConfigParser();
	virtual ~ConfigParser();
	ConfigParser(const ConfigParser& c);
	ConfigParser& operator=(const ConfigParser& c);

	virtual ConfigParser* ptClone() = 0;
	virtual int iReadString(SRI::String config);
	virtual int iReadFile(SRI::String fileName);

	virtual bool bHasParameter(const SRI::String& configPath) = 0;

	virtual SRI::String szEvalQuery(const SRI::String& query) = 0;
	//virtual int iGetConfigNodes(const SRI::String& configPath, ConfigNode& node) =0;

	virtual bool bGetBoolValue(const SRI::String& configPath)= 0;
	virtual int iGetIntValue(const SRI::String& configPath)= 0;
	virtual double dGetDoubleValue(const SRI::String& configPath)= 0;
	virtual SRI::String szGetStringValue(const SRI::String& configPath)= 0;

	virtual SRI::Ref<SRI::ConfigNode> ptGetNode(const SRI::String& configPath) = 0;
	virtual SRI::Ref<SRI::ConfigNodeSet> ptGetNodeSet(const SRI::String& configPath) = 0;

};


}

#endif