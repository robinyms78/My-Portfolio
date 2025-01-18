package SRI;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Port extends Component {

	
	/** A port describes incoming and outgoing data for a component. 
	* The data on a port is typed. 
	*/
	

	/** Base class for the Input and Output ports
	*/
	
	//public:
		//typedef SRI::MapIterator<Connection*, Connection*> ConnectionIt;

	//private:
	//	Logger m_tLog;

	
		
		protected String m_szOwnerComponentIP; 
		
		
		protected int m_iOwnerComponentPID;

		protected List<Connection> m_lConnections=new ArrayList<Connection>();

		//The data type sent of the port
		protected String m_szPortType;

		protected List<Message> m_lPortBuffer=new ArrayList<Message>();

	
		public Port(String name, String type)
		{
			super(name);//init a component
			m_szPortType = type;
			iSetComponentType("SRI.ReactiveComponent.Port");
		}
	

		/** Copies leave owner open.
		* Also the message buffer and connections are not copied*/
	
		/** Copies leave owner open.
		* Also the message buffer and connections are not copied*/

		public Component ptClone()//may not need this
		{
			Port p = this;
			return p;
		}

		/** Connections are added by the engine */ //no longer true
		public int iAddConnection(Connection connection)
		{
			
			if(connection==null){
				//m_tLog.error("Trying to add invalid connection to %s port", this->szGetName().c_str());
				System.out.println("Trying to add invalid connection to %s port"+ this.szGetName());
				return 1; //SRI_ERR_NULL; // TODO: throw Null exception?
			}
			
			
			
			
			if(m_lConnections.size()>0 &&m_lConnections.contains(connection) ){
				
				 //!= m_lConnections.end()){
				return 2;//SRI_ERR_NAMECONFLICT; //TODO: throw exception that same connection is added twice?
			}
			
			//m_tLog.debug("Added connection to port %s",  this->szGetName().c_str());
			System.out.println("Added connection to port %s"+ this.szGetName());
			// IN THE OUTPUT PORT AND INPUT PORT THE SENDER AND RECEIVER MUST BE SET

			m_lConnections.add(connection);//push_back(Ref<Connection>(connection));
			
			return 0;
		}
		
		public void vRemoveConnection(Connection connection)
		{
			Connection rConnection=null;
			Connection rConnection1=null;
			Iterator<Connection> it=m_lConnections.iterator();
			 while(it.hasNext()) {
				 if(it.next()!=null && it.next()==connection)
				 {
					 if(this==(Port)it.next().ptGetReceiver())
					 {
						 it.next().iSetReceiver(null);
						 it.next().vSetReceiverName("");
					 }
					 else if(this==(Port)it.next().ptGetSender())
					 {
						 it.next().iSetSender(null);
						 it.next().vSetSenderName("");
						 
					 }
					 else{
						 System.out.println("A connection was in the list that the port was not part of");
					 }
					 
					 
				 }
				 
					rConnection=it.next();
			
			 } 
			 if(rConnection!=null)
			 {
			 m_lConnections.remove(rConnection) ;
			 System.out.println("Connection removed");
			 }
			 	if (rConnection1==null)
			 	{
			 		
				 System.out.println("Cannot remove non existng connection ");
			 	}
			 
			//SRI::ListIterator<Ref<Connection>> it = m_lConnections.find(connection) ;
			//if(it == m_lConnections.end()){
				//m_tLog.error("Unable to remove non existing connection");
	
		}
		
		
		public int iRemoveConnection(String outport, String inport)
		{
			if ((outport == "") || (inport == "")){
				System.out.println("Trying to remove connection without giving port names");
				//m_tLog.debug("Trying to remove connection without giving port names");
				return 3;//SRI_ERR_INCOMPLETE;
			}
			
			Connection c=null;
			Connection c1=null;
			
			Iterator<Connection> it=m_lConnections.iterator();
			 while(it.hasNext()) {
				
				 c=it.next();
				
				 if(c!=null)
				 {
					 
					 if ((c.szGetSenderName().equals(outport)) && (c.szGetReceiverName().equals(inport))) 
					 {
							vRemoveConnection(c);
							return 0;//SRI_OK;
				 }
				 }
			 }
					System.out.println("Connection with sender: %s and receiver: %s not found: Nothing was removed");
			//m_tLog.warn("Connection with sender: %s and receiver: %s not found: Nothing was removed", outport.c_str(), inport.c_str());
				 
			return 1;// SRI Error;
				 
		}


		public Connection ptFindConnection(OutputPort sender, InputPort receiver)
		{
			Connection con = null;
			if( (sender == null) && (receiver == null)){
				//m_tLog.warn("Unable to find connection: Got NULL on input");
				System.out.println("Unable to find connection: Got NULL on input");
				return con;
			}
			Iterator<Connection> it=m_lConnections.iterator();
			Connection c; 
			while(it.hasNext()) {
				c=it.next();
				 if(c!=null)
				 {
					// c=it.next();
					 
					 if(   (c.ptGetSender() == sender) && (c.ptGetReceiver() == receiver)){
							con = c;
							break;
						}
			
				}
			}
			return con;
			
		}


		//TODO: are these functions only needed for input ports to handle connection requests?
		public void vSetOwnerComponentIP(String ownerIP)
		{
			m_szOwnerComponentIP = ownerIP;
		}
		
		public void vSetOwnerComponentPID(int ownerPID)
		{
			m_iOwnerComponentPID = ownerPID;
		}
		

		/** Returns the data type that is send over this port*/
		public String szGetPortDataType()
		{
			return m_szPortType;
		}

		public PortDefinition tGetPortDefinition()
		{
			//return PortDefinition(m_szName, m_szPortType, PortDefinition::NO_DIRECTION);
			return null;
		}

		//TODO: are these functions only needed for input ports to handle connection requests?
		public String szGetOwnerComponentIP()
		{
			return m_szOwnerComponentIP;
		}
		
		public  int iGetOwnerComponentPID()
		{
			return m_iOwnerComponentPID;
		}

		public void vInit()
		{
			super.vInit();//invoke the parent method
			m_lPortBuffer.clear();
			
		}
		
		public void vFinalize()
		{
			super.vFinalize();
			m_lPortBuffer.clear();
		}
		
		public boolean bHasMoreSteps()
		{
			boolean res = super.bHasMoreSteps();
			return true;
		}



	
}
