#ifndef SRI_SRIML_SRIMLSAXHANDLER_H
#define SRI_SRIML_SRIMLSAXHANDLER_H
#include "Poco/SAX/SAXParser.h"
#include "Poco/SAX/ContentHandler.h"
#include "Poco/SAX/LexicalHandler.h"
#include "Poco/SAX/Attributes.h"
#include "Poco/SAX/Locator.h"
#include "Poco/Exception.h"

#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIRef.h"

#include <iostream>
#include <stack>

namespace SRI {

class MLComponent;
class Component;
class SRIRegistry;

class SRIMLSAXHandler: public Poco::XML::ContentHandler, public Poco::XML::LexicalHandler
{

private:
	const Poco::XML::Locator* _pLocator;
	std::stack<SRI::Ref<SRI::Component>> m_componentStack; 
	SRI::Ref<Component> m_ptLastPoppedComponent;
	SRI::Ref<Component> m_ptFinalComponent; //TODO: expand to list for several script tags
	Logger m_tLog;
	SRI::Ref<SRIRegistry> m_ptRegistry;

	

protected:
	void where(const std::string& meth);

public:
	SRIMLSAXHandler(SRI::Ref<SRIRegistry> eng);
	~SRIMLSAXHandler();

	// ContentHandler
	void setDocumentLocator(const Poco::XML::Locator* loc);
	void startDocument();
	void endDocument();
	void startElement(const Poco::XML::XMLString& uri, const Poco::XML::XMLString& localName, const Poco::XML::XMLString& qname, const Poco::XML::Attributes& attributes);
	void endElement(const Poco::XML::XMLString& uri, const Poco::XML::XMLString& localName, const Poco::XML::XMLString& qname);
	void characters(const Poco::XML::XMLChar ch[], int start, int length);
	void ignorableWhitespace(const Poco::XML::XMLChar ch[], int start, int length);
	void processingInstruction(const Poco::XML::XMLString& target, const Poco::XML::XMLString& data);
	void startPrefixMapping(const Poco::XML::XMLString& prefix, const Poco::XML::XMLString& uri);
	void endPrefixMapping(const Poco::XML::XMLString& prefix);
	void skippedEntity(const Poco::XML::XMLString& name);
	
	// LexicalHandler
	void startDTD(const Poco::XML::XMLString& name, const Poco::XML::XMLString& publicId, const Poco::XML::XMLString& systemId);
	void endDTD();
	void startEntity(const Poco::XML::XMLString& name);
	void endEntity(const Poco::XML::XMLString& name);
	void startCDATA();
	void endCDATA();
	void comment(const Poco::XML::XMLChar ch[], int start, int length);
	
	SRI::Ref<Component> ptGetFinishedComponent();
	

};

} //end namespace

#endif SRI_SRIML_SRIMLSAXHANDLER_H

