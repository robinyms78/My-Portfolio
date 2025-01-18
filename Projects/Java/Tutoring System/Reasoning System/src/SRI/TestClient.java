package SRI;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.Reader;
import java.io.StringWriter;
import java.io.Writer;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Vector;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Text;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import SRI.Server.doComm;

public class TestClient   {
    
  public  Socket kkSocket;//=new Socket(); //= new Socket("taranis", 4444);
  private DataInputStream in; 
  private OutputStream out;
  private int port;
  private String fromUser="";
  //private String fromServer=null;
  Component comp6=new Component();
  private ComponentServer s1=new ComponentServer(comp6);
  
  public TestClient(int port)
  {
	  this.port=port;
	  kkSocket=null;
	  if(port!=1234){//when input as port 1234 means testing that not need to connect to server
	 initiateConnect(port);
	  }//  this.start();
	//doComm conn_c= new doComm(port);//temp remark
	//m_ptMyThread = new Thread(conn_c);//temp remark
//	this.start();
	  
  }
  
  public void run () 
  { 	
	 
		//initiateConnect(port);
		
		//comunicate("myIp");
		
	  
  }
  
  public void initiateConnect(int port)
  {
	  try {
		  
		kkSocket=new Socket("127.0.0.1",port);
				
		out = kkSocket.getOutputStream();

		in = new DataInputStream(kkSocket.getInputStream());
		
		
	
		
		//Component comp5=new Component();
		//ComponentServer s1=new ComponentServer(comp5);
	  } catch (UnknownHostException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
		
  }
  
  
  public void comunicate(String msg)
  {
	 
	
			  try {
				  Vector<String>arg=new Vector<String>();
				fromUser=this.szCreateXMLMessage(msg,arg,1);
			
				ByteBuffer bb = ByteBuffer.allocate(4+fromUser.length());
				bb.order(ByteOrder.LITTLE_ENDIAN);
				bb.putInt(fromUser.length());
		    
		        bb.put(fromUser.getBytes());
		       
		        out.write(bb.array());
		        
		        
		        out.flush();
		        
		    
				
			} catch (TransformerException e) {
				
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
			
			
	        String inputLine="";
	        int len=0;
	   
	        
	        
	        
	        	try {
	        		
	        		byte[] b;
	        		
	        		
	            	len = in.readInt();//pass the control to server
	            	int revLen=Integer.reverseBytes(len);
	            	// revLen=Integer.reverseBytes(revLen);
	            	System.out.println("MY NEW LEN IS "+revLen);
	                b = new byte[revLen];
	               
	                in.readFully(b,0,revLen);//pass the control to server
	               
					inputLine = new String(b);;
					System.out.println("THE MSG FROM SERVER: " + inputLine);
					
					//if(vStopServer(inputLine))
					//{
					//System.out.println("Shutting Down the Comms");
					//in.close();
					//out.close();
					//kkSocket.close();
				//	break;
					//}
	        		
				} catch (IOException e) {
					// TODO Auto-generated catch block
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
				
				NodeList list = pDoc.getElementsByTagName("reply");
				NamedNodeMap arglist = list.item(0).getAttributes();

				Node name = arglist.getNamedItem("retval");
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
 
  protected String szCreateXMLReplyForRCS(String retval) throws TransformerException
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
						
						Element pReply = pDoc.createElement("function");
						pDoc.appendChild(pReply);

						pReply.setAttribute("rettype", "string");
						pReply.setAttribute("arg0", retval);
						pReply.setAttribute("arg1", "1234");
						pReply.setAttribute("arg2", "4449");
						pReply.setAttribute("arg3","10.217.162.235" );
						//CHINYK_NB/10.217.162.235
						outputString=vXMLDocToStringStream(outer, pDoc);
						
					} catch (ParserConfigurationException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}	
		return outputString;
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
  /*static String readInput() {
	    StringBuffer buffer = new StringBuffer();
	    try {
	        FileInputStream fis = new FileInputStream("test.txt");
	        InputStreamReader isr = new InputStreamReader(kkSocket.getInputStream());
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
	*/
	
}

