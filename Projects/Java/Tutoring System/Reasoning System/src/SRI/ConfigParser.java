package SRI;

public abstract class ConfigParser {


	/** The ConfigParser supports reading configuration using a configPath
	* The configPath has a similar syntax as XPath
	*/
	
	protected String m_szConfig;
	protected boolean m_bHoldsFile;


	public ConfigParser()
	{
		m_szConfig = "";
		m_bHoldsFile = false;
	}
		

	public abstract ConfigParser ptClone();
	
	public int iReadString(String config)
	{
		m_szConfig = config;
		m_bHoldsFile = false;
		return 1;//SRI_ERR_NA;
			
	}
		
	public int iReadFile(String fileName)
	{
		m_szConfig = fileName;
		m_bHoldsFile = true;
		return 1;//SRI_ERR_NA;
			
	}

	public abstract boolean bHasParameter(String configPath) ;

	public abstract String szEvalQuery(String query);
		

	public abstract boolean bGetBoolValue(String configPath);
	public abstract int iGetIntValue(String configPath);
	public abstract double dGetDoubleValue(String configPath);
	public abstract String szGetStringValue(String configPath);

	public abstract ConfigNode ptGetNode(String configPath);
	public abstract ConfigNodeSet ptGetNodeSet(String configPath);

	
	
	
	
}
