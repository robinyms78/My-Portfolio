
#ifndef FACTORY_SERVICE_HANDLER_H
#define FACTORY_SERVICE_HANDLER_H

#include "Poco/Net/SocketReactor.h"
#include "Poco/Net/SocketNotification.h"
#include "Poco/Net/StreamSocket.h"
#include "Poco/NObserver.h"
#include "Poco/Exception.h"



namespace SRI {

class ComponentFactory;

class FactoryServiceHandler
{
public:
	
	FactoryServiceHandler(Poco::Net::StreamSocket& socket, Poco::Net::SocketReactor& reactor);
	
	~FactoryServiceHandler();
	
	void onReadable(const Poco::AutoPtr<Poco::Net::ReadableNotification>& pNf);
	
	void onShutdown(const Poco::AutoPtr<Poco::Net::ShutdownNotification>& pNf);

	void vSetParentFactory(ComponentFactory* m);
	
private:
	enum
	{
		BUFFER_SIZE = 1024
	};
	

	ComponentFactory* m_ptParentFactory;
	Poco::Net::StreamSocket   _socket;
	Poco::Net::SocketReactor& _reactor;
	char*          _pBuffer;
	char*			pCurrentBufferPosition;
};

} //end namespace
#endif FACTORY_SERVICE_HANDLER_H