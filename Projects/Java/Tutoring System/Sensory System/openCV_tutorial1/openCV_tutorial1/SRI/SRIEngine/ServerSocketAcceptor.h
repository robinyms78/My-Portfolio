#ifndef SERVER_SOCKET_ACCEPTOR_H
#define SERVER_SOCKET_ACCEPTOR_H

#include "Poco/Net/StreamSocket.h"
#include "Poco/Net/ServerSocket.h"
#include "Poco/Net/SocketAcceptor.h"

namespace SRI{

class Server;

template <class ServiceHandler>
class ServerSocketAcceptor : public Poco::Net::SocketAcceptor<ServiceHandler>  {

public:

	ServerSocketAcceptor(Poco::Net::ServerSocket& socket, Poco::Net::SocketReactor& reactor, Server* s) :
		Poco::Net::SocketAcceptor<ServiceHandler>(socket, reactor), 
		m_ptServer(s) {
	}

protected:

/// Overriden to add ability to set parent server for service handler on creation

	ServiceHandler* createServiceHandler(Poco::Net::StreamSocket& socket) {
		
		ServiceHandler* sh = new ServiceHandler(socket, *Poco::Net::SocketAcceptor<ServiceHandler>::reactor());

		sh->vSetServer(m_ptServer);
		
		return sh;
	}


private:

	Server* m_ptServer;
	
};

} //end namespace

#endif COMPONENT_SOCKET_ACCEPTOR_H

