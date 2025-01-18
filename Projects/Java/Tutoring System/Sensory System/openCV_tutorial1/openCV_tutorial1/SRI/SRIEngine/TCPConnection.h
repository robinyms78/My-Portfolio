#ifndef TCP_CONNECTION_H
#define TCP_CONNECTION_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIEngine/Message.h"
#include "Poco/Net/StreamSocket.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/Connection.h"

/// A Connection encapsulating a TCP socket that handles communication between sockets.
/** A template class for its derivatives: TCPSendConnection and TCPReceiveConnection.
 *	Since TCPSendConnection and TCPReceiveConnection represent asymmetric sides of the connection, 
 * and since the sender and receiver of each connection are determined by the IP address and the 
 * underlying socket of each TCPConnection, this class prevents its child classes from inheriting
 *  methods that do not make sense.
 *  If a user tries to invoke any of these methods, the an error is printed to stdout.
 * TCPConnection doesn't use a buffer. Instead, it sends and receives directly over the socket.
 * The TCPConnection takes over the memory of the TCPSocket and is responsible for
 *	deleting it when the TCPConnection is deleted.
 */


namespace SRI {

	class InputPort;
	class OutputPort;

class SRI_E_API TCPConnection : public Connection {

//Make iSetSender and iSetReceiver methods private
private:
    Logger m_tLog;

	TCPConnection(const TCPConnection& c);
	TCPConnection& operator=(const TCPConnection & c);

public:
	TCPConnection(Ref<Poco::Net::StreamSocket> sock);
	virtual ~TCPConnection();



	/// Sends the Message pointed to by \param m over the TCP connection.
	/**
	 * Prefixes the Message by the size of the Message, so that recipients can check 
	 * if the entire message has been received.
	 * \param m Pointer to Message to be sent.
	 */
	virtual int iSend(Ref<Message>& m) = 0;
	
	/// Sends the Message \param m over the TCP connection.
	/**
	 * Prefixes the Message by the size of the Message, so that recipients can check 
	 * if the entire message has been received.
	 * \param m Pointer to Message to be sent.
	 */
	virtual int iSend(Message* m) = 0;

	/// Returns a received Message. <em>bIsAvailable() must be used first to check if any data is available before calling this method.</em>
	/**
	 * mReceive() blocks until it can retrive the entire message <em>change?</em>
	 * \return One complete received message
	 */
	virtual Ref<Message> ptReceive() = 0;

	

protected:
	Ref<Poco::Net::StreamSocket> m_ptSocket;

};

}//end namespace


#endif
