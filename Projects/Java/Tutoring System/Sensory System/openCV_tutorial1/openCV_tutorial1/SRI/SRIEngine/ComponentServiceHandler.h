
#ifndef COMPONENT_SERVICE_HANDLER_H
#define COMPONENT_SERVICE_HANDLER_H

#include "Poco/Net/SocketReactor.h"
#include "Poco/Net/SocketNotification.h"
#include "Poco/Net/StreamSocket.h"
#include "Poco/NObserver.h"
#include "Poco/Exception.h"


/** Service handler used for receiving incoming messages to Components (both Component and RC).
 *  Messages will be in XML. Waits for the full XML message to arrive, then calls  
 *  ParentComponent's szProcessXMLFunction (virtual function). 
*/


namespace SRI {

class Component;

class ComponentServiceHandler
{
public:
	
	ComponentServiceHandler(Poco::Net::StreamSocket& socket, Poco::Net::SocketReactor& reactor);
	
	~ComponentServiceHandler();
	
	void onReadable(const Poco::AutoPtr<Poco::Net::ReadableNotification>& pNf);
	
	void onShutdown(const Poco::AutoPtr<Poco::Net::ShutdownNotification>& pNf);

	void vSetParentComponent(Component* m);
	
private:
	enum
	{
		BUFFER_SIZE = 1024
	};
	

	Component* m_ptParentComponent;
	Poco::Net::StreamSocket   _socket;
	Poco::Net::SocketReactor& _reactor;
	char*          _pBuffer;
	char*			pCurrentBufferPosition;
};

} //end namespace
#endif COMPONENT_SERVICE_HANDLER_H