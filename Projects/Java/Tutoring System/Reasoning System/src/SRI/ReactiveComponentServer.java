package SRI;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;
import java.util.Map.Entry;

import javax.xml.transform.TransformerException;

import org.w3c.dom.DOMException;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class ReactiveComponentServer extends Server {
	
	
		/// A ReactiveComponentServer acts as a proxy, enabling remote access to a ReactiveComponent
		/* Not inheriting from ComponentServer because will create triangular dependency
		 * as need to have ReactiveComponent as superclass (so that this class can pass 
		 * the casting tests in various methods e.g. methods in SRIEngine). Hence need to
		 * implement Component functions again
		 */
	



			/* Note that there are actually two references to the ReactiveComponent:
			 * one through m_ptReactiveComponent, and one maintained by the superclass ComponentServer
			 * in m_ptComponent. Maintaining a m_ptReactiveComponent saves us the trouble of having
			 * to cast m_ptComponent everytime we want to use functions specific to ReactiveComponent
			 */
			private ReactiveComponent m_ptReactiveComponent; 
			protected ServerSocketChannel m_ptServerSocketChannel; //used for establishing Connections between Ports
			private Component m_ptComponent;

	
			//Component methods
			protected void vSetId(String id)
			{
				
				m_ptReactiveComponent.vSetId(id);
			}
			
			protected int iSetNameSpace(String name)
			{
				return m_ptReactiveComponent.iSetNameSpace(name);
				
			}
			//
			//ReactiveComponent functions
			
			protected int iAddInputPort(InputPort port)
			{
				return m_ptReactiveComponent.iAddInputPort(port);
				
			}
			
			protected int iAddOutputPort(OutputPort port)
			{
				return m_ptReactiveComponent.iAddOutputPort(port);
				
			}

			protected int iAddPrivateInputPort(InputPort port)
			{
				return m_ptReactiveComponent.iAddPrivateInputPort(port);
				
			}
			
			protected int iAddPrivateOutputPort(OutputPort port)
			{
				return m_ptReactiveComponent.iAddPrivateOutputPort(port);
				
			}

			protected int iConnectToChildInput(String privateOutPortName, String childName, String childInPortName)
			{
				return m_ptReactiveComponent.iConnectToChildInput(privateOutPortName, childName, childInPortName);
				
			}
			
			protected int iConnectToChildOutput(String privateInPortName, String childName, String childOutPortName)
			{
				return m_ptReactiveComponent.iConnectToChildOutput(privateInPortName, childName, childOutPortName);
				
			}

			protected int iDisconnectChildInput(String privateOutPortName, String childName, String childInPortName)
			{
				return m_ptReactiveComponent.iDisconnectChildInput(privateOutPortName, childName, childInPortName);
				
			}
			
			protected int iDisconnectChildOutput(String privateInPortName, String childName, String childOutPortName)
			{
				return m_ptReactiveComponent.iDisconnectChildOutput(privateInPortName, childName, childOutPortName);
				
			}


	
			
			
			public ReactiveComponentServer(ReactiveComponent c)
			{
				
				//ReactiveComponent(c.szGetName());
				//m_ptComponent=c.ptGetComponent()
				m_ptReactiveComponent=c;
				
				
			
					m_ptServerSocketChannel=null;
				}
				
		//	}//doesn't take over the memory

			
			
			public String szCallFunction(String funcname, NodeList arglist)
			{
				System.out.println("ReactiveComponentServer calling function: "+ funcname);
				
				String reply = null;

				//BEGIN component functions
				if (funcname.equals("szGetName") ) {
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetName());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("vSetId") ) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
					    		  if(arglist.item(i).getNodeName().equals("arg0"))
					    		  {
					    			   arg0 =arglist.item(i);
					    			  }
					    		  }
					//Node arg0 = arglist.getNamedItem("arg0");//mean get the name of the attribute node
					m_ptReactiveComponent.vSetId(arg0.getTextContent());//means get the value of the attribute node
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}	
				else if (funcname.equals("iSetNameSpace")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
					    		  if(arglist.item(i).getNodeName().equals("arg0"))
					    		  {
					    			   arg0 =arglist.item(i);
					    			  }
					    		  }
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iSetNameSpace(arg0.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("vSetDefinition")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
					    		  if(arglist.item(i).getNodeName().equals("arg0"))
					    		  {
					    			   arg0 =arglist.item(i);
					    			  }
					    		  }

					String def=arg0.getTextContent();
					ComponentDefinition cd = new ComponentDefinition();
					
					cd.iFromString(def);

					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals( "iSetParent")) {
					Node arg0=null;
					Node arg1=null;
					Node arg2=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
					    		  if(arglist.item(i).getNodeName().equals("arg0"))
					    		  {
					    			   arg0 =arglist.item(i);
					    			  }
					    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					//Node arg1 = arglist.getNamedItem("arg1");
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg2"))
			    		  {
			    			   arg2 =arglist.item(i);
			    			  }
			    		  }
					//Node arg2 = arglist.getNamedItem("arg2");//is this a mistake to put as arg1 initially?

					String ip=arg0.getTextContent();
					int port =Integer.parseInt(arg1.getTextContent()); 
							
					String type=arg2.getTextContent();

					Component newParent = null;

					if (type .equals("Component")) {
						//newParent = new Component("", ip, port);
						newParent = new Component(ip+ port);//replace component stub
						
					}
					else if (type.equals("ReactiveComponent")) {
						newParent = new ReactiveComponent( ip+ port);//replace reactiveComponentstub
						
					}

					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iSetParent(newParent));
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}

				}
				else if (funcname.equals("iAddChild")) {
					Node arg0=null;
					Node arg1=null;
					Node arg2=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					//Node arg1 = arglist.getNamedItem("arg1");
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg2"))
			    		  {
			    			   arg2 =arglist.item(i);
			    			  }
			    		  }
					//Node arg2 = arglist.getNamedItem("arg2");//is this a mistake to put as arg1 initially?

					String ip=arg0.getTextContent();
					int port = Integer.parseInt(arg1.getTextContent());
					String type=arg2.getTextContent();

					Component newChild = null;
					if (type.equals ("Component")) {//replace component stub
						newChild = new Component(ip+ port);
						
					}
					else if (type.equals ("ReactiveComponent")) {//replace reactive component stub 
						newChild = new ReactiveComponent( ip+ port);
						
					}

					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iAddChild(newChild));
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}

				}
				else if (funcname .equals("ptGetChild")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					
					String name=arg0.getTextContent();
					
					Component c = m_ptReactiveComponent.ptGetChild(name);
					if (c==null)
						try {
							reply = szCreateXMLReply("null nil 0");
						} catch (TransformerException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
					else {
						Component comp = c;
						Component cc = null;
						ReactiveComponent rc1 = null;
						ReactiveComponentServer rcs1=null;
						ComponentServer cs1 = null;
						StringBuffer info = new StringBuffer();
						//for componentstub and reactivecomponentstub in the future but will temp disable it for now
						/*
						if (comp.getClass().getName().equals(cc) && comp != null) {
							Component cs =comp;//suppose to be component stub 
							info.append("ComponentServer");
							info.append(" ");
							info.append(cs.szGetName());//szGetPeerIp());
							info.append(" ");
							StringBuffer ss = null;
							ss.append(cs.szGetComponentName());//iGetPeerPort();
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().getName().equals(rc1)&&comp != null) {
							ReactiveComponent rcs = (ReactiveComponent) comp;
							info.append("ReactiveComponentServer");
							info.append(" ");
							info.append(rcs.szGetName());//szGetPeerIp());
							info.append(" ");
							StringBuffer ss = null;
							ss.append( rcs.szGetComponentName());//iGetPeerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						*/
						
						 if ( comp.getClass().equals(ComponentServer.class)&&comp != null) {//later need to change back to else if when componentstub and reactivecomponent stub is ready
							//Component cs = new ComponentServer();
						
							 ComponentServer cs =  (ComponentServer) comp;
							  //ChildN copy = orig.getClass().cast(orig.copy());
							info.append("ComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss =  new StringBuffer();
							ss.append(cs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if ( comp.getClass().equals(ReactiveComponentServer.class)&&comp != null) {
							ReactiveComponentServer rcs = (ReactiveComponentServer)comp;
							info.append("ReactiveComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss =  new StringBuffer();
							ss.append( rcs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().equals(Component.class)&&comp != null) {
							Component c1 = (Component)comp;
							//m_ptEngine->vRemoveComponent(comp);
							ComponentServer cs = new ComponentServer(c1);
							//m_ptEngine->iAddSimComponent(cs.ptGetObj());
							
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

							info.append("ComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append(cs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().equals(ReactiveComponent.class)&&comp != null) {
							ReactiveComponent rc = (ReactiveComponent) comp;
							//m_ptEngine->vRemoveComponent(comp);
							ReactiveComponentServer rcs = new ReactiveComponentServer(rc);
							//m_ptEngine->iAddSimComponent(rcs.ptGetObj());
							try {
								rcs.vStartServer(0);
								Thread.sleep(1000);
							} catch (IOException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							} catch (InterruptedException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

							info.append("ReactiveComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append(rcs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}
						else {
							try {
								reply = szCreateXMLReply("null nil 0");
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}

					}
				}
				else if (funcname .equals( "ptGetParent")) {
					/*Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
				
					String name=arg0.getTextContent();
					*/
					Component c = m_ptReactiveComponent.ptGetParent();
					if (c==null)
						try {
							reply = szCreateXMLReply("null nil 0");
						} catch (TransformerException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
					else {
						Component comp = c;
						StringBuffer info = new StringBuffer();
						/*///for future use of stub now temp disable
						if ((Component)comp != null) {
							Component cs = (Component)comp;
							info.append("Component");
							info.append(" ");
							info.append(cs.szGetName());//szGetPeerIp());
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append(cs.szGetComponentName());//iGetPeerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if ((ReactiveComponent)comp != null) {
							ReactiveComponent rcs = (ReactiveComponent)comp;
							info.append("ReactiveComponent");
							info.append(" ");
							info.append(rcs.szGetName());//szGetPeerIp());
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append(rcs.szGetComponentName());//iGetPeerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						*/
					
						 if (comp.getClass().equals(ComponentServer.class)&&comp != null) {
							ComponentServer cs = (ComponentServer)comp;
							info.append("ComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append( cs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().equals(ReactiveComponentServer.class)&&comp != null) {
							ReactiveComponentServer rcs = (ReactiveComponentServer)comp;
							info.append("ReactiveComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append(rcs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().equals(Component.class)&&comp != null) {
							Component c1 = (Component) comp;
							//m_ptEngine->vRemoveComponent(comp);
							ComponentServer cs = new ComponentServer(c1);
							//m_ptEngine->iAddSimComponent(cs.ptGetObj());
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

							info.append("ComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append( cs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().equals(ReactiveComponent.class)&&comp != null) {
							ReactiveComponent rc = (ReactiveComponent)comp;
							//m_ptEngine->vRemoveComponent(comp);
							ReactiveComponentServer rcs = new ReactiveComponentServer(rc);
							//m_ptEngine->iAddSimComponent(rcs.ptGetObj());
							try {
								rcs.vStartServer(0);
								Thread.sleep(1000);
							} catch (IOException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							} catch (InterruptedException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

							info.append("ReactiveComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append( rcs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}
						else {
							try {
								reply = szCreateXMLReply("null nil 0");
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}

					}
				}
				else if (funcname .equals("bHasChild")) {
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
						reply = szCreateXMLReply(m_ptReactiveComponent.bHasChild(name));
						
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("ptRemoveChild")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					
					String name=arg0.getTextContent();

					Component c = m_ptReactiveComponent.ptRemoveChild(name);
					if (c==null)
						try {
							reply = szCreateXMLReply("null nil 0");
						} catch (TransformerException e1) {
							// TODO Auto-generated catch block
							e1.printStackTrace();
						}
					else {
						Component comp = c;
						StringBuffer info = new StringBuffer();
						/*if ((Component)comp != null) {//temp remove for component stub and reactive component stub
							Component cs = (Component)comp;
							info.append("Component");
							info.append(" ");
							info.append(cs.szGetName());
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append (cs.szGetComponentName());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if ((ReactiveComponent)comp != null) {
							ReactiveComponent rcs = (ReactiveComponent)(comp);
							info.append("ReactiveComponent");
							info.append(" ");
							info.append(rcs.szGetName());//szGetPeerIp());
							info.append(" ");
							StringBuffer ss = null;
							ss.append( rcs.szGetComponentName());//iGetPeerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}*/
						 if (comp.getClass().equals(ComponentServer.class)&&comp != null) {
							ComponentServer cs = (ComponentServer)comp;
							info.append("ComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append( cs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().equals(ReactiveComponentServer.class)&&comp != null) {
							ReactiveComponentServer rcs = (ReactiveComponentServer)comp;
							info.append("ReactiveComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss = new StringBuffer();
							ss.append (rcs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().equals(Component.class)&&comp != null) {
							Component c1 = (Component)comp;
							//m_ptEngine->vRemoveComponent(comp);
							ComponentServer cs = new ComponentServer(c1);
							//m_ptEngine->iAddSimComponent(cs.ptGetObj());
							try {
								cs.vStartServer(0);
							} catch (IOException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

							info.append("ComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss =new StringBuffer();
							ss.append( cs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

						}
						else if (comp.getClass().equals(ReactiveComponent.class)&& comp != null) {
							ReactiveComponent rc = (ReactiveComponent)comp;
							//m_ptEngine->vRemoveComponent(comp);
							ReactiveComponentServer rcs = new ReactiveComponentServer(rc);
							//m_ptEngine->iAddSimComponent(rcs.ptGetObj());
							try {
								rcs.vStartServer(0);
							} catch (IOException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

							info.append("ReactiveComponentServer");
							info.append(" ");
							info.append("nil");
							info.append(" ");
							StringBuffer ss =new StringBuffer();
							ss.append( rcs.iGetServerPort());
							info.append(ss.toString());

							try {
								reply = szCreateXMLReply(info.toString());
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}
						else {
							try {
								reply = szCreateXMLReply("null nil 0");
							} catch (TransformerException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}

					}
				}
				else if (funcname.equals("szGetNameSpace")) {
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetNameSpace());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("szGetComponentName")) {
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetComponentName());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals( "szGetID")) {
					
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetID());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("szGetComponentType")) {
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetType());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("eGetStatus")) {
					ComponentStatus cs=m_ptReactiveComponent.eGetStatus();
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
				else if (funcname.equals("vSetStatus")) {
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
						m_ptReactiveComponent.vSetStatus(ComponentStatus.SRI_FAILED);
					if(tempString.equals("0"))
						m_ptReactiveComponent.vSetStatus(ComponentStatus.SRI_STOPPED);
					if(tempString.equals("1"))
						m_ptReactiveComponent.vSetStatus(ComponentStatus.SRI_RUNNING);
					if(tempString.equals("2"))
						m_ptReactiveComponent.vSetStatus(ComponentStatus.SRI_INITIALIZED);
					if(tempString.equals("3"))
						m_ptReactiveComponent.vSetStatus(ComponentStatus.SRI_PAUSED);
					if(tempString.equals("4"))
						m_ptReactiveComponent.vSetStatus(ComponentStatus.SRI_FINALIZED);
					
					
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals ("ptGetDefinition")) {
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetName());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals( "iSetName")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iSetName(arg0.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("iSetComponentType")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iSetComponentType(arg0.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("vInit")) {
					m_ptReactiveComponent.vInit();
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("vFinalize")) {
					m_ptReactiveComponent.vFinalize();
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals( "bHasMoreSteps")) {
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.bHasMoreSteps());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname .equals("vStep")) {
					m_ptReactiveComponent.vStep();
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("vPreStep")) {
					m_ptReactiveComponent.vPreStep();
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("vPostStep")) {
					m_ptReactiveComponent.vPostStep();
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				//END component functions
				//BEGIN reactivecomponent functions
				else if  (funcname.equals("iCreateOutputPort")) {
					Node arg0=null;
					Node arg1=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					//Node arg1 = arglist.getNamedItem("arg1");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iCreateOutputPort(arg0.getTextContent(), arg1.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname .equals("iCreateInputPort")) {
					Node arg0=null;
					Node arg1=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					//Node arg1 = arglist.getNamedItem("arg1");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iCreateInputPort(arg0.getTextContent(), arg1.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("vRemoveOutputPort")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					m_ptReactiveComponent.vRemoveOutputPort(arg0.getTextContent());
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname .equals("vRemoveInputPort")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					m_ptReactiveComponent.vRemoveInputPort(arg0.getTextContent());
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}

				else if  (funcname.equals("bHasInputPort")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.bHasInputPort(arg0.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("bHasOutputPort")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.bHasOutputPort(arg0.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("szGetOutputPortAddress")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetOutputPortAddress(arg0.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("szGetInputPortAddress")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetInputPortAddress(arg0.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("iAddOutputConnection")) {
					try {
						reply = szCreateXMLReply("SRI_ERR_INCOMPLETE");
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname .equals( "iAddInputConnection")) {
					try {
						reply = szCreateXMLReply("SRI_ERR_INCOMPLETE");
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname .equals("iRemoveOutputConnection")) {
					Node arg0=null;
					Node arg1=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					//Node arg1 = arglist.getNamedItem("arg1");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iRemoveOutputConnection(arg0.getTextContent(), arg1.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("iRemoveInputConnection")) {
					Node arg0=null;
					Node arg1=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iRemoveInputConnection(arg0.getTextContent(), arg1.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				
				
				
				else if  (funcname .equals( "iAddRemoteOutputConnection")) {
					
					Node arg0=null;
					Node arg1=null;
					Node arg2=null;
					Node arg3=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg2"))
			    		  {
			    			   arg2 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg3"))
			    		  {
			    			   arg3 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					//Node arg1 = arglist.getNamedItem("arg1");
					//Node arg2 = arglist.getNamedItem("arg2");
					//Node arg3 = arglist.getNamedItem("arg3");

					String outport=arg0.getTextContent();
					String inport=arg1.getTextContent();

					StringBuffer ss = new StringBuffer();
					ss.append(arg2.getTextContent());
					int port =0;
					ss.append (port); //TODO: error checking

					String ip=arg3.getTextContent();
					
					InetSocketAddress sa=new InetSocketAddress(ip, port);
					Socket ptSock = new Socket();
					/*try {
						ptSock.connect(sa);
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					*/
					//TODO: error check if a successful connection has been made?
					Connection ptSendConn = new Connection();

					ptSendConn.vSetReceiverName(inport);

					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iAddOutputConnection(outport, ptSendConn));
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}

				}
				else if  (funcname .equals("iAddRemoteInputConnection")) {
					
					Node arg0=null;
					Node arg1=null;
					Node arg2=null;
					Node arg3=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg2"))
			    		  {
			    			   arg2 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg3"))
			    		  {
			    			   arg3 =arglist.item(i);
			    			  }
			    		  }
					
					//Node arg0 = arglist.getNamedItem("arg0");
					//Node arg1 = arglist.getNamedItem("arg1");
					//Node arg2 = arglist.getNamedItem("arg2");
					//Node arg3 = arglist.getNamedItem("arg3");

					String inport=arg0.getTextContent();
					String outport=arg1.getTextContent();

					StringBuffer ss = new StringBuffer();
					ss.append(arg2.getTextContent());
					int port = 0;
					ss.append(port); //TODO: error checking

					String ip=arg3.getTextContent();
					
					InetSocketAddress sa=new InetSocketAddress(ip, port);
					Socket ptSock = new Socket();
				/*	try {
						ptSock.connect(sa);
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}*/
					//TODO: error check if a successful connection has been made?
					Connection ptRecvConn = new Connection();

					ptRecvConn.vSetSenderName(outport);

					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iAddInputConnection(inport, ptRecvConn));
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}

				}
				else if  (funcname .equals("iListenForConnection")) {
					if (m_ptServerSocketChannel == null)
						try {
							m_ptServerSocketChannel = ServerSocketChannel.open();
							m_ptServerSocketChannel.socket().bind(new InetSocketAddress(0));
							reply = szCreateXMLReply(m_ptServerSocketChannel.socket().getLocalPort());
						//System.out.println(" THE REPLY IS "+reply);
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} catch (TransformerException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}

					
				}
				else if  (funcname .equals("iFinaliseConnection")) {
					Node arg0=null;
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					//Node arg0 = arglist.getNamedItem("arg0");
					
					String inport=arg0.getTextContent();
					SocketChannel sc = null;

					try {
						while (sc == null) sc = m_ptServerSocketChannel.accept();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					
					//TODO return error code if ptStream remains null

					//this helps to test the assumption that making connections is an atomic process,
					//i.e. Listen, Connect, Finalise is an atomic sequence
					//should be correct because the engine code runs in o single thread
					//the test: after accepting, there should be no more stuff waiting in the accept queue
					try {
						//if (m_ptServerSocket.getReceiveBufferSize() != 0)
							
							//System.out.println("more than one pending connection was present!");
						Connection ptRecvConn = new TCPReceiveConnection(sc);
						reply = szCreateXMLReply(m_ptReactiveComponent.iAddInputConnection(inport, ptRecvConn));
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					

				}
				else if  (funcname.equals("iConnectForConnection")) {
					
					Node arg0=null;
					Node arg1=null;
					Node arg2=null;
				
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg2"))
			    		  {
			    			   arg2 =arglist.item(i);
			    			  }
			    		  }
				
					
					
					//Node arg0 = arglist.getNamedItem("arg0");
					//Node arg1 = arglist.getNamedItem("arg1");
					//Node arg2 = arglist.getNamedItem("arg2");

					String outport=arg0.getTextContent();
					String ip=arg1.getTextContent();

					int port = Integer.parseInt(arg2.getTextContent());

								
					
					
					try {
						InetSocketAddress ia = new InetSocketAddress(ip, port);
						System.out.println(ia);
						SocketChannel sc = SocketChannel.open(ia);
						Connection ptSendConn = new TCPSendConnection(sc);

						reply = szCreateXMLReply(m_ptReactiveComponent.iAddOutputConnection(outport, ptSendConn));
					} 
					
						catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (UnknownHostException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
				

				}
				else if (funcname.equals("mGetInputPortList")) {
					HashMap<String, String> m = m_ptReactiveComponent.mGetInputPortList();

					StringBuffer ss = new StringBuffer();

					ss.append( m.size());
					ss.append(" ");//need to add white space so we can extract it easier later

					Set<Entry<String, String>> s = m.entrySet();
			         Iterator<Entry<String, String>> i = s.iterator();
			         while (i.hasNext()) {
			        	 Entry<String, String>entry=i.next();//always need to transfer the item to another set first
			        	 String key=entry.getKey();
			        	 String value=entry.getValue();
			        	 ss.append(key);
			        	 ss.append(" ");
			        	 ss.append(value);
			        	 ss.append(" ");
			         }
					
			
					String rep=ss.toString();
					try {
						reply = szCreateXMLReply(rep);
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname.equals("mGetOutputPortList")) {
					HashMap<String, String> m = m_ptReactiveComponent.mGetOutputPortList();

					StringBuffer ss = new StringBuffer();

					ss.append( m.size());
					ss.append(" ");

					Set<Entry<String, String>> s = m.entrySet();
			         Iterator<Entry<String, String>> i = s.iterator();
			         while (i.hasNext()) {
			        	 Entry<String, String>entry=i.next();//always need to transfer the item to another set first
			        	 String key=entry.getKey();
			        	 String value=entry.getValue();
			        	 ss.append(key);
			        	 ss.append(" ");
			        	 ss.append(value);
			        	 ss.append(" ");
			         }
					//for(SRI::ConstMapIterator<SRI::String, SRI::String> it = m.begin(); it != m.end(); it++){
						//ss << it.first().c_str() << it.second().c_str();
					//}
			
					String rep=ss.toString();
					try {
						reply = szCreateXMLReply(rep);
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname .equals("szGetInputPorts")) {
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetInputPorts());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if (funcname .equals("szGetOutputPorts")) {
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.szGetOutputPorts());
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname .equals( "iCreatePrivateOutputPort")) {
					Node arg0=null;
					Node arg1=null;
					
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
				
					
					
				//	Node arg0 = arglist.getNamedItem("arg0");
				//	Node arg1 = arglist.getNamedItem("arg1");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iCreatePrivateOutputPort(arg0.getTextContent(), arg1.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("iCreatePrivateInputPort")) {
					Node arg0=null;
					Node arg1=null;
					
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg1"))
			    		  {
			    			   arg1 =arglist.item(i);
			    			  }
			    		  }
					
					//Node arg0 = arglist.getNamedItem("arg0");
					//Node arg1 = arglist.getNamedItem("arg1");
					try {
						reply = szCreateXMLReply(m_ptReactiveComponent.iCreatePrivateInputPort(arg0.getTextContent(), arg1.getTextContent()));
					} catch (DOMException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("vRemovePrivateOutputPort")) {
					Node arg0=null;
				
					
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					
					//Node arg0 = arglist.getNamedItem("arg0");
					m_ptReactiveComponent.vRemovePrivateOutputPort(arg0.getTextContent());
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else if  (funcname.equals("vRemovePrivateInputPort")) {
					Node arg0=null;
				
					
					for (int i = 0; i < arglist.getLength(); i++) {
					      
			    		  if(arglist.item(i).getNodeName().equals("arg0"))
			    		  {
			    			   arg0 =arglist.item(i);
			    			  }
			    		  }
					
					
					//Node arg0 = arglist.getNamedItem("arg0");
					m_ptReactiveComponent.vRemovePrivateInputPort(arg0.getTextContent());
					try {
						reply = szCreateXMLReply();
					} catch (TransformerException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				else {
					System.out.println("invalid function name");
					//m_tLog.error("invalid function name"); //TODO: return error value?
				}

				//m_tLog.debug("reply: %s", reply.c_str());
				System.out.println("reply: %s"+ reply.toString());
				return reply;
			}
				
		//	}

			//Component methods
			public String szGetID()
			{
				return m_ptReactiveComponent.szGetID();
				
			}
			
			
			
			public String szGetComponentType()
			{
				return m_ptReactiveComponent.szGetComponentType();
				
			}
			
			public String szGetName()
			{
				return m_ptReactiveComponent.szGetName();
				
			}
			
			public String szGetNameSpace()
			{
				return m_ptReactiveComponent.szGetNameSpace();
				
			}
			
			public String szGetComponentName()
			{
				return m_ptReactiveComponent.szGetComponentName();
				
			}
			
			public int iSetName(String name)
			{
				return m_ptReactiveComponent.iSetName(name);
				
			}
			
			public int iSetComponentType(String type)
			{
				return m_ptReactiveComponent.iSetComponentType(type);
				
			}

			//virtual Component* ptClone() const;
			public ComponentStatus eGetStatus()
			{
				return m_ptReactiveComponent.eGetStatus();
				
			}
			
			public void vSetStatus(ComponentStatus status)
			{
				m_ptReactiveComponent.vSetStatus(status);
			}

			public void vInit()
			{
				m_ptReactiveComponent.vInit();
			}
			
			public void vFinalize()
			{
				m_ptReactiveComponent.vFinalize();
			}
			
			public boolean bHasMoreSteps()
			{
				return m_ptReactiveComponent.bHasMoreSteps();
				
			}
			
			public boolean vStep()
			{
				//m_ptReactiveComponent.vStep();
				return m_ptReactiveComponent.vStep();
			}
			
			public boolean vPreStep()
			{
			//	m_ptReactiveComponent.vPreStep();
				return m_ptReactiveComponent.vPreStep();
			}
			
			public boolean vPostStep()
			{
				//m_ptReactiveComponent.vPostStep();
				return m_ptReactiveComponent.vPostStep();
			}
			
			//ReactiveComponent methods

			/** After copy the IP address must be reset*/
			
			//public ReactiveComponentServer(const ReactiveComponentServer& c);
			//public ReactiveComponentServer& operator=(const ReactiveComponentServer& c);

			//public bool operator==(const ReactiveComponent& c);
			//bool operator==(const ReactiveComponentServer& c);
			//implement this for the component as well
			//virtual Component* ptClone() const;

			public int iCreateOutputPort(String name,String type)
			{
				return m_ptReactiveComponent.iCreateOutputPort(name, type);
				
			}
			
			public int iCreateInputPort(String name, String type)
			{
				return m_ptReactiveComponent.iCreateInputPort(name, type);
				
			}

			public void vRemoveOutputPort(String name)
			{
				m_ptReactiveComponent.vRemoveOutputPort(name);
			}
			
			public void vRemoveInputPort(String name)
			{
				m_ptReactiveComponent.vRemoveInputPort(name);
			}

			public boolean bHasInputPort(String inport)
			{
				return m_ptReactiveComponent.bHasInputPort(inport);
				
			}
			
			public boolean bHasOutputPort(String outport)
			{
				return m_ptReactiveComponent.bHasOutputPort(outport);
				
			}

			public String szGetOutputPortAddress(String outport)
			{
				return m_ptReactiveComponent.szGetOutputPortAddress(outport);
				
			}
			
			public String szGetInputPortAddress(String outport)
			{
				return m_ptReactiveComponent.szGetInputPortAddress(outport);				
			}
		
			public int iAddOutputConnection(String outport, Connection connection)
			{
				return m_ptReactiveComponent.iAddOutputConnection(outport, connection);
				
			}
			
			public int iAddInputConnection(String inport, Connection connection)
			{
				return m_ptReactiveComponent.iAddInputConnection(inport, connection);
				
			}

			public int iRemoveOutputConnection(String outport, String inport)
			{
				return m_ptReactiveComponent.iRemoveOutputConnection(outport, inport);
				
			}
			
			public int iRemoveInputConnection(String inport, String outport)
			{
				return m_ptReactiveComponent.iRemoveInputConnection(inport, outport);
				
			}

			//TODO: consider deprecating, given above two functions? how to implement remotely?
			public int iRemoveOutputConnection(String outport, Connection connection)
			{
				return m_ptReactiveComponent.iRemoveOutputConnection(outport, connection);
				
			}
			
			public int iRemoveInputConnection(String inport, Connection connection)
			{
				return m_ptReactiveComponent.iRemoveInputConnection(inport, connection);
				
			}

			public HashMap<String, String> mGetInputPortList()
			{
				return m_ptReactiveComponent.mGetInputPortList();
				
			}
			
			public HashMap<String, String> mGetOutputPortList()
			{
				return m_ptReactiveComponent.mGetOutputPortList();
				
			}

			public String szGetInputPorts()
			{
				return m_ptReactiveComponent.szGetInputPorts();
				
			}
			
			public String szGetOutputPorts()
			{
				return m_ptReactiveComponent.szGetOutputPorts();
				
			}

			public int iCreatePrivateOutputPort(String name, String type)
			{
				return m_ptReactiveComponent.iCreatePrivateOutputPort(name, type);
				
			}
			
			public int iCreatePrivateInputPort(String name, String type)
			{
				return m_ptReactiveComponent.iCreatePrivateInputPort(name, type);
				
			}

			public void vRemovePrivateOutputPort(String name)
			{
				m_ptReactiveComponent.vRemovePrivateOutputPort(name);
			}
			
			public void vRemovePrivateInputPort(String name)
			{
				 m_ptReactiveComponent.vRemovePrivateInputPort(name);
			}


	
	
}
