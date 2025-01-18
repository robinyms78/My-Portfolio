#ifndef SRI_SERVER_H
#define SRI_SERVER_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIEngine/ServerServiceHandler.h"
#include "SRI/SRIEngine/ServerExecutorObject.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIMutexStack.h"
#include "Poco/ActiveMethod.h"


namespace Poco {

	class Thread;

	namespace XML {
		class Document;
		class NamedNodeMap;
	}

	namespace Net{
		class ServerSocket;
		class StreamSocket;
		class SocketReactor;

	
	}
}

namespace SRI {

	template <class ServiceHandler> class ServerSocketAcceptor;

	/// Base class from which all Servers are derived
	/** A Server acts as a proxy for an object, and allows an object's
		methods to be called remotely. It is in charge of unpacking
		an remote function call's arguments and marshalling the reply.

		Please see the detailed documentation for StubTemplate for an
		explanation of the communication protocol between Servers
		and StubTemplates.
	*/

	class SRI_E_API Server {

	private:
		Poco::Thread* m_ptMyThread;
		Poco::Net::SocketReactor* m_ptSocketReactor;
		ServerSocketAcceptor<ServerServiceHandler>* m_ptServerSocketAcceptor;
		Poco::Net::ServerSocket* m_ptServerSocket;

		Logger m_tLog;

		SRIMutexStack<ServerExecutorObject> m_stMutexStack;

		Poco::ActiveMethod<void, ServerExecutorObject, Server> vCallFunctionHelper;
		void vCallFunctionHelperImpl(const ServerExecutorObject& execObj);

	

	protected:
		SRI::String szCreateXMLReply(const ServerExecutorObject& o); //for now we assume it is robust and can parse correctly
		SRI::String szCreateXMLReply(unsigned int r, const ServerExecutorObject& o);
		SRI::String szCreateXMLReply(int r, const ServerExecutorObject& o); 
		SRI::String szCreateXMLReply(bool r, const ServerExecutorObject& o); 
		SRI::String szCreateXMLReply(const SRI::String& r, const ServerExecutorObject& o);
		void vXMLDocToStringStream(std::stringstream& s, Poco::XML::Document* pDoc);

		

	public:
		Server();
		virtual ~Server();
		//TODO: copy con, assignment op

		Server(const Server& s);
		Server& operator=(const Server& s);

		
		
		/// Binds the server to port and starts the server listening in a separate thread. Pass 0 to use OS-supplied random port.
		virtual void vStartServer(int port);

		//Stops the server and joins the listening thread
		virtual void vStopServer();

		/// Returns the port the server is listening on.
		int iGetServerPort();

		/// Joins the thread that the server listens on.
		void vJoinServerThread(); 		

		/// Called by SocketReactor to process incoming XML messages
		SRI::String szProcessXMLMessage(const SRI::String& msg, Poco::Net::StreamSocket *s);

		/// This function calls the appropriate method of the proxied object. Override to provide server functionality specific to a class.
		virtual SRI::String szCallFunction(const ServerExecutorObject& execObj) = 0;
		

	};
} //end namespace
#endif SRI_SERVER_H