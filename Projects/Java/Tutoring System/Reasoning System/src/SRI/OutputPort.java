package SRI;

import java.util.Iterator;

public class OutputPort extends Port {

	public OutputPort(String name, String type) {
		super(name, type);
		// TODO Auto-generated constructor stub
	}
	
	
	

	public PortDefinition tGetPortDefinition()
	{
		//return PortDefinition(m_szName, m_szPortType, PortDefinition::OUTPUT);
		return null;
	}

	public int iAddConnection(Connection connection)
	{
		if(connection==null){
			//m_tLog.error("Trying to add invalid connection to %s port", this->szGetName().c_str());
			System.out.println("Trying to add invalid connection to %s port"+ this.szGetName());
			return 1;// SRI_ERR_NULL; // TODO: throw Null exception?
		}
		
		if(m_lConnections.contains(connection)){ //!= m_lConnections.end()){
			return 2;//SRI_ERR_NAMECONFLICT;
		//if(m_lConnections.find(connection) != m_lConnections.end()){
			//m_tLog.error("Attempt to add same connection twice");
			//return SRI_ERR_NAMECONFLICT; //TODO: throw exception that same connection is added twice?
		}
		//m_tLog.debug("Added connection to port");
		System.out.println("Added connection to port");
		int res = connection.iSetSender(this);
		//TODO: add here setting to my name

		if(res == 0){//SRI_OK) {
			m_lConnections.add(connection);
		}

		return res;
	}

	
		/** Sends the message to all connections of the port 
		*/
	public int iSend(Message m)
	{
		int res = 0;

		m_lPortBuffer.add(m);

		return res;
	}
		
		
		/** Sends the message to all connections of the port
		* Takes over the memory of the message
		 * @return 
		*/
	//public int iSend(Message m)
	//{
		
	//}

	public boolean vPreStep()
	{
		return true;	
	}
		
	public boolean vPostStep()
	{
		
		int res = 0;
		Message message=null;
		Iterator<Message> mes_it=m_lPortBuffer.iterator();
		
		while(mes_it.hasNext()) {
			
			 message=mes_it.next();
			 Connection rConnection=null;
			 
			 Iterator<Connection> con_it=m_lConnections.iterator();
			 while(con_it.hasNext()) {
				 rConnection=con_it.next();
				 if(message!=null && rConnection!=null)
				 {
					 
					 res=rConnection.iSend(message);
					 if(res!=0){
						 System.out.println("Error sending data: %d"+ res);
					 }
				 }
					 else{
						 System.out.println("Unable to send data. Connection is invalid");
					 }
				 }
			 }
		 
		// }
		//for(SRI::ListIterator<Ref<Message>> mes_it = m_lPortBuffer.begin(); mes_it != m_lPortBuffer.end(); mes_it++){
			//for(SRI::ListIterator<Ref<Connection>> con_it = m_lConnections.begin(); con_it != m_lConnections.end(); con_it++){
				//Connection c = con_it;
				//if(c.bIsValid() && (*mes_it).bIsValid()){
					//res = c->iSend((*mes_it)); 
					//if(res != 0){
					//	m_tLog.error("Error sending data: %d", res);
				//	}
				//}else{
				//	m_tLog.error("Unable to send data. Connection is invalid");
			//	}
			//}
		//}

		m_lPortBuffer.clear();
		
		return true;	
	}


	
	

}
