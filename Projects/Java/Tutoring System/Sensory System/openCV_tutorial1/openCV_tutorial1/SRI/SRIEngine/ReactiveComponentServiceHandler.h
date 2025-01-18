
#ifndef REACTIVE_COMPONENT_SERVICE_HANDLER_H
#define REACTIVE_COMPONENT_SERVICE_HANDLER_H

#include "Poco/Net/SocketReactor.h"
#include "Poco/Net/SocketNotification.h"
#include "Poco/Net/StreamSocket.h"
#include "Poco/NObserver.h"
#include "Poco/Exception.h"



namespace SRI {

class ReactiveComponent;

class ReactiveComponentServiceHandler
{
public:
	
	ReactiveComponentServiceHandler(Poco::Net::StreamSocket& socket, Poco::Net::SocketReactor& reactor);
	
	~ReactiveComponentServiceHandler();
	
	void onReadable(const Poco::AutoPtr<Poco::Net::ReadableNotification>& pNf);
	
	void onShutdown(const Poco::AutoPtr<Poco::Net::ShutdownNotification>& pNf);

	void vSetParentRC(ReactiveComponent* m);
	
private:
	enum
	{
		BUFFER_SIZE = 1024
	};
	

	ReactiveComponent* m_ptParentModule;
	Poco::Net::StreamSocket   _socket;
	Poco::Net::SocketReactor& _reactor;
	char*          _pBuffer;
	char*			pCurrentBufferPosition;
};

} //end namespace
#endif