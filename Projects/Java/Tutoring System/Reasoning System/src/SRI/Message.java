package SRI;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Attr;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

public class Message {

	

	
		protected String m_szMessage;
		protected String m_szContentType;   // is the type of the object that is being send (given by the szGetObjType function of the serializable interface
		protected String m_szMessageType;  // this is the containter type
		protected String m_szSender;
		private boolean bDef=false;
	
		public Message()
		{
			m_szMessage = "";
			m_szContentType = "";
			m_szMessageType = "message";
			m_szSender="";
		}
	
		
		public Message(String m)
		{
			m_szMessage = m;
			m_szContentType = "string";
			m_szMessageType = "message";
			m_szSender="";
		}
		

		
		public void vSetContent(String message)
		{
			m_szMessage = message;
		}
		/** This function takes over the memory. The memory must be initialized using the
		* the array operator new T[] because it is released using delete[]*/
		public void vSetContent( String buffer,int size)
		{
			if(buffer != null){
				m_szMessage = buffer.toString();//((char)buffer, size);
				
			}else{
				m_szMessage = "";
			}
		}

		public String szGetContent()
		{
			return m_szMessage;
		}

		/** This function embeds the message in an xml envelope */
	
		public String szGetMessage()
		{
			StringBuffer mes=new StringBuffer();
			mes.append("<Message messageType=\"");
			mes.append(m_szMessageType);
			mes.append("\" contentType=\"");
			mes.append(m_szContentType);
			mes.append("\" sender=\"");
			mes.append(m_szSender);
			mes.append("\" >");
			mes.append(m_szMessage );
			mes.append("</Message>" );
			return mes.toString();
		}

		/** sets message with xml envelope 
		 * @throws ParserConfigurationException 
		 * @throws IOException 
		 * @throws SAXException 
		 * @throws UnsupportedEncodingException */
		public int iSetMessage(String message) throws ParserConfigurationException, UnsupportedEncodingException, SAXException, IOException
		{
			//#ifdef USE_TINYXML
			if(bDef)
			{
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			
			//Using factory get an instance of document builder
			DocumentBuilder db = dbf.newDocumentBuilder();
				
			//parse using builder to get DOM representation of the XML file
			Document doc = db.parse(new InputSource(new ByteArrayInputStream(message.getBytes("utf-8"))));
			
			//doc.Parse(message);
			//if(doc.Error()){
				//return 1;//SRI::SRI_ERR_SYNTAX;
			//}
			Element txMessage = doc.getDocumentElement();//getElementsByTagName("Message");
			if(txMessage != null && txMessage.toString().equals("Message"))
			{
				String typeId=txMessage.getAttribute("contentType");
				//NamedNodeMap arglist = txMessage.item(0).getAttributes();
				//Node typeId = arglist.getNamedItem("contentType");
				
				if(typeId == null){
					return 1;//SRI_ERR_SYNTAX
				}
				m_szContentType = typeId.toString();
				
				String nodeString="";
				for (Node node=txMessage.getFirstChild(); node.hasChildNodes(); node=node.getNextSibling()) 
			{
					nodeString=node.toString();
					if(node.toString().equals(null))
					{
						break;
						
					}
					
			}
				vSetContent(nodeString);
			}else{
				return 1;//SRI_ERR_LOAD;
			}
			return 0;//SRI_OK;
			}
			else
			{
			//#else
			DocumentBuilderFactory dbf1 = DocumentBuilderFactory.newInstance();
			
			//Using factory get an instance of document builder
			DocumentBuilder db1 = dbf1.newDocumentBuilder();
				
			//parse using builder to get DOM representation of the XML file
			Document doc1 = db1.parse(new InputSource(new ByteArrayInputStream(message.getBytes("utf-8"))));
				//rapidxml::xml_document<char> doc;
				//try{
				//	doc.parse<rapidxml::parse_non_destructive>(const_cast<char*>(message.c_str()));
				//}catch(rapidxml::parse_error& e){
				//	e.what();
				//	return 1;//SRI_ERR_SYNTAX;
			//	}
			
		//	TiXmlElement txMessage = doc.RootElement();
		//	if((txMessage != NULL) && (txMessage->ValueStr() == "Message")){
			//	TiXmlPrinter printer;//it means print to memory
			//	char typeId = txMessage->Attribute("contentType");
			//	if(typeId == NULL){
					//return SRI::SRI_ERR_SYNTAX;
				//}
				//m_szContentType = typeId;
				//printer.SetStreamPrinting();
				//for (  Node node=doc.getFirstChild(); node; node=node.NextSibling()){
				//	if ( !node->Accept(&printer) )
						//break;
				//}
				//vSetContent(printer.Str());
		//	}else{
			//	return SRI::SRI_ERR_LOAD;
			//}
			//return SRI_OK;
	//	#else
		//	rapidxml::xml_document<char> doc;
		//	try{
		//		doc.parse<rapidxml::parse_non_destructive>(const_cast<char*>(message.c_str()));
		//	}catch(rapidxml::parse_error& e){
			//	e.what();
			//	return SRI::SRI_ERR_SYNTAX;
			//}
			Element root =  (Element) doc1.getFirstChild();//("Message");
			//xml_node<>* root = doc.first_node("Message");
			if(root == null||root.toString()!="Message"){
				return 1;//SRI_ERR_SYNTAX;
			}
			
			String rxTypeId=root.getAttribute("contentType");
			//rxTypeId.getValue().length();
			//xml_attribute<>* rxTypeId = root->first_attribute("contentType");
			if(rxTypeId == null){
				return 1;//SRI_ERR_SYNTAX;
			}
			m_szContentType=rxTypeId;//.assign(rxTypeId, rxTypeId.length());

			String rxMTypeId = root.getAttribute("messageType");
			if(rxMTypeId == null){
				return 1;//SRI_ERR_SYNTAX;
			}
			//m_szMessageType.assign(rxMTypeId->value(), rxMTypeId->value_size());
			m_szMessageType=rxMTypeId;
			
			String content = "";
			for (Node node=root.getFirstChild(); node.hasChildNodes(); node=node.getNextSibling()) 
			{
				//for (rapidxml::xml_node<>* n = root->first_node(); n; n = n->next_sibling()){
				//rapidxml::print(std::back_inserter(content), *n, rapidxml::print_no_indenting);
				content=node.toString();
				if(node.toString().equals(null))
				{
					break;
				
				}
			
			}
			vSetContent(content);	
		//}
			

			return 0;//SRI_OK; 
			}
		//#endif
			
		}
	//
	//#ifdef USE_TINYXML
//		virtual int iSetMessage(TiXmlElement* txMessage);
	//#endif

		//virtual Message* ptClone() const;
		/** \returns the type of the object in the message. In case of the base message it is string.
		* In case of RawMessage it returns byteBuffer*/
		public String szGetContentType()
		{
			return m_szContentType;
			
		}
		/*
		 ** \returns the container type (message, rawMessage, objectMessage) */ 
		public String szGetMessageType()
		{
			return m_szMessageType;
		}


		public void vSetSender(String sender){
			m_szSender = sender;
		}


	
}
