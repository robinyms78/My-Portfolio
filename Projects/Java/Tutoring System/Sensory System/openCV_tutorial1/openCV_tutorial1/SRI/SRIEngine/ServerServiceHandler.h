
#ifndef SERVER_SERVICE_HANDLER_H
#define SERVER_SERVICE_HANDLER_H

#include "Poco/Net/SocketReactor.h"
#include "Poco/Net/SocketNotification.h"
#include "Poco/Net/StreamSocket.h"
#include "Poco/NObserver.h"
#include "Poco/Exception.h"

#include "SRI/Logger/Logger.h"




namespace SRI {

class Server;

/// Handles sockets for Server
/** The ServerServiceHandler listens for incoming messages to the Server
	and calls the Server's szProcessXMLMessage method. Once the message
	has been processed by the server, the ServerServiceHandler sends the reply
	back to the client (usually a stub)
*/

class ServerServiceHandler
{
public:
	
	ServerServiceHandler(Poco::Net::StreamSocket& socket, Poco::Net::SocketReactor& reactor);
	
	~ServerServiceHandler();
	
	void onReadable(const Poco::AutoPtr<Poco::Net::ReadableNotification>& pNf);
	
	void onShutdown(const Poco::AutoPtr<Poco::Net::ShutdownNotification>& pNf);

	void vSetServer(Server* s);
	
private:


	Server* m_ptServer;
	Poco::Net::StreamSocket   m_Socket;
	Poco::Net::SocketReactor& m_Reactor;

	Logger m_tLog;
};

} //end namespace
#endif SERVER_SERVICE_HANDLER_H