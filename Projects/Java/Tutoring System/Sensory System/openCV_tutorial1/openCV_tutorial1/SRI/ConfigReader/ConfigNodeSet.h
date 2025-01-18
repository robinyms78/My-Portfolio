#ifndef SRI_CONFIG_NODE_SET
#define SRI_CONFIG_NODE_SET

#include "SRI/ConfigReader/ConfigReaderLib.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/ConfigReader/ConfigNode.h"

namespace SRI{

INST_CR_TEMPL SRI::Map<int, SRI::Ref<ConfigNode>>;

class CR_API ConfigNodeSet{


protected:
	SRI::Map<int, SRI::Ref<ConfigNode>> m_mConfigNodes;
	int m_iNodeSetSize;

public:
	ConfigNodeSet();
	virtual ~ConfigNodeSet();
	ConfigNodeSet(const ConfigNodeSet& c);
	ConfigNodeSet& operator=(const ConfigNodeSet& c);

	virtual SRI::Ref<ConfigNode> ptGetNode(int pos);

	/** \returns the number of nodes in the nodeset */
	virtual int iGetSize() const;

};

}

#endif