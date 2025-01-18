#ifndef SRI_RAW_MESSAGE_H
#define SRI_RAW_MESSAGE_H

#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIEngine/Message.h"

namespace SRI{

class SRI_E_API RawMessage: public Message{
private:
	/** strings don't support zero bytes */
	virtual SRI::String szGetContent(){return "";}
	virtual void vSetContent(SRI::String message);

protected:
	unsigned char* m_ptBuffer;
	unsigned int m_iSize;

	
public:
	RawMessage();
	virtual ~RawMessage();
	RawMessage(const RawMessage& c);
	/** Takes over the memory */
	RawMessage(unsigned char* buffer, unsigned int size);
	/** Memory is copied */
	RawMessage(const unsigned char* buffer, const unsigned int size);
	RawMessage& operator=(const RawMessage& c);
	virtual bool operator==(const RawMessage& c);

	virtual const unsigned char* ptGetContent() const;
	virtual const unsigned int iGetContentSize() const;

	virtual SRI::String szGetMessage();
	
	/** This functiont takes over the memory*/
	virtual void vSetContent(unsigned char* buffer, unsigned int size);

	/** expects an XML string with embedded CDATA text */
	virtual int iSetMessage(SRI::String message);
//
//#ifdef USE_TINYXML
//	virtual int iSetMessage(TiXmlElement* txMessage);
//#endif
//
	virtual Message* ptClone() const;
};

} // end namespace

#endif