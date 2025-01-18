#ifndef OUTPUT_PORT_SOCKET_ACCEPTOR_H
#define OUTPUT_PORT_SOCKET_ACCEPTOR_H

#include "Poco/Net/StreamSocket.h"
#include "Poco/Net/ServerSocket.h"
#include "Poco/Net/SocketAcceptor.h"

class OutputPort;

/// Implements the Acceptor part of the Acceptor-Connector design pattern used by ModuleOutputPorts.
/** 
 *	Waits for connection requets and spawns a new ModuleOutputPortServiceHandler 
 *  when a new connection is formed.
 *
 *  Overrides createServiceHandler to perform custom handling of incoming connections.
 */
template <class ServiceHandler>
class OutputPortSocketAcceptor : public Poco::Net::SocketAcceptor<ServiceHandler>  {

public:

	OutputPortSocketAcceptor(Poco::Net::ServerSocket& socket, Poco::Net::SocketReactor& reactor, OutputPort *o) :
		 Poco::Net::SocketAcceptor<ServiceHandler>(socket, reactor),
		 oport(o) {
	}

protected:

/// Overrides createServiceHandler to perform custom handling of incoming connections.
/** 
 *	Creates a new ServiceHandler, then invokes vRegisterWithOwnerModuleOutputPort() on
 *  the newly created handler to register the connection with its parent ModuleOutputPort.
 */
	ServiceHandler* createServiceHandler(Poco::Net::StreamSocket& socket) {
		
		ServiceHandler *sh = new ServiceHandler(socket, *Poco::Net::SocketAcceptor<ServiceHandler>::reactor());
		
		sh->vRegisterWithOwnerOutputPort(oport);
		//TODO:is this needed? can i just provide a three argument ctor? SEEMS NOT, AS I NEED TO PROVIDE A TWO ARGUMENT CTOR TO SATISFYTHE BASE CLASS, YES?

	

		return sh;
	}

	OutputPort *oport;
};

#endif

//public:
//	/*ModuleOutputPortSocketAcceptor(ServerSocket& socket, SocketReactor& reactor) : Poco::Net::SocketAcceptor<ServiceHandler>(socket, reactor) {
//	}
//
//	//, oport(o)
//
//	//TODO: default constructor should call superclass' default?
//
//	/*ServiceHandler* createServiceHandler(StreamSocket& socket) {
//		return new ServiceHandler(socket, *_pReactor, o);
//	}*/
//
//
//	//TODO: copy and assignment?
//
//private:
//	//ModuleOutputPort& oport;