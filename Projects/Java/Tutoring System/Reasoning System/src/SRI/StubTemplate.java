package SRI;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.StringWriter;
import java.io.UnsupportedEncodingException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.channels.SelectionKey;
import java.nio.channels.SocketChannel;
import java.util.Vector;
import java.util.concurrent.locks.ReentrantLock;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Text;
//import org.w3c.dom.events.Event;
//import org.w3c.dom.events.Event;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

public class StubTemplate {
	
	//	class Mutex;

		//namespace Net {
			//class StreamSocket;
			//class SocketReactor;
	//	}

	//	namespace XML {
		//	class Document;
		//}
	//} //end namespace Poco

	//namespace SRI {


	/// Helper class providing functionality needed by Stubs
	/**	The StubTemplate class provides methods used by all Stubs. These methods are 
		responsible for marshalling arguments to send to Servers, and for unpacking
		their replies.

		Stubs communicate with Servers via XML strings. A stub calls a function on the
		remote object by creating a string containing a single XML element named "function".	This element has a "name" attribute, which contains the name of the function that is to be
		called, and may have one or more attributes with the name "arg[X]" (where X 
		is a number) which contain the values of arguments supplied to the function.
		The first argument will have the name arg0, the second argument arg1, and so on.
		
		For example:<br>
		\<function name="szGetID" /><br>
		\<function name="iSetName" arg0="new_name" /><br>
		\<function name="iCreateOutputPort" arg0="name_of_port" arg1="type_of_port" /><br>

		There are no XML header tags nor metadata in the string, as it is assumed that
		all communication between Stubs and Servers will use XML strings of the format detailed above.

		The Server, after processing the incoming XML string and calling the desired function,
		returns the return value to the Stub by creating a string containing a single
		XML element named "reply". This element has two attributes: "rettype", which 
		identifies the type of the return value, and "retval", which contains the actual
		return value as a string. The currently supported return value types and their
		possible retvals are detailed below:

		<table>
		<tr><td>Rettype</td>			<td>Retval</td></tr>
		<tr><td>void</td>				<td>"" (empty string)</td></tr>
		<tr><td>unsigned int</td>		<td>\<string representation of valid unsigned values></td></tr>
		<tr><td>int</td>				<td>\<string representation of valid int values></td></tr>
		<tr><td>bool</td>				<td>"true"/"false"</td></tr>
		<tr><td>string</td>				<td>\<the literal string></td></tr>
		</table>

		NOTE: replies of type void do _not_ have the rettype attribute, only 
		the retval attribute.

		These are examples of valid replies:<br>
		\<reply retval=""> (void reply)<br>
		\<reply rettype="int" retval="3556"> (int reply)<br>
		\<reply rettype="bool" retval="false"> (bool reply)<br>
		\<reply rettype="string" retval="name of component"> (string reply)<br>

	*/

	
		
		private static String m_ptEmptyString; //to avoid overhead of empty string creation; see szCallFunction
		
		//Logger m_tLog;
		
		private String m_szPeerIp;
		private int m_iPeerPort;
		private String m_szMyIp; //as seen from peer


		//StubTemplate(const StubTemplate& s);
		//StubTemplate& operator=(const StubTemplate& s);

		

		private ReentrantLock m_Mutex ;

		//mutable Poco::Mutex m_Mutex;

		public SocketChannel m_ptSocket;

		private Socket m_SocketReactor;
		
		StubServiceHandler m_ptStubHandler;

		public Thread m_Thread;
		
		public StubTemplate()
		{
			
		}

		public String szCreateXMLMessage(String funcName, Vector<String> args, int id) throws TransformerException
		{//temp change to public for testing
			Document doc = null;
			StreamResult outer = new StreamResult();
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			String outputString = null;
			//get an instance of builder
			DocumentBuilder db;
			
				
					try {
						db = dbf.newDocumentBuilder();
						doc = db.newDocument();
					} catch (ParserConfigurationException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					
					
			//Document doc ;
			
			Element func = doc.createElement("function");
			

			//function name
			Element name = doc.createElement("name");
			Text nametext = doc.createTextNode(funcName);
			name.appendChild(nametext);

			func.appendChild(name);
			
			//arglist
			StringBuffer ss=new StringBuffer(); 
			
			int numargs = args.size();
			ss.append(numargs);
			
			Element argsList = doc.createElement("args");

			argsList.setAttribute("numArgs", ss.toString());
			ss.setLength(0);
			
			for (int i = 0; i < numargs; i++) {
				
				ss.append("arg"); //"arg" << i;
				ss.append(i);
				Element arg = doc.createElement(ss.toString());
				ss.setLength(0);
					
				
				Text argtext = doc.createTextNode(args.elementAt(i));
				ss.setLength(0);

				arg.appendChild(argtext);
				argsList.appendChild(arg);
					
			}

			func.appendChild(argsList);

			ss.append (id);
			//caller id
			Element callerid = doc.createElement("callerid");
			Text calleridtext = doc.createTextNode(ss.toString());
			callerid.appendChild(calleridtext);
			
			func.appendChild(callerid);
			
			ss.setLength(0);

			doc.appendChild(func);

			//std::stringstream outer;

			outputString=vXMLDocToStringStream(outer, doc);
			//m_tLog.debug("%s", outer.str().c_str());
			System.out.println( outer);
			return outputString;
		}
			

		public String vXMLDocToStringStream(StreamResult s, Document pDoc)
		{//temp change to public for testing
			TransformerFactory tFact = TransformerFactory.newInstance();
            Transformer trans;
            StringWriter writer = new StringWriter();
			try {
				trans = tFact.newTransformer();
				 
		            s = new StreamResult(writer);
		            DOMSource source = new DOMSource(pDoc);
		           
		            trans.transform(source, s);
			} catch (TransformerConfigurationException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

          
      
            return writer.getBuffer().toString();
		}
		
		
		private String szParseReply(String reply)
		{
			System.out.println("StubTemplate const function logger "+reply);
			//log.debug("%s", reply.c_str());
			String text=reply;
			
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
			//Using factory get an instance of document builder
			DocumentBuilder db;
			String returnValue = "";
			try {
				db = dbf.newDocumentBuilder();
				Document pDoc = db.parse(new InputSource(new ByteArrayInputStream(text.getBytes("utf-8"))));
				NodeList list1 = pDoc.getElementsByTagName("rettype");//getNodeByPath("rettype");
				NodeList list2 = pDoc.getElementsByTagName("retval");
				
				Node rettype=list1.item(0);
				Node retval=list2.item(0);
				returnValue=retval.getTextContent();
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
				
			//parse using builder to get DOM representation of the XML file
			
			//Parser parser;
			//Document pDoc = parser.parseString(text)
			
			return returnValue;
		}

		///Blocks until reply message from module arrives
	//	private String vGetMessage()
	//	{
			
	//	}

		//Poco::ActiveMethod<String, String, StubTemplate> activeCallDispatch;
		private String szCallDispatch(String msg)//what is this for???
		{
			vSendMessage(msg);
			Event e = new Event(m_Thread)  ;//new to create your own Event class in Java
			
			//e.initEvent("eventTypeArg", false, false);
			try {
				e.wait();
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}

			//a task should contain: a pointer to the event, a place to put the return value, and an id

			return "";
			

			//go the sleep, wait to wake up and reply, information (how to pass)
			//then return
		}

	//public:
		/// Constructor
		/**
			\param ip IP of the Server to connect to
			\param portNo Port number of the Server to connect to
		*/
		public StubTemplate(String ip, int portNo)
		{
			//m_tLog("StubTemplate", LOG_DEBUG),
			m_szPeerIp=ip;
			m_iPeerPort=portNo;
			//activeCallDispatch(this, &StubTemplate::szCallDispatch)
			//{
				String ipaddr=m_szPeerIp;
				InetSocketAddress sa = new InetSocketAddress(ipaddr, m_iPeerPort);
				//SocketAddress sa(ipaddr, m_iPeerPort); 
				try {
					//m_ptSocket=new SocketChannel()
					m_ptSocket=SocketChannel.open(sa);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} //= new Socket(sa);

				//m_ptStubHandler = new StubServiceHandler(*m_ptSocket, m_SocketReactor);
				//socketreactor handles the destructor of the m_ptSTubHandler
				m_Thread=new Thread();
				m_Thread.start();

				StringBuffer reply = new StringBuffer();
					 
				
				
				int err = szCallFunction("myIp", reply); //assumes my ip will never change, should be valid for the duration of the netire connection
				
				if (err != 0){//SRI_OK) {
					System.out.println("unable to connect to server");
					//m_tLog.error("unable to connect to server");
					m_szMyIp = "invalid";
				}

				m_szMyIp = reply.toString();
				System.out.println("connection established. my ip %s\tmy port%d\tpeer ip%s\tpeer port %d"+ szGetMyIp()+ iGetMyPort()+ szGetPeerIp()+ iGetPeerPort());
				//m_Thread.yield();
				/*synchronized (this) {
					try {
						this.wait();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					//this.notifyAll();
				}
				
			*/	
		}
		
	

		//const method provided for use by const functions
		public int szCallFunction(String funcName, Vector<String> args, StringBuffer retValue)
		{
			int ret = 0;
			
			//Event e = new Event(m_ptSocket);//cant be null
			ServerReplyStruct srs = new ServerReplyStruct();
			
			//srs.e = e;

			//new thread sends info, goes to sleep
			
			{
				//ScopedLock slock(m_Mutex);
				 

				if (m_ptStubHandler == null) m_ptStubHandler=new StubServiceHandler(m_ptSocket.socket(),m_SocketReactor);
				int id = m_ptStubHandler.iRegisterEvent(srs);
				
				String message = "";
				try {
					message = szCreateXMLMessage(funcName, args, id);
				} catch (TransformerException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}

				
				ret = vSendSocket(message, m_ptSocket);
				if (ret < 0) { 
					return ret;
				}
				
			}
			
//			try {
//				synchronized (e) {//need to do that in Java only for using the wait()as well as notify()
//				    e.wait(3000);//for testing purpose
//				  //  e.notify();
//				}
//				//e.wait();
//			} catch (InterruptedException e1) {
//				// TODO Auto-generated catch block
//				e1.printStackTrace();
//			}
			
			//the reply is now hard coded for testing purpose only
			//srs.reply="<reply><rettype>bool</rettype><retval>/10.217.162.235:4448</retval><callerid>1</callerid></reply>";//testing purpose only
			
			m_ptStubHandler.onReadable();//the method to get the msg tothe stub is different from C++version as this does not use the event 
			String parsed = szParseReply(srs.reply);
			//System.out.println(" TESTING 1 "+parsed);
			retValue.append(parsed);
			System.out.println(" TESTING 2 "+retValue);
			return 0;// SRI_OK;
		}
		
		
		
		public int szCallFunction(String funcName, StringBuffer retstring)
		{
			Vector<String> args = new Vector<String>();
			return szCallFunction(funcName, args, retstring);
		}

		

		/// Sends the shutdown signal to a server
		public void vShutdownRemote()
		{
			//update this function
			/*std::vector<SRI::String> args;
			SRI::String message = szCreateXMLMessage("shutdown", args, 0); 
			SRITCPUtils::vSendSocket(message, m_ptSocket);*/
		}
		
		void vSendMessage(String msg)
		{
			m_Mutex=new ReentrantLock();
			m_Mutex.lock();
			 vSendSocket(msg, m_ptSocket);
			 m_Mutex.unlock();
		}
	 
		//missing copy constructor, assignment operator, == operator

		/// Returns the IP address of the associated Server
		public String szGetPeerIp()
		{
			return m_szPeerIp;
		}
		/// Returns the port no of the associated Server
		public int iGetPeerPort()
		{
			return m_iPeerPort;
		}
		
		/// Returns this StubTemplate's IP address, as seen by the associated Server
		public String szGetMyIp()
		{
			
			return m_szMyIp;
		}
		/// Returns this StubTemplate's port
		public int iGetMyPort()
		{
			//return socket.getLocalPort();
			return m_ptSocket.socket().getPort();
		}

		
	
		public static int vSendSocket(String msg,SocketChannel socket) {
			int size = msg.length(); 
			
			
					try
					{
					  
			          //convert length to byte array of length 4
			          ByteBuffer bb = ByteBuffer.allocate(4+msg.length()); // +1 for null character
			          bb.order(ByteOrder.LITTLE_ENDIAN);
			          int lenn=msg.length();
			      
			          bb.putInt(msg.length());
			         
			          bb.put(msg.getBytes());
			          bb.flip();
			      //    bb = ByteBuffer.wrap((reply).getBytes());
			          int nBytes = socket.write(bb);
			          System.out.println("nBytes = "+nBytes);
			          System.out.println("retlen " + msg.length());
			          System.out.println("OUTPUT FROM STUB " + msg);
			          
			      
			         
					  msg = "";
					}
			         
					
					catch(Exception e)
					{
						e.printStackTrace();
						return 1;
					}

			    //}
			//vSendNBytes((char *)&size, sizeof(int), socket);

			return 0;

		}




}
