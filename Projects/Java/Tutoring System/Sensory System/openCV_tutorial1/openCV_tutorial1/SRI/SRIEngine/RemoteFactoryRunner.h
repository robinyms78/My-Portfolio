#ifndef REMOTE_FACTORY_RUNNER_H
#define REMOTE_FACTORY_RUNNER_H

#include "Poco/Runnable.h"
#include "ComponentFactory.h"
#include "Server.h"

namespace SRI {

	class RemoteFactoryRunner : public Poco::Runnable {
	private:
		ComponentFactory *m_ptComponentFactory;
		Server *m_ptServer;


	public:

		RemoteFactoryRunner(ComponentFactory *f, Server *s) :
			m_ptComponentFactory(f),
			m_ptServer(s) {
		}

		virtual ~RemoteFactoryRunner() {
			delete m_ptComponentFactory;
			delete m_ptServer;
		}

		void run() {

			m_ptServer->vJoinServerThread();
			delete this;
		}
	};

} //end namespace

#endif REMOTE_FACTORY_RUNNER_H