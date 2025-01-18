#ifndef FACTORY_SOCKET_ACCEPTOR_H
#define FACTORY_SOCKET_ACCEPTOR_H

#include <iostream>

#include "Poco/Net/StreamSocket.h"
#include "Poco/Net/ServerSocket.h"
#include "Poco/Net/SocketAcceptor.h"
#include "ComponentFactory.h"

namespace SRI{



/// Implements the Acceptor part of the Acceptor-Connector design pattern used by ModuleOutputPorts.
/** 

 */
template <class ServiceHandler>
class FactorySocketAcceptor : public Poco::Net::SocketAcceptor<ServiceHandler>  {

public:

	

FactorySocketAcceptor(Poco::Net::ServerSocket& socket, Poco::Net::SocketReactor& reactor, ComponentFactory* parentFactory) :
		Poco::Net::SocketAcceptor<ServiceHandler>(socket, reactor), m_ptParentFactory(parentFactory)
{
		
}

protected:

/// Overrides createServiceHandler to perform custom handling of incoming connections.
/** 
 *	Depending on the type of incoming connection, either spawns a new socket handler or
 *  flags the socket to be added as a connection to an output port
 */

//TODO: since RC creation is a relatively rare occurence, better to 
//have the acceptor be the processor?
ServiceHandler* createServiceHandler(Poco::Net::StreamSocket& socket) {
		
	std::cout << "got a new connection" << std::endl;

	ServiceHandler* sh = new ServiceHandler(socket, *Poco::Net::SocketAcceptor<ServiceHandler>::reactor());
		
	sh->vSetParentFactory(m_ptParentFactory);
		

	return sh;
}


private:

	ComponentFactory* m_ptParentFactory;


	
};

} //end namespace

#endif FACTORY_SOCKET_ACCEPTOR_H
