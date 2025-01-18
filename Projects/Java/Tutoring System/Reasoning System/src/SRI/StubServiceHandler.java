package SRI;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.Socket;
import java.nio.channels.SocketChannel;
import java.util.HashMap;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

public class StubServiceHandler {


/** Monitors socket for incoming replies and wakes up the correct thread.
*/

	public int iCounter;//temp public

	public HashMap<String, ServerReplyStruct> m_Signals;//temp public

	public Socket m_Socket;//temp public
	public Socket m_Reactor;//temp public
	
	public StubServiceHandler(Socket socket, Socket reactor)
	{
		m_Socket=socket;
		//m_Socket.
		m_Reactor=reactor;
		System.out.println("StubServiceHandler");
		//m_tLog("StubServiceHandler", LOG_DEBUG),
		iCounter=0; 
		
		//m_Reactor.addEventHandler(m_Socket, Poco::NObserver<StubServiceHandler, Poco::Net::ReadableNotification>(*this, &StubServiceHandler::onReadable));
		//m_Reactor.addEventHandler(m_Socket, Poco::NObserver<StubServiceHandler, Poco::Net::ShutdownNotification>(*this, &StubServiceHandler::onShutdown));
	}
	
	
	public void onReadable()//ReadableNotification pNf)<-what is this for???
	{
		StringBuffer ptMsg = new StringBuffer();
		int err = 1;
		err = readBytes(m_Socket,ptMsg);
		if (err !=0 ) {//SRI_OK
			System.out.println("encountered network error %d"+ err);
			//m_tLog.error("encountered network error %d", err);
			return;
		}

		//m_tLog.debug("message: %s", ptMsg.ptGetObj()->c_str());
		System.out.println("message: %s" +ptMsg.toString());
		
		DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
		DocumentBuilder db;
		try {
			db = dbf.newDocumentBuilder();
			db = dbf.newDocumentBuilder();
			Document read = null;
			//try {
			read = db.parse(new InputSource(new ByteArrayInputStream(ptMsg.toString().getBytes("utf-8"))));
			//Poco::XML::DOMParser parser;
			//Poco::XML::AutoPtr<Poco::XML::Document> read = parser.parseString(ptMsg->c_str());

			NodeList list1 = read.getElementsByTagName("callerid");
			Node callerid =list1.item(0);
			StringBuffer ss=new StringBuffer();
			ss.append(callerid.getTextContent());
			String id=ss.toString();;
			
			if (!m_Signals.containsKey(id)) {
				//m_tLog.error("ServerReplyStruct not found! ID: %d", id);
				System.out.println("ServerReplyStruct not found! ID: %d "+ id);
				return;
			}

			ServerReplyStruct s = m_Signals.get(id);
			//s.e=new Event(s);
			s.reply = ptMsg.toString();
			System.out.println(" THE FINAL MSG IS "+s.reply);
//			synchronized (s.e) {//need to do that in Java only for using the wait()as well as notify()
//				s.e.notify();//for testing purpose
//			  //  e.notify();
//			}
			
		} catch (ParserConfigurationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
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
		
		
	

		//Poco::XML::Node *reply = read->getNodeByPath("reply");
		//SRI::String rep(reply->innerText());

		
	}
	
	public void onShutdown()//ShutdownNotification pNf)<-What is this for???
	{
		System.out.println("ShutDown");
	}

	public int iRegisterEvent(ServerReplyStruct s)
	{
		String counter1=Integer.toString(++iCounter);
		m_Signals=new HashMap<String,ServerReplyStruct>();
		m_Signals.put(counter1, s) ;

		return iCounter;
	}

	//provide method for registering thread, or rather co-ordinating event
	
//private:
	//co-ordinate with the socket lock
	//register with the service handler first, get a ticket, then send!, got it! problem. signal sent before i get the thing
	
	
	
	public int readBytes(Socket socket, StringBuffer msg) {
		
		DataInputStream in = null;
		String inputLine="";
		try {
			in = new DataInputStream(socket.getInputStream());
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	    
        int len=0;
       
        
       
        	try {
        		
        		byte[] b;
        		
        		
            	len = in.readInt();//pass the control to server
            	int revLen=Integer.reverseBytes(len);
            	// revLen=Integer.reverseBytes(revLen);
            	System.out.println("MY NEW LEN IS "+revLen);
                b = new byte[revLen];
               
                in.readFully(b,0,revLen);//pass the control to server
               
				inputLine = new String(b);
				
				
				//msg=inputLine;
				//if(vStopServer(inputLine))
				//{
				//System.out.println("Shutting Down the Comms");
				//in.close();
				//out.close();
				//kkSocket.close();
			//	break;
			//	}
        		
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
		// Again, probably better to store these objects references in the support class
		/*
        BufferedReader in = new BufferedReader(
                new InputStreamReader(
                socket.getInputStream()));
        String inputLine="";
       // System.out.println("IN is "+inputLine);
       
        while ((inputLine = in.readLine()) != null) {
            System.out.println("IN is "+inputLine);
        	msg=inputLine;
        	return 0;  
        }
    
        in.close();
        return 1;
        *///	msg="testse";
        	 msg.append(inputLine);
        	 
        	 System.out.println("THE MSG FROM SERVER:: " + msg.toString());
        	return 0;
    }


} 