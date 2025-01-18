package SRI;

import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;
import java.util.Vector;
import java.util.Map.Entry;

public class ComponentStub extends Component{

	

	/// A ComponentStub is a local (to the engine/registry) representation of a remote Component
	/** ComponentStubs provide allow the engine/registry to access the services of a 
		remotely running Component. When the ComponentStub is deleted, the memory of the
		remote Component is automatically reclaimed.
	*/ 

	//class SRI_E_API ComponentStub : public Component{
		//friend class SRIEngine; //sets the ID of the module

	//private:
	private StubTemplate m_ptStubTemplate;
	
	private int szCallFunction(String funcName, Vector<String> args, StringBuffer retstring)
	{
		int err = m_ptStubTemplate.szCallFunction(funcName, args, retstring);
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

	private String m_szCachedName; //name of the component

	//protected:

		
		//SRI::Ref<EngineHandle> m_ptEngineHandle;

		/** This function is called by the engine after the initialization of the component*/
		protected void vSetId(String id)
		{
			
		}
		
		protected int iSetNameSpace(String name)
		{
			Vector<String> args = new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iSetNameSpace", args, ptReply);
			
			if (err != 0)//SRI_OK 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d "+ err);
			return err;
		}

		//Logger m_tLog;

	/*
		SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mChildComponents;
		SRI::Ref<SRI::Component> m_ptParent;

		SRI::Ref<ComponentDefinition> m_ptComponentDefinition;*/

		protected HashMap<String,Component> m_mParentServers;
		
			
		//keeps parent servers alive

		/** Creates a copy and sets the copy*/
		protected void vSetDefinition( Definition def)
		{
			Vector<String> args=new Vector<String>();
			args.add(def.toString());
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("vSetDefinition", args, ptReply);
			
			if (err != 0) //SRI_OK
				//m_tLog.error("Network error: %d", err);
			System.out.println("Network error: %d "+ err);
		}
		/** Sets the definition directly */
		//protected void vSetDefinition(Definition ptDef)
		//{
			//duplicated for java
		//}

	//public:
		public ComponentStub(String name, String ip, int portNo)
		{
			//ComponentStub::ComponentStub(SRI::String name, SRI::String ip, int portNo):Component(name),
			//m_tLog("ComponentStub", LOG_DEBUG) {
			super(name);
			System.out.println("ComponentStub");
			m_ptStubTemplate = new StubTemplate(ip, portNo);
			m_szCachedName = szGetName(); //temp remark by chin for Java server C++ client testing
	//	}
		}
		//virtual ~ComponentStub();

		//ComponentStub(const ComponentStub& c);
		//ComponentStub& operator=(const ComponentStub& c);

		public String szGetPeerIp()
		{
			return m_ptStubTemplate.szGetPeerIp();
		}//TODO: think of refactoring stubs
		
		public int iGetPeerPort()
		{
			return m_ptStubTemplate.iGetPeerPort();
		}

		//bool operator==(const Component& c);

		public  int iSetEngineHandle(SRIEngineStub handle)//Handle is replace by enginestub in java
		{
			String engAddr = handle.ptGetStubTemplate().szGetMyIp();

			if (engAddr == "") {
				//m_tLog.error("iSetEngineHandle: engine does not have a server running!");
				System.out.println("iSetEngineHandle: engine does not have a server running!");
				return 1;//SRI_ERR;
			}

			Vector<String> args=new Vector<String>();
			args.add(engAddr);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iSetEngineHandle", args, ptReply);
			
			if (err != 0)//SRI_OK) 
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d"+ err);
			return (Integer.parseInt(ptReply.toString()));
		}//engine should be started with ip add if required =)
		
		public SRIEngineStub ptGetEngineHandle()//Engine handle is replace by engine stub in Java
		{
			//TODO:return an engine handle that is connected to the same engine
			SRIEngineStub engHandle=new SRIEngineStub("",0,"");
			
			Vector<String> args=new Vector<String>();
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("ptGetEngineHandle", args, ptReply);

			if (err != 0) {//SRI_OK
				//m_tLog.error("Network error: %d", err);
				System.out.println("Network error: %d"+ err);
				return engHandle;
			}

			StringBuffer ss=new StringBuffer();
			ss.append(ptReply);
			String ip;
			int port = 0;
			ip=ss.toString();
			//port=
			//ss >> ip >> port;
			
			//I do not need to implement the Engine???
			SRIEngineStub engStub = new SRIEngineStub( ip, port,szGetName());
			//engHandle = new EngineHandle(engStub);
			engHandle=engStub;

			return engHandle;
		}

		public int iSetParent(Component newParent)
		{
			Component c = newParent;
			ComponentStub cs1=null;
			ReactiveComponentStub rcs=null;
			ComponentServer cse=null;
			ReactiveComponentServer rcss=null;
			
			String ip, type;
			int port;


			if (c == null) {
				ip = "NULL";
				port = 0;
				type = "NULL";
			}
			
			else if (c.getClass().isInstance(cs1) ) {
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
						Thread.sleep(1000);
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					port = cs.iGetServerPort();
					type = "Component";
					newServ = cs;
					
				}
				else {
					ReactiveComponentServer rcs1 = new ReactiveComponentServer(rc);
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
					type = "ReactiveComponent";
					newServ = rcs;
				}

				

				assert(newServ!=null);
				
				 Set<Entry<String, Component>> s = m_mParentServers.entrySet();
		         Iterator<Entry<String, Component>> i = s.iterator();
		         while (i.hasNext()) {
		             
		        	 if(i.next().getKey()==(newServ.szGetComponentName()))
		        	 {	
		        		 
		        		 i.next().setValue(newServ);
		        	 }
		         }
				//}
				//m_mParentServers.get(newServ.szGetComponentName())= newServ;
				//m_mParentServers[Integer.parseInt(newServ.szGetComponentName())] = newServ; //data will be overwritten later

				SRIEngineStub eh = newParent.ptGetEngineHandle();

				if (eh!=null) { //if this component is registered to an engine
					String loop = eh.szGetLoopLabel(newParent.szGetName());
					//m_tLog.critical("%s\n", loop.c_str());
					eh.vRemoveComponent(newParent.szGetName());
					eh.iAddComponent(newServ, loop);
				}

				
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
			Component c = comp;
			ComponentStub cs1=null;
			ReactiveComponentStub rcs=null;
			ComponentServer cse=null;
			ReactiveComponentServer rcss=null;
			
			String ip, type;
			int port;


			if (c == null) {
				ip = "NULL";
				port = 0;
				type = "NULL";
			}
			
			else if (c.getClass().isInstance(cs1) ) {
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
						Thread.sleep(1000);
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					port = cs.iGetServerPort();
					type = "Component";
					newServ = cs;
					
				}
				else {
					ReactiveComponentServer rcs1 = new ReactiveComponentServer(rc);
					try {
						rcs1.vStartServer(0);
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					port = rcs1.iGetServerPort();
					type = "ReactiveComponent";
					newServ = rcs;
				}

				

				assert(newServ!=null);
				
				 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
		         Iterator<Entry<String, Component>> i = s.iterator();
		         while (i.hasNext()) {
		             
		        	 if(i.next().getKey()==(newServ.szGetComponentName()))
		        	 {	
		        		 
		        		 i.next().setValue(newServ);
		        	 }
		         }
				//}
				//m_mParentServers.get(newServ.szGetComponentName())= newServ;
				//m_mParentServers[Integer.parseInt(newServ.szGetComponentName())] = newServ; //data will be overwritten later

				SRIEngineStub eh = comp.ptGetEngineHandle();

				if (eh!=null) { //if this component is registered to an engine
					String loop =  comp.ptGetEngineHandle().szGetLoopLabel(comp.szGetName());

					comp.ptGetEngineHandle().vRemoveComponent(comp.szGetName());
					comp.ptGetEngineHandle().iAddComponent(newServ, loop);
				}

				
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

			String sriType=type;
			String ipAdd=ip;

			if (type == "Component") 
				c = new ComponentStub("", ipAdd, port);
			else if (type == "ReactiveComponent")
				c = new ReactiveComponentStub("", ipAdd, port);
			else if (type == "ComponentServer")
				c = new ComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else if (type == "ReactiveComponentServer")
				c = new ReactiveComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else {
				//m_tLog.error("Child not present");
				System.out.println("Child not present");
				return c;
			}
				
			return c;

		}
		
		public  Component ptGetParent()
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

			String sriType=type;
			String ipAdd=ip;

			if (type == "Component") 
				c = new ComponentStub("", ipAdd, port);
			else if (type == "ReactiveComponent")
				c = new ReactiveComponentStub("", ipAdd, port);
			else if (type == "ComponentServer")
				c = new ComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else if (type == "ReactiveComponentServer")
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

			if (type == "Component") 
				c = new ComponentStub("", ipAdd, port);
			else if (type == "ReactiveComponent")
				c = new ReactiveComponentStub("", ipAdd, port);
			else if (type == "ComponentServer")
				c = new ComponentStub("", m_ptStubTemplate.szGetPeerIp() ,port);
			else if (type == "ReactiveComponentServer")
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
				return m_szCachedName; //old name
			else return ptReply.toString();
			//TODO: this is const function, how to save the cached name?
			//remove cached name function
			/*else {
				SRI::String newName = *(ptReply.ptGetObj());
				m_szCachedName = newName;
				return newName;
			}*/
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

			else return (ptReply.toString());
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

			else return (ptReply.toString());
		}
		
		/** The function sets the fully qualified name of the component. The name is parsed
		* to seperate namespace from component name and sets both values accordingly*/
		public int iSetName(String name)
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
		public int iSetComponentType(String type)
		{
			Vector<String> args=new Vector<String>();
			args.add(type);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iSetComponentType", args, ptReply);

			if (err != 0)//SRI_OK)
				return err;	
				
			return Integer.parseInt(ptReply.toString());
		}

		public Component ptClone()
		{
			ComponentStub cs = this;
			return cs;
		}
		
		public ComponentStatus eGetStatus()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("eGetStatus", ptReply);
			if (err != 0)//SRI_OK) 
				return ComponentStatus.SRI_FAILED;
			return ComponentStatus.SRI_RUNNING;
					//static_cast<ComponentStatus>(atoi(ptReply.ptGetObj()->c_str()));
			
			//TODO only return network error? how to differentiate?
		}
		
		public void vSetStatus(ComponentStatus status)
		{
			StringBuffer ptReply = new StringBuffer();

			StringBuffer ss=new StringBuffer(status.toString());
			//ss << static_cast<int>(status);
			String s=ss.toString();

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

		/** A component overwriting this function must call the base class implementation 
		* Baseclass implementation sets the status of the component to "INITIALIZED" and makes sure that all 
		* children initialize. (if this behaviour is not desired for children, the component can simply
		* maintain its own list of component children)
		*/
		public void vInit()
		{
			szCallFunction("vInit", null);
		}
		
		/** A component overwriting this function must call the base class implementation.
		* Baseclass implementation sets the status of the component to "STOPPED" and makes sure that all 
		* children finalize.   (if this behaviour is not desired for children, the component can simply
		* maintain its own list of component children)
		*/
		public void vFinalize()
		{
			szCallFunction("vFinalize", null);
		}
		
		public boolean bHasMoreSteps()
		{
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("bHasMoreSteps", ptReply);
			if (err != 0){//SRI_OK) {
				return false;
			}
			
			else {
				if (ptReply.toString()== "true") 
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

		public void vShutdownRemote()
		{
			m_ptStubTemplate.vShutdownRemote();
		}


	
	
	
}
