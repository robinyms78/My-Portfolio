
#ifndef SRI_PTR_H
#define SRI_PTR_H

#include <typeinfo>
#include "SRI/SRIUtil/SRIUtilLib.h"
#include "SRI/SRIUtil/SRIRefCounted.h"

namespace SRI{

/** Be careful when using this class directly. Not taking the ownership might cause memory leaks.
* But taking ownership of a resource that is managed by someone else might cause access violations */
template <class T> class Ptr : public RefCounted{
	 template <class T> friend class Ref;
private:
	T* m_ptObj;	
	bool m_bOwner; // this flag controls if the pointer is released when the Ptr goes out of scope (default = true)


	/** Only one can release a resource. Use SRI::Ref for this to be handled correctly. 
	* Pointer might be invalidiated by reference managed copy. 
	*/
	Ptr(const Ptr<T>& c): RefCounted(c){
		m_ptObj = c.m_ptObj;
		m_bOwner = false;
	}

	/** Only one can release a resource. Use SRI::Ref for this to be handled correctly. 
	* Pointer might be invalidiated by reference managed copy. 
	*/
	Ptr<T>& operator=(const Ptr<T>& c){
		if(this == &c){
			return *this;
		}
		vRelease();
		RefCounted::operator=(c);
		m_ptObj = c.m_ptObj;

		m_bOwner = false;
		return *this;
	}


public:
	Ptr(): RefCounted(), m_ptObj(NULL), m_bOwner(true){
		m_eRefType = RefCounted::PTR_COUNTED;
	};
	
	/** If takeOwnership is true then the pointer will release memory*/
	Ptr(T* obj, bool takeOwnership = true): RefCounted(), m_ptObj(obj), m_bOwner(takeOwnership){
		m_eRefType = RefCounted::PTR_COUNTED;
	}

	/** The pointer to the resource is set so that an external process can monitor the validity 
	* of the resource. */
	Ptr(T**& obj, bool takeOwnership = true): RefCounted(), m_ptObj(NULL), m_bOwner(takeOwnership){
		m_eRefType = RefCounted::PTR_COUNTED;
		if(obj != NULL){
			m_ptObj = *obj;
			obj = &m_ptObj;
		}
	}

	virtual ~Ptr(){
		vRelease();
	}

	T* ptObj(){return m_ptObj;}

	void vSetObject(T* obj, bool takeOwnership = true){
		vRelease();
		m_ptObj = obj;
		m_bOwner = takeOwnership;
	}

	T& operator*(){
		return *m_ptObj;
	}

	T* operator->(){
		if(m_ptObj == NULL){
			return NULL;
		}else{
			return m_ptObj;
		}
	}

	bool operator==(const Ptr<T> c){
		return (m_ptObj == c.m_ptObj);
	}

	operator bool() const{     // cast to bool operator to allow  SRIPre<MyClass> ptr; if(ptr){ ...}
		return (m_ptObj != NULL);
	}

	bool bIsValid() const{
		return (m_ptObj != NULL);
	}

	///** Converts reference to given type. It does NOT own
	//* the ptr. Therefore if the orginal gets deleted 
	//* the converted one is invalid */
	//template<class P> operator Ptr<P>() const{
	//	Ptr<P> res;
	//	res.m_ptObj = dynamic_cast<P*>(m_ptObj);
	//	res.m_bOwner = false;
	//}

	void vRelease(){
		if(m_ptObj != NULL){
			if(m_bOwner){
				delete m_ptObj;
			}
			m_ptObj = NULL;
		}
	}

	void vIncRef(){
		RefCounted::vIncRef();
	}

	int iDecRef(){
		return RefCounted::iDecRef();
	}

	int iRefCount()const{
		return RefCounted::iRefCount();
	}

	/** This function frees an object from ptr supervision and returns it
	* The caller is responsible to release memory. 
	*/
	T* ptUnlink(){
		T* temp = m_ptObj;
		m_ptObj = NULL;
		m_bOwner = false;
		return temp;
	}

	T** pptGetAddress(){
		if(m_ptObj != NULL){
			return &m_ptObj;
		}

		return NULL;
	}
};


} // end namespace



#endif





