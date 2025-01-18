#ifndef COMPONENT_SOCKET_ACCEPTOR_H
#define COMPONENT_SOCKET_ACCEPTOR_H

#include <iostream>

#include "Poco/Net/StreamSocket.h"
#include "Poco/Net/ServerSocket.h"
#include "Poco/Net/SocketAcceptor.h"
#include "Component.h"

namespace SRI{


template <class ServiceHandler>
class ComponentSocketAcceptor : public Poco::Net::SocketAcceptor<ServiceHandler>  {

public:

	ComponentSocketAcceptor(Poco::Net::ServerSocket& socket, Poco::Net::SocketReactor& reactor, Component* parentComponent) :
		 Poco::Net::SocketAcceptor<ServiceHandler>(socket, reactor), m_ptParentComponent(parentComponent)
	{
	}

protected:

/// Overriden to add ability to set parent component for service handler on creation

	ServiceHandler* createServiceHandler(Poco::Net::StreamSocket& socket) {
		
		std::cout << "got a new connection" << std::endl;

		ServiceHandler* sh = new ServiceHandler(socket, *Poco::Net::SocketAcceptor<ServiceHandler>::reactor());

		sh->vSetParentComponent(m_ptParentComponent);
		
		return sh;
	}


private:

	Component* m_ptParentComponent;
	
};

} //end namespace

#endif COMPONENT_SOCKET_ACCEPTOR_H

