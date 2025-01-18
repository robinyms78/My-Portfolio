package SRI;

import java.io.IOException;
import java.io.StringReader;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

public class XmlConfigParser extends ConfigParser{

	
	
private Document m_tDoc;
		


public XmlConfigParser()
{
			
}
		
public int iReadString(String config)
{
	int res = super.iReadString(config);
	
	DocumentBuilderFactory fact = DocumentBuilderFactory.newInstance();
	DocumentBuilder builder;
	//try {
			try {
				builder = fact.newDocumentBuilder();
				m_tDoc=builder.parse(new InputSource(new StringReader(config)));
				//m_tDoc = builder.parse(config);
			} catch (ParserConfigurationException e) {
				System.out.println("Failed to prase xml");
				e.printStackTrace();
				return 1;
			} catch (SAXException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				System.out.println("Failed to prase xml");
				return 1;
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				System.out.println("Failed to prase xml");
				return 1;
			}
			
			
	
	
	//if(builder.Error()){
		//m_tLog.error("Failed to prase xml: id=%d, Row=%d, Col=%d\nMessage=%s", m_tDoc.ErrorId(), 
					//m_tDoc.ErrorRow(), m_tDoc.ErrorCol(), m_tDoc.ErrorDesc());
		//return SRI_ERR_SYNTAX;
	//}else{
		res = 0;//SRI_OK;
	///}

	return res;
			
}
		
public int iReadFile(String fileName)
{
	int res = super.iReadFile(fileName);
	
	DocumentBuilderFactory fact = DocumentBuilderFactory.newInstance();
	DocumentBuilder builder;
	
	try {
		builder = fact.newDocumentBuilder();
		m_tDoc= builder.parse(fileName);
	} catch (ParserConfigurationException e) {
		
		
	} catch (SAXException e) {
	
		System.out.println("Loading of file failed");
		e.printStackTrace();
		return 1;// SRI_ERR_FILE;
		
	} catch (IOException e) {
		System.out.println("Loading of file failed");
		e.printStackTrace();
		return 1;// SRI_ERR_FILE;
		
	}
	
	return res;
			
}


@Override
public ConfigParser ptClone() {
	// TODO Auto-generated method stub
	return null;
}

@Override
public boolean bHasParameter(String configPath) {
	
	Boolean r = null;
	
	XPathFactory factory = XPathFactory.newInstance();
	XPath xpath = factory.newXPath();
	XPathExpression expr;
	try {
		expr = xpath.compile(configPath);
		Object result = expr.evaluate(m_tDoc, XPathConstants.BOOLEAN);
		r= (Boolean) result;
	//for (int i = 0; i < nodes.getLength(); i++) {
	     //   System.out.println(nodes.item(i).getNodeValue()); 
	   // }
	
	
	} catch (XPathExpressionException e) {
		System.out.println("Unable to parse XPATH %s"+configPath);
		e.printStackTrace();
		return false;
	}
	return r;
	
	//return false;
}

@Override
public String szEvalQuery(String query) {
	// TODO Auto-generated method stub
	return "";
}

@Override
public boolean bGetBoolValue(String configPath) {
Boolean r = null;
	
	XPathFactory factory = XPathFactory.newInstance();
	XPath xpath = factory.newXPath();
	XPathExpression expr;
	try {
		expr = xpath.compile(configPath);
		Object result = expr.evaluate(m_tDoc, XPathConstants.BOOLEAN);
		r= (Boolean) result;
	//for (int i = 0; i < nodes.getLength(); i++) {
	     //   System.out.println(nodes.item(i).getNodeValue()); 
	   // }
	
	
	} catch (XPathExpressionException e) {
		System.out.println("Unable to parse XPATH %s"+configPath);
		e.printStackTrace();
		return false;
	}
	return r;
	
	//return false;
}

@Override
public int iGetIntValue(String configPath) {
int r = 0;
	
	XPathFactory factory = XPathFactory.newInstance();
	XPath xpath = factory.newXPath();
	XPathExpression expr;
	try {
		expr = xpath.compile(configPath);
		Object result = expr.evaluate(m_tDoc, XPathConstants.NUMBER);
		r= (Integer) result;
	//for (int i = 0; i < nodes.getLength(); i++) {
	     //   System.out.println(nodes.item(i).getNodeValue()); 
	   // }
	
	
	} catch (XPathExpressionException e) {
		System.out.println("Unable to parse XPATH %s"+configPath);
		e.printStackTrace();
		return 0;
	}
	return r;
	
	//return false;
}

@Override
public double dGetDoubleValue(String configPath) {
double r = 0;
	
	XPathFactory factory = XPathFactory.newInstance();
	XPath xpath = factory.newXPath();
	XPathExpression expr;
	try {
		expr = xpath.compile(configPath);
		Object result = expr.evaluate(m_tDoc, XPathConstants.NUMBER);
		r= (Double) result;
	//for (int i = 0; i < nodes.getLength(); i++) {
	     //   System.out.println(nodes.item(i).getNodeValue()); 
	   // }
	
	
	} catch (XPathExpressionException e) {
		System.out.println("Unable to parse XPATH %s"+configPath);
		e.printStackTrace();
		return 0;
	}
	return r;
	
	//return false;
}

@Override
public String szGetStringValue(String configPath) {
String r = "";
	
	XPathFactory factory = XPathFactory.newInstance();
	XPath xpath = factory.newXPath();
	XPathExpression expr;
	try {
		expr = xpath.compile(configPath);
		Object result = expr.evaluate(m_tDoc, XPathConstants.STRING);
		r= (String) result;
	//for (int i = 0; i < nodes.getLength(); i++) {
	     //   System.out.println(nodes.item(i).getNodeValue()); 
	   // }
	
	
	} catch (XPathExpressionException e) {
		System.out.println("Unable to parse XPATH %s"+configPath);
		e.printStackTrace();
		return "";
	}
	return r;
	
	//return false;
}

@Override
public ConfigNode ptGetNode(String configPath) {
//int r = 0;
	ConfigNode res = null;
	NodeList nodes = null;
	XPathFactory factory = XPathFactory.newInstance();
	XPath xpath = factory.newXPath();
	XPathExpression expr;
	try {
		expr = xpath.compile(configPath);
		Object result = expr.evaluate(m_tDoc, XPathConstants.NODESET);
		nodes= (NodeList) result;
	//for (int i = 0; i < nodes.getLength(); i++) {
	     //   System.out.println(nodes.item(i).getNodeValue()); 
	   // }
	if(nodes.getLength()>0)
	{
		if (nodes.getLength()>1)
		{
			System.out.println("Multiple matches found on request of node: Just returning first (to retrieve all use getNodeSet()");
			
		}
		Node node=nodes.item(0);
		if(node!=null)
		{
			XmlConfigNode cn=new XmlConfigNode(node);
			res=cn;
		}
	}else{
		System.out.println("No node found for path"+ configPath);
	}
	
	
	} catch (XPathExpressionException e) {
		System.out.println("Unable to parse XPATH %s"+configPath);
		e.printStackTrace();
		return res;
	}
	return res;
	
	//return false;
}

@Override
public ConfigNodeSet ptGetNodeSet(String configPath) {
	ConfigNodeSet res=null;//(new XmlConfigNodeSet(m_tDoc.getFirstChild(), configPath));
	return res;
}

}
		
	