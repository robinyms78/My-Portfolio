#ifndef SRI_OUTPUT_PORT_H
#define SRI_OUTPUT_PORT_H

#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/Port.h"
#include "SRI/SRIEngine/Message.h"


namespace Poco{
	namespace Net{
		class ServerSocket;
		class StreamSocket;
	}
}

namespace SRI{

/// An output port broadcasts Messages to the input ports that are connected to it.
/** Messages passed to the OutputPort are stored in a buffer and sent out during a PostStep.
*/
class SRI_E_API OutputPort: public Port{
	
private:
	Logger m_tLog;

public:
	OutputPort(SRI::String name, SRI::String type);
	virtual ~OutputPort();

	OutputPort(const OutputPort& c);
	OutputPort& operator=(const OutputPort& c);

	virtual Component* ptClone();

	virtual PortDefinition tGetPortDefinition();

	virtual int iAddConnection(Ref<Connection> connection);

	/** Sends the message to all connections of the port 
	*/
	virtual int iSend(Ref<Message> m);
	
	
	/** Sends the message to all connections of the port
	* Takes over the memory of the message
	*/
	virtual int iSend(Message* m);

	virtual void vPreStep();
	virtual void vPostStep();

	/*virtual void vInit();
	virtual void vFinalize();*/
};

} // end namespace

#endif