package SRI;

public class ComponentFactory {



	/** The componentFacotry is modeled as an independent service. They can 
	* be instantiated independently and registered at a registry. For now,
	* a factory can only be registered at one registry at a time. 
	*/


	
	protected String m_szComponentType;
	protected String m_szName;
	protected String m_szConfig;

	public ComponentFactory(String config, String factName)
	{
		
		//config="";
		m_szConfig=config;
		
		m_szComponentType = "Component"; // type of components that are produced
		m_szName = factName; // components must give themselves a unique name
			
		m_ptRegistryHandle = null;
		
	}

		//Soon be replaced by RegistryHandle
		 // Initialized with gloabl registry (not possible to register at multiple registries)
		public RegistryHandle m_ptRegistryHandle;

		public int iSetRegistryHandle(RegistryHandle handle)
		{
			if(m_ptRegistryHandle != null){
				m_ptRegistryHandle.iUnregisterComponentFactory(m_szName);
				//delete m_ptRegistryHandle;
				m_ptRegistryHandle = null;
			}

			if(handle != null){
				m_ptRegistryHandle = handle;
				//register??
			}
			return 0;//SRI_OK
			
		}

	
	
	 public Component  ptCreateComponent(String name, String config )
		{
			Component c=new Component(name);
			config="";
			return c;
			
			
		}
	 
	 
	 int iSetComponentType(String type){
			m_szComponentType = type;
			return 0;
		}
		/** \returns the type of the components are being produced */
		
		
		public int iSetName(String name)
		{
			 m_szName = name; //TODO:: unregister - reregister - change name pattern
			 return 0;
		}
		
		public String szGetName()
		{
			
			return m_szName;
		}


		public String szGetComponentType()
		{
			return m_szComponentType;
			
		}
		
		public void vSetComponentType(String typeId)
		{
			 m_szComponentType = typeId;
		}
		
		public String szGetConfig() 
		{
			
			 return m_szConfig;
					
		}
		
		public RegistryHandle ptGetRegistryHandle() 
		{
			
			
			return m_ptRegistryHandle;
		}


		public ComponentDefinition tGetComponentDefinition(String config) // holds a definition (contract) of what type of components will be produced
		{
			 ComponentDefinition def=new ComponentDefinition("", m_szComponentType,  config);
			 return def;
			 
		}

}

