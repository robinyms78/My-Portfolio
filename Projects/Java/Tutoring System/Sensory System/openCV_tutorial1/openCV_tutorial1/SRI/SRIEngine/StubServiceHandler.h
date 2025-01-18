
#ifndef STUB_SERVICE_HANDLER_H
#define STUB_SERVICE_HANDLER_H

#include "Poco/Net/SocketReactor.h"
#include "Poco/Net/SocketNotification.h"
#include "Poco/Net/StreamSocket.h"
#include "Poco/NObserver.h"
#include "Poco/Exception.h"
#include "Poco/Event.h"

#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIEngine/ServerReplyStruct.h"

namespace SRI {



/// 
/** Monitors socket for incoming replies and wakes up the correct thread.
*/

class StubServiceHandler
{
public:
	
	StubServiceHandler(Poco::Net::StreamSocket& socket, Poco::Net::SocketReactor& reactor);
	
	~StubServiceHandler();
	
	void onReadable(const Poco::AutoPtr<Poco::Net::ReadableNotification>& pNf);
	
	void onShutdown(const Poco::AutoPtr<Poco::Net::ShutdownNotification>& pNf);

	int iRegisterEvent(ServerReplyStruct* s);

	//provide method for registering thread, or rather co-ordinating event
	
private:
	//co-ordinate with the socket lock
	//register with the service handler first, get a ticket, then send!, got it! problem. signal sent before i get the thing
	
	int iCounter;

	Map<int, ServerReplyStruct*> m_Signals;

	Poco::Net::StreamSocket   m_Socket;
	Poco::Net::SocketReactor& m_Reactor;

	Logger m_tLog;
};

} //end namespace
#endif STUB_SERVICE_HANDLER_H