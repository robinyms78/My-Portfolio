

#ifndef STUB_TEMPLATE_H
#define STUB_TEMPLATE_H

#include "Poco/ActiveMethod.h"
#include "Poco/Thread.h"
#include "SRI/SRIUtil/SRIString.h"
#include "Poco/Net/SocketAddress.h"
#include "Poco/Net/SocketReactor.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/StubServiceHandler.h"
#include <vector> 


namespace Poco {
	
	class Mutex;

	namespace Net {
		class StreamSocket;
		class SocketReactor;
	}

	namespace XML {
		class Document;
	}
} //end namespace Poco

namespace SRI {


/// Helper class providing functionality needed by Stubs
/**	The StubTemplate class provides methods used by all Stubs. These methods are 
	responsible for marshalling arguments to send to Servers, and for unpacking
	their replies.

	Stubs communicate with Servers via XML strings. A stub calls a function on the
	remote object by creating a string containing a single XML element named "function".	This element has a "name" attribute, which contains the name of the function that is to be
	called, and may have one or more attributes with the name "arg[X]" (where X 
	is a number) which contain the values of arguments supplied to the function.
	The first argument will have the name arg0, the second argument arg1, and so on.
	
	For example:<br>
	\<function name="szGetID" /><br>
	\<function name="iSetName" arg0="new_name" /><br>
	\<function name="iCreateOutputPort" arg0="name_of_port" arg1="type_of_port" /><br>

	There are no XML header tags nor metadata in the string, as it is assumed that
	all communication between Stubs and Servers will use XML strings of the format detailed above.

	The Server, after processing the incoming XML string and calling the desired function,
	returns the return value to the Stub by creating a string containing a single
	XML element named "reply". This element has two attributes: "rettype", which 
	identifies the type of the return value, and "retval", which contains the actual
	return value as a string. The currently supported return value types and their
	possible retvals are detailed below:

	<table>
	<tr><td>Rettype</td>			<td>Retval</td></tr>
	<tr><td>void</td>				<td>"" (empty string)</td></tr>
	<tr><td>unsigned int</td>		<td>\<string representation of valid unsigned values></td></tr>
	<tr><td>int</td>				<td>\<string representation of valid int values></td></tr>
	<tr><td>bool</td>				<td>"true"/"false"</td></tr>
	<tr><td>string</td>				<td>\<the literal string></td></tr>
	</table>

	NOTE: replies of type void do _not_ have the rettype attribute, only 
	the retval attribute.

	These are examples of valid replies:<br>
	\<reply retval=""> (void reply)<br>
	\<reply rettype="int" retval="3556"> (int reply)<br>
	\<reply rettype="bool" retval="false"> (bool reply)<br>
	\<reply rettype="string" retval="name of component"> (string reply)<br>

*/

class StubTemplate {
	
private: 
	
	static Ref<SRI::String> m_ptEmptyString; //to avoid overhead of empty string creation; see szCallFunction
	
	Logger m_tLog;
	
	SRI::String m_szPeerIp;
	int m_iPeerPort;
	SRI::String m_szMyIp; //as seen from peer


	StubTemplate(const StubTemplate& s);
	StubTemplate& operator=(const StubTemplate& s);

	

	

	mutable Poco::Mutex m_Mutex;

	Poco::Net::StreamSocket* m_ptSocket;

	Poco::Net::SocketReactor m_SocketReactor;
	StubServiceHandler* m_ptStubHandler;

	Poco::Thread m_Thread;

	SRI::String szCreateXMLMessage(const SRI::String& funcName, const std::vector<SRI::String>& args, int id) const;
		

	void vXMLDocToStringStream(std::stringstream& s, Poco::XML::Document* pDoc);
	SRI::String szParseReply(const SRI::String& reply) const; 

	///Blocks until reply message from module arrives
	SRI::String vGetMessage() const;

	Poco::ActiveMethod<SRI::String, SRI::String, StubTemplate> activeCallDispatch;
	SRI::String szCallDispatch(const SRI::String& msg);

public:
	/// Constructor
	/**
		\param ip IP of the Server to connect to
		\param portNo Port number of the Server to connect to
	*/
	StubTemplate(SRI::String ip, int portNo);
	virtual ~StubTemplate();

	//const method provided for use by const functions
	int szCallFunction(SRI::String funcName, const std::vector<SRI::String>& args, Ref<SRI::String> retstring) const;
	int szCallFunction(SRI::String funcName, Ref<SRI::String> retstring) const;

	

	/// Sends the shutdown signal to a server
	void vShutdownRemote() const;
	
	void vSendMessage(SRI::String msg) const;
 
	//missing copy constructor, assignment operator, == operator

	/// Returns the IP address of the associated Server
	SRI::String szGetPeerIp() const;
	/// Returns the port no of the associated Server
	int iGetPeerPort() const;
	
	/// Returns this StubTemplate's IP address, as seen by the associated Server
	SRI::String szGetMyIp() const;
	/// Returns this StubTemplate's port
	int iGetMyPort() const;

	
};

} // end namespace


#endif STUB_TEMPLATE_H