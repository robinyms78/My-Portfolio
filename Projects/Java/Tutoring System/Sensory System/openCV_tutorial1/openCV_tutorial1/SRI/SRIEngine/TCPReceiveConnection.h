#ifndef TCP_RECEIVE_CONNECTION_H
#define TCP_RECEIVE_CONNECTION_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIEngine/TCPConnection.h"
#include "SRI/SRIEngine/Message.h"
#include "Poco/Net/StreamSocket.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIRef.h"

#include "SRI/Logger/Logger.h"

/// A Connection encapsulating a TCP socket that handles incoming communication to a port.
/** 
 * The TCPConnection takes over the memory of the TCPSocket and is responsible for
 *	deleting it when the TCPConnection is deleted.
 */

namespace SRI {

class SRI_E_API TCPReceiveConnection : public TCPConnection {

private:
	//THESE METHODS SHOULD *NOT* be used
	int iSend(Ref<Message>& m);
	int iSend(Message* m);
	int iSetSender(OutputPort *sender);


	//note: assumes that m_ptReceiver was set to null in Connection.h (parent class)
	//and that m_ptReceiver will never be changed to non-null
	Logger m_tLog;




public:
	TCPReceiveConnection(Ref<Poco::Net::StreamSocket> sock);
	virtual ~TCPReceiveConnection();

	//int iSetReceiver(InputPort *receiver);

			
	/// Returns a received Message.
	/**
	 * mReceive() blocks until it can retrive the entire message <em>change?</em>
	 * \return Pointer to one complete received message
	 */
	Ref<Message> ptReceive();
};

}//end namespace


#endif