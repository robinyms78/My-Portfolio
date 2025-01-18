

#ifndef SRI_MODULE_STUB_H
#define SRI_MODULE_STUB_H

#include "Component.h"
#include <sstream>
#include <vector>
//#include "Poco\Net\StreamSocket.h"

namespace Poco {
	namespace Net {
		class StreamSocket;
	}

	namespace XML {
		class Document;
	}
}

namespace SRI{

typedef enum{
	SZGETID,
	SZGETCOMPONENTTYPE,
	SZGETNAME,
	ISETNAME,
	PTCLONE,
	EGETSTATUS,
	VSETSTATUS,
	VINIT,
	VFINALIZE,
	BHASMORESTEPS,
	VSTEP,
	VPRESTEP,
	VPOSTSTEP
} CalledFunction;

//Provides interface on socket level
//Ports of Modules use sockets for conenction
class SRI_E_API ModuleStub : public Component{
	friend class SRIEngine; //sets the ID of the module

private: 
	Poco::Net::StreamSocket* m_ptSocket;

	SRI::String szCreateXMLMessage(SRI::String funcName, std::vector<SRI::String>* args) const;
	


	SRI::String szCallFunction(SRI::String funcName, std::vector<SRI::String>* args) const;
	

	void vXMLDocToStringStream(std::stringstream& s, Poco::XML::Document* pDoc);
	SRI::String szParseReply(const SRI::String& reply); //TODO: make more robust?? more versatile for bool?
	SRI::String szParseReply(const SRI::String& reply) const; 


	///Blocks until reply message from module arrives
	SRI::String vGetMessage() const;

	void vSetId(SRI::String id); 


public:
	ModuleStub(SRI::String name, int portNo);
	//Module(Component* c);
	virtual ~ModuleStub();

	void vStopModule();

		//Component methods:

	virtual SRI::String szGetID();
	virtual SRI::String szGetComponentType() const;

	virtual SRI::String szGetName() const;
	virtual int iSetName(SRI::String name);

	//virtual Component* ptClone();
	//virtual ComponentStatus eGetStatus();
	//virtual void vSetStatus(ComponentStatus status);

	virtual void vInit();
	virtual void vFinalize();
	virtual bool bHasMoreSteps();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();

	//missing vSetIP

	//TODO: move to private
	SRI::String szCreateXMLReply(); //for now we assume it is robust and can parse correctly
	SRI::String szCreateXMLReply(bool retval); 
	SRI::String szCreateXMLReply(const SRI::String& retval);
	SRI::String szCreateXMLReply(int retval);

	SRI::String szProcessXMLMessage(const SRI::String& xmlMessage);	
	SRI::String szCallFunction(SRI::String funcName, std::vector<SRI::String>* args);
	//though it's not ture that szCallFunction is const in the full sense of the word, if 
	//the ModuleStub is const then the only method that is callable is szGetname, so effectively
	//it's ok, because the const szCallFunction is private 

 //TODO: should use enum vals for funcName?

	//void vSetComponent(Component* m_ptComponent);

	//TODO:should this have a logger ? a component status?

	//missing copy constructor, assignment operator, == operator






};

} // end namespace


#endif