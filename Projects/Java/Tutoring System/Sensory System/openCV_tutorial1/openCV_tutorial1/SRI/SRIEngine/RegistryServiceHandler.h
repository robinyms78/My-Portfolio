
#ifndef REGISTRY_SERVICE_HANDLER_H
#define REGISTRY_SERVICE_HANDLER_H

#include "Poco/Net/SocketReactor.h"
#include "Poco/Net/SocketNotification.h"
#include "Poco/Net/StreamSocket.h"
#include "Poco/NObserver.h"
#include "Poco/Exception.h"
#include "Logger.h"



namespace SRI {

class SRIRegistry;

class RegistryServiceHandler
{
public:
	
	RegistryServiceHandler(Poco::Net::StreamSocket& socket, Poco::Net::SocketReactor& reactor);
	
	~RegistryServiceHandler();
	
	void onReadable(const Poco::AutoPtr<Poco::Net::ReadableNotification>& pNf);
	
	void onShutdown(const Poco::AutoPtr<Poco::Net::ShutdownNotification>& pNf);

	void vSetParentRegistry(SRIRegistry* m);
	
private:
	enum
	{
		BUFFER_SIZE = 1024
	};
	

	SRIRegistry* m_ptParentRegistry;
	Poco::Net::StreamSocket   _socket;
	Poco::Net::SocketReactor& _reactor;
	char*          _pBuffer;
	char*			pCurrentBufferPosition;
	Logger	m_tLog;
};

} //end namespace
#endif REGISTRY_SERVICE_HANDLER_H