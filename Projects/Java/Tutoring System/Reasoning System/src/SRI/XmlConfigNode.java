package SRI;

import java.io.IOException;
import java.io.StringWriter;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.TransformerFactoryConfigurationError;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class XmlConfigNode extends ConfigNode {

	
	
	private Node m_ptXmlNode;
	
		public XmlConfigNode(Node node) {
			m_ptXmlNode=node;
		}
	
	
		protected Node ptGetTiXmlNode()
		{
			return m_ptXmlNode;
			
		}


		public XmlConfigNode()
		{
			
			
		}
		/**By default the XML tree holds the memory. Therefore this memory is not managed.*/
		
		public XmlConfigNode(String xmlText)
		{
			DocumentBuilderFactory fact = DocumentBuilderFactory.newInstance();
			DocumentBuilder builder;
			
			try {
				builder = fact.newDocumentBuilder();
				Document doc= builder.parse(xmlText);
				Element root = (Element) doc.getFirstChild();
				if(root != null){
					m_ptXmlNode=root;
				}
				else
				{
					System.out.println("Unable to find root element");
				} 
			}
				catch (ParserConfigurationException e) {
				System.out.println("Failed to initialize xmlConfigNode from xml string because failed to prase xml:");
				e.printStackTrace();
			} catch (SAXException e) {
				System.out.println("Failed to initialize xmlConfigNode from xml string because failed to prase xml:");
					e.printStackTrace();
				} 
			catch (IOException e) {
					System.out.println("Failed to initialize xmlConfigNode from xml string because failed to prase xml:");
					e.printStackTrace();
				}
			
			
		}
		
	

		public String szGetValue()
		{
			String res = "";
			if(m_ptXmlNode!=null){
				res = m_ptXmlNode.getNodeValue();
			}
			return res;
			
		}
		
		public ConfigNode ptGetFirstChild(String name)
		{
			name="";
			ConfigNode res = null;
			if(m_ptXmlNode!=null){
				Node n = null;
				if(name == ""){
					n = m_ptXmlNode.getFirstChild();
				}else{
					//n = m_ptXmlNode.get(name);
				}
				if( n != null){
					res=new XmlConfigNode(n);
				}
			}
			return res;
			
		}
		
		public ConfigNode ptIterateChildren(String value, ConfigNode previous)
		{
			ConfigNode res=new ConfigNode();
			if(m_ptXmlNode!=null){
				XmlConfigNode xn = (XmlConfigNode)previous;		
				//NodeList nl=null;
				Node n = null;
				if( value == ""){
					if(xn != null){
						//nl = m_ptXmlNode.getChildNodes();
						n=xn.ptGetTiXmlNode().getNextSibling();
					}else{
						n = m_ptXmlNode.getFirstChild();
					}
				}else{
					if(xn != null){
						if(xn.ptGetTiXmlNode().getNextSibling().getNodeValue().equals(value))
						{
							n=xn.ptGetTiXmlNode().getNextSibling();
						}
						//n = m_ptXmlNode->IterateChildren(value, xn.ptGetTiXmlNode());
					}else{
						if(m_ptXmlNode.getFirstChild().getNodeValue().equals(value))
						{
							n=m_ptXmlNode.getFirstChild();
						}
						//n = m_ptXmlNode->IterateChildren(value.c_str(), NULL);
					}
				}
				if(n != null){
					res= new XmlConfigNode(n);
				}
					
			}
			return res;
			
		}

		
		/** Appends the a copy of the given child and returns a pointer to the copy. */
		public int iAppendChild(ConfigNode node)
		{
			if( m_ptXmlNode==null || node==null){
				//m_tLog.error("Unable to insert node: Got NULL");
				System.out.println("Unable to insert node: Got NULL");
			}

			if(node.szGetNodeType() != "XmlNode"){
				//m_tLog.error("Node type conversion currently not supported");
				System.out.println("Node type conversion currently not supported");
				return 1;//SRI_ERR_TYPE;
			}

			XmlConfigNode xmlNode = (XmlConfigNode)node;
			Node tixNode = xmlNode.ptGetTiXmlNode();
			

			if(tixNode!=null){
				Node res = m_ptXmlNode.appendChild(tixNode);
				Node parent = m_ptXmlNode;
				if(res != null){
					XmlConfigNode inserted = new XmlConfigNode(res);
					node=inserted;
					return 0;//SRI_OK;
				}else{
					System.out.println("Error inserting child xml node");
					//m_tLog.error("Error inserting child xml node");
				}
			}
			return 1;//SRI_ERR_INCOMPLETE;
			}
		
		/** Inserts a copy of the node after the specified child and returns a pointer to the copy. If the child is NULL it will be inserted as first element*/
		public int iInsertChild(ConfigNode node, ConfigNode prev )
		{
			if( m_ptXmlNode==null || node==null){
				//m_tLog.error("Unable to insert node: Got NULL");
				System.out.println("Unable to insert node: Got NULL");
			}

			if(node.szGetNodeType() != "XmlNode"){
				//m_tLog.error("Node type conversion currently not supported");
				System.out.println("Node type conversion currently not supported");
				return 1;//SRI_ERR_TYPE;
			}

			XmlConfigNode xmlNode = (XmlConfigNode)node;
			Node tixNode = xmlNode.ptGetTiXmlNode();
			Node prevTiX = null;

			if(prev!=null && (prev.szGetNodeType() == "XmlNode")){
				XmlConfigNode prevNode = (XmlConfigNode)prev;
				if(prevNode!=null){
					Node prevTiXNode = prevNode.ptGetTiXmlNode();
					if(prevTiXNode!=null){
						prevTiX = prevTiXNode;
					}
				}
			}

			if(tixNode!=null){
				Node res = null;

				if(prevTiX == null){
					Node first = m_ptXmlNode.getFirstChild();
					if(first != null){
						res = m_ptXmlNode.insertBefore(tixNode, first);
					}else{
						m_ptXmlNode.appendChild(tixNode);//InsertEndChild(*(tixNode.ptGetObj()));
					}
				}else{
				
					res=m_ptXmlNode.insertBefore(tixNode, prevTiX.getNextSibling());
					//res = m_ptXmlNode.InsertAfterChild(prevTiX, *(tixNode.ptGetObj()));
				}
				if(res != null){
					XmlConfigNode inserted = new XmlConfigNode(res);
					node=inserted;
					return 0;//SRI_OK;
				}else{
					System.out.println("Error inserting child xml node");
					//m_tLog.error("Error inserting child xml node");
				}
			}
			return 1;//SRI_ERR_INCOMPLETE;
		}

		/** Removes the given child and returns a reference to it if successful*/
		public int iRemoveChild(ConfigNode node)
		{
			if( m_ptXmlNode==null || node==null){
				//m_tLog.error("Unable to remove node: Got NULL");
				System.out.println("Unable to remove node: Got NULL");
			}

			if(node.szGetNodeType() != "XmlNode"){
				//m_tLog.error("Node type conversion currently not supported");
				
				System.out.println("Node type conversion currently not supported");
				return  1;//SRI_ERR_NULL;
			}

			XmlConfigNode xmlNode = (XmlConfigNode)node;
			Node tixNode;
			Node nodeTiX = null;

			if(xmlNode!=null){
				tixNode = xmlNode.ptGetTiXmlNode();
				if(tixNode!=null){
					nodeTiX = tixNode;
				}
			}

			if(nodeTiX != null){
				Node c = nodeTiX;
				Node n=m_ptXmlNode.removeChild(nodeTiX);
				//boolean res =  // returns true if successful
				if(n!=null && (c != null)){
					XmlConfigNode removed = new XmlConfigNode(c);
					node=removed;
					return 0;//SRI_OK;
				}else{
					//m_tLog.error("Error removing element");
					System.out.println("Error removing element");
					return 1;//SRI_ERR_NULL;
				}
			}

			return 0;//SRI_OK;
			
		}

		public int iSetAttribute(String attribute, String value)
		{
			Node nodeTiX =  m_ptXmlNode;
			if(nodeTiX != null){
				if(nodeTiX.getNodeType() ==  Node.ELEMENT_NODE){
					Element elem = (Element) nodeTiX;
					elem.setAttribute(attribute, value);
					return 0;//SRI_OK;
				}
			}
			//m_tLog.error("Attribute was not set (%s-%s)", attribute.c_str(), value.c_str());
			System.out.println("Attribute was not set (%s-%s)"+ attribute+ value);
			return 2;//SRI_ERR_ABORT;
			
		}

		public String szGetNodeType()
		{
			return "XmlNode";
			
		}

		public String szGetTextChild()
		{
			String res = "";
			if(m_ptXmlNode!=null){
				Node n = m_ptXmlNode;
				if((n != null) && (n.getNodeType() == Node.ELEMENT_NODE)){
					Element e = (Element) n;
					if(e !=null){
						String s = e.getTextContent();
						if( s !=null){
							res = s;
						}
					}
				}
			}

			return res;
			
		}
		
		public double dGetDoubleAttribute(String attribName)
		{
			double res = 0;
			if (m_ptXmlNode!=null){
				if (m_ptXmlNode.getNodeType() ==  Node.ELEMENT_NODE){
					Element elem = (Element) m_ptXmlNode;
					if(elem != null){
						double r = 0;
						if (elem.hasAttribute(attribName))
							{
								
									if ( isDouble(elem.getAttribute(attribName))==true) 
									{
										r=Double.parseDouble(elem.getAttribute(attribName));
										res=r;
									}
								
							}
								//elem->QueryDoubleAttribute(attribName, &r) == TIXML_SUCCESS){
							
						}
					}
				}
			return res;
			}
			
		
			
		

		public boolean isInteger( String input ) {
			try {
				Integer.parseInt( input );
				return true;
			}
			catch( NumberFormatException nfe ) {
				return false;
			}
		}
		
		public boolean isDouble( String input ) {
			try {
				Double.parseDouble( input );
				return true;
			}
			catch( NumberFormatException nfe ) {
				return false;
			}
		}
	
	
		public int iGetIntAttribute(String attribName)
		{
			int res = 0;
			if (m_ptXmlNode!=null){
				if (m_ptXmlNode.getNodeType() ==  Node.ELEMENT_NODE){
					Element elem = (Element) m_ptXmlNode;
					if(elem != null){
						int r = 0;
						if (elem.hasAttribute(attribName))
							{
								
									if ( isDouble(elem.getAttribute(attribName))==true) 
									{
										r=Integer.parseInt(elem.getAttribute(attribName));
										res=r;
									}
								
							}
								//elem->QueryDoubleAttribute(attribName, &r) == TIXML_SUCCESS){
							
						}
					}
				}
			return res;
			}
			
		
		
		public String szGetStringAttribute(String attribName)
		{
			String res = "";
			if (m_ptXmlNode!=null){
				if (m_ptXmlNode.getNodeType() == Node.ELEMENT_NODE){
					Element elem = (Element) m_ptXmlNode;
					if(elem != null){
						String attrib = elem.getAttribute(attribName);
						if (attrib != null){
							res = attrib;
						}
					}
				}
			}
			return res;
			
		}
		

		public String szGetXmlString()
		{
			String res="";
			if (m_ptXmlNode!=null){
				StringWriter writer = new StringWriter();
				Transformer transformer;
				try {
					transformer = TransformerFactory.newInstance().newTransformer();
					transformer.transform(new DOMSource(m_ptXmlNode), new StreamResult(writer));
				} catch (TransformerConfigurationException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (TransformerFactoryConfigurationError e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (TransformerException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				res = writer.toString();
				//TiXmlPrinter printer; 
				//printer.SetStreamPrinting();
				//m_ptXmlNode->Accept(&printer);
			}
			return res;
			
		}
		
		public boolean bHasAttribute(String attribName)
		{
			boolean res = false;
			if (m_ptXmlNode!=null){
				if (m_ptXmlNode.getNodeType() ==  Node.ELEMENT_NODE){
					Element elem = (Element) m_ptXmlNode;
					if(elem != null){
						String attrib = elem.getAttribute(attribName);
						res = (attrib != null);
					}
				}
			}
			return res;
			
			
		}


}
