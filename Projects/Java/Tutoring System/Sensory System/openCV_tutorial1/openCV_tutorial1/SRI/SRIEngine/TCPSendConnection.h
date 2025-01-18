#ifndef TCP_SEND_CONNECTION_H
#define TCP_SEND_CONNECTION_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIEngine/TCPConnection.h"
#include "SRI/SRIEngine/Message.h"
#include "Poco/Net/StreamSocket.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/Logger/Logger.h"

/// A Connection encapsulating a TCP socket that handles outgoing communication to sockets.
/** 
 * The TCPConnection takes over the memory of the TCPSocket and is responsible for
 *	deleting it when the TCPConnection is deleted.
 */

namespace SRI {

class SRI_E_API TCPSendConnection : public TCPConnection {

private:
	//THESE METHODS SHOULD *NOT* BE USED
	//print error message on attempted use
	//making private does not hide because is virtual
	Ref<Message> ptReceive();
	int iSetReceiver(InputPort *receiver);

	//note: assumes that m_ptReceiver was set to null in Connection.h (parent class)
	//and that m_ptReceiver will never be changed to non-null

	Logger m_tLog;


public:
	TCPSendConnection(Ref<Poco::Net::StreamSocket> sock);
	virtual ~TCPSendConnection();
		

	/// Sends the Message pointed to by \param m over the TCP connection.
	/**
	 * Prefixes the Message by the size of the Message, so that recipients can check 
	 * if the entire message has been received.
	 * \param m Pointer to Message to be sent.
	 */
	virtual int iSend(Ref<Message>& m);
	
	/// Sends the Message \param m over the TCP connection.
	/**
	 * Prefixes the Message by the size of the Message, so that recipients can check 
	 * if the entire message has been received.
	 * \param m Pointer to Message to be sent.
	 */
	virtual int iSend(Message* m);

};

}//end namespace


#endif