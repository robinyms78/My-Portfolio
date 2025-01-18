#ifndef BROADCAST_SOCKET_ACCEPTOR_H
#define BROADCAST_SOCKET_ACCEPTOR_H

#include "Poco/Net/StreamSocket.h"
#include "Poco/Net/ServerSocket.h"
#include "Poco/Net/SocketAcceptor.h"
#include "SRI/SRIEngine/Component.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIEngine/BroadcastComponent.h"
#include "SRI/SRIEngine/ComponentStub.h"
#include "SRI/SRIEngine/ReactiveComponentStub.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/SRITCPUtils.h"

#include <sstream>

namespace SRI{

template <class ServiceHandler>
class BroadcastSocketAcceptor : public Poco::Net::SocketAcceptor<ServiceHandler>  {

public:

	BroadcastSocketAcceptor(Poco::Net::ServerSocket& socket, Poco::Net::SocketReactor& reactor, Ref<BroadcastComponent> bc) :
		Poco::Net::SocketAcceptor<ServiceHandler>(socket, reactor), 
		m_ptBroadcastComponent(bc) {
	}

protected:

/// Overriden to add ability to set parent server for service handler on creation

	ServiceHandler* createServiceHandler(Poco::Net::StreamSocket& socket) {
		Ref<Component> c;

		Ref<SRI::String> ptMsg = new SRI::String();
		SRITCPUtils::szReadSocket(&socket, ptMsg);

		std::string type;
		int port;
		
		std::stringstream ss(ptMsg.ptGetObj()->c_str());

		ss >> type >> port;

		SRI::String sriType(type);
		SRI::String ipAdd(socket.peerAddress().host().toString().c_str());
		
		if (sriType == "Component") 
			c = new ComponentStub("", ipAdd, port);
		else if (sriType == "ReactiveComponent")
			c = new ReactiveComponentStub("", ipAdd, port);
		
		m_ptBroadcastComponent->iAddListener(c);
		
		return NULL;
		
	}


private:

	Ref<BroadcastComponent> m_ptBroadcastComponent;
	
};

} //end namespace

#endif BROADCAST_SOCKET_ACCEPTOR_H

