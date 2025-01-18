#ifndef SRI_OBJECT_MESSAGE_H
#define SRI_OBJECT_MESSAGE_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/SRIEngine/RawMessage.h"
#include "SRI/SRIUtil/Serializable.h"
#include "SRI/SRIUtil/SRIRef.h"

namespace SRI{

INST_SRI_E_TEMPL SRI::Ref<SRI::Serializable>;

class SRI_E_API ObjectMessage: public Message{

private:
	SRI::Ref<SRI::Serializable> m_ptObj;

public:
	ObjectMessage();
	virtual ~ObjectMessage();
	ObjectMessage(const ObjectMessage& c);

	/** Calls the toString method to serialize the object and sets the
	* message content. It doesn't store an object reference.*/
	ObjectMessage(const SRI::Serializable& obj);
	/** Instead of immediate serialization an object reference is stored.
	* the object is only serialized when necessary */
	ObjectMessage(SRI::Ref<SRI::Serializable> obj);
	ObjectMessage& operator=(const ObjectMessage& c);
	

	virtual Message* ptClone() const;

	/** The object is serialized to string (call of toString method) and 
	* stored as message conent. No object reference is stored. */
	virtual void vSetContent(const SRI::Serializable& obj);

	/** Stores only the object reference for serialization if communicated
	* through ports */
	virtual void vSetObject(SRI::Ref<SRI::Serializable> obj);
	
	template <class T> int iInitObject(T* obj){
		if(obj != NULL){
			return obj->iFromString(m_szMessage);
		}
		return SRI::SRI_ERR_NULL;
	}

	/** If object reference is already set, it is returned. If it is not
	* set, it uses the given type to initialize from xml data.
	*/
	template <class T> SRI::Ref<T> ptGetObjectRef(){
		if(m_ptObj.bIsValid()){
			return m_ptObj;
		}else{
			T* ptObj = new T();
			if( ptObj->iFromString(m_szMessage) == SRI_OK){
				m_ptObj.ptAttachNew(ptObj);
				return m_ptObj;
			}else{
				delete ptObj;
			}
		}

		return SRI::Ref<SRI::Serializable>((SRI::Serializable*)NULL);
	}

	virtual SRI::String szGetMessage();
	SRI::String  ObjectMessage::szGetContent();

};


}


#endif