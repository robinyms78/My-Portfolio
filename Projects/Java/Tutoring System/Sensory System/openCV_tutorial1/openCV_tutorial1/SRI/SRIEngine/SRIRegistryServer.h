#ifndef SRI_REGISTRY_SERVER_H
#define SRI_REGISTRY_SERVER_H

#include "SRI/SRIEngine/Server.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/SRIRegistry.h"

namespace Poco {
	namespace XML {
		class NamedNodeMap;
	}
}

/// An SRIRegistryServer is a proxy service allowing remote access to an SRIRegistry
/** Unlike other servers, the SRIRegistryServer does not shut down when an SRIRegistryStub
	disconnects from the server.
*/

namespace SRI {

	class SRI_E_API SRIRegistryServer : public Server {

	private:
		Logger m_tLog;
		Ref<SRIRegistry> m_ptRegistry; 

	public:
		SRIRegistryServer(Ref<SRIRegistry> r); //doesn't take over the memory
		virtual ~SRIRegistryServer();
		//TODO: copy con, assignment op
		SRI::String szCallFunction(const ServerExecutorObject& execObj);

	};
} //end namespace
#endif SRI_REGISTRY_SERVER_H