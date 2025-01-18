package SRI;

import java.util.ArrayList;
import java.util.List;

public class Connection extends Component {

//	#ifndef SRI_CONNECTION_H
//	#define SRI_CONNECTION_H

//	#include "SRI/SRIEngine/SRIEngineLib.h"
//	#include "SRI/Logger/Logger.h"
	//#include "SRI/SRIUtil/SRIRef.h"
	//#include "SRI/SRIEngine/Component.h"
	//#include "SRI/ConfigReader/ConfigNode.h"
	//#include "SRI/SRIEngine/Message.h"
	//#include "SRI/SRIUtil/SRIList.h"


	//namespace SRI{
		
		//class OutputPort;
		//class InputPort;

	//INST_SRI_E_TEMPL SRI::List<Ref<Message>>;


	/// An abstraction of a connection between an InputPort and an OutputPort
	/** A Connection acts as an intermediary storing messages sent from
		an OutputPort to an InputPort. Message storing semantics are FIFO.
	*/
	//class SRI_E_API Connection: public Component{

	//private:
	  //SRI::Logger m_tLog;
	  
	  //to identify sender/receiver when not in same address space
	  //facilitates removal of connections
	  private String m_szSenderName;
	  private String m_szReceiverName;
		
	  //TODO: consider using names "outport" and "inport" in place of sender and receiver to unify naming,
	  //easing cognitive load; maintenance++

	//protected:
	  protected OutputPort m_ptSender;
	  protected InputPort m_ptReceiver;

	  protected List<Message> m_lMessageBuffer=new ArrayList<Message>();

		// don't allow to make copies of connection objects publicly (subclasses are allowed)
		//Connection(const Connection& c);
		//Connection& operator=(const Connection& c);

	//public:
		public Connection()
		{
			m_ptSender = null;
			m_ptReceiver = null;
			
		}
		
		//virtual ~Connection();

		public boolean bIsConnected()
		{
			return ((m_ptSender != null) && (m_ptReceiver != null));
			//return false;
		}

		public void vSetSenderName(String sender)
		{
			m_szSenderName = sender;
		}
		
		public void vSetReceiverName(String receiver)
		{
			m_szReceiverName = receiver;
		}

		public String szGetSenderName()
		{
			return m_szSenderName;
		}
		
		public String szGetReceiverName()
		{
			return m_szReceiverName;
		}

		public OutputPort ptGetSender() 
		{
			return m_ptSender;
		}
		
		public InputPort ptGetReceiver() 
		{
			return m_ptReceiver;
			
		}

		/** These methods are accessed by the Ports*/
		public int iSend(Message m)
		{
			m_lMessageBuffer.add(m);
			return 0;
		}
		/** This function takes over the memory of the message*/
		//public int iSend(Message m);
		public Message ptReceive()
		{
			if(m_lMessageBuffer.size() <= 0){
				Message m=null;
				return m; // no message in buffer;
			}else{
				Message m = m_lMessageBuffer.get(0);
				m_lMessageBuffer.remove(0);
				return m;
			}
		}

		/** for manually setting sender and receiver
		* connection is added at the given port. As the connection is owned
		* by ports the memory is merely a reference and will not be freed by
		* the connection.*/
		public int iSetSender(OutputPort sender)
		{
			if(sender == null){
				m_ptSender = null;
				//m_tLog.debug("Set sender of connection to NULL");
				return 0;// SRI::SRI_OK;
			}
			if (sender == m_ptSender){
				//m_tLog.debug("Sender was already set");
				System.out.println("Sender was already set");
				return 0;// SRI_OK;
			}

			if((m_ptReceiver != null) && (m_ptReceiver.szGetPortDataType() != sender.szGetPortDataType())){
				//m_tLog.error("Sender port type does not match  %s != %s", sender->szGetPortDataType().c_str(), m_ptReceiver->szGetPortDataType().c_str()); 
				System.out.println("Sender port type does not match  %s != %s"+ sender.szGetPortDataType()+ m_ptReceiver.szGetPortDataType());
				return 1;// SRI::SRI_ERR_TYPE;
			}
			
			m_ptSender = sender;
			m_szSenderName = sender.szGetName();
			System.out.println("Sender set");
			//m_tLog.debug("sender set");
			return 0;// SRI_OK;
			
		}
		
		/** for manually setting sender and receiver
		* connection is added at the given port. As the connection is owned
		* by ports the memory is merely a reference and will not be freed by
		* the connection.*/
		public int iSetReceiver(InputPort receiver)
		{
			
			if(receiver == null){
				m_ptReceiver = null;
				//m_tLog.debug("Set receiver of connection to NULL");
				return 0;//SRI::SRI_OK;
			}
			if(m_ptReceiver == receiver){
				//m_tLog.debug("Receiver was already set");
				System.out.println("Receiver was already set");
				return 0;// SRI_OK;
			}

			if((m_ptSender != null) && (m_ptSender.szGetPortDataType() != receiver.szGetPortDataType())){
				System.out.println("Receiver port type does not match  %s != %s"+ receiver.szGetPortDataType()+ m_ptSender.szGetPortDataType()); 
				return 1;// SRI::SRI_ERR_TYPE;
			}

			m_ptReceiver = receiver;
			m_szReceiverName = receiver.szGetName();
			System.out.println("receiver set");
			return 0;// SRI_OK;
		}
	//};


	//}// end namespace

	//#endif

	
	
	
	
}
