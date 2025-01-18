#ifndef SRI_REACTIVE_COMPONENT_H
#define SRI_REACTIVE_COMPONENT_H


#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIUtil/SRIList.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIEngine/Component.h"
#include "SRI/SRIEngine/InputPort.h"
#include "SRI/SRIEngine/OutputPort.h"



namespace SRI{


INST_SRI_E_TEMPL SRI::Map<SRI::String, SRI::Ref<InputPort>>;
INST_SRI_E_TEMPL SRI::Map<SRI::String, SRI::Ref<OutputPort>>;

/// A ReactiveComponent is a Component that has Ports, enabling it to communicate with other ReactiveComponents via Messages.

class SRI_E_API ReactiveComponent: public Component {

	friend class ReactiveComponentServer;


public:
	//typedef SRI::MapIterator<SRI::String, Ref<InputPort>> InputPortIt;
	//typedef SRI::MapIterator<SRI::String, Ref<OutputPort>> OutputPortIt;
	
private:
	Logger m_tLog;

protected:
	//A component owns its ports (memory must be released = handles by smartpointers)
	SRI::Map<SRI::String, Ref<InputPort>> m_mInputPorts;
	SRI::Map<SRI::String, Ref<OutputPort>> m_mOutputPorts;

	SRI::Map<SRI::String, Ref<InputPort>> m_mPrivateInputPorts;
	SRI::Map<SRI::String, Ref<OutputPort>> m_mPrivateOutputPorts;

	/** Called during PostStep to add all pending sockets to appropriate output ports **/
	int iProcessPendingSockets();
	/***DEPRECATED***/

	/** Adds a new port to the component. Memory is taken over. That means that the 
	memory becomes invalid after this function call.*/
	virtual int iAddInputPort(InputPort* port);
	/** Adds a new OutputPort to the component. Memory is taken over. That means that the 
	memory becomes invalid after this function call.*/
	virtual int iAddOutputPort(OutputPort* port);

	/** Adds a new port to the component. Memory is taken over. That means that the 
	memory becomes invalid after this function call.*/
	virtual int iAddPrivateInputPort(InputPort* port);
	/** Adds a new OutputPort to the component. Memory is taken over. That means that the 
	memory becomes invalid after this function call.*/
	virtual int iAddPrivateOutputPort(OutputPort* port);

	virtual SRI::Ref<SRI::InputPort> ptGetInputPort(SRI::String portName);
	virtual SRI::Ref<SRI::OutputPort> ptGetOutputPort(SRI::String portName);

	virtual int iConnectToChildInput(SRI::String privateOutPortName, SRI::String childName, SRI::String childInPortName);
	virtual int iConnectToChildOutput(SRI::String privateInPortName, SRI::String childName, SRI::String childOutPortName);

	virtual int iDisconnectChildInput(SRI::String privateOutPortName, SRI::String childName, SRI::String childInPortName);
	virtual int iDisconnectChildOutput(SRI::String privateInPortName, SRI::String childName, SRI::String childOutPortName);

public:
		
	ReactiveComponent(SRI::String name);
	virtual ~ReactiveComponent();

	/** After copy the IP address must be reset*/
	ReactiveComponent(const ReactiveComponent& c);
	ReactiveComponent& operator=(const ReactiveComponent& c);

	virtual bool operator==(const ReactiveComponent& c);

	virtual Component* ptClone() const;

	// =================== Public Port =============================================================
	
	virtual int iCreateOutputPort(SRI::String name, SRI::String type);
	virtual int iCreateInputPort(SRI::String name, SRI::String type);

	virtual void vRemoveOutputPort(SRI::String name);
	virtual void vRemoveInputPort(SRI::String name);

	virtual bool bHasInputPort(const SRI::String& inport);
	virtual bool bHasOutputPort(const SRI::String& outport);

	virtual SRI::String szGetOutputPortAddress(const SRI::String& outport);
	virtual SRI::String szGetInputPortAddress(const SRI::String& inport);
	
	/** Adds connection object to the specified output port*/
	virtual int iAddOutputConnection(const SRI::String& outport, Ref<Connection> connection);
	/** Adds connection object to the specified input port*/
	virtual int iAddInputConnection(const SRI::String& inport, Ref<Connection> connection);

	virtual int iRemoveOutputConnection(const SRI::String& outport, const SRI::String& inport);
	virtual int iRemoveInputConnection(const SRI::String& inport, const SRI::String& outport);

	virtual int iRemoveOutputConnection(const SRI::String& outport, Ref<Connection> connection);
	virtual int iRemoveInputConnection(const SRI::String& inport, Ref<Connection> connection);

	virtual bool bIsConnected(const SRI::String& senderPort, const SRI::String& receiverPort);

	/** Returns a list of ports in the format: Name, Type*/
	virtual SRI::Map<SRI::String, SRI::String> mGetInputPortList();
	virtual SRI::Map<SRI::String, SRI::String> mGetOutputPortList();

	/** Retruns a list of ports encoded in an xml string */
	virtual SRI::String szGetInputPorts();
	/** Retruns a list of ports encoded in an xml string */
	virtual SRI::String szGetOutputPorts();

	// =================== Private Port =============================================================
	virtual int iCreatePrivateOutputPort(SRI::String name, SRI::String type);
	virtual int iCreatePrivateInputPort(SRI::String name, SRI::String type);

	virtual void vRemovePrivateOutputPort(SRI::String name);
	virtual void vRemovePrivateInputPort(SRI::String name);

	virtual void vInit();

	// From Component Interface
	virtual void vPreStep();
	virtual void vPostStep();

	virtual void vFinalize();
	
};


} // end namespace



#endif
