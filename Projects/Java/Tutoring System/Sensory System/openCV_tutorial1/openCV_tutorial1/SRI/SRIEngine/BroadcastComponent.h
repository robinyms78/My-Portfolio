#ifndef BROADCAST_COMPONENT_H
#define BROADCAST_COMPONENT_H

#include "SRI/SRIEngine/Server.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIMap.h"
#include "SRI/SRIEngine/Component.h"

namespace Poco {
	class Thread;

	namespace Net{
		class ServerSocket;
		class StreamSocket;
		class SocketReactor;

	
	}
}

/// The ComponentServer is a proxy service allowing remote access to a Component

namespace SRI {

	template <class ServiceHandler> class BroadcastSocketAcceptor;

	class SRI_E_API BroadcastComponent : public Component {

	private:
		Logger m_tLog;
		Ref<Component> m_ptComponent; 

		Poco::Thread* m_ptMyThread;
		Poco::Net::SocketReactor* m_ptSocketReactor;
		BroadcastSocketAcceptor<ServerServiceHandler>* m_ptBroadcastSocketAcceptor;
		Poco::Net::ServerSocket* m_ptServerSocket;

		SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mListeningComponents;

	protected:
		//Component methods
		//virtual void vSetId(SRI::String id); 
		//virtual int iSetNameSpace(SRI::String name);

	public:
		
		//Server methods
		BroadcastComponent(SRI::String name, int portNo = 0); 
		virtual ~BroadcastComponent();
		//TODO: copy con, assignment op
		SRI::String szCallFunction(const SRI::String& funcname, Poco::XML::NamedNodeMap *arglist);

		int iAddListener(Ref<Component> c);
		void vStartServer(int portNo);
		int iGetServerPort();

		//Component methods
		//virtual SRI::String szGetID() const;
		//virtual SRI::String szGetComponentType() const;
		//virtual SRI::String szGetName() const;
		//virtual SRI::String szGetNameSpace() const;
		//virtual SRI::String szGetComponentName() const;
		//virtual int iSetName(SRI::String name);
		//virtual int iSetComponentType(SRI::String type);

		//virtual Component* ptClone() const;
		//virtual ComponentStatus eGetStatus() const;
		virtual void vSetStatus(ComponentStatus status);

		virtual void vInit();
		virtual void vFinalize();
		virtual bool bHasMoreSteps();
		virtual void vStep();
		virtual void vPreStep();
		virtual void vPostStep();
	};
} //end namespace
#endif BROADCAST_COMPONENT_H