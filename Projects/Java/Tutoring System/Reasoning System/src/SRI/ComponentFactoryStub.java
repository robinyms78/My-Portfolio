package SRI;

import java.io.InputStreamReader;
import java.io.StringWriter;
import java.util.Vector;

import javax.xml.transform.stream.StreamResult;

public class ComponentFactoryStub extends ComponentFactory {

	

	/// A ComponentFactoryStub is a local (to the engine/registry) representation of a remote ComponentFactory
	/** ComponentFactoryStubs provide allow the engine/registry to access the services of a 
		remotely running ComponentFactory. When ptCreateComponent is called, the stub communicates
		with its associated ComponentFactoryServer, receives the port number of the newly created
		ComponentServer/ReactiveComponentServer, creates a new ComponentStub/ReactiveComponent stub that
		connects to the newly created servers, and returns the ComponentStub/ReactiveComponent stub to
		the caller of ptCreateComponent.
	*/ 

	


		private StubTemplate m_ptStubTemplate;
		private String m_szPeerIp;

		private int szCallFunction(String funcName, Vector<String> args, StringBuffer retstring) 
		{
			int err=0;
			err = m_ptStubTemplate.szCallFunction(funcName, args, retstring);
			if (err != 0){//SRI_OK) {
				//Logger tempLogger("ComponentFactoryStub");
				////tempLogger.error("%s caused network error %d. invoking removal", funcName.c_str(), err); //TODO get error name
				System.out.println(" caused network error %d. invoking removal"+ funcName+ err);
				//TODO: invoke callback removal
			}
			return err;
		}


	
	
		public ComponentFactoryStub(String factName, String ip, int portNo, String config )
		{
			
			super(factName,"");
			config = "";
			
			m_szPeerIp=ip;
			
			vSetComponentType("ComponentFactoryStub");
			m_ptStubTemplate = new StubTemplate(ip, portNo);
		}
		
		//***ComponentFactory
		public  Component ptCreateComponent(String name, String config )
		{
			config="";
			Vector<String> args = new Vector<String>();
			args.add(name);
			args.add(config);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("ptCreateComponent", args, ptReply);

			if (err != 0) {
				System.out.println("network error %d encountered"+ err);
				//m_tLog.error("network error %d encountered", err);
				return null;
			}
			
			String type = "";
			int port = 0;
			
			
				
			StringBuffer s=new StringBuffer();
			s.append(ptReply);
			int ind1=s.indexOf(" ", 0);
			type=s.substring(0, ind1);
			
			port=Integer.parseInt(s.substring(ind1+1));
		
			

			String sriType=type;
			
			//m_tLog.debug("type: %s\tport:%d", sriType.c_str(), port);
			System.out.println("type: %s\tport:%d"+ sriType+ port);
			Component comp = null;
			
			
			if(sriType.equals ("SRIComponentNameString")) {
				System.out.println("Creating ComponentStub\n");
			//	m_tLog.debug("Creating ComponentStub\n");
				comp = new ComponentStub(name, m_szPeerIp, port);
			}
			else if(sriType.equals("SRIReactiveComponentNameString")) {
				//m_tLog.debug("Creating ReactiveComponentStub\n");
				System.out.println("Creating ReactiveComponentStub\n");
				comp = new ReactiveComponentStub(name, m_szPeerIp, port);
			}
			else {
				System.out.println("Unrecognised type %s\n"+ sriType);
				//m_tLog.error("Unrecognised type %s\n", sriType.c_str());
			}
			
			return comp;
		}
		
		
		public void vSetComponentType(String typeId)
		{
			Vector<String> args = new Vector<String>();
			args.add(typeId);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("vSetComponentType", args, ptReply);

			if (err != 0) {//SRI_OK
				//m_tLog.error("network error %d encountered", err);
				System.out.println("network error %d encountered"+ err);
				return;
			}	
		}
		
		//TODO: calling logger in const
		public int iSetName(String name)
		{
			Vector<String> args = new Vector<String>();
			args.add(name);
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("iSetName", args, ptReply);

			if (err !=0) {//SRI_OK
				//m_tLog.error("network error %d encountered", err);
				System.out.println("network error %d encountered"+ err);
				return err;
			}
			return Integer.parseInt(ptReply.toString());
			//return atoi(ptReply);
		}
		
		public String szGetName()
		{
			
			Vector<String> args = null;
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetName", args, ptReply);

			if (err != 0) {//SRI_OK
				//Logger tempLog(m_tLog);
				//String errmsg ="";
				String errmsg=("network error %d encountered "+ err);
				//tempLog.error(errmsg);
				return errmsg;
			}

			return (ptReply.toString());
		}
		
		public String szGetComponentType()
		{
			Vector<String> args = null;
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetComponentType", args, ptReply);

			if (err != 0) {//SRI_OK
				//Logger tempLog(m_tLog);
				//String errmsg = null;
				String errmsg=("network error %d encountered "+ err);
				//tempLog.error(errmsg);
				return errmsg;
			}

			return (ptReply.toString());
		}
		
		public String szGetConfig()
		{
			Vector<String> args = null;
			StringBuffer ptReply = new StringBuffer();
			int err = szCallFunction("szGetConfig", args, ptReply);

			if (err != 0) {//SRI_OK
				//Logger tempLog(m_tLog);
				//String errmsg = null;
				String errmsg=("network error %d encountered "+ err);
				//tempLog.error(errmsg);
				return errmsg;
			}

			return (ptReply.toString());
		}
		//returns handle in same address space. is ok because the registry is a singleton across the entire system
		//so not overridden
		//virtual SRI::RegistryHandle* ptGetRegistryHandle() const;

		public  ComponentDefinition tGetComponentDefinition(String config)// holds a definition (contract) of what type of components will be produced
		{
		ComponentDefinition cd=new ComponentDefinition();
		
		Vector<String> args=new Vector<String>();
		args.add(config);
		StringBuffer ptReply = new StringBuffer();
		int err = szCallFunction("tGetComponentDefinition", args, ptReply);

		if (err != 0) {
			//m_tLog.error("network error %d encountered", err);
			System.out.println("network error %d encountered "+ err);
			return cd;
		}

		cd.vSetConfig((ptReply.toString()));
		
		return cd;
		
		}
		
	


		///Sends shutdown signal to remote server
		public void vShutdownRemote()
		{
			m_ptStubTemplate.vShutdownRemote();
		}


	
	
	
}
