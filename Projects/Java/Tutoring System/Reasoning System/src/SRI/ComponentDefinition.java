package SRI;

import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;

public class ComponentDefinition extends Definition {
	



		protected Map<String, PortDefinition> m_mInputPorts;
		protected Map<String, PortDefinition> m_mOutputPorts;

		protected Map<String, ComponentDefinition> m_mChildren;
		String m_szEngineName; //indicates if component is attached to an engine
		String m_szComponentName;  // the base name property is used for the fully qualified name. This holds the unqualified name
		String m_szComponentType; //holds the type of the component

	
		public ComponentDefinition()
		{
			vSetDefinitionType("ComponentDefinition");
		}
		
		/** Assumes that component name is the same as full qualified name */
		public ComponentDefinition( String name, String type, String config)
		{
			super(name, "ComponentDefinition", config);
			m_szComponentName=name;
			m_szComponentType=type;
			
		}
		
		/** Allows to give individual component name and fully qualified name */
		public ComponentDefinition(String componentName, String fullName, String type, String config)
		{
			super(fullName,"ComponentDefinition", config);
			m_szComponentName=componentName;
			m_szComponentType=type;
		}
		

		public  void vSetComponentName(String compName)
		{
			m_szComponentName = compName;
		}
		
		public void vSetEngineName(String engineName)
		{
			m_szEngineName = engineName;
		}
		
		public void vSetComponentType(String compType)
		{
			m_szComponentType = compType;
		}

		public int iAddInputPortDefinition(PortDefinition c)
		{
			if(!m_mInputPorts.containsKey(c.szGetName())){//create port definition class first
				m_mInputPorts.put(c.szGetName(), c);
				return 0;//SRI_OK;
			}else{
				return 1;//SRI_ERR_NAMECONFLICT;
			}
			
		}
		
		public int iAddOutputPortDefinition(PortDefinition c)
		{
			if(!m_mOutputPorts.containsKey(c.szGetName())){//create port definition class first
				m_mOutputPorts.put(c.szGetName(), c);
				return 0;//SRI_OK;
			}else{
				return 1;//SRI_ERR_NAMECONFLICT;
			}
			
			
		}

		public int iRemoveInputPortDefinition(String name)
		{
			if(m_mOutputPorts.containsKey(name)){
				m_mOutputPorts.remove(name);
				return 0;//SRI_OK;
			}else{
				return 1;//SRI_ERR_NAMECONFLICT;
			}
			
		}
		
		public int iRemoveOutputPortDefinition(String name)
		{
			if(m_mInputPorts.containsKey(name)){
				m_mInputPorts.remove(name);
				return 0;//SRI_OK;
			}else{
				return 1;//SRI_ERR_NAMECONFLICT;
			}
			
		}

		public String szGetComponentName()
		{
			return m_szComponentName;
			
		}
		
		public String szGetEngineName()
		{
			return m_szEngineName;
			
		}
		
		public String szGetComponentType()
		{
			return m_szComponentType;
			
		}

		public Map<String, PortDefinition> tGetInputPortDefinitions()
		{
			return m_mInputPorts;
			
		}
		
		public Map<String, PortDefinition> tGetOutputPortDefinitions()
		{
			return m_mOutputPorts;
			
		}

		
		/** Inserts the reference as a child of the current definition */
		public int iAddChildDefinition(ComponentDefinition def)
		{
			if(def!=null){
				if(m_mChildren.containsKey(def.szGetName())){
					//m_tLog.error("Unable to add child definition: Name already exists");
					return 1;//SRI::SRI_ERR_NAMECONFLICT;
				}else{
					m_mChildren.put(def.szGetName(), def);
				}
			}
			return 0;//SRI_OK;
			
		}
		
		public  void vRemoveChildDefinition(String name)
		{
			if(!m_mChildren.containsKey(name)){
				m_mChildren.remove(name);
			}
		}
		
		
		public  void vClearChildren()
		{
			m_mChildren.clear();
		}

		public Definition ptClone()
		{
			return null;
			
		}


		//================ Interface from Serializable ====================================
		public String szToString()
		{
			
			String def = szToString();
			ConfigReader reader = new ConfigReader();
			reader.iReadXmlConfig(def);
			ConfigNode base = reader.ptGetNode("/Definition");

			String inputPorts = "<InputPorts>";
			Set<Entry<String, PortDefinition>> s = m_mInputPorts.entrySet();
	         Iterator<Entry<String, PortDefinition>> i = s.iterator();
	         while (i.hasNext()) {
	        	 
	        	PortDefinition pd =   i.next().getValue();
				if(pd!=null){
					inputPorts +=pd.szToString();
					
				}
			}
			
			inputPorts += "</InputPorts>";
			ConfigNode inportsNode=new XmlConfigNode(inputPorts);

			String outPorts = "<OutputPorts>";
			Set<Entry<String, PortDefinition>> s1 = m_mOutputPorts.entrySet();
	         Iterator<Entry<String, PortDefinition>> i1 = s1.iterator();
	         while (i1.hasNext()) {
	        	 
	        	PortDefinition pd =   i1.next().getValue();
				if(pd!=null){
					outPorts +=pd.szToString();
					
				}
			}
			outPorts += "</OutputPorts>";
			ConfigNode outportsNode=new XmlConfigNode(outPorts);

			String children = "<Children>";
			Set<Entry<String, ComponentDefinition>> s2 = m_mChildren.entrySet();
	         Iterator<Entry<String, ComponentDefinition>> i2 = s2.iterator();
	         while (i2.hasNext()) {
	        	 
	        	 ComponentDefinition cd =   i2.next().getValue();
				if(cd!=null){
					outPorts +=cd.szToString();
					
				}
			}
			
			children += "</Children>";
			ConfigNode childrenNode=new XmlConfigNode(children);
				
			if(base!=null){
				base.iAppendChild(inportsNode);
				base.iAppendChild(outportsNode);
				base.iAppendChild(childrenNode);
				base.iSetAttribute("engineName", m_szEngineName);
				base.iSetAttribute("componentName", m_szComponentName);
				base.iSetAttribute("componentType", m_szComponentType);

				return base.szGetXmlString();
			}else{
				return def;
			}
			
			
		}
		
		public int iFromString(String data)
		{
			
			ConfigReader reader = new ConfigReader();
			int res = reader.iReadXmlConfig(data);
			if (res != 0){//SRI_OK){
				//m_tLog.error("Unable to parse serialized string");
				return res;
			}
			res = super.iFromString(data);

			ConfigNode inPorts = reader.ptGetNode("/Definition/InputPorts");
			if(inPorts!=null){
				ConfigNode con=new ConfigNode();
				ConfigNode port = inPorts.ptIterateChildren("Definition",con );
				while(port!=null){
					PortDefinition def = new PortDefinition();
					if( def.iFromString(port.szGetXmlString()) == 0){//SRI_OK
						iAddInputPortDefinition(def);
					}
					port = inPorts.ptIterateChildren("Definition", port);
				}
			}

			ConfigNode outPorts = reader.ptGetNode("/Definition/OutputPorts");
			if(outPorts!=null){
				ConfigNode con=new ConfigNode();
				ConfigNode port = outPorts.ptIterateChildren("Definition", con);
				while(port!=null){
					PortDefinition def =  new PortDefinition();
					if( def.iFromString(port.szGetXmlString()) == 0){//SRI_OK){
						iAddOutputPortDefinition(def);
					}
					port = outPorts.ptIterateChildren("Definition", port);
				}
			}

			ConfigNode children = reader.ptGetNode("/Definition/Children");
			if(children!=null){
				ConfigNode con=new ConfigNode();
				ConfigNode child = children.ptIterateChildren("Definition", con);
				while(child!=null){
					ComponentDefinition def = new ComponentDefinition();   // TODO: How to parse derived definitions correctly?
					if(def.iFromString(child.szGetXmlString()) == 0){//SRI_OK){
						iAddChildDefinition(def);   
					}
					child = children.ptIterateChildren("Definition", child);
				}
			}

			if( reader.bHasParameter("/Definition/@engineName")){
				m_szEngineName = reader.szGetStringValue("/Definition/@engineName");
			}

			if( reader.bHasParameter("/Definition/@componentName")){
				m_szComponentName = reader.szGetStringValue("/Definition/@componentName");
			}

			if( reader.bHasParameter("/Definition/@componentType")){
				m_szComponentType = reader.szGetStringValue("/Definition/@componentType");
			}

			return res;
			
			
		}
		
		public String szGetObjType()
		{
			return "ComponentDefinition";
			
		}
	
}
