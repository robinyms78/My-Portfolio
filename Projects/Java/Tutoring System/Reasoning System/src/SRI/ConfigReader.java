package SRI;

public class ConfigReader {
	
	


	/** Config information can be given either directly or through a 
	* config file. 
	* In case a config string is given, the format has to be specified:
	* @xml: <example var=3>c:\file.txt</example>
	* The @ sign and everything that follows until the : are truncated before
	* the actual parse. 
	*
	* @lua: var = 3; file="c:\\file.txt";
	*
	* In case it is a fileName the ending of the file is taken to determine 
	* the type of configuration:
	* c:\exampleConf.xml
	* c:\exampleConf.lua
	*/

	private	ConfigParser m_ptParser;

	
	public ConfigReader()
	{
		m_ptParser = null;
	}
		
	public ConfigReader(String config)
	{
		m_ptParser = null;
		int res = iReadConfig(config);
	}
		
	

		/** This version tries to parse if the config is lua or xml.
		* Therefor it should start with @lua: or @xml:   directly followed
		* by the actual config string 
		* If this prefix is missing, it assumed that a filename is given and then
		* it takes the file suffix to decide which parser to use.
		*/
	public int iReadConfig(String config)
	{
		int res = 0;//SRI_OK;

		if(m_ptParser != null){
			
			m_ptParser = null;
		}

		if(config.startsWith("@",0)){
			//configuration string
			int pos = config.indexOf(":", 1);//(':', 1);
			if(pos == -1){
				System.out.println("Config had wrong format: Should have been @xxx:config");
				
				return 1;//SRI_ERR_SYNTAX;
			}
			String type = config.substring(1, pos-1);
			type.toLowerCase();
			if(type == "lua"){
				//m_ptParser = new LuaConfigParser();
			}else if(type == "xml"){
				m_ptParser = new XmlConfigParser();
			}else{
				System.out.println("Unsupported type found in config reader");
				return 1;//SRI_ERR_NOT_DEFINED;
			}

			if(m_ptParser != null){
				String conf = config.substring(pos+1, -1);  //after the :
				res = m_ptParser.iReadString(conf);//need t implement in configparser later
				if(res != 0){//SRI_OK
					//m_tLog.error("Unable to parase config string");
					System.out.println("Unable to parase config string");
					return 1;//SRI_ERR_SYNTAX;
				}
			}
			

		}else{
			//search for the suffix and load file
			int pos = config.indexOf(".");
			if(pos == -1){
				System.out.println("Unable to find suffix");
				//m_tLog.error("Unable to find suffix");
				return 1;//SRI_ERR_LOAD;
			}

			String suffix = config.substring(pos+1, config.length() - pos);
			suffix.toLowerCase();
			if(suffix == "lua"){
				//m_ptParser = new LuaConfigParser();
			}else if(suffix == "xml"){
				m_ptParser = new XmlConfigParser();
			}else{
				System.out.println("Unsupported type found in config file reader");
				//m_tLog.error("Unsupported type found in config file reader");
				return 1;//SRI_ERR_NOT_DEFINED;
			}

			if(m_ptParser != null){
				res = m_ptParser.iReadFile(config);
				if(res != 0){//SRI_OK
					//m_tLog.error("Unable to parase config file");
					System.out.println("Unable to parase config file");
					return 1;//SRI_ERR_SYNTAX;
				}
			}
		}

		return res;
			
	}

		//virtual int iReadLuaConfig(const SRI::String luaConfig);
		//virtual int iReadLuaFile(const SRI::String luaFileName);

	public int iReadXmlConfig(String xmlConfig)
	{
		if(m_ptParser != null){
			//delete m_ptParser;
			m_ptParser = null;
		}
		m_ptParser = new XmlConfigParser();
		int res = m_ptParser.iReadString(xmlConfig);
		return res;
			
	}
		
	public int iReadXmlConfigFile(String xmlFileName)
	{
		if(m_ptParser != null){
			//delete m_ptParser;
			m_ptParser = null;
		}
		m_ptParser = new XmlConfigParser();
		int res = m_ptParser.iReadFile(xmlFileName);
		return res;
			
	}

	public boolean bHasParameter(String configPath)
	{
		if(m_ptParser != null){
			return m_ptParser.bHasParameter(configPath);
		}
		return false;
			
	}

		//int iGetConfigNodes(const SRI::String& configPath, ConfigNode& node);

	public boolean bGetBoolValue(String configPath)
	{
		if(m_ptParser != null){
			return m_ptParser.bGetBoolValue(configPath);
		}
		return false;
			
	}
		
	public int iGetIntValue(String configPath)
	{
		if(m_ptParser != null){
			return m_ptParser.iGetIntValue(configPath);
		}
		return 0;
			
	}
		
	public double dGetDoubleValue(String configPath)
	{
		if(m_ptParser != null){
			return m_ptParser.dGetDoubleValue(configPath);
		}
		return 0.0;
			
	}
		
	public String szGetStringValue(String configPath)
	{
		if(m_ptParser != null){
			return m_ptParser.szGetStringValue(configPath);
		}
		return "";
			
	}
		
	public ConfigNode ptGetNode(String configPath)
	{
		ConfigNode res = null;
		if(m_ptParser != null){
			res = m_ptParser.ptGetNode(configPath);
		}
		return res;
			
	}
		
	public ConfigNodeSet ptGetNodeSet(String configPath)
	{
		ConfigNodeSet res = null;
		if(m_ptParser != null){
			res = m_ptParser.ptGetNodeSet(configPath);
		}
		return res;
			
	}

	

}
