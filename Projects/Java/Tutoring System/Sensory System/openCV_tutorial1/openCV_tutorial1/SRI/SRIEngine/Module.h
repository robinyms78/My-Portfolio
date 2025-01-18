

#ifndef SRI_MODULE_H
#define SRI_MODULE_H

#include "Component.h"
#include <sstream>

#include "ModuleServiceHandler.h"
#include "ModuleSocketAcceptor.h"


namespace Poco {

	class Thread;

	namespace XML {
		class Document;
	}

	namespace Net{
		class ServerSocket;
		class StreamSocket;
		class SocketReactor;
	
	}
}


namespace SRI{


///Module takes over the memory of the component

//Provides interface on socket level
//Ports of Modules use sockets for conenction
class Module{ //should a module be a component too?

private:
	Poco::Thread* m_ptMyThread;
	Poco::Net::SocketReactor* m_ptSocketReactor;
	ModuleServiceHandler* m_ptServiceHandler;
	ModuleSocketAcceptor<ModuleServiceHandler>* m_ptSocketAcceptor;
	

	Component* m_ptComponent;
	int m_iPortNo;
	Poco::Net::ServerSocket* m_ptServerSocket;
	Poco::Net::StreamSocket* m_ptStreamSocket;

	//TODO: copy constructor, assignment operator

public:
	//TODO: make private
	SRI::String szProcessXMLMessage(const SRI::String& xmlMessage);
	
	SRI::String szCreateXMLReply(); //for now we assume it is robust and can parse correctly
	SRI::String szCreateXMLReply(bool retval); 
	SRI::String szCreateXMLReply(const SRI::String& retval);
	void vXMLDocToStringStream(std::stringstream& s, Poco::XML::Document* pDoc);
	
	Module(Component* c, int portNo);
	virtual ~Module();
	


	//void vSetComponent(Component* m_ptComponent);

	////TODO:should this have a logger ? a component status?

	////missing copy constructor, assignment operator, == operator

	////Component methods:

	//virtual SRI::String szGetID();
	//virtual SRI::String szGetComponentType() const;


	//virtual SRI::String szGetName() const;
	//virtual void vSetName(SRI::String name);

	//virtual Component* ptClone();
	//virtual ComponentStatus eGetStatus();
	//virtual void vSetStatus(ComponentStatus status);

	//virtual void vInit();
	//virtual void vFinalize();
	//virtual bool bHasMoreSteps();
	//virtual void vStep();
	//virtual void vPreStep();
	//virtual void vPostStep();

	//missing vSetIP




};

} // end namespace


#endif