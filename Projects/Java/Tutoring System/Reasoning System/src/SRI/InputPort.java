package SRI;

import java.util.Iterator;

public class InputPort extends Port {

	public InputPort(String name, String dataType) {
		super(name, dataType);//if there is no default constructor then you got to add this
		System.out.println("InputPort");
		// TODO Auto-generated constructor stub
	}
	
	//private:
		//Logger m_tLog;

	
		//InputPort(SRI::String name, SRI::String dataType);
		//virtual Component* ptClone();

		public PortDefinition tGetPortDefinition()
		{
			//return PortDefinition(m_szName, m_szPortType, PortDefinition::INPUT);
			return null;
		}

		/// Attaches connection to the InputPort.
		public int iAddConnection(Connection connection)
		{
			if(connection==null){
				//m_tLog.error("Trying to add invalid connection to %s port", this->szGetName().c_str());
				System.out.println("Trying to add invalid connection to %s port"+ this.szGetName());
				return 1;// SRI_ERR_NULL; // TODO: throw Null exception?
			}
			
			if(m_lConnections.contains(connection)){ //!= m_lConnections.end()){
				System.out.println("Attempt to add same connection twice");
				return 2;//SRI_ERR_NAMECONFLICT;
			//if(m_lConnections.find(connection) != m_lConnections.end()){
				//m_tLog.error("Attempt to add same connection twice");
				//return SRI_ERR_NAMECONFLICT; //TODO: throw exception that same connection is added twice?
			}
			//m_tLog.debug("Added connection to port");
			System.out.println("Added connection to port");
			int res = connection.iSetReceiver(this);
			//TODO: add here setting to my name

			if(res == 0){//SRI_OK) {
				m_lConnections.add(connection);
			}

			return res;
		}

		public boolean vPreStep()
		{
			Connection rConnection=null;
			Iterator<Connection> it=m_lConnections.iterator();
			 while(it.hasNext()) {
				 rConnection=it.next();
				 if(rConnection==null) {
					 System.out.println("Found invalid connection");
					 continue;
				 }
					 
				 Message m = rConnection.ptReceive();
				 while (m != null) {
					 m_lPortBuffer.add(m);
					m = rConnection.ptReceive();
				 }
				 
				 
			 }	 
				
				 
			//for(SRI::ListIterator<Ref<Connection>> it = m_lConnections.begin(); it != m_lConnections.end(); it++){
			//	Ref<Connection>& c = *it;
				//if(!c.bIsValid()){
				//	m_tLog.warn("Found invalid connection");//TODO:: throw null pointer exception?
				//	continue; // one connection failed -> go on with the others
				//}
			//	Ref<Message> m = c->ptReceive();
				//while(m.bIsValid()){
					//m_lPortBuffer.push_back(m);
					//m = c->ptReceive();
				
			
			return true;
		}

		
		/** Tries to receives a message. If none are available ptReceive().bisValid() will return false 
		*/
		public Message ptReceive()
		{
			if(m_lPortBuffer.size() <= 0){
				return null;
			}

			Message ret = m_lPortBuffer.get(0);
			m_lPortBuffer.remove(0);
			return ret;
		}

		//int iConnectToOutputPort(const SRI::String& outportAddress, const SRI::String& outportName);

		//virtual void vInit();
		//virtual void vFinalize();

	

}
