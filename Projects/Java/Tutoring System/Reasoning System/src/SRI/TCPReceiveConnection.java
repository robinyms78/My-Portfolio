package SRI;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.CharBuffer;
import java.nio.channels.SocketChannel;
import java.nio.charset.CharacterCodingException;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

public class TCPReceiveConnection extends TCPConnection{

	

	/// A Connection encapsulating a TCP socket that handles incoming communication to a port.
	/** 
	 * The TCPConnection takes over the memory of the TCPSocket and is responsible for
	 *	deleting it when the TCPConnection is deleted.
	 */

	
	//private:
		//THESE METHODS SHOULD *NOT* be used
		//int iSend(Ref<Message>& m);
		//int iSend(Message* m);
		public int iSetSender(OutputPort sender)
		{
			System.out.println("attempted to set sender in a remote rcv-only conection");
			//m_tLog.error("attempted to set sender in a remote rcv-only conection");
			return 1;//SRI_ERR;
			
			
		}


		//note: assumes that m_ptReceiver was set to null in Connection.h (parent class)
		//and that m_ptReceiver will never be changed to non-null
		//Logger m_tLog;




	//public:
		public TCPReceiveConnection(SocketChannel sc)
		{
			m_ptSocketChannel = sc;
			try {
				sc.configureBlocking(false);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println("TCPReceiveConnection");
		}

				
		/// Returns a received Message.
		/**
		 * mReceive() blocks until it can retrive the entire message <em>change?</em>
		 * \return Pointer to one complete received message
		 */
		//Ref<Message> ptReceive();
		@Override
		public int iSend(Message m) {
			System.out.println("attempted to call iSend in a remote rcv-only conection");
			//m_tLog.error("attempted to call iSend in a remote rcv-only conection");
			return 1;// SRI_ERR;
		}
	//};
		@Override
		public Message ptReceive()  {
			

			
			
			
			 ByteBuffer lenbuf = ByteBuffer.allocateDirect(4);
			 String result="";
			try {
			    // Clear the buffer and read bytes from socket
			    lenbuf.clear();
			    
			    int numBytesRead = m_ptSocketChannel.read(lenbuf);
			    
			    while (lenbuf.position() != 4) {
			    	if (numBytesRead == -1) {
					    
				        // No more bytes can be read from the channel
			    		m_ptSocketChannel.close();
				    	break;
				    }
			    	if (numBytesRead == 0) return null;
			    	numBytesRead += m_ptSocketChannel.read(lenbuf);
			    }
			    
			    
			     
			    
			        // To read the bytes, flip the buffer
			    	lenbuf.flip();
			    	lenbuf.order(ByteOrder.LITTLE_ENDIAN);
			    	int lens=lenbuf.getInt();
			    	System.out.println("TCP Recv conn I read " + numBytesRead);
			    	System.out.println("TCP Recv connMessage length is  " + lens);
			    	System.out.println("TCP Recv conn Getting the message");
			    	
			    	ByteBuffer msgbuf = ByteBuffer.allocateDirect(lens);
			    	msgbuf.clear();
			    	
			    	numBytesRead = m_ptSocketChannel.read(msgbuf);
			    	
			    	
				    while (msgbuf.position() != lens) {
				    	if (numBytesRead == -1) {
						    
					        // No more bytes can be read from the channel
				    		m_ptSocketChannel.close();
					    	break;
					    }
				    	numBytesRead += m_ptSocketChannel.read(msgbuf);
				    	
				    }
			    	
			    	
			    	msgbuf.flip();
			    	msgbuf.order(ByteOrder.LITTLE_ENDIAN);
			    	
			    	
			        Charset charset = Charset.forName("us-ascii");
					CharsetDecoder decoder = charset.newDecoder();
					CharBuffer charBuffer = decoder.decode(msgbuf);
					result = charBuffer.toString();
					System.out.println("TCPRcev Conn INPUT FROM CLIENT RECEIVED IS "+result);

			        // Read the bytes from the buffer ...;
			        // see Getting Bytes from a ByteBuffer
			    
			} catch (IOException e) {
			    // Connection may have been closed
			}
			
	
			//m_ptSocket->receiveBytes(&messageLength, sizeof(int));
			//while(m_ptSocket->available() < messageLength); //block till full message comes over
			//TODO: change this networking code to be more efficient
			//char* temp = new char[messageLength]; //TODO: is there a better awy to do this?
			//m_ptSocket->receiveBytes(temp, messageLength);
			
			Message res = null;
			//TODO:: parse meta information what type of message to construct  ("Raw, meta or Object")
			
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
			//Using factory get an instance of document builder
			DocumentBuilder db;
			try {
				db = dbf.newDocumentBuilder();
				Document doc = db.parse(new InputSource(new ByteArrayInputStream(result.getBytes("utf-8"))));
				Element message;
				message=doc.getDocumentElement();//get the root element in Java method
				if(message == null){
					System.out.println("Received invalid message");
					//m_tLog.error("Received invalid message");
					return res;
				}
				String msgType = message.getAttribute("messageType"); 
				System.out.println("m type " + msgType);
				if(msgType.equals("")){
					//m_tLog.error("Unable to determine message type");
					System.out.println("Unable to determine message type");
					return res;
				}
				else if(msgType.equals("message")){
					res = new Message(message.getTextContent());
					System.out.println(res.szGetMessage());
					
				
				}
			} catch (ParserConfigurationException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			} catch (UnsupportedEncodingException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (SAXException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
				
			//parse using builder to get DOM representation of the XML file
			
		//#ifdef USE_TINYXML
			//TiXmlDocument doc;
			//doc.Parse(temp);
			
			//TiXmlElement* message = doc.RootElement();
			
			
		//#else
	/*		rapidxml::xml_document<> doc;
			doc.parse<rapidxml::parse_non_destructive>(temp);
			rapidxml::xml_node<>* rxMessage = doc.first_node("Message");
			if(rxMessage == NULL){
				m_tLog.error("Received invalid message");
				return res;
			}
			rapidxml::xml_attribute<>* rxaType = rxMessage->first_attribute("type");
			if(rxaType == NULL){
				m_tLog.error("Unable to determine message type");
				return res;
			}
			msgType = SRI::String(rxaType->value(),rxaType->value_size());
		#endif
*/
			
		/* to be implemented later when raw message class is created
			}else if(msgType == "rawMessage"){
				RawMessage m = new RawMessage();
				m->iSetMessage(temp);
				res.ptAttachNew(m);
			}else if(msgType == "objectMessage"){
				ObjectMessage* m = new ObjectMessage();
				m->iSetMessage(temp);
				res.ptAttachNew(m);
			}else{
				System.out.println("Received unsupported message");
				//m_tLog.error("Received unsupported message");
			}
			*/
			//delete[] temp;
			
			return res;
		}

	}


