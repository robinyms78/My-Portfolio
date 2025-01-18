#ifndef REACTIVE_COMPONENT_SOCKET_ACCEPTOR_H
#define REACTIVE_COMPONENT_SOCKET_ACCEPTOR_H

#include <iostream>

#include "Poco/Net/StreamSocket.h"
#include "Poco/Net/ServerSocket.h"
#include "Poco/Net/SocketAcceptor.h"
#include "SRITCPUtils.h"
#include "ReactiveComponent.h"

namespace SRI{

//class ReactiveComponent;

/// Implements the Acceptor part of the Acceptor-Connector design pattern used by ModuleOutputPorts.
/** 

 */
template <class ServiceHandler>
class ReactiveComponentSocketAcceptor : public Poco::Net::SocketAcceptor<ServiceHandler>  {

public:

	ReactiveComponentSocketAcceptor(Poco::Net::ServerSocket& socket, Poco::Net::SocketReactor& reactor, ReactiveComponent* parentRC) :
		 Poco::Net::SocketAcceptor<ServiceHandler>(socket, reactor), m_ptParentRC(parentRC)
	{
	}

protected:

/// Overrides createServiceHandler to perform custom handling of incoming connections.
/** 
 *	Depending on the type of incoming connection, either spawns a new socket handler or
 *  flags the socket to be added as a connection to an output port
 */
	ServiceHandler* createServiceHandler(Poco::Net::StreamSocket& socket) {
		
		std::cout << "got a new connection" << std::endl;

		SRI::String type = SRITCPUtils::szReadSocket(&socket);

		

		ServiceHandler* sh = NULL;

		//TODO: ensure that there's only one server type connection (i.e. using  the service handler) by using a boolean guard

		if (type == "port") { //is a connection meant for an output port
			std::cout << "got a connection for a port" << std::endl;
			
			m_ptParentRC->vAddPendingSocketForOutputPort(socket);
			//note: StreamSockets are reference counted, so making copies is ok (automatically deleted)
		}
		else if (type == "control") {//create new ReactiveComponentServiceHandler to handle incoming messages
			std::cout << "got a connection for control" << std::endl;
			sh = new ServiceHandler(socket, *Poco::Net::SocketAcceptor<ServiceHandler>::reactor());
		
			sh->vSetParentComponent(m_ptParentRC);
		}
		else {
			std::cout << "error!" << std::endl;
		}

		return sh;
	}


private:

	ReactiveComponent* m_ptParentRC;


	
};

} //end namespace

#endif REACTIVE_COMPONENT_SOCKET_ACCEPTOR_H

