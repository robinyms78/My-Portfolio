#ifndef REMOTE_COMPONENT_RUNNER_H
#define REMOTE_COMPONENT_RUNNER_H

#include "Poco/Runnable.h"
#include "SRI/SRIEngine/Component.h"
#include "SRI/SRIEngine/Server.h"

namespace SRI {


	/// A RemoteComponentRunner is used by a ComponentFactoryServer to manage the memory of a Component
	class RemoteComponentRunner : public Poco::Runnable {
	private:
		SRI::Ref<Component> m_ptComponent;
		Server *m_ptServer;


	public:

		RemoteComponentRunner(SRI::Ref<Component> c, Server *s) :
			m_ptComponent(c),
			m_ptServer(s) {
		}

		virtual ~RemoteComponentRunner() {
			delete m_ptServer;
		}

		void run() {

			m_ptServer->vJoinServerThread();
			delete this;
		}
	};

} //end namespace

#endif REMOTE_COMPONENT_RUNNER_H