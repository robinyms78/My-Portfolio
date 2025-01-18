package SRI;

import org.w3c.dom.Document;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Text;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
//import java.io.StringWriter;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
//import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import java.io.*;
import java.net.*;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
//import java.lang.Object;
import java.nio.ByteOrder;
import java.nio.channels.Channel;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.util.Iterator;
import java.util.Set;

public abstract class Server extends Component
{

	
		private Thread m_ptMyThread;
	    //private Reactor m_ptSocketReactor;
	    //private ServerSocketAcceptor<ServerServiceHandler> m_ptServerSocketAcceptor;
		public ServerSocket m_ptServerSocket;
		
		public Selector sel = null;
	    public ServerSocketChannel server =null;
	    public SocketChannel socket = null;
	    public int callerId=0;
	    //public static int connectedPort;
	    
	   // public int port = 4900;
	    String result = "";
		
		public Server()
		{
			
		}
	
		/*// not using
		 public void initializeOperations() throws IOException,UnknownHostException
		    {
				System.out.println("Inside initialization");
				sel = Selector.open();
				server = ServerSocketChannel.open();
				server.configureBlocking(false);
				InetAddress ia = InetAddress.getLocalHost();
				InetSocketAddress isa = new InetSocketAddress(ia,port);
				server.socket().bind(isa);
		    }
		*/
		protected String szCreateXMLReply() throws TransformerException //for now we assume it is robust and can parse correctly
		{
			String outputString = null;
			Document pDoc;
			StreamResult outer = new StreamResult();
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
			//get an instance of builder
			DocumentBuilder db;
			
						try {
							db = dbf.newDocumentBuilder();
							pDoc = db.newDocument();
							
							Element reply = pDoc.createElement("reply");
							//Element rettype = pDoc.createElement("rettype");
							//Text rettypetext =pDoc.createTextNode("int");
							//rettype.appendChild(rettypetext);
							//reply.appendChild(rettype);
							
							Element retval = pDoc.createElement("retval");
							Text retvaltext =pDoc.createTextNode("");
							retval.appendChild(retvaltext);
							reply.appendChild(retval);
							Element callerid = pDoc.createElement("callerid");
							Text calleridtext =pDoc.createTextNode(String.valueOf(callerId));
							//Text calleridtext =pDoc.createTextNode("1");
							
							//Poco::XML::AutoPtr<Poco::XML::Element> callerid = doc->createElement("callerid");
							//Poco::XML::AutoPtr<Poco::XML::Text> calleridtext = doc->createTextNode(o.szGetCallerID().c_str());
							callerid.appendChild(calleridtext);

							reply.appendChild(callerid);
							
							pDoc.appendChild(reply);
							
							//pDoc.appendChild(pReply);

							//pReply.setAttribute("rettype", "string");
							//pReply.setAttribute("retval", retval);

							outputString=vXMLDocToStringStream(outer, pDoc);
							
						} catch (ParserConfigurationException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}	
						
			
			return outputString;
			
			
		}
		
		
		protected String szCreateXMLReply(int retval1) throws TransformerException
		{
			//Document pDoc = null;
			String outputString = null;
			Document pDoc;
			StreamResult outer = new StreamResult();
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
			//get an instance of builder
			DocumentBuilder db;
			
						try {
							db = dbf.newDocumentBuilder();
							pDoc = db.newDocument();
							
							Element reply = pDoc.createElement("reply");
							Element rettype = pDoc.createElement("rettype");
							Text rettypetext =pDoc.createTextNode("int");
							rettype.appendChild(rettypetext);
							reply.appendChild(rettype);
							
							Element retval = pDoc.createElement("retval");
							Text retvaltext =pDoc.createTextNode(Integer.toString(retval1));
							retval.appendChild(retvaltext);
							reply.appendChild(retval);
							Element callerid = pDoc.createElement("callerid");
							Text calleridtext =pDoc.createTextNode(String.valueOf(callerId));
							
							//Poco::XML::AutoPtr<Poco::XML::Element> callerid = doc->createElement("callerid");
							//Poco::XML::AutoPtr<Poco::XML::Text> calleridtext = doc->createTextNode(o.szGetCallerID().c_str());
							callerid.appendChild(calleridtext);

							reply.appendChild(callerid);
							
							pDoc.appendChild(reply);
							
							//pDoc.appendChild(pReply);

							//pReply.setAttribute("rettype", "string");
							//pReply.setAttribute("retval", retval);

							outputString=vXMLDocToStringStream(outer, pDoc);
							
						} catch (ParserConfigurationException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}	
						
			
			return outputString;
		}
		
		
		//protected String szCreateXMLReply(int retval); 
		protected String szCreateXMLReply(boolean retval1) throws TransformerException
		{
		
			//Document pDoc = null;
			String outputString = null;
			Document pDoc;
			StreamResult outer = new StreamResult();
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
			//get an instance of builder
			DocumentBuilder db;
			
						try {
							db = dbf.newDocumentBuilder();
							pDoc = db.newDocument();
							Text retvaltext=null;
							Element reply = pDoc.createElement("reply");
							Element rettype = pDoc.createElement("rettype");
							Text rettypetext =pDoc.createTextNode("string");
							rettype.appendChild(rettypetext);
							reply.appendChild(rettype);
							
							Element retval = pDoc.createElement("retval");
							if(retval1){
							retvaltext =pDoc.createTextNode("true");
							}
							else{
							retvaltext =pDoc.createTextNode("false");
							}
							retval.appendChild(retvaltext);
							reply.appendChild(retval);
							Element callerid = pDoc.createElement("callerid");
							Text calleridtext =pDoc.createTextNode(String.valueOf(callerId));
							//Text calleridtext =pDoc.createTextNode("1");
							
							//Poco::XML::AutoPtr<Poco::XML::Element> callerid = doc->createElement("callerid");
							//Poco::XML::AutoPtr<Poco::XML::Text> calleridtext = doc->createTextNode(o.szGetCallerID().c_str());
							callerid.appendChild(calleridtext);

							reply.appendChild(callerid);
							
							pDoc.appendChild(reply);
							
							//pDoc.appendChild(pReply);

							//pReply.setAttribute("rettype", "string");
							//pReply.setAttribute("retval", retval);

							outputString=vXMLDocToStringStream(outer, pDoc);
							
						} catch (ParserConfigurationException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}	
			return outputString;
			
		}
		
		
		protected String szCreateXMLReply(String retval1) throws TransformerException
		{
			
			//Document pDoc = null;
			String outputString = null;
			Document pDoc;
			StreamResult outer = new StreamResult();
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
			//get an instance of builder
			DocumentBuilder db;
			
						try {
							db = dbf.newDocumentBuilder();
							pDoc = db.newDocument();
							
							Element reply = pDoc.createElement("reply");
							Element rettype = pDoc.createElement("rettype");
							Text rettypetext =pDoc.createTextNode("string");
							rettype.appendChild(rettypetext);
							reply.appendChild(rettype);
							
							Element retval = pDoc.createElement("retval");
							Text retvaltext =pDoc.createTextNode(retval1);
							retval.appendChild(retvaltext);
							reply.appendChild(retval);
							Element callerid = pDoc.createElement("callerid");
							Text calleridtext =pDoc.createTextNode(String.valueOf(callerId));
							//Text calleridtext =pDoc.createTextNode("1");
							
							//Poco::XML::AutoPtr<Poco::XML::Element> callerid = doc->createElement("callerid");
							//Poco::XML::AutoPtr<Poco::XML::Text> calleridtext = doc->createTextNode(o.szGetCallerID().c_str());
							callerid.appendChild(calleridtext);

							reply.appendChild(callerid);
							
							pDoc.appendChild(reply);
							
							//pDoc.appendChild(pReply);

							//pReply.setAttribute("rettype", "string");
							//pReply.setAttribute("retval", retval);

							outputString=vXMLDocToStringStream(outer, pDoc);
							
						} catch (ParserConfigurationException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}	
			return outputString;
			
			
			
			
		}
		
		
		protected String vXMLDocToStringStream(StreamResult result, Document pDoc) throws TransformerException
		{
			
			TransformerFactory tFact = TransformerFactory.newInstance();
            Transformer trans = tFact.newTransformer();

            StringWriter writer = new StringWriter();
            result = new StreamResult(writer);
            DOMSource source = new DOMSource(pDoc);
           
            trans.transform(source, result);
      
            return writer.getBuffer().toString();
		}

	
		
		/// Binds the server to port and starts the server listening in a separate thread. Pass 0 to use OS-supplied random port.
		public void vStartServer(int port) throws IOException
		{
			//Socket clientSocket=new Socket();
			 //boolean listening=true;
			
				
			//try{
				
					//m_ptServerSocket = new ServerSocket(port);
				//new doComms(m_ptServerSocket.accept()).start();
				//System.out.println("I M HERE ");
					
			
	   
			doComm conn_c= new doComm(port);//temp remark
			m_ptMyThread = new Thread(conn_c);//temp remark
			m_ptMyThread.start();// temp remark this will indirectly invoke the run() method in doComm class
			      
			        // }
		//	    }
			// catch (IOException ioe) {
			     // System.out.println("IOException on socket listen: " + ioe);
			     // ioe.printStackTrace();
			   // }
		
		//	m_ptServerSocket.close();
			
			//return clientSocket;
		}
		
		
		
	
		 
		 
		 
		class doComm extends Thread {
		  
		   int port;

		    doComm(int port) {
		      this.port=port;
		     
		    }
		    
		    public void run () {
			    
		    	try {
		    		
					sel = Selector.open();
					//server.configureBlocking(false);
					server = ServerSocketChannel.open();
					
					server.configureBlocking(false);
					InetAddress ia = InetAddress.getLoopbackAddress();
					InetSocketAddress isa = new InetSocketAddress(ia,port);
					server.socket().bind(isa);
					//Server.connectedPort=server.socket().getLocalPort();
					
				//	if (server==null)
					//{
						
						
					//}
					
						
					
			        			
					SelectionKey acceptKey = server.register(sel, SelectionKey.OP_ACCEPT );	
					
					while(acceptKey.selector().select() > 0 )
					{	
						
						//System.out.println(" ABCDB ");
						Set<SelectionKey> readyKeys = sel.selectedKeys();
						Iterator<SelectionKey> it = readyKeys.iterator();

						while (it.hasNext()) {
							SelectionKey key = (SelectionKey)it.next();
							it.remove();
							//if (!key.isValid()) {
							//	continue;
						//	}
							if (key.isAcceptable()) {
								
								 //System.out.println("Host Address is 123 ");
								
								ServerSocketChannel ssc = (ServerSocketChannel) key.channel();
								socket = (SocketChannel) ssc.accept();
								socket.configureBlocking(false);
								SelectionKey another = socket.register(sel,SelectionKey.OP_READ);//SelectionKey.OP_READ|
								//Thread.yield();
								
								
							}
							
							if (key.isConnectable()) {
								//System.out.println("TESTETE");
							
							}
							if (key.isReadable()) {
								
								String ret = readMessage(key);
								if (ret.length() > 0) {
									writeMessage(ret,key);
								}
							}
							if (key.isWritable()) {
								
								String ret = readMessage(key);
								
								socket = (SocketChannel)key.channel();
								if (result.length() > 0 ) {
									
									
									writeMessage(ret,key);
								}
							}
						}
					}
					
					
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				
				
		}
		}
		
		
		 public String readMessage(SelectionKey key)
		    {
			 
			// Create a direct buffer to get bytes from socket.
			// Direct buffers should be long-lived and be reused as much as possible.
			 SocketChannel socket1 = (SocketChannel)key.channel();
			 ByteBuffer lenbuf = ByteBuffer.allocateDirect(4);

			try {
			    // Clear the buffer and read bytes from socket
			    lenbuf.clear();
			    int numBytesRead = socket1.read(lenbuf);
			    
			    while (lenbuf.position() != 4) {
			    	if (numBytesRead == -1) {
					    
				        // No more bytes can be read from the channel
				    	socket1.close();
				    	break;
				    }
			    	numBytesRead = socket1.read(lenbuf);
			    }
			    
			    
			     
			    
			        // To read the bytes, flip the buffer
			    	lenbuf.flip();
			    	lenbuf.order(ByteOrder.LITTLE_ENDIAN);
			    	int lens=lenbuf.getInt();
			    	System.out.println("I read " + numBytesRead);
			    	System.out.println("Message length is  " + lens);
			    	System.out.println("Getting the message");
			    	
			    	ByteBuffer msgbuf = ByteBuffer.allocateDirect(lens);
			    	
			    	numBytesRead = socket1.read(msgbuf);
			    	
				    while (msgbuf.position() != lens) {
				    	if (numBytesRead == -1) {
						    
					        // No more bytes can be read from the channel
					    	socket1.close();
					    	break;
					    }
				    	numBytesRead = socket1.read(msgbuf); 
				    }
			    	
			    	
			    	msgbuf.flip();
			    	msgbuf.order(ByteOrder.LITTLE_ENDIAN);
			    	
			    	
			        Charset charset = Charset.forName("us-ascii");
					CharsetDecoder decoder = charset.newDecoder();
					CharBuffer charBuffer = decoder.decode(msgbuf);
					result = charBuffer.toString();
					System.out.println("INPUT FROM CLIENT RECEIVED IS "+result);

			        // Read the bytes from the buffer ...;
			        // see Getting Bytes from a ByteBuffer
			    
			} catch (IOException e) {
			    // Connection may have been closed
			}
			
		
		    
		    
				
				return result;
		    }
		
		
		 
		 public void writeMessage(String ret,SelectionKey key)
		    {
			 	System.out.println("Inside the loop " + ret);
				SocketChannel socket = (SocketChannel)key.channel();
				
				try
				{
				  
				  String reply=szProcessXMLMessage( ret, socket);
				 
		          //convert length to byte array of length 4
		          ByteBuffer bb = ByteBuffer.allocate(4+reply.length()); // +1 for null character
		          bb.order(ByteOrder.LITTLE_ENDIAN);
		          int lenn=reply.length();
		      
		          bb.putInt(reply.length());
		         
		          bb.put(reply.getBytes());
		          bb.flip();
		      //    bb = ByteBuffer.wrap((reply).getBytes());
		          int nBytes = socket.write(bb);
		          System.out.println("nBytes = "+nBytes);
		          System.out.println("retlen " + reply.length());
		          System.out.println("OUTPUT FROM SERVER " + reply);
		          
		       //if (vStopServer(ret)) {
		        	
		    	 //   key.channel().close();
				//	key.cancel();
					//return;
					//stop all communication
					
				//}
		         
				  result = "";
				}
		         
				
				catch(Exception e)
				{
					e.printStackTrace();
				}

		    }
		
	
		
		public boolean vStopServer(String msg)
		{
				String funcname=null;
				String text=msg;
				boolean shutdown=false;
			//get the factory
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
		//	try {
				
				//Using factory get an instance of document builder
			try {	
				DocumentBuilder db = dbf.newDocumentBuilder();
				
				   

					db = dbf.newDocumentBuilder();
					Document pDoc = null;
					try {
						pDoc = db.parse(new InputSource(new ByteArrayInputStream(text.getBytes("utf-8"))));
					} catch (SAXException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					
					NodeList list = pDoc.getElementsByTagName("function");
					NamedNodeMap arglist = list.item(0).getAttributes();

					Node name = arglist.getNamedItem("name");
					//TODO handle cases where name is void
					funcname=name.getNodeValue();
				} catch (ParserConfigurationException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				
			if (funcname.equals("shutdown")) { 
			
			
				shutdown=true;
				//stop all communication
				
			}
			return shutdown;
		}
		
		
		public String readBytes(Socket socket) throws IOException {
		    // Again, probably better to store these objects references in the support class
			
	        BufferedReader in = new BufferedReader(
	                new InputStreamReader(
	                socket.getInputStream()));
	        String inputLine="";
	       
	 
	        while ((inputLine = in.readLine()) != null) {
	           //  System.out.println("IN is "+inputLine);
	        	return inputLine;  
	        }
	      //  in.close();
	        in.close();
	        return "";
	        
	    }

			
			
		public void sendBytes(String str1 ,Socket socket) throws IOException {
			
	
				 PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
			     
			        //String outputLine = str1;
			        System.out.println("OUTPUT FROM SERVER " + str1);
			        out.println(str1);
			      
			        out.close();
			    }
		
			

		

		
		/// Returns the port the server is listening on.
		public int iGetServerPort()
		{
			//if (server==null)
			//System.out.println(" ITS A NULL ");
			if (server.socket().getLocalPort()!=-1||server.socket().getLocalPort()!=0) {
				
				return server.socket().getLocalPort();
			}
			
			else 
				
				return 0;
			
		}

		/// Joins the thread that the server listens on.
		public void vJoinServerThread() 
		{
			try {
				m_ptMyThread.join();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		/// Called by SocketReactor to process incoming XML messages
		//TODO: make private, make Reactor friend?
		public String szProcessXMLMessage(String msg, SocketChannel s) throws ParserConfigurationException, SAXException, IOException, TransformerException
		{
			
			String text=msg;
			
			//get the factory
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
			//Using factory get an instance of document builder
			DocumentBuilder db = dbf.newDocumentBuilder();
				
			//parse using builder to get DOM representation of the XML file
			Document pDoc = db.parse(new InputSource(new ByteArrayInputStream(text.getBytes("utf-8"))));
				
			
			//DOMParser parser;
			//NodeList list = pDoc.getElementsByTagName("reply");
			
			////NodeList list = pDoc.getElementsByTagName("function");
			NodeList list = pDoc.getElementsByTagName("args");
			NodeList list1 = pDoc.getElementsByTagName("name");
			String funcname=list1.item(0).getTextContent();
			Node n=list.item(0);
			
			//System.out.println(" LIST NAME "+list.getLength());
			NodeList arglist =  list.item(0).getChildNodes();//means get the first item in the list
			NodeList list2=pDoc.getElementsByTagName("callerid");
			callerId=Integer.parseInt(list2.item(0).getTextContent());
			//Node name = arglist.getNamedItem("name");
			//Node name = arglist.getNamedItem("retval");
			//TODO handle cases where name is void
			//String funcname=name.getNodeValue();
			
			String reply="";
			//String replyList[] = new String[100];
			//functions common to all types of servers
			if (funcname.equals("shutdown")) { 
				
				reply = szCreateXMLReply("shutdown");
				
				s.close();
				//key.cancel();
				//return;
				//stop all communication
				
			}
			else if (funcname.equals("myIp")) {
				SocketAddress ip=s.getLocalAddress();
				
				reply = szCreateXMLReply(ip.toString());
			}
			
			else 
				
				//reply = szCreateXMLReply("No Such Command");
				reply=szCallFunction(funcname, arglist);
			 
			return reply;
			
		}
		
		static void writeOutput(String str) {
		    try {
		        FileOutputStream fos = new FileOutputStream("test.txt");
		        Writer out = new OutputStreamWriter(fos, "UTF8");
		        out.write(str);
		        //out.close();
		    } 
		    catch (IOException e) {
		        e.printStackTrace();
		    }
		}
	  
	  
	  static String readInput() {
		    StringBuffer buffer = new StringBuffer();
		    try {
		        FileInputStream fis = new FileInputStream("test.txt");
		        InputStreamReader isr = new InputStreamReader(fis, "UTF8");
		        Reader in = new BufferedReader(isr);
		        int ch;
		        while ((ch = in.read()) > -1) {
		            buffer.append((char)ch);
		        }
		        in.close();
		        return buffer.toString();
		    } 
		    catch (IOException e) {
		        e.printStackTrace();
		        return null;
		    }
		}
		

		/// This function calls the appropriate method of the proxied object. Override to provide server functionality specific to a class.
		public abstract String szCallFunction(String msg, NodeList arglist);//temp disabled for testing purpose
		
	
	
}

