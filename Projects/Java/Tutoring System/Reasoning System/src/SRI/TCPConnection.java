package SRI;

import java.net.Socket;
import java.nio.channels.SocketChannel;

public abstract class TCPConnection extends Connection {

	

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


	


		/// Sends the Message pointed to by \param m over the TCP connection.
		/**
		 * Prefixes the Message by the size of the Message, so that recipients can check 
		 * if the entire message has been received.
		 * \param m Pointer to Message to be sent.
		 */
		public abstract int iSend(Message m);
		
		/// Sends the Message \param m over the TCP connection.
		/**
		 * Prefixes the Message by the size of the Message, so that recipients can check 
		 * if the entire message has been received.
		 * \param m Pointer to Message to be sent.
		 */
		//p int iSend(Message* m) = 0;

		/// Returns a received Message. <em>bIsAvailable() must be used first to check if any data is available before calling this method.</em>
		/**
		 * mReceive() blocks until it can retrieve the entire message <em>change?</em>
		 * \return One complete received message
		 */
		 public abstract Message ptReceive();

		

	//protected:
		protected SocketChannel m_ptSocketChannel = null;

	//};

	//}//end namespace




	
	
}
