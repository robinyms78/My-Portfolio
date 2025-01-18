package SRI;

public class RegistryHandle {
	
	
	
	




		protected SRIRegistry m_ptRegistry=null;
		protected String m_szConfig="";

		private int iGetRegistry(String config)
		{
			m_ptRegistry = SRIRegistry.ptGetInstance();
			return 0;//SRI_OK
			
		}


		public RegistryHandle(String config )
		{
			
			//config="";
			
			m_szConfig = config;
			iGetRegistry(config);
			
		}
		
		public RegistryHandle(SRIRegistry registry)
		{
			m_szConfig = "";
			m_ptRegistry = registry;
			
		}
		
		//virtual ~RegistryHandle();
		//RegistryHandle(const RegistryHandle& c);
		//RegistryHandle& operator=(const RegistryHandle&c);

		public boolean bIsValid()
		{
			if (m_ptRegistry!=null)
			{
				return true;
				
			}
			else
			return false;
		}
		
		public int iUnregisterComponentFactory(String name)
		{
			if(m_ptRegistry!=null){
				if(bIsRegistered(name)){
					m_ptRegistry.iUnregisterComponentFactory(name);
				}
			}
			return 0;//SRI_OK
		}
		
		
		public boolean bIsRegistered(String name)
		{
			if(m_ptRegistry!=null){
				return m_ptRegistry.bIsRegistered(name);
			}
			return false;
			
		}
		
	

	}



	
	
	
	
	
	
	
	
	
	
	
	


