package SRI;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.CDATASection;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Text;
import org.w3c.dom.CharacterData;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;


public class RawMessage extends Message {

		protected char[] m_ptBuffer; 	//short b = (short)(a & 0xff);
		long m_iSize;// 	long b = a & 0xffffffffL;


		/** strings don't support zero bytes */
		public String szGetContent()
		{
			String rString="";
			try {
				DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
				DocumentBuilder docBuilder ;
				docBuilder = docFactory.newDocumentBuilder();
				
				Document doc = docBuilder.newDocument();
				//Element element = doc.createElement("company");
			
	 
			// root elements
			
			
			
			//#ifdef USE_TINYXML
			Element txMes = doc.createElement("");
	
			txMes.setNodeValue("Message");
			//TiXmlElement txMes("Message");
			txMes.setAttribute("messageType", m_szMessageType);
			//txMes.SetAttribute("messageType", m_szMessageType.c_str());
			txMes.setAttribute("contentType", m_szMessageType);
			//txMes.SetAttribute("contentType", m_szContentType.c_str());
			String s = String.valueOf(m_iSize);
			txMes.setAttribute("bufSize", s);
			
			Text txText = doc.createTextNode("");
			txText.setNodeValue("");
		//	XmlText txText
			//CDATA cdata;
			//CDATASection cdata;
			
			CharacterData cdata = doc.createCDATASection(""); ;
			// cdata = commentNode;
			 //cdata = textNode;

			cdata.setData(txText.toString());
			
					//TiXmlText txText("");
		//	txText.SetCDATA(true);
			/*
			if(m_ptBuffer != null){
				short [] buf = new short[(int) (m_iSize * 3 + 1)];
				vEncodeBytes(buf, (unsigned char)m_ptBuffer, m_iSize);
				txText.SetValue((char) buf);
			}
			*/
			//txMes.InsertEndChild(txText);
			txMes.appendChild(cdata);
			//TiXmlPrinter printer;
			//txMes.Accept(printer);
			rString= txMes.toString();
			
			} catch (ParserConfigurationException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			//return "";
			return rString;
		}
		
		public void vSetContent(String message)
		{
			
			if(m_ptBuffer != null){
				//delete[] m_ptBuffer;
				m_ptBuffer = null;
				m_iSize = 0;
			}

			if(message.length() > 0){
				m_iSize = message.length() + 1;  // for the /0
				m_ptBuffer = new char[(int) m_iSize];
				//sprintf_s(m_ptBuffer,m_iSize,"%s", message);//store as string in buffer
				//m_ptBuffer=message;//need to convert String to Char and then loop each string to char array
				
				int i=0;
				for(i=0;i<m_iSize;i++)
				{
					m_ptBuffer[i]=message.charAt(i);
					i++;
					
				}
				//String oneLetter = String.valueOf(someChar);
			}
			m_szContentType = "byteBuffer";
		}

		

		
		
	
		public RawMessage()
		{
			m_ptBuffer =  null;
			m_iSize = 0;
			m_szContentType = "byteBuffer";
			m_szMessageType = "rawMessage";
		}
		//virtual ~RawMessage();
	//	RawMessage(const RawMessage& c);
		/** Takes over the memory */
		public RawMessage(char[] buffer, long size)
		{
			char[] s = buffer;//(buffer & 0xff);
			long l = size & 0xffffffffL;
			
			m_ptBuffer = s;
			m_iSize = l;
			m_szContentType = "byteBuffer";
			m_szMessageType = "rawMessage";
			
		}
		/** Memory is copied */
		//RawMessage(const unsigned char* buffer, const unsigned int size);
		//RawMessage& operator=(const RawMessage& c);
		//virtual bool operator==(const RawMessage& c);

		public char[] ptGetContent()
		 {
			
			char[] buffer = m_ptBuffer;
			
			char[] s = (buffer);// & 0xff);
			return s;
		 }
		
		public long iGetContentSize()
		{
			  
			long size = m_iSize;
			
			long l = size & 0xffffffffL;
			return l;
		}

		public String szGetMessage()
		{
			return "";
		}
		
		/** This function takes over the memory*/
		public void vSetContent(char[] buffer, long size)
		{
			char[] s = (buffer);// & 0xff);
			long l = size & 0xffffffffL;
			
			//if(m_ptBuffer != null){
				//delete[] m_ptBuffer;
			//	m_ptBuffer = (Short) null;
			//	m_iSize = 0;
			//}

			m_ptBuffer = s;
			m_iSize = size;
			m_szContentType = "byteBuffer";
			
		}

		/** expects an XML string with embedded CDATA text */
		public int iSetMessage(String message)
		{
			//#ifdef USE_TINYXML
			String tempBufSize;
			DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder docBuilder ;
			try {
				docBuilder = docFactory.newDocumentBuilder();
			
			
			Document doc = docBuilder.newDocument();
	
		
		//#ifdef USE_TINYXML
			Element txMes = doc.createElement("");
			//TiXmlDocument doc;
			 doc = docBuilder.parse(new InputSource(new ByteArrayInputStream(message.getBytes("utf-8"))));
			//if(doc.Error()){
				//return 1;//SRI::SRI_ERR_SYNTAX;
		//	}

			Element txMessage = doc.createElement("");
			if((txMessage != null) && (txMessage.toString() == "Message")){
				int bufSize = 0;
				String typeId = txMessage.getAttribute("contentType");
				if(typeId == null){
					return 1;//SRI::SRI_ERR_SYNTAX;
				}
				//m_szTypeId = typeId;
				 String mTypeId = txMessage.getAttribute("messageType");
				if(mTypeId == null){
					return 1;//SRI::SRI_ERR_SYNTAX;
				}
				m_szMessageType = mTypeId;
				tempBufSize=txMessage.getAttribute("bufSize");
				if (tempBufSize==null)
				{
					return 1;//SRI_ERR_SYNTAX;
				}
				//if(txMessage.getAttribute("bufSize", bufSize) != TIXML_SUCCESS){
				//	return SRI_ERR_SYNTAX;
				//}
				m_iSize = Long.valueOf(tempBufSize).longValue();
				 String data = txMessage.getTextContent(); // assume that only the cdata text child is present
			//	if((data != null) && (bufSize > 0)){
					//if(m_ptBuffer != null){
						//delete[] m_ptBuffer;
						//m_ptBuffer = null;
						//m_iSize = 0;
					//}
					//TODO: check if data has size * 3
				 		//short s = (short)(buffer & 0xff);
					m_ptBuffer = new char[(int) m_iSize];
					//SRI::vDecodeBytes(m_ptBuffer, (unsigned char*) data, bufSize* 3);
				}
			else{
				return 1;//SRI::SRI_ERR_LOAD;
			}
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
			return 0;//SRI_OK;
			
			//return 0;
			
		}
	//
	
	//	virtual Message* ptClone() const;


	} 

	
	
	
	
	
	
	
	
	
	

