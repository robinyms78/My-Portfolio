package SRI;

import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;
import java.util.Vector;
import java.util.Map.Entry;

public class ReactiveComponentStub extends ReactiveComponent {

//	public ReactiveComponentStub(String name) {
	//	super(name);
		// TODO Auto-generated constructor stub
//	}


	

	/// A ReactiveComponentStub is a local (to the engine/registry) representation of a remote ReactiveComponent
	/** ReactiveComponentStubs provide allow the engine/registry to access the services of a 
		remotely running ReactiveComponent. When the ReactiveComponentStub is deleted, the memory of the
		remote ReactiveComponent is automatically reclaimed.
	*/ 

	//class SRI_E_API ReactiveComponentStub: public ReactiveComponent {
		
		//friend class SRIEngine; //sets the ID of the module
								

	//private:
		private StubTemplate m_ptStubTemplate;
		//Logger m_tLog;

		private final int szCallFunction(String funcName, Vector<String> args, StringBuffer retstring)//return string got to change to string buffer in JAva because we need it does not have pointer 
		{
			//if(m_ptStubTemplate==null)
			//{
				//System.out.println(" ITS A NULL ");
			//}
			
			int err = m_ptStubTemplate.szCallFunction(funcName, args, retstring);
		if(m_ptStubTemplate==null)
		{
			System.out.println(" ITS A NULL ");
		}
			if (err != 0){//SRI_OK) {
				//Logger tempLogger("ComponentStub");
				//tempLogger.error("%s caused network error %d. invoking removal", funcName.c_str(), err); //TODO get error name
				System.out.println("%s caused network error %d. invoking removal "+ funcName+ err);
				//	m_ptEngineHandle->vRemoveComponent(m_szCachedName); //calling szGetname will result in infinite recursion, since already disconnected
				//invoke callback removal
			}
			return err;
		}
		
		private int szCallFunction(String funcName, StringBuffer retstring)
		{
			Vector<String> args=new Vector<String>();
			return szCallFunction(funcName, args, retstring);
		}
		//int szCallFunction(SRI::String funcName, std::vector<SRI::String>* args) const;

		/** Creates a copy and sets the copy
		 * @return */
		public void vSetDefinition(Definition def)//temp change to public for testing
		{
			Vector<String> args=new Vector<String>();
			if(def != null){
				args.add(def.szToString());
			}
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("vSetDefinition", args, ptReply);
			
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
			System.out.println("Network error: %d "+ err);

		}
		/** Sets the definition directly */
		//private void vSetDefinition(Definition ptDef)
		//{
			
		//}
		

		//used by SRIEngine when connecting ports
		public int iListenForConnection()//temp change to public for testing
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iListenForConnection", ptReply);

			if (err != 0)//SRI_OK) 
				return 1;//SRI_ERR;

			int port;
			//System.out.println("THE PTREPLY IS "+ptReply);
			StringBuffer ss=new StringBuffer(ptReply);
			//std::stringstream ss(ptReply.ptGetObj()->c_str());
			port=Integer.parseInt(ss.toString());

			if (port < 0) {
				//m_tLog.error("unable to start port for establishng Connection between remote ports");
				System.out.println("unable to start port for establishng Connection between remote ports");
				return 1;//SRI_ERR; 
			}

			return port;
		}
		
		public int iFinaliseConnection(String inport)//temp public 
		{
			Vector<String> args=new Vector<String>();
			args.add(inport);
			StringBuffer ptReply = new StringBuffer();
			
			int err = szCallFunction("iFinaliseConnection", args, ptReply);
			if (err != 0)//SRI_OK) 
				return 1;//SRI_ERR;
			
			return Integer.parseInt(ptReply.toString());
		}
		
		public int iConnectForConnection(String outport, String ip, int listenPort)//temp public
		{
			Vector<String> args=new Vector<String>();
			args.add(outport);

			args.add(ip);

			StringBuffer ss=new StringBuffer();
			//std::stringstream ss;
			ss.append (listenPort);
			String lPort=ss.toString();

			args.add(lPort);

			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iConnectForConnection", args, ptReply);
			return Integer.parseInt(ptReply.toString());
		}

	//protected:
		protected int iSetNameSpace(String name)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iSetNameSpace", args, ptReply);
			
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
			System.out.println("Network error: %d"+ err);

			return err;
		}
		
		protected void vSetId(String id)
		{
			StringBuffer ptReply = new StringBuffer();
			Vector<String> args= new Vector<String>();
			args.add(id);
			szCallFunction("vSetId", args, ptReply);
		}
		
	//public:
		
		public ReactiveComponentStub(String name, String ip, int portNo)
		{
			super(name);
			m_ptStubTemplate = new StubTemplate(ip, portNo);
			System.out.println("ReactiveComponentStub");
		}
		
		//virtual ~ReactiveComponentStub();

		//ReactiveComponentStub(const ReactiveComponentStub& c);
		//ReactiveComponentStub& operator=(const ReactiveComponentStub& c);


		
		public String szGetPeerIp()
		{
			return m_ptStubTemplate.szGetPeerIp();
		}//TODO: think of refactoring stubs
		
		public int iGetPeerPort()
		{
			return m_ptStubTemplate.iGetPeerPort();
		}
		
		public Component ptClone()
		{
			Component c = this;
			return c;
		}

		public int iAddRemoteOutputConnection(String outport, String inport, int listenPort)
		{
			Vector<String> args=new Vector<String>();
			args.add(outport);
			args.add(inport);
			
			StringBuffer ss=new StringBuffer();
			//std::stringstream ss;
			ss.append (listenPort);

			String lPort=ss.toString();

			args.add(lPort);

			args.add(m_ptStubTemplate.szGetMyIp());

			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iAddRemoteOutputConnection", args, ptReply);
			if (err != 0) {
				return err;
			}
			return Integer.parseInt(ptReply.toString());	
		}
		
		public int iAddRemoteInputConnection(String inport, String outport, int listenPort)
		{
			Vector<String> args=new Vector<String>();
			args.add(inport);
			args.add(outport);
			
			StringBuffer ss=new StringBuffer();
			//std::stringstream ss;
			ss.append (listenPort);

			String lPort=ss.toString();

			args.add(lPort);

			args.add(m_ptStubTemplate.szGetMyIp());

			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iAddRemoteInputConnection", args, ptReply);
			if (err != 0) {
				return err;
			}
			return Integer.parseInt(ptReply.toString());	
		}

		//Exposed functions
		//BEGIN from ReactiveComponent
		public int iCreateOutputPort(String name, String type)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			args.add(type);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iCreateOutputPort", args, ptReply);
			if (err != 0)//SRI_OK) 
				return err;
			return Integer.parseInt(ptReply.toString());
		}
		
		public int iCreateInputPort(String name, String type)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			args.add(type);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iCreateInputPort", args, ptReply);
			if (err != 0)//SRI_OK) 
				return err;
			return Integer.parseInt(ptReply.toString());
		}

		public void vRemoveOutputPort(String name)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("vRemoveOutputPort", args, ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
			System.out.println ("Network error: %d "+ err);
		}
		
		public void vRemoveInputPort(String name)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("vRemoveInputPort", args, ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d "+ err);
		}

		public boolean bHasInputPort(String inport)
		{
			Vector<String> args=new Vector<String>();
			args.add(inport);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("bHasInputPort", args, ptReply);
			if (err != 0){//SRI_OK) {
				return false;
			}
			else {
				//m_tLog.debug("%s", ptReply.ptGetObj()->c_str());
				System.out.println("%s" + ptReply.toString());
				if (ptReply.toString() == "true") 
					System.out.println("true");//m_tLog.debug("true");
				else 
					System.out.println("false");//m_tLog.debug("false");
				if (ptReply.toString() == "true") return true;
				else return false;
			}
		}
		
		public boolean bHasOutputPort(String outport)
		{
			Vector<String> args=new Vector<String>();
			args.add(outport);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("bHasOutputPort", args, ptReply);
			if (err != 0){//SRI_OK) {
				return false;
			}
			else {
				if (ptReply.toString() == "true") return true;
				else return false;
			}
		}

		public String szGetOutputPortAddress(String outport)
		{
			Vector<String> args=new Vector<String>();
			args.add(outport);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetOutputPortAddress", args, ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d " + err);
			return ptReply.toString();
		}
		
		public String szGetInputPortAddress(String inport)
		{
			Vector<String> args=new Vector<String>();
			args.add(inport);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetInputPortAddress", args, ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d " + err);
			return ptReply.toString();
		}
		
		/** Adds connection object to the specified output port*/
		public int iAddOutputConnection(String outport, Connection connection)
		{
			//create relay object
			//connect up connection to relay object
			//ask server side to add a remote connection connecting to the relay object
			return 1;//SRI_ERR_INCOMPLETE;
		}
		/** Adds connection object to the specified input port*/
		public int iAddInputConnection(String inport, Connection connection)
		{
			//create relay object
			//connect up connection to relay object
			//ask server side to add a remote connection connecting to the relay object
			return 1;//SRI_ERR_INCOMPLETE;
		}

		public int iRemoveOutputConnection(String outport, String inport)
		{
			Vector<String> args= new Vector<String>();
			args.add(outport);
			args.add(inport);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iRemoveOutputConnection", args, ptReply);
			if (err != 0)//SRI_OK) 
				return err;
			return Integer.parseInt(ptReply.toString());
		}
		
		public int iRemoveInputConnection(String inport, String outport)
		{
			Vector<String> args=new Vector<String>();
			args.add(inport);
			args.add(outport);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iRemoveInputConnection", args, ptReply);
			if (err != 0)//SRI_OK) 
				return err;
			return Integer.parseInt(ptReply.toString());
		}

		//TODO: consider deprecating, given above two functions? how to implement remotely?
		public int iRemoveOutputConnection(String outport, Connection connection)
		{
			//TODO how should this be implemented?
			return 1;//SRI_ERR_INCOMPLETE;
		}
		
		public int iRemoveInputConnection(String inport, Connection connection)
		{
			//TODO how should this be implemented?
			return 1;//SRI_ERR_INCOMPLETE;
		}

		

		/** Returns a list of ports in the format: Name, Type*/
		public HashMap<String, String> mGetInputPortList()
		{
			HashMap<String, String> m=new HashMap<String,String>();

			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("mGetInputPortList", ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d "+ err);
			//std::stringstream ss(ptReply.ptGetObj()->c_str());
			int numEntries;
			//ss >> numEntries;
			String s1, s2;
			
			StringBuffer ss=new StringBuffer();
			ss.append(ptReply);
			
			if(Integer.parseInt(ss.substring(0,1))>0)//check if the entries are 0
			{
				int ind1=ss.indexOf(" ", 0);
				
				numEntries=Integer.parseInt(ss.substring(0, ind1));
				
			//int ind2=ss.indexOf(" ", ind1);
			//s1=ss.substring(ind1,ind2-1);
			//port=Integer.parseInt(s.substring(ind2));
			//s >> type >> ip >> port;
				
				int ind3=0;
				while (numEntries > 0) 
				{
				
				//ss >> s1 >> s2;
				//int ind3
					int ind2=ss.indexOf(" ", ind1+1);
					
					s1=ss.substring(ind1+1,ind2);
					
					numEntries--;
					if(numEntries==0)
					{
						s2=ss.substring(ind2+1);
					}
					else
					{
						ind3=ss.indexOf(" ", ind2+1);
						s2=ss.substring(ind2+1,ind3);
						//System.out.println("THE REPLY IS "+s2);
					}
					String k=s1;
					String v=s2;
			
					m.put(k, v);
				
					if(numEntries>0)
					{
						ind1=ind3;
					}
				}
			
			}
			return m;
		}
		
		public HashMap<String, String> mGetOutputPortList()
		{
			HashMap<String, String> m=new HashMap<String,String>();

			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("mGetOutputPortList", ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d "+ err);
			//std::stringstream ss(ptReply.ptGetObj()->c_str());
			int numEntries;
			//ss >> numEntries;
			String s1, s2;
			
			StringBuffer ss=new StringBuffer();
			ss.append(ptReply);
			
			if(Integer.parseInt(ss.substring(0,1))>0)//check if the entries are 0
			{
				int ind1=ss.indexOf(" ", 0);
				
				numEntries=Integer.parseInt(ss.substring(0, ind1));
				
			//int ind2=ss.indexOf(" ", ind1);
			//s1=ss.substring(ind1,ind2-1);
			//port=Integer.parseInt(s.substring(ind2));
			//s >> type >> ip >> port;
				
				int ind3=0;
				while (numEntries > 0) 
				{
				
				//ss >> s1 >> s2;
				//int ind3
					int ind2=ss.indexOf(" ", ind1+1);
					
					s1=ss.substring(ind1+1,ind2);
					
					numEntries--;
					if(numEntries==0)
					{
						s2=ss.substring(ind2+1);
					}
					else
					{
						ind3=ss.indexOf(" ", ind2+1);
						s2=ss.substring(ind2+1,ind3);
						//System.out.println("THE REPLY IS "+s2);
					}
					String k=s1;
					String v=s2;
			
					m.put(k, v);
				
					if(numEntries>0)
					{
						ind1=ind3;
					}
				}
			
			
			}
			return m;
		}

		/** Retruns a list of ports encoded in an xml string */
		public String szGetInputPorts()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetInputPorts", ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d"+ err);
			return ptReply.toString();
		}
		/** Retruns a list of ports encoded in an xml string */
		public String szGetOutputPorts()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetOutputPorts", ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d"+ err);
			return ptReply.toString();
		}

		// =================== Private Port =============================================================
		public int iCreatePrivateOutputPort(String name, String type)
		{
			
			Vector<String> args=new Vector<String>();
			args.add(name);
			args.add(type);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iCreatePrivateOutputPort", args, ptReply);
			
			if (err != 0)//SRI_OK) 
				return err;
			return Integer.parseInt(ptReply.toString());
		}
		
		public int iCreatePrivateInputPort(String name, String type)
		{
		
			Vector<String> args=new Vector<String>();
			args.add(name);
			args.add(type);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iCreatePrivateInputPort", args, ptReply);
			if (err != 0){//SRI_OK) 
				return err;}
			
			return Integer.parseInt(ptReply.toString());
		}

		public void vRemovePrivateOutputPort(String name)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("vRemovePrivateOutputPort", args, ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
			System.out.println("Network error: %d"+ err);
		}
		
		public void vRemovePrivateInputPort(String name)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("vRemovePrivateInputPort", args, ptReply);
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
			System.out.println("Network error: %d"+ err);
		}

		//END from ReactiveComponent
		
		//Begin from Component
		//bool operator==(const Component& c);

		public int iSetEngineHandle(SRIEngineStub handle)//replace by stub in Java
		{
			//TODO: revise when overall structure becomes clear
			return super.iSetEngineHandle(handle);
		}//engine should be started with ip add if required =)
		
		public SRIEngineStub ptGetEngineHandle()
		{
			return super.ptGetEngineHandle();//need to implement new function in Component class
		}

		public int iSetParent(Component newParent)
		{
			if(newParent==null){
				//m_tLog.error("Unable to add component. Got NULL");
				System.out.println("Unable to add component. Got NULL");
				return 1;
			}
			Component c = newParent;
			ComponentStub cs1=null;
			ReactiveComponentStub rcs=null;
			ComponentServer cse=null;
			ReactiveComponentServer rcss=null;
			
			String ip, type;
			int port;


		//	if (c == null) {
				//ip = "NULL";
				//port = 0;
				//type = "NULL";
			//}
			
			if (c.getClass().isInstance(cs1) ) {
				cs1 = (ComponentStub)c;
				ip = cs1.szGetPeerIp();
				port = cs1.iGetPeerPort();
				type = "Component";
			}
			else if (c.getClass().isInstance(rcs) ) {
				rcs = (ReactiveComponentStub)c;
				ip = rcs.szGetPeerIp();
				port = rcs.iGetPeerPort();
				type = "ReactiveComponent";
			}
			else if (c.getClass().isInstance(cse) ) {//componentserver
				rcs = (ReactiveComponentStub)c;
				ip = rcs.szGetPeerIp();
				port = rcs.iGetPeerPort();
				type = "Component";
			}
			else if (c.getClass().isInstance(rcss) ){
				rcs = (ReactiveComponentStub)c;
				ip = rcs.szGetPeerIp();
				port = rcs.iGetPeerPort();
				type = "ReactiveComponent";
			}

			else {
				Component newServ;
				ReactiveComponent rc =null;
				if (c instanceof ReactiveComponent)
				{
				 rc = (ReactiveComponent)c;
				}
				ip = m_ptStubTemplate.szGetMyIp();
			
				
				if (rc == null)	{
					ComponentServer cs = new ComponentServer(c);
					try {
						cs.vStartServer(0);
						Thread.sleep(1000);//need to put this if not the iGetseverport will get error
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					port = cs.iGetServerPort();
					type = "Component";
					//newServ = cs;
					
				}
				else {
					ReactiveComponentServer rcs1 = new ReactiveComponentServer(rc);
					try {
						rcs1.vStartServer(0);
						Thread.sleep(1000);//need to put this if not the iGetseverport will get error
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					
					port = rcs1.iGetServerPort();
					type = "ReactiveComponent";
					//newServ = rcs;
				}

				
				newServ = newParent;
				//assert(newServ!=null);
				
				// Set<Entry<String, Component>> s = m_mParentServers.entrySet();
		        // Iterator<Entry<String, Component>> i = s.iterator();
		         //while (i.hasNext()) {
		             
		        	 //if(i.next().getKey()==(newServ.szGetComponentName()))
		        	// {	
		        		 
		        	//	 i.next().setValue(newServ);
		        	// }
		        // }
				//}
				//m_mParentServers.get(newServ.szGetComponentName())= newServ;
				//m_mParentServers[Integer.parseInt(newServ.szGetComponentName())] = newServ; //data will be overwritten later
				if (newParent.ptGetEngineHandle()!=null)
				{
					
				String loop = newParent.ptGetEngineHandle().szGetLoopLabel(newParent.szGetName());

				newParent.ptGetEngineHandle().vRemoveComponent(newParent.szGetName());
				newParent.ptGetEngineHandle().iAddComponent(newServ, loop);
				}
				//EngineHandle eh = newParent.ptGetEngineHandle();

			//	if (eh!=null) { //if this component is registered to an engine
				//	String loop = eh.szGetLoopLabel(newParent.szGetName());
					//m_tLog.critical("%s\n", loop.c_str());
				//	eh.vRemoveComponent(newParent.szGetName());
				//	eh.iAddComponent(newServ, loop);
				//}

				
			}

			//marshall args
			StringBuffer pNo=new StringBuffer();
			
			pNo.append( port);
			String szPort=pNo.toString();

			Vector<String> args=new Vector<String>();
			
			args.add(ip);
			args.add(szPort);
			args.add(type);

			StringBuffer ptReply = new StringBuffer();

			int err = m_ptStubTemplate.szCallFunction("iSetParent", args, ptReply);
			
			if (err != 0){//SRI_OK) {
				//m_tLog.error("network error %d encountered", err);
				System.out.println("network error %d encountered "+ err);
				return err;
			}

			err = Integer.parseInt(ptReply.toString());//atoi(ptReply.ptGetObj()->c_str());

			if (err != 0){//SRI_OK) {
				//m_tLog.debug("Main engine returned error %d", err);
				System.out.println("Main engine returned error %d "+ err);
				return err;
			}

			return err;
		}
		
		
		public int iAddChild(Component comp)
		{
			if(comp==null){
				//m_tLog.error("Unable to add component. Got NULL");
				System.out.println("Unable to add component. Got NULL");
				return 1;
			}
			Component c = comp;
			ComponentStub cs1=null;
			ReactiveComponentStub rcs=null;
			ComponentServer cse=null;
			ReactiveComponentServer rcss=null;
			
			String ip, type;
			int port;


		//	if (c == null) {
				//ip = "NULL";
				//port = 0;
				//type = "NULL";
			//}
			
			if (c.getClass().isInstance(cs1) ) {
				cs1 = (ComponentStub)c;
				ip = cs1.szGetPeerIp();
				port = cs1.iGetPeerPort();
				type = "Component";
			}
			else if (c.getClass().isInstance(rcs) ) {
				rcs = (ReactiveComponentStub)c;
				ip = rcs.szGetPeerIp();
				port = rcs.iGetPeerPort();
				type = "ReactiveComponent";
			}
			else if (c.getClass().isInstance(cse) ) {//componentserver
				rcs = (ReactiveComponentStub)c;
				ip = rcs.szGetPeerIp();
				port = rcs.iGetPeerPort();
				type = "Component";
			}
			else if (c.getClass().isInstance(rcss) ){
				rcs = (ReactiveComponentStub)c;
				ip = rcs.szGetPeerIp();
				port = rcs.iGetPeerPort();
				type = "ReactiveComponent";
			}

			else {
				Component newServ;
				
				ReactiveComponent rc =null;
				if (c instanceof ReactiveComponent)
				{
				 rc = (ReactiveComponent)c;
				}
				
				ip = m_ptStubTemplate.szGetMyIp();

				if (rc == null)	{
					ComponentServer cs = new ComponentServer(c);
					try {
						cs.vStartServer(0);
						Thread.sleep(1000);//need to put this if not the iGetseverport will get error
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					port = cs.iGetServerPort();
					type = "Component";
					//newServ = cs;
					
				}
				else {
					ReactiveComponentServer rcs1 = new ReactiveComponentServer(rc);
					try {
						rcs1.vStartServer(0);
						Thread.sleep(1000);//need to put this if not the iGetseverport will get error
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					port = rcs1.iGetServerPort();
					type = "ReactiveComponent";
					//newServ = rcs;
				}

				
				newServ = comp;
				//assert(newServ!=null);
				
				// Set<Entry<String, Component>> s = m_mParentServers.entrySet();
		        // Iterator<Entry<String, Component>> i = s.iterator();
		         //while (i.hasNext()) {
		             
		        	 //if(i.next().getKey()==(newServ.szGetComponentName()))
		        	// {	
		        		 
		        	//	 i.next().setValue(newServ);
		        	// }
		        // }
				//}
				//m_mParentServers.get(newServ.szGetComponentName())= newServ;
				//m_mParentServers[Integer.parseInt(newServ.szGetComponentName())] = newServ; //data will be overwritten later
				if (comp.ptGetEngineHandle()!=null)
				{
				String loop = comp.ptGetEngineHandle().szGetLoopLabel(comp.szGetName());

				comp.ptGetEngineHandle().vRemoveComponent(comp.szGetName());
				comp.ptGetEngineHandle().iAddComponent(newServ, loop);
				}
			//	EngineHandle eh = newParent.ptGetEngineHandle();

			//	if (eh!=null) { //if this component is registered to an engine
				//	String loop = eh.szGetLoopLabel(newParent.szGetName());
					//m_tLog.critical("%s\n", loop.c_str());
				//	eh.vRemoveComponent(newParent.szGetName());
				//	eh.iAddComponent(newServ, loop);
				//}

				
			}

			//marshall args
			StringBuffer pNo=new StringBuffer();
			
			pNo.append( port);
			String szPort=pNo.toString();

			Vector<String> args=new Vector<String>();
			
			args.add(ip);
			args.add(szPort);
			args.add(type);

			StringBuffer ptReply = new StringBuffer();

			int err = m_ptStubTemplate.szCallFunction("iAddChild", args, ptReply);
			
			if (err != 0){//SRI_OK) {
				//m_tLog.error("network error %d encountered", err);
				System.out.println("network error %d encountered "+ err);
				return err;
			}

			err = Integer.parseInt(ptReply.toString());//atoi(ptReply.ptGetObj()->c_str());

			if (err != 0){//SRI_OK) {
				//m_tLog.debug("Main engine returned error %d", err);
				System.out.println("Main engine returned error %d "+ err);
				return err;
			}

			return err;
		}
		
		public Component ptGetChild(String name)
		{
			Component c=new Component();	

			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("ptGetChild", args, ptReply);
			
			if (err != 0)//SRI_OK) 
			return c;
			
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
			System.out.println(" THE TYPE,IP,PORT "+type+" "+ip+" "+port);
			String sriType=type;
			String ipAdd=ip;

			if (type.equals("Component")) 
				c = new ComponentStub("", ipAdd, port);
			else if (type.equals("ReactiveComponent"))
				c = new ReactiveComponentStub("", ipAdd, port);
			else if (type.equals("ComponentServer"))
				c = new ComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else if (type.equals("ReactiveComponentServer"))
				c = new ReactiveComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else {
				//m_tLog.error("Child not present");
				System.out.println("Child not present");
				return c;
			}
				
			return c;
		}
		
		public Component ptGetParent()
		{
			Component c=new Component();	

			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("ptGetParent", ptReply);
			
			if (err !=0)// SRI_OK) 
				return c;
			
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
			System.out.println(" THE PARENT TYPE,IP,PORT "+type+" "+ip+" "+port);
			String sriType=type;
			String ipAdd=ip;

			if (type .equals("Component")) 
				c = new ComponentStub("", ipAdd, port);
			else if (type.equals ("ReactiveComponent"))
				c = new ReactiveComponentStub("", ipAdd, port);
			else if (type .equals("ComponentServer"))
				c = new ComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else if (type.equals("ReactiveComponentServer"))
				c = new ReactiveComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else {
				//m_tLog.debug("Parent not found");
				System.out.println("Parent not found");
				return c;
			}
				
				
			return c;
		}
		
		public boolean bHasChild(String name)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("bHasChild", args, ptReply);

			if (err != 0){//SRI_OK) {
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d"+ err);
				return false;	
			}

			String reply=ptReply.toString();

			if (reply == "true")
				return true;
			else return false;
		}
		
		/** returns reference to removed child. Child keeps its children*/
		public Component ptRemoveChild(String name)
		{
			//ComponentStubs do not have any refs to components, so is ok to establish a stub connection every time
			Component c=new Component();	

			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("ptRemoveChild", args, ptReply);

			if (err != 0)//SRI_OK) 
				return c;
			
			String type;
			String ip;
			int port;
				
			StringBuffer s=new StringBuffer(ptReply);
			int ind1=s.indexOf(" ", 0);
			type=s.substring(0, ind1);
			int ind2=s.indexOf(" ", ind1+1);
			ip=s.substring(ind1+1,ind2);
			port=Integer.parseInt(s.substring(ind2+1));
			//s >> type >> ip >> port;
			

			String sriType=type;
			String ipAdd=ip;

			if (type.equals ("Component")) 
				c = new ComponentStub("", ipAdd, port);
			else if (type.equals ("ReactiveComponent"))
				c = new ReactiveComponentStub("", ipAdd, port);
			else if (type.equals ("ComponentServer"))
				c = new ComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else if (type.equals ("ReactiveComponentServer"))
				c = new ReactiveComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else {
				//m_tLog.error("Child not found");
				System.out.println("Child not found");
				return c;
			}
				
			return c;
		}
		
		public Component ptRemoveChild(Component comp)
		{
			 if(comp!=null){
				 return ptRemoveChild(comp.szGetComponentName());
			 }else{
				 return comp;
			 }
		}

		public String szGetID()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetID", ptReply);

			if (err != 0)//SRI_OK) 
				return "";
			else return ptReply.toString();
		}
		
		/** returns a descriptive label of the type of component */
		public String szGetComponentType()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetComponentType", ptReply);

			if (err != 0)//SRI_OK) 
				return "";
			else return ptReply.toString();
		}
		
		/** \returns returns fully qualified name including namespace */
		public String szGetName()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetName", ptReply);

			if (err != 0)//SRI_OK) 
				return ""; //old name
			else return ptReply.toString();
		}
		
		/** \returns returns only the current namespace */
		public String szGetNameSpace()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetNameSpace", ptReply);

			if (err != 0)//SRI_OK) {
				{
				//Logger l(m_tLog);
				//l.error("Failed to read definition, err code: %d", err);
				System.out.println("Failed to read definition, err code: %d " + err);
				return "";
			}

			else return ptReply.toString();
		}
		
		/** \returns returns just the name of the component without the namespace */
		public String szGetComponentName()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetComponentName", ptReply);

			if (err != 0){//SRI_OK) {
				//Logger l(m_tLog);
				//l.error("Failed to read definition, err code: %d", err);
				System.out.println("Failed to read definition, err code: %d "+ err);
				return "";
			}

			else return ptReply.toString();
		}
		
		/** The function sets the fully qualified name of the component. The name is parsed
		* to seperate namespace from component name and sets both values accordingly*/
		public int iSetName1(String name)
		{
			Vector<String> args=new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iSetName", args, ptReply);

			if (err != 0)//SRI_OK)
				return err;	
				
			int retval;
			StringBuffer ss=new StringBuffer(ptReply);
			retval=Integer.parseInt(ss.toString());
			return retval;
		}

		/** Components should ALWYAS set their type in the constructor. The type string should match the
		* type string that is given by the factory. The Factory can set the type
		* of the component during construction if a configuration deserves a specific type name. */
		public int iSetComponentType1(String type)
		{
			Vector<String> args=new Vector<String>();
			args.add(type);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iSetComponentType", args, ptReply);

			if (err != 0)//SRI_OK)
				return err;	
				
			return Integer.parseInt(ptReply.toString());
		}

		
		public  ComponentStatus eGetStatus()
		{
			StringBuffer ptReply = new StringBuffer();
			ComponentStatus comsta=null;
			int err = szCallFunction("eGetStatus", ptReply);
			//System.out.println("THE COMSTA IS "+ptReply.toString());
			if (err != 0)//SRI_OK) 
				return ComponentStatus.SRI_FAILED;
			if(ptReply.toString().equals("SRI_FAILED"))
			{comsta=ComponentStatus.SRI_FAILED;}
			else if (ptReply.toString().equals("SRI_STOPPED"))
			{
				comsta=ComponentStatus.SRI_STOPPED;
			}
			else if (ptReply.toString().equals("SRI_RUNNING"))
			{
				comsta=ComponentStatus.SRI_RUNNING;
			}
			else if (ptReply.toString().equals("SRI_INITIALIZED"))
			{
				comsta=ComponentStatus.SRI_INITIALIZED;
			}
			else if (ptReply.toString().equals("SRI_PAUSED"))
			{
				comsta=ComponentStatus.SRI_PAUSED;
			}
			else if (ptReply.toString().equals("SRI_FINALIZED"))
			{
				comsta=ComponentStatus.SRI_FINALIZED;
			}
			return comsta;
		}
		
		public void vSetStatus(ComponentStatus status)
		{
			StringBuffer ptReply = new StringBuffer();
			String s=new String();
			if(status.toString()=="SRI_FAILED")
			{s="-1";}
			else if (status.toString().equals("SRI_STOPPED"))
			{
				{s="0";}
			}
			else if (status.toString().equals("SRI_RUNNING"))
			{
				{s="1";}
			}
			else if (status.toString().equals("SRI_INITIALIZED"))
			{
				{s="2";}
			}
			else if (status.toString().equals("SRI_PAUSED"))
			{
				{s="3";}
			}
			else if (status.toString().equals("SRI_FINALIZED"))
			{
				{s="4";}
			}
				
			//StringBuffer ss=new StringBuffer(status.toString());
			//ss << static_cast<int>(status);
			//String s=ss.toString();

			Vector<String> args=new Vector<String>();
			args.add(s);
			szCallFunction("vSetStatus", args, ptReply);
		}
		
		public Definition ptGetDefinition()
		{
			Definition cd=new Definition();

			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("ptGetDefinition", ptReply);
			if (err != 0)//SRI_OK) 
				return cd;

			cd = new ComponentDefinition();

			err = cd.iFromString((ptReply.toString()));

			if (err != 0) {//SRI_ok
				//Logger l(m_tLog);
				//l.error("Failed to read definition, err code: %d", err);
				System.out.println("Failed to read definition, err code: %d "+ err);
				//cd.vRelease();//Java don't need this
				
			}

			return cd;
		}
		
		public String szGetDefinition()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("ptGetDefinition", ptReply);
			if (err !=0){ 
				System.out.println("Network error: %d "+ err);
				return "";
			}
			if(ptReply!=null){
				return ptReply.toString();
			}

			return "";
		}

		/** A component overwriting this function must call the base class implementation 
		* Baseclass implementation sets the status of the component to "INITIALIZED" and makes sure that all 
		* children initialize. (if this behaviour is not desired for children, the component can simply
		* maintain its own list of component children)
		*/
		public void vInit()
		{
			StringBuffer ptReply = new StringBuffer();
			szCallFunction("vInit",ptReply );
		}
		/** A component overwriting this function must call the base class implementation.
		* Baseclass implementation sets the status of the component to "STOPPED" and makes sure that all 
		* children finalize.   (if this behaviour is not desired for children, the component can simply
		* maintain its own list of component children)
		*/
		public void vFinalize()
		{
			StringBuffer ptReply = new StringBuffer();
			szCallFunction("vFinalize", ptReply);
		}
		
		public boolean bHasMoreSteps()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("bHasMoreSteps", ptReply);
			if (err != 0){//SRI_OK) {
				return false;
			}
			
			else {
				if (ptReply.toString().equals("true")) 
					return true;
				else return false;
			}
		}
		
		public boolean vStep()
		{
			StringBuffer ptReply = new StringBuffer();
			szCallFunction("vStep", ptReply);
			return true;
		}
		
		public boolean vPreStep()
		{
			StringBuffer ptReply = new StringBuffer();
			szCallFunction("vPreStep", ptReply);
			return true;
		}
		
		public boolean vPostStep()
		{
			StringBuffer ptReply = new StringBuffer();
			szCallFunction("vPostStep", ptReply);
			return true;
		}

		//END from Component
		public void vShutdownRemote()
		{
			m_ptStubTemplate.vShutdownRemote();
		}
		

	
	
}
