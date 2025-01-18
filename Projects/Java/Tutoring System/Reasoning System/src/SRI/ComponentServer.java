package SRI;

//import javax.xml.stream.;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.TransformerException;


import org.w3c.dom.DOMException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Text;
//import org.dom4j.Document;
import com.sun.org.apache.xml.internal.serialize.*;



//For jdk1.5 with built in xerces parser
//import com.sun.org.apache.xml.internal.serialize.OutputFormat;
//import com.sun.org.apache.xml.internal.serialize.XMLSerializer;
import java.net.*;
import java.io.*;


public class ComponentServer extends Server
{
	private Component m_ptComponent; 

	
		//Component methods
	protected void vSetId(String id)
	{
		m_ptComponent.vSetId(id);
	}
	
	protected int iSetNameSpace(String name)
	{
		return m_ptComponent.iSetNameSpace(name);
	}
		
		//Server methods
	public ComponentServer(Component c)
	{
		m_ptComponent=c;
		m_ptComponent.m_szName=c.szGetName();
		
	}
		
		//TODO: copy con, assignment op
	public String szCallFunction(String funcname, NodeList arglist)
	{
		System.out.println("ComponentServer calling function: "+ funcname);

		String reply = "";
		
		if (funcname.equals ("szGetName")) {
			
			try {
				
				reply = szCreateXMLReply(m_ptComponent.szGetName());
				
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("vSetId")) {
			Node arg0=null;
			for (int i = 0; i < arglist.getLength(); i++) {
			      
	    		  if(arglist.item(i).getNodeName().equals("arg0"))
	    		  {
	    			   arg0 =arglist.item(i);
	    			  }
	    		  }
			//Node arg0 = arglist.getNamedItem("arg0");//change from arg0 to retval
			m_ptComponent.vSetId(arg0.getTextContent());
			try {
				reply = szCreateXMLReply();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}	
		else if (funcname.equals ("iSetNameSpace")) {
			Node arg0=null;
			for (int i = 0; i < arglist.getLength(); i++) {
			      
	    		  if(arglist.item(i).getNodeName().equals("arg0"))
	    		  {
	    			   arg0 =arglist.item(i);
	    			  }
	    		  }
			//Node arg0 = arglist.getNamedItem("arg0");//change from arg0 to retval
			try {
				reply = szCreateXMLReply(m_ptComponent.iSetNameSpace(arg0.getTextContent()));
			} catch (DOMException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
	else if (funcname.equals ("iSetEngineHandle")) {
			Node arg0=null;
			for (int i = 0; i < arglist.getLength(); i++) {
		      
    		  if(arglist.item(i).getNodeName().equals("arg0"))
    		  {
    			   arg0 =arglist.item(i);
    			  }
    		  }
			StringBuffer ss=new StringBuffer(arg0.getTextContent());
			//std::stringstream ss(execObj.szGetArg(0).c_str());
			
			String ip;
			int port;
			
			int ind1=ss.indexOf(" ", 0);
			ip=ss.substring(0, ind1);
			//int ind2=ss.indexOf(" ", ind1+1);
			//ip=s.substring(ind1+1,ind2);
			port=Integer.parseInt(ss.substring(ind1+1));
			//ss >> ip >> port;

			SRIEngineStub engStub = new SRIEngineStub(ip, port,"EngineStubName");
			//EngineHandle engHandle = new EngineHandle(engStub);

			try {
				reply = szCreateXMLReply(m_ptComponent.iSetEngineHandle(engStub));
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		}
		//else if (funcname == "ptGetEngineHandle") {
			//reply = szCreateXMLReply(m_ptComponent.ptGetEngineHandle().szGetEngineAddress());

		//}
		else if (funcname.equals ("szGetNameSpace")) {
			try {
				reply = szCreateXMLReply(m_ptComponent.szGetNameSpace());
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("szGetComponentName")) {
			try {
				reply = szCreateXMLReply(m_ptComponent.szGetComponentName());
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("szGetID")) {
			try {
				//System.out.println(" THE SZGETNAME REPLY IS ");
				reply = szCreateXMLReply(m_ptComponent.szGetID());
				
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("szGetType")) {
			try {
				reply = szCreateXMLReply(m_ptComponent.szGetType());
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("eGetStatus")) {
			ComponentStatus cs=m_ptComponent.eGetStatus();
			int status = -99;
			switch (cs) {
			case SRI_FAILED:
				status = -1;
				break;
			case SRI_STOPPED:
				status = 0;
				break;
			case SRI_RUNNING:
				status = 1;
				break;
			case SRI_INITIALIZED:
				status = 2;
				break;
			case SRI_PAUSED:
				status = 3;
				break;
			case SRI_FINALIZED:
				status = 4;
				break;
			default:
				System.out.println("ERROR: unknown component status");
				
			}
			
			try {
				reply = szCreateXMLReply(status);
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("vSetStatus")) {

			Node arg0=null;
			for (int i = 0; i < arglist.getLength(); i++) {
			      
	    		  if(arglist.item(i).getNodeName().equals("arg0"))
	    		  {
	    			   arg0 =arglist.item(i);
	    			  }
	    		  }
			//Node arg0 = arglist.getNamedItem("arg0");//change from arg0 to retval
			String tempString=arg0.getTextContent();//getNodeValue()
			
			if(tempString.equals("-1"))
				m_ptComponent.vSetStatus(ComponentStatus.SRI_FAILED);
			if(tempString.equals("0"))
				m_ptComponent.vSetStatus(ComponentStatus.SRI_STOPPED);
			if(tempString.equals("1"))
				m_ptComponent.vSetStatus(ComponentStatus.SRI_RUNNING);
			if(tempString.equals("2"))
				m_ptComponent.vSetStatus(ComponentStatus.SRI_INITIALIZED);
			if(tempString.equals("3"))
				m_ptComponent.vSetStatus(ComponentStatus.SRI_PAUSED);
			if(tempString.equals("4"))
				m_ptComponent.vSetStatus(ComponentStatus.SRI_FINALIZED);
			
			
			try {
				reply = szCreateXMLReply();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("iSetName")) {
			Node arg0=null;
			for (int i = 0; i < arglist.getLength(); i++) {
			      
	    		  if(arglist.item(i).getNodeName().equals("arg0"))
	    		  {
	    			   arg0 =arglist.item(i);
	    			  }
	    		  }
			//Node arg0 = arglist.getNamedItem("arg0");//changed from arg0 to retval
			try {
				reply = szCreateXMLReply(m_ptComponent.iSetName(arg0.getTextContent()));
			} catch (DOMException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("iSetType")) {
			Node arg0=null;
			for (int i = 0; i < arglist.getLength(); i++) {
			      
	    		  if(arglist.item(i).getNodeName().equals("arg0"))
	    		  {
	    			   arg0 =arglist.item(i);
	    			  }
	    		  }
			//Node arg0 = arglist.getNamedItem("arg0");//changed from arg0 to retval
			try {
				reply = szCreateXMLReply(m_ptComponent.iSetType(arg0.getTextContent()));
			} catch (DOMException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("vInit")) {
			m_ptComponent.vInit();
			try {
				reply = szCreateXMLReply();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals("vFinalize")) {
			m_ptComponent.vFinalize();
			try {
				reply = szCreateXMLReply();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("bHasMoreSteps")) {
			try {
				reply = szCreateXMLReply(m_ptComponent.bHasMoreSteps());
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals("vStep")) {
			m_ptComponent.vStep();
			try {
				reply = szCreateXMLReply();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("vPreStep")) {
			m_ptComponent.vPreStep();
			try {
				reply = szCreateXMLReply();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("vPostStep")) {
			m_ptComponent.vPostStep();
			try {
				reply = szCreateXMLReply();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if (funcname.equals ("shutdown")) {
			//TODO: as yet NOT IMPLEMENTED
			//should do something about stopping the thread so can return from join
			//*m_ptStopModuleSwitch = true;
		}

		else {
			System.out.println("invalid function name"); //TODO: return error value?
			try {
				reply = szCreateXMLReply("INVALID REQUEST");
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		System.out.println("reply: "+ reply);

		return reply;
	}

		//Component methods
	public String szGetID()
	{
		return m_ptComponent.szGetID();
	}
	public String szGetType() 
	{
		return m_ptComponent.szGetType();
	}
	
	public String szGetName()
	{
		return m_ptComponent.szGetName();
	}
	
	public String szGetNameSpace()
	{
		return m_ptComponent.szGetNameSpace();
	}
	
	public String szGetComponentName()
	{
		return m_ptComponent.szGetComponentName();
	}
	
	public int iSetName(String name)
	{
		return m_ptComponent.iSetName(name);
	}
	
	public int iSetType(String type)
	{
		return m_ptComponent.iSetType(type);
	}


	public ComponentStatus eGetStatus()
	{
		return m_ptComponent.eGetStatus();
	}
	
	public void vSetStatus(ComponentStatus status)
	{
		m_ptComponent.vSetStatus(status);
		
	}

	public void vInit()
	{
		m_ptComponent.vInit();
	}
	
	public void vFinalize()
	{
		m_ptComponent.vFinalize();
	}
	
	public boolean bHasMoreSteps()
	{
		return m_ptComponent.bHasMoreSteps();
	}
	
	public boolean vStep()
	{
		 m_ptComponent.vStep();
		 return true;
	}
	
	public boolean vPreStep()
	{
		 m_ptComponent.vPreStep();
		 return true;
	}
	
	public boolean vPostStep()
	{
		m_ptComponent.vPostStep();
		return true;
	}
	
	
	
	
	
	
	
	
	
	
	
	
}
