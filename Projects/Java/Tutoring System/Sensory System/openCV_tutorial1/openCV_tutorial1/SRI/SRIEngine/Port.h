#ifndef SRI_PORT_H
#define SRI_PORT_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIList.h"
#include "SRI/SRIEngine/Component.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/Connection.h"
#include "SRI/SRIEngine/PortDefinition.h"

namespace SRI{


/** A port describes incoming and outgoing data for a component. 
* The data on a port is typed. 
*/
class Message;

INST_SRI_E_TEMPL SRI::List<Ref<Connection>>;
INST_SRI_E_TEMPL SRI::List<SRI::Ref<Message>>;

/** Base class for the Input and Output ports
*/
class SRI_E_API Port: public Component{
	friend class ReactiveComponent;

public:
	//typedef SRI::MapIterator<Connection*, Connection*> ConnectionIt;

private:
	Logger m_tLog;

protected:
	
	SRI::String m_szOwnerComponentIP; 
	unsigned int m_iOwnerComponentPID;

	SRI::List<Ref<Connection>> m_lConnections;

	//The data type sent of the port
	SRI::String m_szPortType;

	SRI::List<Ref<Message>> m_lPortBuffer;

	SRI::Ref<SRI::Component> m_ptParent;

	void vSetParent(SRI::Ref<SRI::Component> parent);
	

public:
	Port(SRI::String name, SRI::String type);
	virtual ~Port();

	/** Copies leave owner open.
	* Also the message buffer and connections are not copied*/
	Port(const Port& c);
	/** Copies leave owner open.
	* Also the message buffer and connections are not copied*/
	Port& operator=(const Port& c);
	virtual Component* ptClone();

	SRI::Ref<SRI::Component> ptGetParent();

	/** Clears the internal port buffer */
	virtual void vClearPortBuffer(); 

	/** Connections are added by the engine */ //no longer true
	virtual int iAddConnection(Ref<Connection>& connection);
	virtual void vRemoveConnection(Ref<Connection>& connection);
	virtual int iRemoveConnection(SRI::String outport, SRI::String inport);

	virtual Ref<Connection> ptFindConnection(OutputPort* sender, InputPort* receiver);
	virtual SRI::List<Ref<Connection>>& tGetConnections();

	virtual bool bIsConnected(SRI::String portName);


	//TODO: are these functions only needed for input ports to handle connection requests?
	virtual void vSetOwnerComponentIP(const SRI::String& ownerIP);
	virtual void vSetOwnerComponentPID(const unsigned int ownerPID);
	

	/** Returns the data type that is send over this port*/
	virtual SRI::String szGetPortDataType() const;

	virtual PortDefinition tGetPortDefinition();

	//TODO: are these functions only neede for input ports to handle connection requests?
	virtual SRI::String szGetOwnerComponentIP();
	virtual unsigned int iGetOwnerComponentPID();

	virtual void vInit();
	virtual void vFinalize();
	virtual bool bHasMoreSteps();

};


}// end namespace

#endif
