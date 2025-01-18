#ifndef OUTPUT_PORT_SERVICE_HANDLER_H
#define OUTPUT_PORT_SERVICE_HANDLER_H

#include "Poco/Net/SocketReactor.h"
#include "Poco/Net/SocketNotification.h"
#include "Poco/Net/StreamSocket.h"
#include "Poco/NObserver.h"
#include "Poco/Exception.h"

namespace SRI {

class OutputPort;

/// Handles events occuring on the underlying socket of each connection to a ModuleOutputPort
/** 
 *	Used in conjunction with ModuleOutputPortSocketAcceptor to handle new incoming connections.
 *
 *	A new ModuleOutputPortServiceHandler is created for each new incoming connection to 
 *  a ModuleOutputPort and registers itself with the appropriate SocketReactor. 
 *  Currently handles two notifications: ReadableNotification and ShutdownNotification.
 *  ReadableNotification is used to signal a closure of the connection by the peer socket.
 *
 *  ModuleOutputPortSocketAcceptor calls vRegisterWithOwnerModuleOutputPort() when it creates
 *  a new ModuleOutputPortServiceHandler to register the newly created connection with 
 *  the OutputPort. 
 */

class SRI_E_API OutputPortServiceHandler {
public:
	
	/// Called by ModuleOutputPortSocketAcceptor to create a new ModuleOutputPortServiceHandler to handle the connection
	/**
	 *  On creation, the ModuleOutputPortServiceHandler registers its event callbacks with \param reactor.
	 *	\param socket The local socket created when the connection was established
	 *  \param reactor The SocketReactor responsible for event callbacks
	 */
	OutputPortServiceHandler(Poco::Net::StreamSocket& socket, Poco::Net::SocketReactor& reactor);
	// a constructor that accepts a ModuleOutputPort as an argument can't be used, as this method
	// needs to be provided for subclasses of SocketAcceptor

	/// Destructor.
	/**
	 *	On deletion, deregisters the connection this ModuleOutputPortServiceHandler represents 
	 *  with its owner ModuleOutputPort and removes its event callbacks.
	 */
	~OutputPortServiceHandler();
	
	/// Callback for ReadableNotifications. Used to handle connection closure by ModuleInputPorts
	/**
	 *	When a connected ModuleInputPort wants to close a connection, it sends a single byte over
	 *  the connection, triggering this callback and causing the deletion of this ModuleOutputPortServiceHandler 
	 */
	void onReadable(const Poco::AutoPtr<Poco::Net::ReadableNotification>& pNf);
	
	/// Handles shutdown event from parent SocketHandler
	void onShutdown(const Poco::AutoPtr<Poco::Net::ShutdownNotification>& pNf);

	/// Register this ModuleOutputPortServiceHandler with \param o
	/**
	 *  Usually called by ModuleOutputPortSocketAcceptor on creation of a new 
	 *  ModuleOutputPortServiceHandler to notify ModuleOutputPort \param o that a
	 *  new ModuleOutputPortServiceHandler and its underlying connection have been created.
	 */
	void vRegisterWithOwnerOutputPort(OutputPort *o);

	/// Removes this ModuleOutputPortServiceHandler from the list of connections maintained by 
	/// its parent ModuleOutputPort.
	void vUnregisterWithOwnerOutputPort();
	

	
private:
	Poco::Net::StreamSocket   _socket;
	Poco::Net::SocketReactor& _reactor;
	OutputPort *oport;

	
};

} //end namespace
#endif