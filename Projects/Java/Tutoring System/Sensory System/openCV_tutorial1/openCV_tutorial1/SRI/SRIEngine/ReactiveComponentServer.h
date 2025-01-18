#ifndef SRI_REACTIVE_COMPONENT_SERVER_H
#define SRI_REACTIVE_COMPONENT_SERVER_H

#include "SRI/SRIEngine/Server.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/ComponentServer.h"
#include "SRI/SRIEngine/ReactiveComponent.h"


namespace Poco {
	namespace XML {
		class NamedNodeMap;
	}

	namespace Net {
		class ServerSocket;
	}
}


namespace SRI {

	/// A ReactiveComponentServer acts as a proxy, enabling remote access to a ReactiveComponent
	/* Not inheriting from ComponentServer because will create triangular dependency
	 * as need to have ReactiveComponent as superclass (so that this class can pass 
	 * the casting tests in various methods e.g. methods in SRIEngine). Hence need to
	 * implement Component functions again
	 */
	class SRI_E_API ReactiveComponentServer : public ReactiveComponent, public Server {

	private:
		Logger m_tLog;

		/* Note that there are actually two references to the ReactiveComponent:
		 * one through m_ptReactiveComponent, and one maintained by the superclass ComponentServer
		 * in m_ptComponent. Maintaining a m_ptReactiveComponent saves us the trouble of having
		 * to cast m_ptComponent everytime we want to use functions specific to ReactiveComponent
		 */
		Ref<ReactiveComponent> m_ptReactiveComponent; 
		Poco::Net::ServerSocket *m_ptServerSocket;

	protected:
		//Component methods
		virtual void vSetId(SRI::String id); 
		virtual int iSetNameSpace(SRI::String name);
		//
		//ReactiveComponent functions
		
		virtual int iAddInputPort(InputPort* port);
		virtual int iAddOutputPort(OutputPort* port);

		virtual int iAddPrivateInputPort(InputPort* port);
		virtual int iAddPrivateOutputPort(OutputPort* port);

		virtual int iConnectToChildInput(SRI::String privateOutPortName, SRI::String childName, SRI::String childInPortName);
		virtual int iConnectToChildOutput(SRI::String privateInPortName, SRI::String childName, SRI::String childOutPortName);

		virtual int iDisconnectChildInput(SRI::String privateOutPortName, SRI::String childName, SRI::String childInPortName);
		virtual int iDisconnectChildOutput(SRI::String privateInPortName, SRI::String childName, SRI::String childOutPortName);


	public:
		//Server functions
		ReactiveComponentServer(Ref<ReactiveComponent> c); //doesn't take over the memory
		virtual ~ReactiveComponentServer();
		
		SRI::String szCallFunction(const ServerExecutorObject& execObj);

		//Component methods
		virtual SRI::String szGetID() const;
		virtual SRI::String szGetComponentType() const;
		virtual SRI::String szGetName() const;
		virtual SRI::String szGetNameSpace() const;
		virtual SRI::String szGetComponentName() const;
		virtual int iSetName(SRI::String name);
		virtual int iSetComponentType(SRI::String type);

		//virtual Component* ptClone() const;
		virtual ComponentStatus eGetStatus() const;
		virtual void vSetStatus(ComponentStatus status);

		virtual void vInit();
		virtual void vFinalize();
		virtual bool bHasMoreSteps();
		virtual void vStep();
		virtual void vPreStep();
		virtual void vPostStep();
		
		//ReactiveComponent methods

		/** After copy the IP address must be reset*/
		
		ReactiveComponentServer(const ReactiveComponentServer& c);
		ReactiveComponentServer& operator=(const ReactiveComponentServer& c);

		virtual bool operator==(const ReactiveComponent& c);
		bool operator==(const ReactiveComponentServer& c);
		//implement this for the component as well
		//virtual Component* ptClone() const;

		virtual int iCreateOutputPort(SRI::String name, SRI::String type);
		virtual int iCreateInputPort(SRI::String name, SRI::String type);

		virtual void vRemoveOutputPort(SRI::String name);
		virtual void vRemoveInputPort(SRI::String name);

		virtual bool bHasInputPort(const SRI::String& inport);
		virtual bool bHasOutputPort(const SRI::String& outport);

		virtual SRI::String szGetOutputPortAddress(const SRI::String& outport);
		virtual SRI::String szGetInputPortAddress(const SRI::String& outport);
	
		virtual int iAddOutputConnection(const SRI::String& outport, Ref<Connection> connection);
		virtual int iAddInputConnection(const SRI::String& inport, Ref<Connection> connection);

		virtual int iRemoveOutputConnection(const SRI::String& outport, const SRI::String& inport);
		virtual int iRemoveInputConnection(const SRI::String& inport, const SRI::String& outport);

		//TODO: consider deprecating, given above two functions? how to implement remotely?
		virtual int iRemoveOutputConnection(const SRI::String& outport, Ref<Connection> connection);
		virtual int iRemoveInputConnection(const SRI::String& inport, Ref<Connection> connection);

		virtual SRI::Map<SRI::String, SRI::String> mGetInputPortList();
		virtual SRI::Map<SRI::String, SRI::String> mGetOutputPortList();

		virtual SRI::String szGetInputPorts();
		virtual SRI::String szGetOutputPorts();

		virtual int iCreatePrivateOutputPort(SRI::String name, SRI::String type);
		virtual int iCreatePrivateInputPort(SRI::String name, SRI::String type);

		virtual void vRemovePrivateOutputPort(SRI::String name);
		virtual void vRemovePrivateInputPort(SRI::String name);


	};
} //end namespace
#endif SRI_REACTIVE_COMPONENT_SERVER_H