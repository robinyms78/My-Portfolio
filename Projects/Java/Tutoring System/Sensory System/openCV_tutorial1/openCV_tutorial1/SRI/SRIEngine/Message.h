#ifndef SRI_MESSAGE_H
#define SRI_MESSAGE_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/Cloneable.h"

#ifdef USE_TINYXML
class TiXmlElement;
#else 

#endif



namespace SRI{




/// An abstraction representing a message that is sent from an OutputPort to an InputPort

class SRI_E_API Message: public SRI::Cloneable{


	
protected:
	SRI::String m_szMessage;
	SRI::String m_szContentType;   // is the type of the object that is being send (given by the szGetObjType function of the serializable interface
	SRI::String m_szMessageType;  // this is the containter type
	SRI::String m_szSender;

public:
	Message();
	virtual ~Message();
	Message(const Message& c);
	Message(const SRI::String m);
	Message& operator=(const Message& c);

	virtual bool operator==(const Message& c);

	/** Sets the string content of the message */
	virtual void vSetContent(SRI::String message);

	/** This functiont takes over the memory. The memory must be initialized using the
	* the array operator new T[] because it is released using delete[]*/
	virtual void vSetContent(unsigned char* buffer, unsigned int size);

	/** This function returns just the message content encoded as string (no xml message envelope) */
	virtual SRI::String szGetContent();
	
	/** This function embeds the message in an xml envelope. It returns the whole encoded message. */
	virtual SRI::String szGetMessage() const;

	/** sets message with xml envelope */
	virtual int iSetMessage(SRI::String message);

	virtual void vSetSender(SRI::String sender);

//
//#ifdef USE_TINYXML
//	virtual int iSetMessage(TiXmlElement* txMessage);
//#endif

	virtual Message* ptClone() const;
	/** \returns the type of the object in the message. In case of the base message it is string.
	* In case of RawMessage it returns byteBuffer*/
	virtual SRI::String szGetContentType() const;
	/** \returns the container type (message, rawMessage, objectMessage) */ 
	virtual SRI::String szGetMessageType() const;

	virtual SRI::String szGetSender() const;

};

} // end namespace

#endif
