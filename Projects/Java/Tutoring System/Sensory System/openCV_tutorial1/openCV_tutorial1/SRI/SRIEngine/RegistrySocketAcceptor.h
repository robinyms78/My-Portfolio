#ifndef REGISTRY_SOCKET_ACCEPTOR_H
#define REGISTRY_SOCKET_ACCEPTOR_H



#include "Poco/Net/StreamSocket.h"
#include "Poco/Net/ServerSocket.h"
#include "Poco/Net/SocketAcceptor.h"
#include "SRIRegistry.h"

namespace SRI{



/// Implements the Acceptor part of the Acceptor-Connector design pattern used by ModuleOutputPorts.
/** 

 */
template <class ServiceHandler>
class RegistrySocketAcceptor : public Poco::Net::SocketAcceptor<ServiceHandler>  {

public:

	

RegistrySocketAcceptor(Poco::Net::ServerSocket& socket, Poco::Net::SocketReactor& reactor, SRIRegistry* parentRegistry) :
		Poco::Net::SocketAcceptor<ServiceHandler>(socket, reactor), m_ptParentRegistry(parentRegistry)
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
		
	ServiceHandler* sh = new ServiceHandler(socket, *Poco::Net::SocketAcceptor<ServiceHandler>::reactor());
		
	sh->vSetParentRegistry(m_ptParentRegistry);
		

	return sh;
}


private:

	SRIRegistry* m_ptParentRegistry;


	
};

} //end namespace

#endif REGISTRY_SOCKET_ACCEPTOR_H
