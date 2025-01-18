package SRI;

import java.io.IOException;
import java.util.HashMap;
import java.util.Vector;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class SRIEngineStub {
	



/** The engine takes owenership of the components under its control
* The engine has two loops. One is called the simulation loop and the other the engine loop.
* The two loops are identical in that they host and run components.
* A component name must be unique for the whole engine (all loops).
* There is an ordering in execution of the two loops. vPreStep() and vStep() of the
* engine loop components are executed BEFORE the simulation loop (preStep, Step, postStep).
* The vPostStep() method of the engine loop components is executed afterwards.
* There is no ordering in execution of the modulues within one loop. Due to this ordering, engine loop components
* enclose the simulation loop and can provide control functionality (GUI, Console, etc.)
* Usually, engine loop components are added and removed by SRIEnginePlugins.
* Simulation loop components are created through factories that are accessed through the registry.
*/
//class SRI_E_API SRIEngineStub : public SRIEngine {
	//friend class SRI::EngineHandle;
	
//private:
	private SRIRegistry m_ptSRIRegistry;
	//private LoggerManager m_ptLoggerManager;

	//Ref<SRIEngine> m_ptSelfRef;

	private StubTemplate m_ptStubTemplate;

	//Poco::ThreadPool *m_ptThreadPool;
	private ExecutorService  m_ptThreadPool ;

	//Logger m_tLog;
	private boolean m_bIsRunning;

	/** Engine plugins are libraries that are loaded on runtime. 
	* There are two functions called from the lirbary:
	* 1) InitSRIEnginePlugin(SRI::SRIEngine* engine, SRI::String name, SRI::String pluginPath, SRI::String config)
	* 2) FreeSRIEnginePlugin(SRI::SRIEngine* engine, SRI::String pluginName, SRI::String pluginPath, SRI::String config);
	* On load, a plugin does whatever it needs to do on the engine: including adding components to the engineloop.
	* On close, a plugin removes whatever it has done and removes the components that it had added. (Plugins need to be 
	* released before the components of the two SRIEngine loops are released. 
	*/
	//HashMap<String, SRIEnginePluginHandle> m_mSRIEnginePlugins;
	private HashMap<String, Component> m_mEngineLoopComponents;
	private HashMap<String, Component> m_mSimulationLoopComponents;
	private HashMap<String,Component> m_mEmbeddedComponents;  // holds references to all components that are children

	
	//these components in these maps facilitate:
	//1. creating connections between component. the enginestub will check if the components
	//	are both local (using dynamic casting) and will handle the creation of the connection;
	//	otherwise, it will pass the connect request to the main engine
	// anything else???
		

	//TODO: what should these functions do?
	//SRIEngineStub(const SRIEngineStub& c);
	//SRIEngineStub operator=(const SRIEngineStub& c);

	private String m_szName;
	
	public StubTemplate ptGetStubTemplate()//created by chin
	{
		return m_ptStubTemplate;
		
	}

	public void vSetStubTemplate(StubTemplate st)//created by chin
	{
		m_ptStubTemplate=st;
		
	}

	//TODO: what should these functions do? to make virtual and override?
	/** This function frees all components registered in the engine loop*/
	private void vDeleteAllEngineComponents()
	{
		
	}
	
	/** This function frees all components registered in the simulation loop*/
	private void vDeleteAllSimulationComponents()
	{
		
	}
	
	/** Frees all loaded plugins. The FreeSRIEnginePlugin function is called and the library is closed. */
	///At present enginestubs don't have plugins loaded, so this shouldn't remove anything
	private void vReleaseAllPlugins()
	{
		
	}
	
	/** Function called Component (through EngineHandle) */
	public void vRemoveComponent(String compName)
	{
		
	}

	private int m_iEngineProcessId;
	

//public:
	public SRIEngineStub(String ip, int portNo, String name)
	{
		//name="SRIEngineStub";
		m_ptSRIRegistry=new SRIRegistry();
		m_szName=name;
		//m_ptSelfRef(this, false),
		//m_ptThreadPool
		//m_ptLoggerManager = LoggerManager::ptGetInstance();
		m_bIsRunning = false;
		m_iEngineProcessId = GetCurrentProcessId();//Inherited from Engine class //TODO has this been deprecated?
		m_ptStubTemplate = new StubTemplate(ip, portNo);
		
		m_mEngineLoopComponents = new HashMap<String, Component>();
		m_mSimulationLoopComponents = new HashMap<String, Component>();
		m_mEmbeddedComponents = new HashMap<String,Component>();  
		
	}
		
	public int GetCurrentProcessId() {
	// TODO Auto-generated method stub
	return 0;
}

	//virtual ~SRIEngineStub();

	//TODO: how to implement
	//bool operator==(const SRIEngine& e);

	/**
	* This method creates a component and assigns the given name to identify it in the application.
	* The name must be unique.
	* \returns 0 on success, otherwise an error code reflected by a negative number
	*/

	
	public int iConnect(String sender, String outport, String receiver, String inport)
	{
		ReactiveComponent ptSender=null;
		ReactiveComponent ptReceiver=null;
		if(ptGetComponent(sender, "*")instanceof ReactiveComponent)
		{
			 ptSender = (ReactiveComponent)(ptGetComponent(sender, "*"));
		}
		
		if(ptGetComponent(receiver, "*")instanceof ReactiveComponent)
		{
			 ptReceiver = (ReactiveComponent)(ptGetComponent(receiver, "*"));
		}
		//ReactiveComponent ptSender = dynamic_cast<ReactiveComponent*>(ptGetComponent(sender, "*").ptGetObj());
		//ReactiveComponent ptReceiver = dynamic_cast<ReactiveComponent*>(ptGetComponent(receiver, "*").ptGetObj());
		ReactiveComponentStub ptSenderStub =null;
		ReactiveComponentStub ptReceiverStub =null;
		if ((ptSender != null) && (ptReceiver != null)) {
			if(ptGetComponent(sender, "*")instanceof ReactiveComponentStub)
			{
				ptSenderStub = (ReactiveComponentStub)ptSender;
			}
			
			if(ptGetComponent(receiver, "*")instanceof ReactiveComponentStub)
			{
				ptReceiverStub = (ReactiveComponentStub)ptReceiver;
			}
			
			
			if ((ptSenderStub == null) && (ptReceiverStub == null)) { //test for both local
				if (!ptSender.bHasOutputPort(outport)) {
					//m_tLog.error("Unable to connect: Sender %s doesn't has a port %s", sender.c_str(), outport.c_str());
					System.out.println("Unable to connect: Sender %s doesn't has a port %s"+ sender+ outport);
					return -2;
				}
		
				if (!ptReceiver.bHasInputPort(inport)) {
					//m_tLog.error("Unable to connect: Receiver %s doesn't has a port %s", sender.c_str(),			outport.c_str());
					System.out.println("Unable to connect: Receiver %s doesn't has a port %s"+ sender+outport);
					return -2;
				}
				
				Connection conn = new Connection();
				if (ptSender.iAddOutputConnection(outport, conn) != 0){
					//m_tLog.error("error adding local connection to outport %s", outport.c_str());
					System.out.println("error adding local connection to outport "+ outport);
					return 1;//SRI_ERR_CALL;
				}
				if (ptReceiver.iAddInputConnection(inport, conn) != 0){
					//m_tLog.error("error adding local connection to inport %s", inport.c_str());
					System.out.println("error adding local connection to inport %s"+ inport);
					ptSender.iRemoveOutputConnection(outport,conn);
					return 1;//SRI_ERR_CALL;
				}

			}
			
		
		}

		//otherwise get main engine to handle
		Vector<String> args = new Vector<String>();
		args.add(sender);
		args.add(outport);
		args.add(receiver);
		args.add(inport);

		StringBuffer ptReply = new StringBuffer();
		int err = m_ptStubTemplate.szCallFunction("iConnect", args, ptReply);

		if (err != 0)
			return err;	
			
		return Integer.parseInt(ptReply.toString());
		
		
	}

	public int iDisconnect(String sender, String outport, String receiver, String inport)
	{
		return 0;
		
	}


	/** Initalizes all simulation loop components */
	public void vInitSimulationLoop()
	{
		
	}
	
	/** Performs a single step of all components*/
	public void vStepSimulationLoop()
	{
		
	}
	

	/** Engine loop convenience fucntions */
	public void vInitEngineLoop()
	{
		
	}
	
	public void vPreStepEngineLoop()
	{
		
	}
	public void vStepEngineLoop()
	{
		
	}
	public void vPostStepEngineLoop()
	{
		
	}
	

	
	// Main functions to control the engine. They handle engineloop as well as simulation loop components 
	/** Initializes all components. First of the engine loop, then of the simulation loop. */
	public void vInit()
	{
		
	}
	/** Steps all components. First preStep and Step of engine loop are executed. Then preStep, Step postStep of
	* simulation loop. At last postStep of engine loop components are executed.*/
	public void vStep()
	{
		
	}
	/** Encloses the vStep() function in a while loop. The loop stops if vStop() is called (For example by one of the
	* engine loop components. This allows to react on events such as closing of control window.*/
	public void vRun()
	{
		
	}
	/** Sets a flag that is evaluated by the vRun() method before it enters a Step(). The vRun() method returns. A stopped
	* engine can be restarted by calling vRun() again.*/
	public void vStop()
	{
		
	}
	/** Calls the finalize function on all components (engine and simulation loop) */
	public void vFinalize()
	{
		
	}

	/** This function is called by the destructor and frees all components and plugins*/
	public void vReleaseAll()
	{
		
	}

	public void vFinalizeAllSimulationComponents()
	{
		
	}
	
	public void vFinalizeAllEngineComponents()
	{
		
	}

	//TODO: can remote engines have plugins?

	/*virtual int iLoadEnginePlugin(SRI::String pluginName, SRI::String pluginPath = "", SRI::String config = "");
	virtual void vReleaseEnginePlugin(SRI::String pluginName);*/
	//virtual int iCreateRemoteComponent(int portNo, SRI::String typeId, SRI::String name, SRI::String config = "");

	//==================== Paramter component access ===========================================================
	/** This function searches the registry for a component factory with given type. If found
	* it creates a component with given name and adds it to the specified loop within the engine. The two supported labels
	* are currently "engine" and "simulation". By default it will choose the simulation loop*/
	public int iCreateComponent(String typeId, String name, String config , String loopLabel, String selectionCriteria )
	{
		 config = ""; 
		 loopLabel = "simulation";
		 selectionCriteria = "";
		return 0;
		
	}// using a string as an identifier (futur extensions might include regular expressions)
	/** This function takes an existing component and adds it to the engine. The engine will take over
	* and release the memory when it is no longer needed. The component is added to the simulation loop
	* and can be stepped. When the adding fails, the component is released immediately*/
	public int iAddComponent(Component comp, String loopLabel )
	{
		System.out.println(loopLabel);
		if(loopLabel == "simulation"){
			return iAddSimComponent(comp);
		}else if(loopLabel == "engine"){
			return iAddEngineComponent(comp);
		}else if(loopLabel == "embedded"){
			return iAddEmbeddedComponent(comp);
		}else{
			return iAddSimComponent(comp);
		}
	}
	/** Used to remove and delete a component associated with the engine. It will search for the component in the specified loop.
	*   A "*" string will trigger to search through all loops and delete all components wiht the given name.*/
	public void vDeleteComponent(String name, String loopLabel )
	{
		 loopLabel = "*";
	}
	/** Breaks the association of the component with the engine. The component is neither finalized, nor deleted.
	* The caller takes over the responsibility to release the component. */
	public void vRemoveComponent(Component comp, String loopLabel )
	{
		loopLabel = "*";
		
	}
	/** \returns the component with the given name from the simulation loop. NULL if none is found. A "*" value 
	* will search through both loops.*/
	public Component ptGetComponent(String name, String loopLabel )
	{
		Component comp= new Component();

		String label = loopLabel;
		if(label.equals("*")){
			label = szGetLoopLabel(name);
		}

		if(label.equals ("simulation")){
			comp = ptGetSimComponent(name);
		}else if(label .equals ("engine")){
			comp = ptGetEngineComponent(name);
		}else if(label .equals("embedded")){
			comp = ptGetEmbeddedComponent(name);
		}else {
			System.out.println("Unable to find component%s: Unsuported loop "+ name+ loopLabel);
			//m_tLog.error("Unable to find component%s: Unsuported loop %s", name.c_str(), loopLabel.c_str());
		}
		return comp;
	
	}

	public boolean bHasComponent(String name, String loopLabel )
	{
		loopLabel = "simulation";
		return false;
	}
	
	/** This function checks for pointer equality if a component is already existing */
	public boolean bHasComponent(Component comp)
	{
		return false;
		
	}
	
	public String szGetLoopLabel(String name)
	{
		Vector<String> args = new Vector<String>();
		args.add(name);
		StringBuffer ptReply = new StringBuffer();
		int err = m_ptStubTemplate.szCallFunction("szGetLoopLabel", args, ptReply);
		
		if (err != 0) {
			System.out.println("Network error: %d "+ err);
			return "";
		}
		
		return ptReply.toString();
		
	}
	
	public String szGetLoopLabel(Component comp)
	{
		return null;
		
	}

	//==================== Simulation components ===========================================================
	/** This function searches the registry for a component factory with given type. If found
	* it creates a component with given name and adds it to the engines simulation loop*/
	public int iCreateSimComponent(String typeId, String name, String config )
	{
		config = "";
		return 0;
	}
	
	/** Adds the ref to the engine if valid*/
	public int iAddSimComponent(Component comp)
	{
		if(comp==null){
			System.out.println("Unable to add component. Got NULL");
		
			//m_tLog.error("Unable to add component. Got NULL");
			return 1;// SRI_ERR_NULL;
		}

		if(comp.szGetName().equals("*")){
		//	m_tLog.error("Unable to add component %s. The name already exists.", comp->szGetName().c_str());
			System.out.println("Unable to add component %s. The name already exists. "+ comp.szGetName());
			comp.vFinalize();
			return 2;// SRI_ERR_NAMECONFLICT;
		}
		Component c = comp;
		ComponentStub cs1=null;
		ReactiveComponentStub rcs=null;
		//ComponentServer cse=null;
		//ReactiveComponentServer rcss=null;
		
		String ip, type;
		int port;


		
		//if (c.getClass().isInstance(cs1) ) {
		//	cs1 = (ComponentStub)c;
		
		
		

		if (c.getClass().isInstance(cs1) ) {
			cs1 = (ComponentStub)comp;
			ip = cs1.szGetPeerIp();
			port = cs1.iGetPeerPort();
			type = "Component";
		}
		else if (c.getClass().isInstance(rcs)) {
			rcs = (ReactiveComponentStub) comp;
			ip = rcs.szGetPeerIp();
			port = rcs.iGetPeerPort();
			type = "ReactiveComponent";
		}
		else {
			RemoteComponentRunner runner;

			ip = m_ptStubTemplate.szGetMyIp();
			if (comp instanceof Component )	{
				ComponentServer cs = new ComponentServer(comp);
				try {
					cs.vStartServer(0);
					Thread.sleep(1000);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				port = cs.iGetServerPort();
				runner = new RemoteComponentRunner(comp, cs);
				type = "Component";
				
			}
			else {
				ReactiveComponentServer rcs1 = new ReactiveComponentServer((ReactiveComponent)comp);
				try {
					rcs1.vStartServer(0);
					Thread.sleep(1000);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				port = rcs1.iGetServerPort();
				runner = new RemoteComponentRunner(comp, rcs1);
				type = "ReactiveComponent";
			}

		//	try {
			m_ptThreadPool=Executors.newFixedThreadPool(1000);
				m_ptThreadPool.execute(runner);
		//	}
			//catch (Exception e) {
				//String exceptionName=e);
				//if (exceptionName == "class Poco::NoThreadAvailableException") {
					//m_tLog.debug("Threadpool hit max capacity: %d", m_ptThreadPool->capacity());
				//	m_ptThreadPool->addCapacity(m_ptThreadPool->capacity()); //doubles the capacity of the threadool
				//	m_tLog.debug("Increased threadpool capacity to %d", m_ptThreadPool->capacity());
						
				//	m_ptThreadPool.start(runner);
			//	}
				//else 
					//m_tLog.error("Poco exception thrown: %s", e.displayText().c_str());
					
		//	}
			
		}

		//marshall args
	
		StringBuffer pNo=new StringBuffer();
		pNo.append(port);
		String szPort=pNo.toString();
		
		Vector<String> args = new Vector<String>();
		args.add(ip);
		args.add(szPort);
		args.add(type);

		StringBuffer ptReply = new StringBuffer();

		int err = m_ptStubTemplate.szCallFunction("iAddSimComponent", args, ptReply);
		
		if (err != 0) {
			//m_tLog.error("network error %d encountered", err);
			System.out.println("network error %d encountered "+err);
			return err;
		}

		err = Integer.parseInt(ptReply.toString());

		if (err != 0){//SRI_OK) {
		//	m_tLog.debug("Main engine returned error %d", err);
			System.out.println("Main engine returned error %d "+ err);
			return err;
		}

		//this is done by the main engine
		/*	SRI::String id = m_ptSRIRegistry->szCreateComponentID();
			comp->vSetId(id);*/
		m_mSimulationLoopComponents.put(comp.szGetName(), comp);
		if (err != 0){//SRI_OK){
			System.out.println("Unable to add component %s. "+ comp.szGetName());
			comp.vFinalize();
			return 1;
		}else{
			//SRIEngineStub es=new SRIEngineStub("",0,"");
			comp.iSetEngineHandle(this); //Since java is always the remote party , you can replace it with the engine stub instead of the handle //TODO : how can the remote part be parameterized? (give own address string??)
			System.out.println("Added component %s to Simulation loop "+ comp.szGetName());
			
		}

		return err;
	}
	
	/** This function takes an existing component and adds it to the engine. The engine will take over
	* and release the memory when it is no longer needed. The component is added to the simulation loop
	* and can be stepped. When the adding fails, the component is released immediately*/
	//public int iAddSimComponent(Component comp)
	//{
		
	//}
	
	/** Used to remove and delete a component associated with the engien.*/
	public void vDeleteSimComponent(String name)
	{
		
	}
	
	/** Breaks the association of the component with the engine. The component is neither finalized, nor deleted.
	* The caller takes over the responsibility to release the component. */
	public void vRemoveSimComponent(Component comp)
	{
		
	}
	/** \returns the component with the given name from the simulation loop. NULL if none is found.*/
	public Component ptGetSimComponent(String name)
	{
		return null;
		
	}

	//==================== Engine Components ===========================================================
	/** Functions for engine loop components are usually accessed by SRIEngineLoop plugins. They behave like
	* the simulation loop counterparts but target the engine loop instead of the simulation loop.*/
	public int iCreateEngineComponent(String typeId, String name, String config )
	{
		config = "";
		return 0;
	}
	
	public int iAddEngineComponent(Component comp)
	{
		if(comp==null){
			System.out.println("Unable to add component. Got NULL");
		
			//m_tLog.error("Unable to add component. Got NULL");
			return 1;// SRI_ERR_NULL;
		}

		if(comp.szGetName()== "*"){
		//	m_tLog.error("Unable to add component %s. The name already exists.", comp->szGetName().c_str());
			System.out.println("Unable to add component %s. The name already exists. "+ comp.szGetName());
			comp.vFinalize();
			return 2;// SRI_ERR_NAMECONFLICT;
		}
		
		Component c = comp;
		ComponentStub cs1=null;
		ReactiveComponentStub rcs=null;
		//ComponentServer cse=null;
		//ReactiveComponentServer rcss=null;
		
		String ip, type;
		int port;
		
		if (c.getClass().isInstance(cs1) ) {
			cs1 = (ComponentStub)comp;
			ip = cs1.szGetPeerIp();
			port = cs1.iGetPeerPort();
			type = "Component";
		}
		else if (c.getClass().isInstance(rcs)) {
			rcs = (ReactiveComponentStub) comp;
			ip = rcs.szGetPeerIp();
			port = rcs.iGetPeerPort();
			type = "ReactiveComponent";
		}
		
		
		else {
			RemoteComponentRunner runner;

			
			
			
			
			ip = m_ptStubTemplate.szGetMyIp();
			if (comp instanceof ReactiveComponent )	{
				ReactiveComponentServer rcs1 = new ReactiveComponentServer((ReactiveComponent)comp);
				try {
					rcs1.vStartServer(0);
					Thread.sleep(1000);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				port = rcs1.iGetServerPort();
				runner = new RemoteComponentRunner(comp, rcs1);
				type = "ReactiveComponent";

				
			}
			else {
				ComponentServer cs = new ComponentServer(comp);
				try {
					cs.vStartServer(0);
					Thread.sleep(1000);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				port = cs.iGetServerPort();
				runner = new RemoteComponentRunner(comp, cs);
				type = "Component";
			}


		//	try {
			m_ptThreadPool=Executors.newFixedThreadPool(1000);
			m_ptThreadPool.execute(runner);
				
		//	}
			//catch (Exception e) {
				//String exceptionName=e);
				//if (exceptionName == "class Poco::NoThreadAvailableException") {
					//m_tLog.debug("Threadpool hit max capacity: %d", m_ptThreadPool->capacity());
				//	m_ptThreadPool->addCapacity(m_ptThreadPool->capacity()); //doubles the capacity of the threadool
				//	m_tLog.debug("Increased threadpool capacity to %d", m_ptThreadPool->capacity());
						
				//	m_ptThreadPool.start(runner);
			//	}
				//else 
					//m_tLog.error("Poco exception thrown: %s", e.displayText().c_str());
					
		//	}
			
		}

		//marshall args
	
		StringBuffer pNo=new StringBuffer();
		pNo.append(port);
		String szPort=pNo.toString();
		
		Vector<String> args = new Vector<String>();
		args.add(ip);
		args.add(szPort);
		args.add(type);

		System.out.println(ip + " " + szPort + " " + type);
		
		StringBuffer ptReply = new StringBuffer();

		int err = m_ptStubTemplate.szCallFunction("iAddEngineComponent", args, ptReply);
		
		if (err != 0) {
			//m_tLog.error("network error %d encountered", err);
			System.out.println("network error %d encountered "+err);
			return err;
		}

		err = Integer.parseInt(ptReply.toString());

		if (err != 0){//SRI_OK) {
		//	m_tLog.debug("Main engine returned error %d", err);
			System.out.println("Main engine returned error %d "+ err);
			return err;
		}

		//this is done by the main engine
		/*	SRI::String id = m_ptSRIRegistry->szCreateComponentID();
			comp->vSetId(id);*/
		System.out.println("com name " + comp.szGetName());
		m_mEngineLoopComponents.put(comp.szGetName(), comp);
		if (err != 0){//SRI_OK){
			System.out.println("Unable to add component %s. "+ comp.szGetName());
			comp.vFinalize();
			return 1;
		}else{
//			SRIEngineStub es=new SRIEngineStub("",0,"");
			comp.iSetEngineHandle(this); //Since java is always the remote party , you can replace it with the engine stub instead of the handle //TODO : how can the remote part be parameterized? (give own address string??)
			System.out.println("Added component %s to Engine loop "+ comp.szGetName());
			
		}

		return err;
		
	}
	
	//public int iAddEngineComponent(Component comp)
	//{
		
	//}
	/** The remove functions just remove the component without releasing the memory */
	public void vRemoveEngineComponent(Component comp)
	{
		
	}
	
	public void vDeleteEngineComponent(String name)
	{
		
	}
	
	public Component ptGetEngineComponent(String name)
	{
		Component c=new Component();

		Vector<String> args=new Vector<String>();

		args.add(name);
		
		StringBuffer ptReply = new StringBuffer();

		int err = m_ptStubTemplate.szCallFunction("ptGetEngineComponent", args, ptReply);
		
		if (err != 0) {
			//m_tLog.error("network error %d encountered", err);
			System.out.println("network error %d encountered "+ err);
		}

		String type;
		String ip;
		int port;
		
		StringBuffer s=new StringBuffer();
		s.append(ptReply);
		
		int ind1=s.indexOf(" ", 0);
		type=s.substring(0, ind1);
		int ind2=s.indexOf(" ", ind1+1);
		ip=s.substring(ind1+1,ind2);
		port=Integer.parseInt(s.substring(ind2+1));
		//s >> type >> ip >> port;
		//System.out.println(" THE TYPE,IP,PORT "+type+" "+ip+" "+port);
		//String sriType=type;
		String ipAdd=ip;
		
		//std::stringstream s(ptReply.ptGetObj()->c_str());
		//s >> type >> ip >> port;

		//String sriType=type;
		//String ipAdd=ip;

		if (type.equals( "Component")) 
			c = new ComponentStub("", ipAdd, port);
		else if (type. equals( "ReactiveComponent"))
			c = new ReactiveComponentStub("", ipAdd, port);
		else if (type. equals( "ComponentServer"))
			c = new ComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
		else if (type.equals ("ReactiveComponentServer"))
			c = new ReactiveComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
		else {
			//m_tLog.error("Component not present in engine");
			System.out.println("Component not present in engine");
			return c;
		}
			
		c.iSetEngineHandle(this);
		
		return c;
		
	}


	/** This function changes the name of a component. It returns and
	* error code if a component with oldName could not be found or if
	* the new name is already in use in the engine*/
	public int iChangeName(String oldName, String newName)
	{
		return 0;
		
	}

	//==================== Embedded functionality ===========================================================
	public int iAddEmbeddedComponent(Component comp)
	{
		if(comp==null){
			System.out.println("Unable to add component. Got NULL");
		
			//m_tLog.error("Unable to add component. Got NULL");
			return 1;// SRI_ERR_NULL;
		}

		if(comp.szGetName()== "*"){
		//	m_tLog.error("Unable to add component %s. The name already exists.", comp->szGetName().c_str());
			System.out.println("Unable to add component %s. The name already exists. "+ comp.szGetName());
			comp.vFinalize();
			return 2;// SRI_ERR_NAMECONFLICT;
		}
		

		Component c = comp;
		ComponentStub cs1=null;
		ReactiveComponentStub rcs=null;
		//ComponentServer cse=null;
		//ReactiveComponentServer rcss=null;
		
		String ip, type;
		int port;
		
		if (c.getClass().isInstance(cs1) ) {
			cs1 = (ComponentStub)comp;
			ip = cs1.szGetPeerIp();
			port = cs1.iGetPeerPort();
			type = "Component";
		}
		else if (c.getClass().isInstance(rcs)) {
			rcs = (ReactiveComponentStub) comp;
			ip = rcs.szGetPeerIp();
			port = rcs.iGetPeerPort();
			type = "ReactiveComponent";
		}
		
		
		else {
			RemoteComponentRunner runner;

			ip = m_ptStubTemplate.szGetMyIp();
			if (comp instanceof Component )	{
				ComponentServer cs = new ComponentServer(comp);
				try {
					cs.vStartServer(0);
					Thread.sleep(1000);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				port = cs.iGetServerPort();
				runner = new RemoteComponentRunner(comp, cs);
				type = "Component";
				
			}
			else {
				ReactiveComponentServer rcs1 = new ReactiveComponentServer((ReactiveComponent)comp);
				try {
					rcs1.vStartServer(0);
					Thread.sleep(1000);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				port = rcs1.iGetServerPort();
				runner = new RemoteComponentRunner(comp, rcs1);
				type = "ReactiveComponent";
			}


		//	try {
			m_ptThreadPool=Executors.newFixedThreadPool(1000);
			m_ptThreadPool.execute(runner);
		//	}
			//catch (Exception e) {
				//String exceptionName=e);
				//if (exceptionName == "class Poco::NoThreadAvailableException") {
					//m_tLog.debug("Threadpool hit max capacity: %d", m_ptThreadPool->capacity());
				//	m_ptThreadPool->addCapacity(m_ptThreadPool->capacity()); //doubles the capacity of the threadool
				//	m_tLog.debug("Increased threadpool capacity to %d", m_ptThreadPool->capacity());
						
				//	m_ptThreadPool.start(runner);
			//	}
				//else 
					//m_tLog.error("Poco exception thrown: %s", e.displayText().c_str());
					
		//	}
			
		}

		//marshall args
	
		StringBuffer pNo=new StringBuffer();
		pNo.append(port);
		String szPort=pNo.toString();
		
		Vector<String> args = new Vector<String>();
		args.add(ip);
		args.add(szPort);
		args.add(type);

		StringBuffer ptReply = new StringBuffer();

		int err = m_ptStubTemplate.szCallFunction("iAddEmbeddedComponent", args, ptReply);
		
		if (err != 0) {
			//m_tLog.error("network error %d encountered", err);
			System.out.println("network error %d encountered "+err);
			return err;
		}

		err = Integer.parseInt(ptReply.toString());

		if (err != 0){//SRI_OK) {
		//	m_tLog.debug("Main engine returned error %d", err);
			System.out.println("Main engine returned error %d "+ err);
			return err;
		}

		//this is done by the main engine
		/*	SRI::String id = m_ptSRIRegistry->szCreateComponentID();
			comp->vSetId(id);*/
		m_mEngineLoopComponents.put(comp.szGetName(), comp);
		if (err != 0){//SRI_OK){
			System.out.println("Unable to add component %s. "+ comp.szGetName());
			comp.vFinalize();
			return 1;
		}else{
			//SRIEngineStub es=new SRIEngineStub("",0,"");
			comp.iSetEngineHandle(this); //Since java is always the remote party , you can replace it with the engine stub instead of the handle //TODO : how can the remote part be parameterized? (give own address string??)
			System.out.println("Added component %s to Embedded loop "+ comp.szGetName());
			
		}

		return err;
		
	}
	
	/** The memory of the component is taken over*/
	//public int iAddEmbeddedComponent(Component comp)
	//{
		
	//}
	public int iCreateEmbeddedComponent(String typeId, String name, String config )
	{
		config = "";
		return 0;
	}
	
	/** The caller takes over the responsibility to release the memory*/
	public void vRemoveEmbeddedComponent(Component comp)
	{
		
	}
	
	public void vDeleteEmbeddedComponent(String name)
	{
		
	}
	
	public Component ptGetEmbeddedComponent(String name)
	{
		return null;
		
	}


	//==================== Convenience functions ===========================================================
	/** Convenience access functions to target individual components of the simulation loop*/
	public void vInitComponent(String name)
	{
		
	}
	
	public void vFinalizeComponent(String name)
	{
		
	}
	
	public void vStopComponent(String name)
	{
		
	}
	
	public void vPauseComponent(String name)
	{
		
	}

	public String szGetName()
	{
		return m_szName;
		
	}
	
	public void vSetName(String name)
	{
		
	}

	//Convenience access functions
	/** The Engine requests a handle to the registry when it is created and releases it when it 
	* goes out of scope. During the lifetime of the engine the handle is stays valid*/
	//SRIRegistry* ptGetSRIRegistry();
	//Ref<LoggerManager> ptGetLoggerManager();
	public SRIRegistry ptGetSRIRegistry()
	{
		return m_ptSRIRegistry;
		
	}

	public int szCallFunction(String funcName, Vector<String> args, String retstring) 
	{
		return 0;
		
	}
	//int szCallFunction(SRI::String funcName, const std::vector<SRI::String>& args) const;
	public void vShutdownRemote()
	{
		
	}



	
	
	
	
	
}
