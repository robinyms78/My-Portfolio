package SRI;

import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import javax.xml.transform.TransformerException;

import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class ComponentFactoryServer extends Server {//extend ComponentFactory

	


		/// A ComponentFactoryServer is a proxy service allowing remote access to a ComponentFactory
		/** NOTE: In the current framework, all components created by the proxied ComponentFactory
			exist in the same address space as the ComponentFactoryServer and the proxied ComponentFactory,
			as opposed to running as a separate process.
			The ComponentFactoryServer is responsible for providing remote access to created
			Components by creating an accompanying ComponentServer/ReactiveComponentServer. The
			ComponentServer/ReactiveComponentServer runs in a separate thread, and cleans up
			after itself when it shuts down.
		*/

		

	 // create ExecutorService to manage threads                        
	        ExecutorService  m_ptThreadPool ;
	        
	
			

			
			protected ComponentFactory m_ptComponentFactory;

			protected String szGetComponentType(Component c)
			{
				if(c instanceof ReactiveComponent)
				{
					ReactiveComponent rc=(ReactiveComponent)c;
				}
				if(c.getClass().equals(Component.class))
				{return "Component";
				}//"Component"
		        else return "ReactiveComponent";
				//Component c1=new ReactiveComponent("");
				
				//ReactiveComponent rc = (ReactiveComponent) c1;
			        //if (rc == null) return "Component";//"Component"
			       // else return "ReactiveCompoenent";//"ReactiveComponent"
				
			//	return "";
				
			}


		
			public ComponentFactoryServer(ComponentFactory f)
			{
				
				m_ptComponentFactory=f;
			
				System.out.println("ComponentFactoryServer");
				m_ptThreadPool= Executors.newCachedThreadPool( );//create a thread when needed
			}
			
			
			public String szCallFunction(String funcname, NodeList arglist)
			{
				System.out.println("calling function: %s"+ funcname);

				String reply = "";

				if (funcname == "ptCreateComponent") {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					String cname=arg0.getTextContent();
					
					
					Component c=new ReactiveComponent("");
					c = m_ptComponentFactory.ptCreateComponent(cname,"");
					//ReactiveComponent rc = (ReactiveComponent) c;
					

				RemoteComponentRunner runner;
				ReactiveComponent rc = null;
				if(c!=null && c instanceof ReactiveComponent)
				{
					rc=(ReactiveComponent) c;
				}
				
				
				

				StringBuffer msg=new StringBuffer();
				msg.append(szGetComponentType(c)+ " ");
					
					if ( rc==null)	
					{
						ComponentServer cs = new ComponentServer(c);
						try {
							cs.vStartServer(0);
							Thread.sleep(1000);
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} catch (InterruptedException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
						msg.append(cs.iGetServerPort());
						
						runner = new RemoteComponentRunner(c, cs);
					}
					else {
						ReactiveComponentServer rcs=null;
						if (c instanceof ReactiveComponent)
						{
							 rcs= new ReactiveComponentServer((ReactiveComponent) c);
						}
						//rc=(ReactiveComponent) c;
						
						try {
							rcs.vStartServer(0);
							Thread.sleep(1000);
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
							catch (InterruptedException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
						
						
						runner = new RemoteComponentRunner(c, rcs);
						msg.append(rcs.iGetServerPort());
					}
					
					
					//try {
						m_ptThreadPool.execute(runner);
						
					//}
					//catch (Poco::Exception& e) {
						//SRI::String exceptionName(e.className());
						//if (exceptionName == "class Poco::NoThreadAvailableException") {
						//	m_tLog.debug("Threadpool hit max capacity: %d", m_ptThreadPool->capacity());
				//	m_ptThreadPool->addCapacity(m_ptThreadPool->capacity()); //doubles the capacity of the threadool
							//m_tLog.debug("Increased threadpool capacity to %d", m_ptThreadPool->capacity());
							
							//m_ptThreadPool.execute(runner);
						//}
						//else 
							//System.out.println("Poco exception thrown: %s");
							
					

					String szMsg=msg.toString();
		            try {
						reply = szCreateXMLReply(szMsg);
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
								
				}
				
				else if (funcname == "vSetComponentType") {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					
					String typeId=arg0.getTextContent();
					m_ptComponentFactory.vSetComponentType(typeId);
				}
				else if (funcname == "iSetName") {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					
					String name=arg0.getTextContent();

					try {
						reply = szCreateXMLReply(m_ptComponentFactory.iSetName(name));
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname == "szGetName") {
					try {
						reply = szCreateXMLReply(m_ptComponentFactory.szGetName());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname == "szComponentType") {
					try {
						reply = szCreateXMLReply(m_ptComponentFactory.szGetComponentType());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname == "szGetConfig") {
					try {
						reply = szCreateXMLReply(m_ptComponentFactory.szGetConfig());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname == "tGetComponentDefinition") {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					
					String config=arg0.getTextContent();
					try {
						reply = szCreateXMLReply(m_ptComponentFactory.szGetComponentType());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else {
					
				System.out.println("invalid function name");
				}
				System.out.println("reply: %s"+ reply);


				return reply;
			}


	
	
}
