#ifndef SRI_CONNECTION_H
#define SRI_CONNECTION_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/Component.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIEngine/Message.h"
#include "SRI/SRIUtil/SRIList.h"


namespace SRI{
	
	class OutputPort;
	class InputPort;

INST_SRI_E_TEMPL SRI::List<Ref<Message>>;


/// An abstraction of a connection between an InputPort and an OutputPort
/** A Connection acts as an intermediary storing messages sent from
	an OutputPort to an InputPort. Message storing semantics are FIFO.
*/
class SRI_E_API Connection: private Component{

private:
  SRI::Logger m_tLog;
  
  //to identify sender/receiver when not in same address space
  //facilitates removal of connections
  SRI::String m_szSendPortName;
  SRI::String m_szReceivePortName;

	
  //TODO: consider using names "outport" and "inport" in place of sender and receiver to unify naming,
  //easing cognitive load; maintenance++

protected:
	OutputPort* m_ptSender;
	InputPort* m_ptReceiver;

	SRI::List<Ref<Message>> m_lMessageBuffer;

	// don't allow to make copies of connection objects publicly (subclasses are allowed)
	Connection(const Connection& c);
	Connection& operator=(const Connection& c);

public:
	Connection();
	
	virtual ~Connection();

	virtual bool bIsConnected();

	/** Sets name of sender port (unqualified) */
	void vSetSendPortName(const SRI::String& sender);
	/** Sets name of receiver port (unqualified) */
	void vSetReceivePortName(const SRI::String& receiver);

	virtual SRI::String szGetSendPortName() const;
	virtual SRI::String szGetReceivePortName() const;

	virtual SRI::String szGetSenderComponentName();
	virtual SRI::String szGetReceiverComponentName();

	virtual OutputPort* ptGetSender() const;
	virtual InputPort* ptGetReceiver() const;

	/** These methods are accessed by the Ports*/
	virtual int iSend(Ref<Message> m);
	/** This function takes over the memory of the message*/
	virtual int iSend(Message* m);
	virtual Ref<Message> ptReceive();

	/** for manually setting sender and receiver
	* connection is added at the given port. As the connection is owned
	* by ports the memory is merely a reference and will not be freed by
	* the connection.*/
	virtual int iSetSender(OutputPort* sender);
	
	/** for manually setting sender and receiver
	* connection is added at the given port. As the connection is owned
	* by ports the memory is merely a reference and will not be freed by
	* the connection.*/
	virtual int iSetReceiver(InputPort* receiver);
};


}// end namespace

#endif
