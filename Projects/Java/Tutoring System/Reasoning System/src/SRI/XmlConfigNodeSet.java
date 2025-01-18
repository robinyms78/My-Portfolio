package SRI;

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Node;

public class XmlConfigNodeSet extends ConfigNodeSet {

	

	

		private XPath m_ptXPath;
		


		public XmlConfigNodeSet()
		{
			System.out.println("XmlConfigNodeSet");
		}
		
		public XmlConfigNodeSet(Node XNp_source_tree, String cp_xpath_exp)
		{
			XPathFactory factory = XPathFactory.newInstance();
			m_ptXPath = factory.newXPath();
			XPathExpression expr = null;
			//try {
				try {
					expr = m_ptXPath.compile(cp_xpath_exp);
				} catch (XPathExpressionException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				//r= (Boolean) result;
			
		
		//	m_ptXPath(new TinyXPath::xpath_processor(XNp_source_tree,cp_xpath_exp)),
			//m_tLog("XmlConfigNodeSet", LOG_DEBUG)
			System.out.println("XmlCongfigNodeSet");
			//{
			
			if(m_ptXPath!=null){// && (m_ptXPath->e_error != TinyXPath::xpath_processor::e_no_error)){
				Object result = null;
				try {
					result = expr.evaluate(XNp_source_tree, XPathConstants.NUMBER);
				} catch (XPathExpressionException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				m_iNodeSetSize = (Integer)result;
			}else{
				System.out.println("Unable to compute node set: %s"+cp_xpath_exp);
				//m_tLog.error("Unable to compute node set: %s",cp_xpath_exp);
			}
		}
			
			
		public XmlConfigNodeSet(XPath pathProcessor,  int nodeSetSize)
		{
			System.out.println("XmlConfigNodeSet");
			
				m_ptXPath = pathProcessor;
				m_iNodeSetSize = nodeSetSize;
		}
		//virtual ~XmlConfigNodeSet();

		//XmlConfigNodeSet(const XmlConfigNodeSet& c);
		//XmlConfigNodeSet& operator=(const XmlConfigNodeSet& c);

		public ConfigNode ptGetNode(int pos)
		{
			ConfigNode res = new ConfigNode();
			XPathExpression expr = null;
			if(m_ptXPath!=null){
				if((pos >= 0) && (pos < m_iNodeSetSize)){
					Object result = null;
					try {
						result = expr.evaluate(pos, XPathConstants.NODE);
					} catch (XPathExpressionException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					//Node node = m_ptXPath.XNp_get_xpath_node(pos);
					Node node=(Node)result;
					if(node != null){
						XmlConfigNode xn = new XmlConfigNode(node);
						res=xn;
					}
				}else{
					//m_tLog.error("Unable to get node: Number out of scope: %d  NodeSetSize is %s", pos, m_iNodeSetSize);
					System.out.println("Unable to get node: Number out of scope: %d  NodeSetSize is %s"+ pos+ m_iNodeSetSize);
				}
			}else{
				//m_tLog.error("Unable to get node: document not ready");
				System.out.println("Unable to get node: document not ready");
			}
			return res;
		}

	

	} 





	
	

