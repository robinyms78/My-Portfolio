package SRI;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;

public class ReactiveComponent extends Component {
	
	
		//A component owns its ports (memory must be released = handles by smartpointers)
		protected HashMap<String, InputPort> m_mInputPorts=new HashMap<String, InputPort>();
		protected HashMap<String, OutputPort> m_mOutputPorts=new HashMap<String, OutputPort>();;

		protected HashMap<String, InputPort> m_mPrivateInputPorts=new HashMap<String, InputPort>();;
		protected HashMap<String, OutputPort> m_mPrivateOutputPorts=new HashMap<String, OutputPort>();;

		/** Called during PostStep to add all pending sockets to appropriate output ports **/
		protected int iProcessPendingSockets()
		{
			return 0;
		}
		/***DEPRECATED***/

		/** Adds a new port to the component. Memory is taken over. That means that the 
		memory becomes invalid after this function call.*/
		protected int iAddInputPort(InputPort port)
		{
			if(port == null){
				
				
				System.out.println("Unable to add input port. Got NULL pointer");//TODO: throw nullpointer exception?
				return 0;// SRI_ERR_NULL;
			}

			if( m_mInputPorts.containsKey(port.szGetName())){
				
				System.out.println("Unable to add input port %s. Port already exists"+ port.szGetName());
			
				return 1;// SRI_ERR_NAMECONFLICT; //TODO: throw exception of double port naming?
			}

			m_mInputPorts.put(port.szGetName(),port) ;
			//Ref<ComponentDefinition> def = ptGetDefinition();
			//if(def.bIsValid()){
				//def->iAddInputPortDefinition(port->tGetPortDefinition());
			//}
			System.out.println("The added input port name is "+port.szGetName());
			return 0;// SRI_OK;
		}
		/** Adds a new OutputPort to the component. Memory is taken over. That means that the 
		memory becomes invalid after this function call.*/
		protected int iAddOutputPort(OutputPort port)
		{

			if(port == null){
			
				
				System.out.println("Unable to add output port. Got NULL pointer");//TODO: throw nullpointer exception?
				return 0;// SRI_ERR_NULL;
			}

			if( m_mOutputPorts.containsKey(port.szGetName())){
				
				System.out.println("Unable to add output port %s. Port already exists"+ port.szGetName());
				
				return 1;// SRI_ERR_NAMECONFLICT; //TODO: throw exception of double port naming?
			}

			m_mOutputPorts.put(port.szGetName(),port) ;
			//Ref<ComponentDefinition> def = ptGetDefinition();
			//if(def.bIsValid()){
				//def->iAddInputPortDefinition(port->tGetPortDefinition());
			//}

			return 0;// SRI_OK;
			
		}

		/** Adds a new port to the component. Memory is taken over. That means that the 
		memory becomes invalid after this function call.*/
		protected int iAddPrivateInputPort(InputPort port)
		{

			if(port == null){
				
				
				System.out.println("Unable to add private input port. Got NULL pointer");//TODO: throw nullpointer exception?
				return 0;// SRI_ERR_NULL;
			}

			if( m_mPrivateInputPorts.containsKey(port.szGetName())){
				
				System.out.println("Unable to add private input port %s. Port already exists"+ port.szGetName());
			
				return 1;// SRI_ERR_NAMECONFLICT; //TODO: throw exception of double port naming?
			}

			m_mPrivateInputPorts.put(port.szGetName(),port) ;
			//Ref<ComponentDefinition> def = ptGetDefinition();
			//if(def.bIsValid()){
				//def->iAddInputPortDefinition(port->tGetPortDefinition());
			//}

			return 0;// SRI_OK;
		}
		/** Adds a new OutputPort to the component. Memory is taken over. That means that the 
		memory becomes invalid after this function call.*/
		protected int iAddPrivateOutputPort(OutputPort port)
		{
			
			if(port == null){
				
				
				System.out.println("Unable to add private output port. Got NULL pointer");//TODO: throw nullpointer exception?
				return 0;// SRI_ERR_NULL;
			}

			if( m_mPrivateOutputPorts.containsKey(port.szGetName())){
				
				System.out.println("Unable to add private output port %s. Port already exists"+ port.szGetName());
				
				return 1;// SRI_ERR_NAMECONFLICT; //TODO: throw exception of double port naming?
			}

			m_mPrivateOutputPorts.put(port.szGetName(),port) ;
			System.out.println("IN HERE "+m_mPrivateOutputPorts.size());
			//Ref<ComponentDefinition> def = ptGetDefinition();
			//if(def.bIsValid()){
				//def->iAddInputPortDefinition(port->tGetPortDefinition());
			//}

			return 0;// SRI_OK;
			
		}

		protected InputPort ptGetInputPort(String portName)
		{
			if(m_mInputPorts.containsKey(portName)){
				return m_mInputPorts.get(portName);
			}
			return null;
		}
		
		protected OutputPort ptGetOutputPort(String portName)
		{
			
			if(m_mOutputPorts.containsKey(portName)){
				return m_mOutputPorts.get(portName);
			}
			return null;
		}

		protected int iConnectToChildInput(String privateOutPortName, String childName, String childInPortName)
		{
			
			
			
			Component myObject=new ReactiveComponent("");
			 myObject=ptGetChild(childName);
			if(myObject == null){
				
				System.out.println("Unable to connect child %s: Child not found"+ childName);
				return 1;// SRI_ERR_NOT_DEFINED;
			}
		
			ReactiveComponent ptChild=(ReactiveComponent) myObject;
			
			

			if(!m_mPrivateOutputPorts.containsKey(privateOutPortName)){
				
				System.out.println("Unable to connect child input %s-%s: Private out port %s not found"+ childName+ childInPortName+ privateOutPortName);
				return 2;// SRI_ERR_NOT_DEFINED;
			}

			if(!ptChild.bHasInputPort(childInPortName)){//input should at the child not this reactive component
			
				System.out.println("Unable to connect to child input %s: Child input port %s not defined"+ childName+ childInPortName);
				return 3;// SRI_ERR_NOT_DEFINED;
			}

			//Test if child is remote:
			ReactiveComponent ptChildStub =null;
			if (ptChild instanceof ReactiveComponent)
			{
				ptChildStub = (ReactiveComponent)ptChild;
			}
			//ReactiveComponent ptChildStub = (ReactiveComponent)ptChild;
			int res = 0;//SRI_OK;
			
			if(ptChildStub == null){
				//child is local
				Connection connection=new Connection();
				res = m_mPrivateOutputPorts.get(privateOutPortName).iAddConnection(connection);
				if( res != 0){//SRI_OK){
					
					System.out.println("Unable to add connection to private output port: %s"+ privateOutPortName);
					return res;
				}
				
				res = ptChild.iAddInputConnection(childInPortName, connection);
				if(res !=0){// SRI_OK){
					
					System.out.println("Failed to connect to child %s input: Unable to add connection to inputPort %s"+ childName+ childInPortName);
					m_mPrivateOutputPorts.get(privateOutPortName).vRemoveConnection(connection);
					return res;
				}
			}else{ // child is remote
				Connection connection=new Connection();
				ServerSocket ss = null;
				try {
					ss = new ServerSocket(0);
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				int listenPort = ss.getLocalPort();//address().port();
				res = ptChildStub.iAddInputConnection(childInPortName, connection);
				
				if( res != 0){//SRI_OK){
					
					System.out.println("Failed to connect to child %s input: Unable to add connection to inputPort %s"+ childName+ childInPortName);
					return res;
				}

				Socket ptStream = new Socket();
				/*try {
					
					ptStream=ss.accept();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}*/ //temporary remark if not system will keep on stuck at waiting for client to connect
				////Connection ptSendConn=new TCPSendConnection(ptStream);
				////res = m_mPrivateOutputPorts.get(privateOutPortName).iAddConnection(ptSendConn);
				if( res != 0){//SRI_OK){
					System.out.println("Failed to connect to child inpute %s-%s: Unable to add connection to private output port: %s "+ 
						childName+ childInPortName+ privateOutPortName);			
					ptChildStub.iRemoveInputConnection(childInPortName, privateOutPortName);
					return res;
				}
				
			}

			
			return res;
		}
		
		protected int iConnectToChildOutput(String privateInPortName, String childName, String childOutPortName)
		{
			//ReactiveComponent ptChild = (ReactiveComponent)ptGetChild(childName);
			Component myObject=new ReactiveComponent("");
			 myObject=ptGetChild(childName);
			if(myObject == null){
			
				System.out.println("Unable to connect child %s: Child not found"+ childName);
				return 1;// SRI_ERR_NOT_DEFINED;
			}
		
			ReactiveComponent ptChild=(ReactiveComponent)myObject;
			
			
			//if(ptChild == null){
				//m_tLog.error("Unable to connect child %s: Child not found", childName.c_str());
			//	System.out.println("Unable to connect child %s: Child not found"+ childName);
			//	return 1;// SRI_ERR_NOT_DEFINED;
		//	}

			if(!m_mPrivateInputPorts.containsKey(privateInPortName)){
				
				System.out.println("Unable to connect child input %s-%s: Private out port %s not found"+ childName+ childOutPortName+ privateInPortName);
				return 2;// SRI_ERR_NOT_DEFINED;
			}

			if(!ptChild.bHasOutputPort(childOutPortName)){
				
				System.out.println("Unable to connect to child input %s: Child input port %s not defined"+ childName+ childOutPortName);
				return 3;// SRI_ERR_NOT_DEFINED;
			}

			//Test if child is remote:
			ReactiveComponent ptChildStub =null;
			if (ptChild instanceof ReactiveComponent)
			{
				ptChildStub = (ReactiveComponent)ptChild;
			}
			//ReactiveComponent ptChildStub = (ReactiveComponent)ptChild;
			int res = 0;//SRI_OK;

			if(ptChildStub == null){
				//child is local
				Connection connection=new Connection();
				res = m_mPrivateInputPorts.get(privateInPortName).iAddConnection(connection);
				if( res != 0){//SRI_OK){
					
					System.out.println("Unable to add connection to private output port: %s"+ privateInPortName);
					return res;
				}
				res = ptChild.iAddInputConnection(childOutPortName, connection);
				if(res !=0){// SRI_OK){
					
					System.out.println("Failed to connect to child %s input: Unable to add connection to inputPort %s"+ childName+ childOutPortName);
					m_mPrivateInputPorts.get(privateInPortName).vRemoveConnection(connection);
					return res;
				}
			}else{ // child is remote
				Connection connection=new Connection();
				ServerSocket ss = null;
				try {
					ss = new ServerSocket(0);
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				int listenPort = ss.getLocalPort();//address().port();
				res = ptChildStub.iAddOutputConnection(childOutPortName, connection);
				if( res != 0){//SRI_OK){
				
					System.out.println("Failed to connect to child %s input: Unable to add connection to inputPort %s"+ childName+ childOutPortName);
					return res;
				}

				Socket ptStream = new Socket();
				/*
				try {
					ptStream=ss.accept();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}*///temp remark if not the system will stuck waiting for client to connect
				////Connection ptSendConn=new TCPSendConnection(ptStream);
				////res = m_mPrivateOutputPorts.get(privateOutPortName).iAddConnection(ptSendConn);
				if( res != 0){//SRI_OK){
					System.out.println("Failed to connect to child inpute %s-%s: Unable to add connection to private output port: %s "+ 
						childName+ childOutPortName+ privateInPortName);			
					ptChildStub.iRemoveOutputConnection(childOutPortName, privateInPortName);
					return res;
				}
			}


			return res;
		}

		protected int iDisconnectChildInput(String privateOutPortName, String childName, String childInPortName)
		{
			ReactiveComponent ptChild = (ReactiveComponent)(ptGetChild(childName));
			if(ptChild == null){
			
				System.out.println("Unable to disconnect child %s: Child not found"+ childName);
				return 1;// SRI_ERR_NOT_DEFINED;
			}

			if(!m_mPrivateOutputPorts.containsKey(privateOutPortName)){
			
				System.out.println("Unable to disconnect child input %s-%s: Private out port %s not found"+ childName+ childInPortName+ privateOutPortName);
				return 2;//SRI_ERR_NOT_DEFINED;
			}

			if(!ptChild.bHasInputPort(childInPortName)){
			
				System.out.println("Unable to disconnect to child input %s: Child input port %s not defined"+ childName+ childInPortName);
				return 3;// SRI_ERR_NOT_DEFINED;
			}

			return m_mPrivateOutputPorts.get(privateOutPortName).iRemoveConnection(privateOutPortName, childInPortName);
		}


		
		
		protected int iDisconnectChildOutput(String privateInPortName, String childName, String childOutPortName)
		{
			ReactiveComponent ptChild = (ReactiveComponent)(ptGetChild(childName));
			if(ptChild == null){
			
				System.out.println("Unable to disconnect child %s: Child not found"+ childName);
				return 1;// SRI_ERR_NOT_DEFINED;
			}

			if(!m_mPrivateInputPorts.containsKey(privateInPortName)){
			
				System.out.println("Unable to disconnect child input %s-%s: Private out port %s not found"+ childName+ childOutPortName+ privateInPortName);
				return 2;//SRI_ERR_NOT_DEFINED;
			}

			if(!ptChild.bHasOutputPort(childOutPortName)){
				
				System.out.println("Unable to disconnect to child input %s: Child input port %s not defined"+ childName+ childOutPortName);
				return 3;// SRI_ERR_NOT_DEFINED;
			}

			return m_mPrivateInputPorts.get(privateInPortName).iRemoveConnection(childOutPortName,privateInPortName);
		}

	//public:
			
		public ReactiveComponent(String name)
		{
			super(name);
			
				System.out.println("ReactiveComponent" + name);
				this.iSetComponentType("ReactiveComponent");
				
				
				
		}
	

		/** After copy the IP address must be reset*/
		

		// =================== Public Port =============================================================
		
		public int iCreateOutputPort(String name, String type)
		{
			OutputPort port = new OutputPort(name, type);
			int res = iAddOutputPort(port);//shld return 0
			return res;
		}
		
		public int iCreateInputPort(String name,String type)
		{
			InputPort port = new InputPort(name, type);
			int res = iAddInputPort(port);
			return res;
			
		}

		public void vRemoveOutputPort(String name)
		{
			if (m_mOutputPorts.containsKey(name)){
				if( m_mOutputPorts.get(name)!=null){
					m_mOutputPorts.get(name).vFinalize();
				}
				m_mOutputPorts.remove(name);
				//Ref<ComponentDefinition> def = ptGetDefinition();
				//if(def.bIsValid()){
					//def->iRemoveOutputPortDefeinition(name);
				//}
			}
		}
		
		public void vRemoveInputPort(String name)
		{
			if (m_mInputPorts.containsKey(name)){
				if( m_mInputPorts.get(name)!=null){
					m_mInputPorts.get(name).vFinalize();
				}
				m_mInputPorts.remove(name);
				//Ref<ComponentDefinition> def = ptGetDefinition();
				//if(def.bIsValid()){
					//def->iRemoveOutputPortDefeinition(name);
				//}
			}
		}

		public boolean bHasInputPort(String inport)
		{
			return m_mInputPorts.containsKey(inport); 
			
		}
		
		public boolean bHasOutputPort(String outport)
		{
			return m_mOutputPorts.containsKey(outport); 
		}

		public String szGetOutputPortAddress(String outport)
		{
			//TODO: Implement remove address
			return "local";
		}
		
		public String szGetInputPortAddress(String inport)
		{
			//TODO: Implement remove address
			return "local";
		}
		
		/** Adds connection object to the specified output port*/
		public int iAddOutputConnection(String outport, Connection connection)
		{
			if(!m_mOutputPorts.containsKey(outport)){
			
				System.out.println("Unable to add connection to port %s: No such port available"+ outport);
				return 1;// SRI_ERR_NOT_DEFINED;
			}
			//System.out.println("TESTTSS");
			return m_mOutputPorts.get(outport).iAddConnection(connection);
		}
		
		/** Adds connection object to the specified input port*/
		public int iAddInputConnection(String inport, Connection connection)
		{
			if(!m_mInputPorts.containsKey(inport)){
			
				System.out.println("Unable to add connection to port %s: No such port available"+ inport);
				return 1;// SRI_ERR_NOT_DEFINED;
			}
			return m_mInputPorts.get(inport).iAddConnection(connection);
		}

		public int iRemoveOutputConnection(String outport, String inport)
		{
			if(!m_mOutputPorts.containsKey(outport)){
			
				System.out.println("Unable to remove connection from outport %s: No such port available"+ outport);
				return 1;//SRI_ERR_NOT_DEFINED;
			}
			//System.out.println("OUTPORT NAME IS "+outport);
			return m_mOutputPorts.get(outport).iRemoveConnection(outport, inport);
		}
		
		public int iRemoveInputConnection(String inport, String outport)
		{
			if(!m_mInputPorts.containsKey(inport)){
				
					System.out.println("Unable to remove connection from outport %s: No such port available"+ inport);
					return 1;//SRI_ERR_NOT_DEFINED;
				}

				return m_mInputPorts.get(inport).iRemoveConnection(outport, inport);
			
		}

		
		public int iRemoveOutputConnection(String outport, Connection connection)
		{
		
				if(!m_mOutputPorts.containsKey(outport)){
					
					System.out.println("Unable to remove connection to port %s: No such port available"+ outport);
					return 1;// SRI_ERR_NOT_DEFINED;
				}
				m_mOutputPorts.get(outport).vRemoveConnection(connection);
				return 0;// SRI_OK;
		}
		
		public int iRemoveInputConnection(String inport, Connection connection)
		{
			if(!m_mInputPorts.containsKey(inport)){
			
				System.out.println("Unable to remove connection to port %s: No such port available"+ inport);
				return 1;// SRI_ERR_NOT_DEFINED;
			}
			m_mInputPorts.get(inport).vRemoveConnection(connection);
			return 0;// SRI_OK;
		}

		

		/** Returns a list of ports in the format: Name, Type*/
		public HashMap<String, String> mGetInputPortList()
		{
			HashMap<String, String> ports = new HashMap<String, String>();
			Set<Entry<String, InputPort>> s = m_mInputPorts.entrySet();
	         Iterator<Entry<String, InputPort>> i = s.iterator();
	         while (i.hasNext()) {
			
				InputPort in = (InputPort) i.next().getValue();
				if(in!=null){
					ports.put(in.szGetName(), in.szGetPortDataType());
				}
			}
			return ports;
			
		}
		
		public HashMap<String, String> mGetOutputPortList()
		{
			HashMap<String, String> ports = new HashMap<String, String>();
		
			Set<Entry<String, OutputPort>> s = m_mOutputPorts.entrySet();
	         Iterator<Entry<String, OutputPort>> i = s.iterator();
	         while (i.hasNext()) {
	        	 
				OutputPort out =   i.next().getValue();
				if(out!=null){
					ports.put(out.szGetName(), out.szGetPortDataType());
				}
			}
			return ports;
		}

		/** Returns a list of ports encoded in an xml string */
		public String szGetInputPorts()
		{
			String inputPorts = "<InputPorts>";
			Set<Entry<String, InputPort>> s = m_mInputPorts.entrySet();
	         Iterator<Entry<String, InputPort>> i = s.iterator();
	         while (i.hasNext()) {
	        	 InputPort in= i.next().getValue();
	        	 if(in!=null)
	        	 {
	        		 
	        		// PortDefinition def = in.tGetPortDefinition();//temprem
						//inputPorts += def.toString();// temprem
	        		 		inputPorts+=in.m_szName;
	        	 }
	         }
			//for(SRI::MapIterator<SRI::String, Ref<InputPort>> it = m_mInputPorts.begin(); it!= m_mInputPorts.end(); it++){
				//Ref<InputPort>& in = it.second();
				//if(in.bIsValid()){
					//PortDefinition def = in->tGetPortDefinition();
					//inputPorts += def.szToString();
				//}
			//}
			inputPorts += "</InputPorts>";
			
			return inputPorts;
		}
		/** Returns a list of ports encoded in an XML string */
		public String szGetOutputPorts()
		{
			String outputPorts = "<OutputPorts>";
			Set<Entry<String, OutputPort>> s = m_mOutputPorts.entrySet();
	         Iterator<Entry<String, OutputPort>> i = s.iterator();
	         while (i.hasNext()) {
	        	 OutputPort out=(OutputPort) i.next().getValue();
	        	 if(out!=null)
	        	 {
	        		 //PortDefinition def = out.tGetPortDefinition();
						//outputPorts += def.toString();
	        		 outputPorts+=out.m_szName;
	        	 }
	         }
			//for(SRI::MapIterator<SRI::String, Ref<InputPort>> it = m_mInputPorts.begin(); it!= m_mInputPorts.end(); it++){
				//Ref<InputPort>& in = it.second();
				//if(in.bIsValid()){
					//PortDefinition def = in->tGetPortDefinition();
					//inputPorts += def.szToString();
				//}
			//}
			outputPorts += "</OutputPorts>";
			return outputPorts;
		}

		// =================== Private Port =============================================================
		public int iCreatePrivateOutputPort(String name, String type)
		{
			OutputPort port = new OutputPort(name, type);
			int res = iAddPrivateOutputPort(port);
			port = null; //port was taken over
			return res;
		}
		
		public int iCreatePrivateInputPort(String name, String type)
		{
			InputPort port = new InputPort(name, type);
			int res = iAddPrivateInputPort(port);
			port = null; // memory was taken over
			return res;
		}

		public void vRemovePrivateOutputPort(String name)
		{
			if( m_mPrivateOutputPorts.containsKey(name)){
				if(m_mPrivateOutputPorts.get(name)!=null){
					m_mPrivateOutputPorts.get(name).vFinalize();
				}
				m_mPrivateOutputPorts.remove(name);
			}
			
		}
		
		public void vRemovePrivateInputPort(String name)
		{
			if( m_mPrivateInputPorts.containsKey(name)){
				if(m_mPrivateInputPorts.get(name)!=null){
					m_mPrivateInputPorts.get(name).vFinalize();
				}
				m_mPrivateInputPorts.remove(name);
			}
		}

		public void vInit()
		{
			super.vInit();
			//String inputPorts = "<InputPorts>";
			Set<Entry<String, InputPort>> s = m_mInputPorts.entrySet();
	         Iterator<Entry<String, InputPort>> i = s.iterator();
	         while (i.hasNext()) {
	        	 InputPort in= i.next().getValue();
	        	 if(in!=null){
						in.vInit();
					}
	         }
		
	     	Set<Entry<String, OutputPort>> s2 = m_mOutputPorts.entrySet();
	         Iterator<Entry<String, OutputPort>> i2 = s2.iterator();
	         while (i2.hasNext()) {
	        	 OutputPort out= i2.next().getValue();
	        	 if(out!=null){
						out.vInit();
					}
	         }
			
		}

		// From Component Interface
		public boolean vPreStep()
		{
			super.vPreStep();
			//String inputPorts = "<InputPorts>";
			Set<Entry<String, InputPort>> s = m_mPrivateInputPorts.entrySet();
	         Iterator<Entry<String, InputPort>> i = s.iterator();
	         while (i.hasNext()) {
	        	 InputPort in=i.next().getValue();
	        	 if(in!=null){
						in.vPreStep();
					}
	         }
	         
	         Set<Entry<String, InputPort>> s1 = m_mInputPorts.entrySet();
	         Iterator<Entry<String, InputPort>> i1 = s1.iterator();
	         while (i1.hasNext()) {
	        	 InputPort in=i1.next().getValue();
	        	 if(in!=null){
						in.vPreStep();
					}
	         }
	         
	         Set<Entry<String, OutputPort>> s2 = m_mOutputPorts.entrySet();
	         Iterator<Entry<String, OutputPort>> i2 = s2.iterator();
	         while (i2.hasNext()) {
	        	 OutputPort out=i2.next().getValue();
	        	 if(out!=null){
						out.vPreStep();
					}
	         }
	         return true;
	         
		}
		
		public boolean vPostStep()
		{
			super.vPostStep();
			//String inputPorts = "<InputPorts>";
			Set<Entry<String, OutputPort>> s = m_mPrivateOutputPorts.entrySet();
	         Iterator<Entry<String, OutputPort>> i = s.iterator();
	         while (i.hasNext()) {
	        	 OutputPort out=i.next().getValue();
	        	 if(out!=null){
						out.vPostStep();
					}
	         }
	         
	         System.out.println("Writing on output port");
	         Set<Entry<String, OutputPort>> s1 = m_mOutputPorts.entrySet();
	         Iterator<Entry<String, OutputPort>> i1 = s1.iterator();
	         while (i1.hasNext()) {
	        	 OutputPort out= i1.next().getValue();
	        	 if(out!=null){
						out.vPostStep();
					}
	         }
	         
			return true;
		}

		public void vFinalize()
		{
			super.vFinalize();
			
			 Set<Entry<String, InputPort>> s1 = m_mInputPorts.entrySet();
	         Iterator<Entry<String, InputPort>> i1 = s1.iterator();
	         while (i1.hasNext()) {
	        	 InputPort in= i1.next().getValue();
	        	 if(in!=null){
						in.vFinalize();
					}
	         }
			
			 Set<Entry<String, OutputPort>> s2 = m_mOutputPorts.entrySet();
	         Iterator<Entry<String, OutputPort>> i2 = s2.iterator();
	         while (i2.hasNext()) {
	        	 OutputPort out= i2.next().getValue();
	        	 if(out!=null){
						out.vFinalize();
					}
	         }
			
	         Set<Entry<String, InputPort>> s3 = m_mPrivateInputPorts.entrySet();
	         Iterator<Entry<String, InputPort>> i3 = s3.iterator();
	         while (i3.hasNext()) {
	        	 InputPort in=i3.next().getValue();
	        	 if(in!=null){
						in.vFinalize();
					}
	         }
	         
			Set<Entry<String, OutputPort>> s4 = m_mPrivateOutputPorts.entrySet();
	         Iterator<Entry<String, OutputPort>> i4 = s4.iterator();
	         while (i4.hasNext()) {
	        	 OutputPort out=i4.next().getValue();
	        	 if(out!=null){
						out.vFinalize();
					}
	         }
			
			
		}
		

}
