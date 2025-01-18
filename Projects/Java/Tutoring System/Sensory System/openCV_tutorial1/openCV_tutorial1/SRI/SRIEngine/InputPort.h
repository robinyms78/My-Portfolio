#ifndef SRI_INPUT_PORT_H
#define SRI_INPUT_PORT_H

#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/Port.h"
#include "SRI/SRIEngine/Message.h"


namespace SRI{

/** The InputPort has to maintain a receive buffer in which all incomming messages get combined.
	Messages within a Step are guaranteed to be retrieved before Messages sent within the next Step,
	but there is no guarantee on the order of messages sent within a Step.
*/
	

class SRI_E_API InputPort: public Port{

private:
	Logger m_tLog;

public:
	InputPort(SRI::String name, SRI::String dataType);
	virtual ~InputPort();
	InputPort(const InputPort& c);
	InputPort& operator=(const InputPort& c);

	virtual Component* ptClone();

	virtual PortDefinition tGetPortDefinition();

	/// Attaches connection to the InputPort.
	virtual int iAddConnection(Ref<Connection> connection);

	virtual void vPreStep();


	/** Tries to receives a message. If none are available ptReceive().bisValid() will return false 
	*/
	Ref<Message> ptReceive();

	//int iConnectToOutputPort(const SRI::String& outportAddress, const SRI::String& outportName);

	//virtual void vInit();
	//virtual void vFinalize();

};

} // end namespace

#endif