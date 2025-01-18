package SRI;

import java.io.IOException;
import java.io.StringReader;
import java.io.StringWriter;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

public class PortDefinition extends Definition{
	
	

		public static String szDirectionToString(PortDirection dir)
		{
			String res = "NO_DIRECTION";
			switch(dir){
				case INPUT:{
					res = "input";
					break;
				}
				case OUTPUT:{
					res = "output";
					break;
				}default:{
				}
			}
			return res;
			
		}
		
		public static PortDirection eDirectionFromString(String dir)
		{
			if(dir == "input"){
				return PortDirection.INPUT;
			}else if(dir == "output"){
				return PortDirection.OUTPUT;
			}else{
				return PortDirection.NO_DIRECTION;
			}
		
			
		}


		private String m_szPortDataType;
		private PortDirection m_ePortDirection;


		public PortDefinition()
		{
			vSetDefinitionType("PortDefinition");
			m_szPortDataType = "";
			m_ePortDirection = PortDirection.NO_DIRECTION;
		}
		
		public PortDefinition(String name, String portDataType, PortDirection direction)
		{
			super(name, "PortDefinition", "");
			m_szPortDataType=portDataType;
			direction=PortDirection.NO_DIRECTION;
			m_ePortDirection=direction;
			
		}
	
		
		public Definition ptClone()
		{
			return null;
			
		}

		public void vSetPortDataType(String type)
		{
			m_szPortDataType = type;
		}
		
		public String szGetPortDataType()
		{
			return m_szPortDataType;
			
		}
		
		public PortDirection eGetPortDirection()
		{
			return m_ePortDirection;
			
		}

		//================ Interface from Serializable ====================================
		public String szToString()
		{
			String def = super.szToString();
			DocumentBuilderFactory fact = 
			DocumentBuilderFactory.newInstance();
			DocumentBuilder builder;
			try {
				builder = fact.newDocumentBuilder();
			
			//Document doc = builder.parse(def);
			Document doc=builder.parse(new InputSource(new StringReader(def)));
			int res = 0;//SRI_OK;

		

			NodeList list1  = doc.getElementsByTagName("Definition");
			Element root = (Element) list1.item(0);
			StreamResult outer = new StreamResult();
			if(root == null){
				return def;
			}
			
				root.setAttribute("portDataType", m_szPortDataType);
				
				String direction = szDirectionToString(m_ePortDirection);

			
				root.setAttribute("direction", direction);

				String xml;
				xml=vXMLDocToStringStream(outer,doc);
				
				return xml;
			
			} catch (ParserConfigurationException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (SAXException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (TransformerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return def;
		}
			
		
		
		public int iFromString(String data)
		{
			int res = iFromString(data);
			
			DocumentBuilderFactory fact = 
					DocumentBuilderFactory.newInstance();
					DocumentBuilder builder;
					try {
						builder = fact.newDocumentBuilder();
					
					Document doc = builder.parse(data);
					

					NodeList list1  = doc.getElementsByTagName("Definition");
					Element root = (Element) list1.item(0);
					StreamResult outer = new StreamResult();
					if(root == null){
						return 1;//SRI error;
					}
						Attr rxType=root.getAttributeNode("portDataType");
					
						if(rxType!=null)
						{
							m_szPortDataType=rxType.getValue();
						}
						
						Attr rxDirection=root.getAttributeNode("direction");
						
						if(rxDirection!=null)
						{
							String direction=rxDirection.getValue();
							m_ePortDirection = eDirectionFromString(direction);
						}
					
				
					} catch (ParserConfigurationException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (SAXException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
			
					return res;
		}
		
		
		public String szGetObjType()
		{
			return "PortDefinition";
			
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



}
