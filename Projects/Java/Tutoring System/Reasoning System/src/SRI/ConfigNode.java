package SRI;

public class ConfigNode {

	
		public ConfigNode()
		{
			
		}
		

		/** Returns the value of the node. Depending on the type this might have different
		* meaning. For elements it is the node name. For text elements it is the value of
		* the text*/
		public String szGetValue()
		{
			return "";
			
		}
		/** If empty string is given, this function returns the first child */
		public ConfigNode ptGetFirstChild(String value )
		{
			value="";
			return new ConfigNode();
			
		}
		/** If the node has a text child this function returns its value. Otherwise
		* it returns "" */
		public String szGetTextChild()
		{
			return "";
			
		}
		
		public ConfigNode ptIterateChildren(String value, ConfigNode previous )
		{
			value="";
			return previous=new ConfigNode();
		}

		/** The node is given by reference, because the pointer might be modified for memory optimization */
		public int iAppendChild(ConfigNode node)
		{
			return 1;//SRI::SRI_ERR_NOT_DEFINED;
			
		}
		/** Inserts the node after the specified child */
		public int iInsertChild(ConfigNode node, ConfigNode prev)
		{
			return 1;//SRI::SRI_ERR_NOT_DEFINED;
			
		}
		
		/** Removes the given child. The node reference receives a copy of the removed element*/
		public int iRemoveChild(ConfigNode node)
		{
			return 1;//SRI::SRI_ERR_NOT_DEFINED;
			
		}
		
		public int iSetAttribute(String attribute, String value)
		{
			return 1;//SRI::SRI_ERR_NOT_DEFINED;
			
		}
		
		/** \returns "ConfigNode" for base class and "LuaNode" or "XmlNode" according to implementation */
		public String szGetNodeType()
		{
			return "ConfigNode";
			
		}

		public double dGetDoubleAttribute(String attribName)
		{
			return 0.0;
			
		}
		
		public int iGetIntAttribute(String attribName)
		{
			return 0;
			
		}
		public String szGetStringAttribute(String attribName)
		{
			return "";
			
		}
		
		public String szGetXmlString()
		{
			return "";
			
		}
		
		public boolean bHasAttribute(String attribName)
		{
			return false;
			
			
		}


	
}
