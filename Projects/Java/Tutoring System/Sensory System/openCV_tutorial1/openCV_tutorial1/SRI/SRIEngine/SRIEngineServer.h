#ifndef SRI_ENGINE_SERVER_H
#define SRI_ENGINE_SERVER_H

#include "SRI/SRIEngine/Server.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIRef.h"

namespace Poco {
	namespace XML {
		class NamedNodeMap;
	}
}

/// The SRIEngineServer is a proxy service allowing remote access to an engine

namespace SRI {

	class SRIEngine;

	class SRI_E_API SRIEngineServer : public Server {

	private:
		Logger m_tLog;
		Ref<SRIEngine> m_ptEngine; //TODO: eventually change to smart ref/ptr
		int m_iPort;
		SRI::String m_szIp;

	public:
		SRIEngineServer(Ref<SRIEngine> e, SRI::String ip, int port = 0);
		virtual ~SRIEngineServer();
		//TODO: copy con, assignment op
		SRI::String szCallFunction(const ServerExecutorObject& execObj);
		void vStartServer(int port);

	};
} //end namespace
#endif SRI_COMPONENT_SERVER_H