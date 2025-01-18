package SRI;

public class Definition {

	//ifndef SRI_DEFINITION_H
	//#define SRI_DEFINITION_H

	/** A definition holds a textual representation of a software component */

	//#include "SRI/SRIEngine/SRIEngineLib.h"
	//#include "SRI/SRIUtil/SRIString.h"
//
	//namespace SRI{
//
	//class SRI_E_API Definition{

	//private:

	//protected:
		protected String m_szName;
		protected String m_szDefType;
		protected String m_szConfig;

		/** Definition type should be set from within the class definition */
		 protected void vSetDefinitionType(String type)
		 {
			 m_szDefType = type;
		 }

	//public:
		public Definition()
		{
			
		}
		public Definition(String name, String defType, String config)
		{
			m_szDefType = defType;
			m_szName = name;
			m_szConfig = config;
		}
		//Definition(const Definition& c);
		//Definition& operator=(const Definition& c);
		//virtual ~Definition();

		//bool operator==(const Definition& c) const;
		//bool operator!=(const Definition& c) const;

		public void vSetName(String name)
		{
			m_szName = name;
		}
		
		public void vSetConfig(String config)
		{
			m_szConfig = config;
		}
		

		public String szGetDefinitionType()
		{
			return m_szDefType;
			
		}
		
		public String szGetName()
		{
			return m_szName;
			
		}
		
		public String szGetConfig()
		{
			return m_szConfig;
			
		}

		public Definition ptClone()
		{
			return null;
			
		}

		//================ Interface from Serializable ====================================
		public String szToString()
		{
			String def="<Definition defType=\\" + m_szDefType+ "\\"+" name=\\"+m_szName+"\\"+" ><Config>"+m_szConfig+"</Config></Definition>";
			//def.vFormat("<Definition defType=\"%s\" name=\"%s\" ><Config>%s</Config></Definition>", 
				//m_szDefType, m_szName, m_szConfig);
			
			return def;
		
		}
		
		public int iFromString(String data)
		{
			/* Is this useful?? For LUA??
			ConfigReader reader;
			int res = reader.iReadXmlConfig(data);
			if (res != SRI_OK){
				//m_tLog.error("Unable to parse serialized string");
				return res;
			}
			*/
			String queryPath = "/Definition/@name";
			//if(reader.bHasParameter(queryPath)){
				m_szName = queryPath;//reader.szGetStringValue(queryPath);
			//}

			queryPath = "/Definition/@defType";
			//if(reader.bHasParameter(queryPath)){
				m_szDefType = queryPath;//reader.szGetStringValue(queryPath);
			//}

			queryPath = "/Definition/Config";
			//Ref<SRI::ConfigNode> confNode = reader.ptGetNode(queryPath);
		//	if(confNode.bIsValid()){
				m_szConfig = queryPath;//confNode->szGetTextChild();
			//}

			return 0;//SRI_OK;
		
			
		}
		
		public String szGetObjType()
		{
			return "Definition";
			
		}

	


	}



	
	

