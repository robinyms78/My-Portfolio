package SRI;

import java.io.IOException;
import java.net.Socket;
import java.nio.channels.SocketChannel;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class TCPSendConnection extends TCPConnection{



	/// A Connection encapsulating a TCP socket that handles outgoing communication to sockets.
	/** 
	 * The TCPConnection takes over the memory of the TCPSocket and is responsible for
	 *	deleting it when the TCPConnection is deleted.
	 */

	


		//THESE METHODS SHOULD *NOT* BE USED
		//print error message on attempted use
		//making private does not hide because is virtual
		public Message ptReceive()
		{
			System.out.println("attempted to call ptReceive in a remote send-only conection");
			//m_tLog.error("attempted to call ptReceive in a remote send-only conection");
			return null;
			
		}
		
		public int iSetReceiver(InputPort receiver)
		{
			System.out.println("attempted to set receiver in a remote send-only connection. receiver should be set by passing in a tcp socket");
			//m_tLog.error("attempted to set receiver in a remote send-only connection. receiver should be set by passing in a tcp socket");
			return 1;//SRI_ERR;
			
			
		}

		//note: assumes that m_ptReceiver was set to null in Connection.h (parent class)
		//and that m_ptReceiver will never be changed to non-null

	



		public TCPSendConnection(SocketChannel sc)
		{
			m_ptSocketChannel = sc;
			System.out.println("TCPSendConnection");
			
		}
		
		
			

		/// Sends the Message pointed to by \param m over the TCP connection.
		/**
		 * Prefixes the Message by the size of the Message, so that recipients can check 
		 * if the entire message has been received.
		 * \param m Pointer to Message to be sent.
		 */
		public int iSend(Message m)
		{
			
			if(m == null){
				//m_tLog.error("Trying to send invalid message");
				System.out.println("Trying to send invalid message");
				return 1;//SRI::SRI_ERR_NULL;
			}

			int messageLength = m.szGetMessage().length(); 
			
			if (m_ptSocketChannel != null){

				  ByteBuffer bb = ByteBuffer.allocate(4+messageLength); 
		          bb.order(ByteOrder.LITTLE_ENDIAN);
		       
		          bb.putInt(messageLength);
		         
		          bb.put(m.szGetMessage().getBytes());
		          bb.flip();
		         // bb = ByteBuffer.wrap((reply).getBytes());
		          try {
					int nBytes = m_ptSocketChannel.write(bb);
					System.out.println("Wrote " + nBytes + ", message length: " + m.szGetMessage().length());
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				//m_ptSocket.sendBytes(messageLength, sizeof());
				//m_ptSocket.sendBytes(m.szGetMessage(), messageLength);
			}

			return 0;//SRI_OK
			
		}
		
		/// Sends the Message \param m over the TCP connection.
		/**
		 * Prefixes the Message by the size of the Message, so that recipients can check 
		 * if the entire message has been received.
		 * \param m Pointer to Message to be sent.
		 */
		//virtual int iSend(Message* m);

	
}
