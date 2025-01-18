package SRI;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;
import java.util.Map.Entry;
import java.util.concurrent.locks.ReentrantLock;

public class SRIRegistry {

	
	


	/** The component registry is implemented as a singelton and accessible for all
	* components in the SRI architecture
	* Plugins can be loaded from DLL.
	* The plugins must provide the InitSRIPlugin() and FreeSRIPlugin() functions.
	* 
	* The lifespan of factories is modeled independent from the lifespan of the registry.
	* That means that factories can be services that register or unregister at a registry.
	* The base implementation of a factory requires to unregister from a registry.
	*
	* A registry is global for a namespace. Multiple engines of a namespace can
	* use the same registry. 
	*/
	
	

		public static SRIRegistry m_ptInstance;
		//static Ref<SRIRegistry> m_tBaseRef;
		
		//Logger SRIRegistry::m_tLog ("SRIRegistry", LOG_DEBUG);
		public int m_iIdNum=4000;
		public static boolean m_bIsRemote=false;
		public static String m_szIp=""; //ip of real registry
		public static int m_iPort=0;
		public int m_iRefCount=0;
		ReentrantLock m_hRegistryMutex ;
		
		protected HashMap<String, ComponentFactory> m_mComponentFactories=new HashMap<String, ComponentFactory>();
		//SRI::Map<SRI::String, Ref<ComponentFactory>> m_mComponentFactories;
		//SRI::Map<SRI::String, SRIEngine*> m_mEngines;
		
		public static SRIRegistry ptGetInstance(){	//static function	
			if(m_ptInstance==null){
				SRIRegistry ref = null;
				if (m_bIsRemote) {
				////	ref.ptAttachNew(new SRIRegistryStub(m_szIp, m_iPort));To be implemented later
					System.out.println("created registry stub");
					//do not have registry stub class yet so cannot test this part
					//m_tLog.debug("created registry stub");
				}
				else {
					ref=new SRIRegistry();
					//ref.ptAttachNew(new SRIRegistry());
					//m_tLog.debug("created local SRIRegistry");
					System.out.println("created local SRIRegistry");
				}
				//m_ptInstance = ref.tGetWeakRef();
				return ref;
			}else{
				return m_ptInstance;
			}
			
//			Ref<SRIRegistry> ref = m_tBaseRef.tGetCounterRef();
//			return ref;
		}
		
		public SRIRegistry(){
			//#ifdef SRI_THREADSAFE
			m_hRegistryMutex=new ReentrantLock() ;
				if (m_hRegistryMutex == null) {
					System.out.println("Error initialising registry mutex");
					//m_tLog.error("Error initialising registry mutex");
				}
			//#endif
			}
		
		
		/** This function is used internally to assign an ID to a new component.*/
		protected String szCreateComponentID()
		{
			StringBuffer id =new StringBuffer(48);
			
			id.append("Component_127.0.0.1:%4d"+m_iIdNum);
			m_iIdNum++;
			return id.toString();
		}

	
		public HashMap<String, ComponentFactory> tGetComponentFactories()
		{
			
			return m_mComponentFactories;
			
		}


		//static SRIRegistry* ptGetInstance();
	//public SRIRegistry ptGetInstance()
	//{ 
		
	//}
		

		//virtual ~SRIRegistry();

		/** The function registers a component with the registry. 
		* The base class of the factory makes sure that it is unregistered in the destructor.
		* The memory is NOT taken over. All factories that are present when the factory goes out 
		* of scope are deleted. 
		*/
		public int iRegisterComponentFactory(ComponentFactory c)
		{
		
	//	#ifdef SRI_THREADSAFE
			synchronized (m_hRegistryMutex){
			try {
		
			m_hRegistryMutex.wait(10);
			} 
			catch (InterruptedException e) {
			// TODO Auto-generated catch block
				e.printStackTrace();
			}
			//}
		//WaitForSingleObject(m_hRegistryMutex, INFINITE);
	//#endif
			//synchronized (m_hRegistryMutex){
			if(c!=null){
				if(m_mComponentFactories.containsKey(c.szGetName()))
				{
					System.out.println("ComponentFactory with given name is already registered"+ c.szGetName());
				//m_tLog.warn("ComponentFactory with given name (%s) is already registered", c->szGetName().c_str());
//	#ifdef SRI_THREADSAFE
					m_hRegistryMutex.notify();
//	#endif
					return -2;  //TODO: unify errorcodes
				}
		

				else{
					m_mComponentFactories.put(c.szGetName(), c);
			//c->iSetRegistryHandle(&SRI::RegistryHandle(ptGetInstance()));implement later
					System.out.println("Registered factory %s at Registry"+ c.szGetName());
				}
			}
			else{
				System.out.println("Unable to register component: Got NULL pointer");
//#ifdef SRI_THREADSAFE
				m_hRegistryMutex.notify();
//#endif
				return 1;//SRI_ERR_NULL
			}
//#ifdef SRI_THREADSAFE
			m_hRegistryMutex.notify();
//#endif
	
			return 0;//SRI_OK
			}
		
		}


		/** Removes the given factory from the list of available factories*/
		public int iUnregisterComponentFactory(ComponentFactory c)
		{
			//#ifdef SRI_THREADSAFE
			synchronized (m_hRegistryMutex){
			try {
				m_hRegistryMutex.wait(10);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			//}
		//#endif
			//synchronized (m_hRegistryMutex){
			if(c!=null){
				if(m_mComponentFactories.containsKey(c.szGetName())){
					m_mComponentFactories.remove(c.szGetName());
					//c.iSetRegistryHandle(NULL);
					System.out.println("Removed factory %s from registry"+ c.szGetName());
				}else{
					System.out.println("No need to unregister: The factory %s has not been registered"+ c.szGetName());
				}
			}else{
				System.out.println("Unable to unregister invalid factory");
		//#ifdef SRI_THREADSAFE
				m_hRegistryMutex.notify();
		//#endif
				return 1;//SRI_ERR_NULL;
			}

		//#ifdef SRI_THREADSAFE
			m_hRegistryMutex.notify();
		//#endif
			return 0;//SRI_OK
			}
		}
		
		
		
		public int iUnregisterComponentFactory(String name)
		{
			//#ifdef SRI_THREADSAFE
			synchronized (m_hRegistryMutex){
			try {
				m_hRegistryMutex.wait(10);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	//	#endif
			if(m_mComponentFactories.containsKey(name)){
				ComponentFactory fact = m_mComponentFactories.get(name);
				m_mComponentFactories.remove(name);
				System.out.println("Removed factory %s from registry"+ name);
				if(fact!=null){
					//fact.iSetRegistryHandle(NULL);implement later
				}
				
			}else{
				System.out.println("No need to unregister: The factory %s has not been registered"+ name);
			}

		//#ifdef SRI_THREADSAFE
			m_hRegistryMutex.notify();
		//#endif

			return 0;
			}
		}
		
		
		/** Thin unregisters and delete all factories*/
		public void vUnregisterAllComponentFactories()
		{
			//#ifdef SRI_THREADSAFE
			synchronized (m_hRegistryMutex){
			try {
				m_hRegistryMutex.wait(10);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		//#endif
			 
			
			
	         Set<Entry<String, ComponentFactory>> s = m_mComponentFactories.entrySet();
	         Iterator<Entry<String, ComponentFactory>> i = s.iterator();
	         while (i.hasNext()) {
	                // System.out.println(i.next());
	        	// count++;
	        	 Entry<String, ComponentFactory>entry=i.next();//always need to transfer the item to another set first
	        	 
	        	 if( entry!=null  )
	        	 {
	        		String key=entry.getKey();
		        	ComponentFactory value=entry.getValue();
					//memory deleted through reference
					ComponentFactory fact = (ComponentFactory)value;
					m_mComponentFactories.remove(key);

					if(fact!=null){
						fact.iSetRegistryHandle(null);//implement later
					}
					
				}
			}
			m_mComponentFactories.clear();
			m_iIdNum = 4000;

		//#ifdef SRI_THREADSAFE
			m_hRegistryMutex.notify();
		//#endif
			
			}
		}
		
		
		public boolean bIsRegistered(ComponentFactory c)
		{
			if(c==null){
				return false;
			}

			if(m_mComponentFactories.containsKey(c.szGetName())){
				return true;
			}
			return false;
		}
		
		public boolean bIsRegistered(String name)
		{
			return m_mComponentFactories.containsKey(name);
		}
		
		/** returns the number of factories that could produce the given type */
		public  int iFactoriesWithType(String type)
		{
			int res = 0;
			 Set<Entry<String, ComponentFactory>> s = m_mComponentFactories.entrySet();
	         Iterator<Entry<String, ComponentFactory>> i = s.iterator();
	         while (i.hasNext()) {
	        	 Entry<String, ComponentFactory>entry=i.next();
	                // System.out.println(i.next());
	        	// count++;
	        	 if( entry!=null  )
	        	 {
				ComponentFactory f = (ComponentFactory) entry.getValue();
				if(f!=null){
					if(f.szGetComponentType() == type){
						res++;
					}
				}
			}
	         }
			return res;
			
		}

		
		
		/**
		* \param typeId Type of ComponentFactory
		* \returns A reference to the ComponentFactory registerd with the given typeId if it exists, otherwise NULL
		*/
		public ComponentFactory ptGetComponentFactory(String typeId, String selectionCriteria )
		{
			ComponentFactory res = null;
			
			 Set<Entry<String, ComponentFactory>> s = m_mComponentFactories.entrySet();
	         Iterator<Entry<String, ComponentFactory>> i = s.iterator();
	         while (i.hasNext()) {
	                // System.out.println(i.next());
	        	// count++;
	        	 Entry<String, ComponentFactory>entry=i.next();
	        	 if( i.next()!=null &&m_mComponentFactories.size()>0 )
	        	 {
	        		 ComponentFactory f=(ComponentFactory) entry.getValue();
	        		 if(f.szGetComponentType()==typeId)
	        		 {
	        			 res=(ComponentFactory) f;
	        			 break;
	        		 }
	        		 
	        		
	        	 }
	         }
			
			return res;
			
		}
		
		
		public ComponentFactory ptGetComponentFactoryByName(String name)
		{
			//TODO: how can this be protected? no way of guaranteeing once lock is released, and 
			//have to release the lock before returning
			if(m_mComponentFactories.containsKey(name)){
				return m_mComponentFactories.get(name);
			}else{
				return null;
			}
		}

		//virtual int iRegisterEngine(SRIEngine* engine);
		//virtual int iUnregisterEngine(SRIEngine* engine);
		//SRIEngine* ptGetEngine(SRI::String name);

		public static void vMakeRemote(String ip, int port)
		{
			if (!m_bIsRemote) {
				m_bIsRemote = true;
				//m_tLog.debug("made registry remote");
				System.out.println("made registry remote");
				m_szIp = ip;
				m_iPort = port;
			}
			else {
				//m_tLog.error("attempted to make registry remote when already remote\n");
				System.out.println("attempted to make registry remote when already remote\n");
			}
		}
	





	
	
	
	
	
}