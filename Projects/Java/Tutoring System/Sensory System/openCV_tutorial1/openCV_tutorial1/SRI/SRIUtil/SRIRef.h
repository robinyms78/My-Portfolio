#ifndef SRI_REF_H
#define SRI_REF_H

#include <typeinfo>
#include "SRI/SRIUtil/SRIUtilLib.h"
#include "SRI/SRIUtil/SRIRefCounted.h"
#include "SRI/SRIUtil/SRIPtr.h"

/** ***************************************************************************
*   Comments
*******************************************************************************
*   Enclose als dynamic_cast operators in try-catch. Otherwise the catch of the
*   cxxTest framework will be triggered. This is unintentional because the
*   return of the dynamic_cast only tells the result of a type comparison.
*
* The role of the different Reference types:
*
* 1) SRI_REF
* 2) SRI_WEAK_REF
* 3) SRI_COUNTER_REF
*
* The SRI_REF is the standard reference. It manages an assigned resource and frees
* the memory if the counter of references drops to zero. The principle of smart
* references work as follows: The managed object is placed inside a RefCounted
* container. This is usually the Ptr<T> class. The Ptr<T> class also supports
* not to take over the ownership over the object T. Everytime a reference is
* created/copyied/assigned the container counter increases. However, the
* refCount counter only increases if the type of reference is SRI_REF or
* SRI_COUNTER_REF. This allows weak references to not block the deletion
* of an object. Furthermore, the container stays intact to that even
* weak references can do checks on validity of the object. 
*
* For special resources a new subclass of RefCounted might be created as a handler.
* The handler is a container for the resource. The SRI::Ref<T> class can handle
* the reference count for this object. If the handle should not be destroyed
* after the last SRI::Ref goes out of scope, the reference has to be created
* with SRI_COUNTER_REF as parameter. This effectively increases the container
* ref count by an additional increment and therefore prevents that the container
* is deleted afterwards. (USE WITH CARE: Memory leaks can be created this way)
*
* The SRI_WEAK_REF does not increase or decrease the counter. In case the counter
* drops to zero while a weakreference still links to it, the link becomes invalid.
* The advantage is that weak references do not block the free of memory.
*
* 
*/


namespace SRI{


typedef enum{
	SRI_REF = 1,
	SRI_WEAK_REF,
	SRI_COUNTER_REF
}tRefType;


template <class T> class Ref{
	
protected:
	RefCounted* m_ptRef;
	static void vDecRef(RefCounted** ref, tRefType type);  // keep the parameter to be able to release temporary old instances
	
	static void vIncRef(RefCounted** ref, tRefType type);
	static void vDecContainerRef(RefCounted** ref);  
	static void vIncContainerRef(RefCounted** ref);

	tRefType m_eRefType;
	void vSetRefType(tRefType type);
	/** This function returns if the managed object is a Ptr container.*/
	bool bIsPtrCont(RefCounted* ref) const; // to check if the RefCounted object is a Ptr container or a base RefCounted container
	                                        // if the first is true the Ptr access functions have to be used to get to the object

public:
	Ref();
	
	/** This will place the given object under ref counting of the Ref class.
	* When the Ref goes out of scope the following rules apply: 
	* If the given ref type is SRI_WAEK_REF or SRI_COUNTER_REF the object is
	* not deleted afterwards. However it is guaranteed to exist as long as 
	* there are references of Ref to the object. The SRI_COUNTER_REF protects
	* container and resource whereas SRI_WEAK_REF only protects the resource.
	* (To use with RefCounted derived class specify the useCustomContainer flag.
	* Any value would do. It is just to disambigue with the Ref(T*, bool TakeOwnership = true)
	* constructor*/
	Ref(RefCounted* obj, tRefType type, int useCustomContainer);
	
	/** The same rules hold as for the above. Take ownership is not necessary as the actual T object is
	* maintained by the Ptr<T> class. The memeory of the Ptr<T> object is controlled by the
	* reference type.*/
	Ref(Ptr<T>* obj, tRefType type);
	
	/** This will construct a Ptr<T> around the object to keep track of references. 
	* Therefore it is of type SRI_REF to release this container.
	* The takeOwnership flag is passed to Ptr and manages if object is released*/
	Ref(T* obj, bool takeOwnership = true);

	//Ref(const Ptr<T>* obj);

	Ref(const Ref<T>& c);
	template <class P> Ref(Ref<P>& c);
	virtual ~Ref();


	/** Explicitly frees the hold reference (refcount - 1) if type is of SRI_REF or SRI_COUNTER_REF. 
	* If it was the last the object is released immediately. The reference is implicitlty converted
	* to a weakref to make sure the object is not released again on destruction of the Ref container.
	* */	
	virtual void vRelease();
	// Once an object is managed by a reference the only way to protect it from deletion is to fake
	// add the refcount so that also the last reference still doesn't delete it
	// Any other way of deleting the object before might invalidate other Ref instances pointing to 
	// the same object

	virtual T& operator*();

	virtual RefCounted* ptGetManagedPtr();
	virtual RefCounted* ptGetManagedPtr() const;

	virtual Ref<T>& operator=(const Ref<T>& c);
	/** Sets a new refcounted object. It also increases the recount by one*/
	virtual Ref<T>& operator=(RefCounted* obj);
	virtual Ref<T>& operator=(T* obj);
	/** Memory is taken over */
	virtual Ref<T>& operator=(Ptr<T>* obj);
	//virtual Ref<T>& operator=(const Ptr<T>* obj);
	template <class P> Ref<T>& operator=(Ref<P>& c);

	/** Retruns a pointer to the associated object (casted to the derived object type)*/
	virtual T* operator->();
	virtual T* operator->() const;
	virtual T* ptGetObj() const;
	//virtual operator T*(); // implicit cast commented out because too many operators have similar conversions

	virtual bool operator==(const Ref<T>& c)const;
	virtual bool operator!=(const Ref<T>& c)const;

	//virtual bool operator==(const RefCounted* obj)const;
	//virtual bool operator!=(const RefCounted* obj)const;

	//virtual bool operator==(const T* obj)const;
	//virtual bool operator!=(const T* obj)const;

	virtual operator bool() const;    // cast to bool operator to allow  Ref<MyClass> ref; if(ref){ ...}
	virtual bool bIsValid() const;
	template <class P> operator Ref<P>() const;  // cast to a reference of type P
	
	/** Attaches a new object to the reference. It decreases the counter of the current handled object (causing it to free if it reacehs 0).
	* \returns A pointer to the internal handle for monitoring purposes
	* If the object given is of type RefCounted then the ref type is evaluated. In case SRI_WEAK_REF or SRI_COUNTER_REF
	* is given, the obj container is not released. In case the object is of any other type, the takeOwnership
	* flag is defines if the object should be released with the reference. The three parameters are evaluated depending on the
	* type of obj. 
	*/
	virtual RefCounted** ptAttachNew(T* obj, tRefType type = SRI_REF, bool takeOwnership = true);
	virtual RefCounted** ptAttachNew(Ptr<T>* obj, tRefType type = SRI_REF);

	virtual Ref<T> tGetCounterRef();
	virtual Ref<T> tGetWeakRef();
	virtual Ref<T> tGetFullRef();

	virtual tRefType eGetRefType() const;
	virtual int iRefCount() const;
	virtual int iContainerRefCount() const;
};




//=================================================================================
//================ private functions ==============================================
//=================================================================================

template <class T>	void Ref<T>::vDecContainerRef(RefCounted** ref){
	if (( ref != NULL) && (*ref != NULL)) {
		if((*ref)->iDecContainerCount() == 0){
			delete *ref;
			*ref = NULL;
		}
	}
}

template<class T> void Ref<T>::vIncContainerRef(RefCounted** ref){
	if ( (ref != NULL) && ((*ref) != NULL) ){
		(*ref)->vIncContainerCount();
	}
}

/** A helper function to release objs/ temp objects */
template <class T>	void Ref<T>::vDecRef(RefCounted** ref, tRefType type){
	if (( ref != NULL) && (*ref != NULL)) {

		int nRef = 0;
		if((type == SRI_REF) || (type == SRI_COUNTER_REF)){
			nRef = (*ref)->iDecRef();
			if(nRef == 0){
				(*ref)->vRelease();
			}
		}
		
		if((*ref)->iDecContainerCount() == 0){
			delete *ref;
			*ref = NULL;
		}
		//*ref = NULL;
	}
}

template<class T> void Ref<T>::vIncRef(RefCounted** ref, tRefType type){
	if ( (ref != NULL) && ((*ref) != NULL) ){

		if((type == SRI_REF) || (type == SRI_COUNTER_REF)){
			(*ref)->vIncRef();	
		}
		(*ref)->vIncContainerCount();
	}
}

template<class T> void Ref<T>::vSetRefType(tRefType type){
	m_eRefType = type;
}


template<class T> bool Ref<T>::bIsPtrCont(RefCounted* ref) const{
	if(ref != NULL){
		return (ref->eGetContainerType() == RefCounted::PTR_COUNTED);
	}else{
		return false;
	}
}

//=================================================================================
//============= Constructors ======================================================
//=================================================================================

template <class T> Ref<T>::Ref(): m_ptRef(NULL), m_eRefType(SRI_REF){
}

template <class T>	Ref<T>::Ref(T* obj, bool takeOwnership): m_eRefType(SRI_REF){
	if(obj != NULL){
		m_ptRef = new Ptr<T>(obj, takeOwnership);
		vIncRef(&m_ptRef, m_eRefType);
	}else{
		m_ptRef = NULL;
	}
}

//template <class T>	Ref<T>::Ref(T**& obj, bool takeOwnership): m_ptRef(NULL), m_eRefType(SRI_REF){
//		m_ptRef = new Ptr<T>(obj, takeOwnership);
//		vIncRef(&m_ptRef, m_eRefType);
//	}

template <class T>	Ref<T>::Ref(Ptr<T>* obj, tRefType type): m_ptRef(obj), m_eRefType(type){
	vIncRef(&m_ptRef, m_eRefType);
	if(m_ptRef != NULL){
		if(( m_eRefType == SRI_WEAK_REF) || (m_eRefType == SRI_COUNTER_REF)){
			m_ptRef->vIncContainerCount();
		}
	}
}

template <class T>	Ref<T>::Ref(RefCounted* obj, tRefType type,  int useCustomContainer): m_ptRef(obj), m_eRefType(type){
	vIncRef(&m_ptRef, m_eRefType);
	if(m_ptRef != NULL){
		if(( m_eRefType == SRI_WEAK_REF) || (m_eRefType == SRI_COUNTER_REF)){
			m_ptRef->vIncContainerCount();
		}
	}
}


//template <class T>	Ref<T>::Ref(const Ptr<T>* obj): m_ptRef(NULL), m_eRefType(SRI_REF){
//		if(obj != NULL){
//			m_ptRef = new Ptr<T>(*obj);
//		}else{
//			m_ptRef = new Ptr<T>((T*)NULL);
//		}
//		vIncRef(&m_ptRef, m_eRefType);
//	}


template <class T>	Ref<T>::Ref(const Ref<T>& c){
		m_ptRef = c.m_ptRef;
		m_eRefType = c.m_eRefType;
		
		vIncRef(&m_ptRef, m_eRefType);

	}

template <class T> template <class P> Ref<T>::Ref(Ref<P>& c){
	
	//Ptr<P>* refP = NULL;
	//try{
	//	refP = dynamic_cast<Ptr<P>*>(c.ptGetManagedPtr());		
	//}catch(...){}

	//check if classes are convertible
	if(bIsPtrCont(c.ptGetManagedPtr())){
	//if(refP != NULL){
		Ptr<P>* refP = static_cast<Ptr<P>*>(c.ptGetManagedPtr());
		T* typeTest = NULL;
		try{
			if(refP != NULL){
				typeTest = dynamic_cast<T*>(refP->ptObj());
			}
		}catch(...){}
		if( typeTest != NULL){
			m_ptRef = static_cast<Ptr<T>*>(c.ptGetManagedPtr());
		}else{
			m_ptRef = NULL;
		}
	}else{
		m_ptRef = c.ptGetManagedPtr();
	}

	m_eRefType = c.eGetRefType();	
	vIncRef(&m_ptRef, m_eRefType);
}

template <class T>	 Ref<T>::~Ref(){
		vDecRef(&m_ptRef, m_eRefType);	
		m_ptRef = NULL; //mark reference as not holding any locks
	}

template <class T>	void Ref<T>::vRelease(){
	vDecRef(&m_ptRef, m_eRefType);
	m_eRefType = SRI_WEAK_REF; 
	m_ptRef = NULL; //mark reference as not holding any locks
}


template <class T>	T& Ref<T>::operator*(){
		/*Ptr<T>* ref = NULL;
		try{
			ref = dynamic_cast<Ptr<T>*>(m_ptRef);		
		}catch(...){}
		if(ref != NULL){ */

		if(bIsPtrCont(m_ptRef)){
			Ptr<T>* ref = static_cast<Ptr<T>*>(m_ptRef);
			if(ref != NULL){
				return (*(ref->ptObj()));
			}else{
				*ref;
			}
		}

		T* ptr = NULL;
		try{
			ptr = dynamic_cast<T*>(m_ptRef);
		}catch(...){}
		
		return *ptr;
	}


template <class T>	RefCounted* Ref<T>::ptGetManagedPtr(){
		return m_ptRef;
	}

template <class T> RefCounted* Ref<T>::ptGetManagedPtr() const{
	return m_ptRef;
}

template <class T> Ref<T>& Ref<T>::operator=(const Ref<T>& c){
		if((void*)this == (void*)&c){
			return *this;
		}
		
		RefCounted* oldRef = m_ptRef;
		m_ptRef = c.m_ptRef;

		vIncRef(&m_ptRef, c.m_eRefType);

		// Release old reference if allowed
		vDecRef(&oldRef, m_eRefType);
		m_eRefType = c.m_eRefType;  // take over the type

		return *this;
	}

	/** Sets a new refcounted object. It also increases the recount by one
	* It will take over the memory and convert the reference in SRI_REF type
	*/
template <class T> Ref<T>& Ref<T>::operator=(RefCounted* obj){
		if(obj == m_ptRef){
			return *this;
		}
		
		RefCounted* oldRef = m_ptRef;
		m_ptRef = obj;
		
		vIncRef(&m_ptRef, SRI_REF);
		
		vDecRef(&oldRef, m_eRefType);
		m_eRefType = SRI_REF;
		
		return *this;
	}

template <class T> Ref<T>& Ref<T>::operator=(T* obj){
		if((RefCounted*)obj == m_ptRef){
			return *this;
		}

		/*Ptr<T>* ptr = NULL;
		try{
			ptr = dynamic_cast<Ptr<T>*>(m_ptRef);
		}catch(...){}

		if(ptr != NULL){*/
		if(bIsPtrCont(m_ptRef)){ // check if object already set in Ptr cont
			Ptr<T>* ptr = static_cast<Ptr<T>*>(m_ptRef);
			if( (ptr != NULL) && (ptr->ptObj() == obj)){
				return *this;
			}
		}

		ptAttachNew(obj);
		return *this;
	}

/** Sets a new refcounted object. It also increases the recount by one
	* It will take over the memory and convert the reference in SRI_REF type
	*/
template <class T> Ref<T>& Ref<T>::operator=(Ptr<T>* obj){
		if((RefCounted*)obj == m_ptRef){
			return *this;
		}

		RefCounted* oldRef = m_ptRef;
		m_ptRef = obj;
		
		vIncRef(&m_ptRef, SRI_REF);
		
		vDecRef(&oldRef, m_eRefType);
		m_eRefType = SRI_REF;

		return *this;
	}


///** Automatically converts the ref type to SRI_COUNTER_REF */
//template <class T> Ref<T>& Ref<T>::operator=(const Ptr<T>* obj){
//		if((RefCounted*)obj == m_ptRef){
//			return *this;
//		}
//
//		RefCounted* oldRef = m_ptRef;
//
//		if(obj != NULL){
//			m_ptRef = new Ptr<T>(*obj); // copy constructor of obj
//		}else{
//			m_ptRef = new Ptr<T>((T*)NULL);
//		}
//		
//		vIncRef(&m_ptRef, SRI_REF);
//		
//		vDecRef(&oldRef, m_eRefType);
//		m_eRefType = SRI_COUNTER_REF;
//
//		return *this;
//	}


template <class T> template <class P> Ref<T>& Ref<T>::operator=(Ref<P>& c){
		if((void*)this == (void*)&c){
			return *this;
		}
		
		RefCounted* oldRef = m_ptRef;
		
		
	/*	Ptr<P>* refP = NULL;
		try{
			refP = dynamic_cast<Ptr<P>*>(c.ptGetManagedPtr());		
		}catch(...){}

		if(refP != NULL){*/
		
		if(bIsPtrCont(c.ptGetManagedPtr())){
			Ptr<P>* refP = static_cast<Ptr<P>*>(c.ptGetManagedPtr());
			T* typeTest = NULL;
			try{
				if(refP != NULL){
					typeTest = dynamic_cast<T*>(refP->ptObj());
				}
			}catch(...){}
			if( typeTest != NULL){
				m_ptRef = static_cast<Ptr<T>*>(c.ptGetManagedPtr());
			}else{
				m_ptRef = NULL;
			}
		}else{
			m_ptRef = c.ptGetManagedPtr();
		}

		vIncRef(&m_ptRef, c.eGetRefType());

		// Release old reference if allowed
		vDecRef(&oldRef, m_eRefType);
		m_eRefType = c.eGetRefType();  // take over the type

		return *this;
}

	// TODO check if -> operator works in all cases  (RefCounted object, Ptr object, plain object)
	/** Retruns a pointer to the associated object (casted to the derived object type)*/
template <class T> T* Ref<T>::operator->(){
		return ptGetObj();
	}

template <class T> T* Ref<T>::operator->() const{
		return ptGetObj();
	}

template <class T> T* Ref<T>::ptGetObj() const{
	/*Ptr<T>* ptr = NULL;
	try{
		ptr = dynamic_cast<Ptr<T>*>(m_ptRef);
	}catch(...){}

	if(ptr != NULL){*/
	
	if(bIsPtrCont(m_ptRef)){
		Ptr<T>* ptr = static_cast<Ptr<T>*>(m_ptRef);
		if(ptr != NULL){
			return ptr->ptObj();
		}
	}

	T* ret = NULL;
	try{
		ret = dynamic_cast<T*>(m_ptRef);
		//ret = (T*)m_ptRef;
	}catch(...){}

	if(ret != NULL){
		return ret;
	}

	return NULL;
}

//template <class T> Ref<T>::operator T*(){
//		Ptr<T>* ptr = NULL;
//		try{
//			ptr = dynamic_cast<Ptr<T>*>(m_ptRef);
//		}catch(...){}
//
//		if(ptr != NULL){
//			return ptr->ptObj();
//		}
//
//		T* ret = NULL;
//		try{
//			T* ret = dynamic_cast<T*>(m_ptRef);
//		}catch(...){}
//
//		if(ret != NULL){
//			return ret;
//		}
//
//		return NULL;
//	}



template <class T> bool Ref<T>::operator==(const Ref<T>& c)const{

		/*Ptr<T>* ref = NULL;
		Ptr<T>* cref = NULL;

		try{	
			ref = dynamic_cast<Ptr<T>*>(m_ptRef);
		}catch(...){}

		try{	
			cref = dynamic_cast<Ptr<T>*>(c.m_ptRef);
		}catch(...){}

		if( (ref != NULL) && (cref != NULL)){*/

		if( (bIsPtrCont(m_ptRef)) && (bIsPtrCont(c.m_ptRef))) {
			Ptr<T>* ref = static_cast<Ptr<T>*>(m_ptRef);
			Ptr<T>* cref = static_cast<Ptr<T>*>(c.m_ptRef);
			if((ref != NULL) && (cref != NULL)){
				return (ref->ptObj() == cref->ptObj());
			}
		}
		
		return m_ptRef == c.m_ptRef;
		
	}

template <class T> bool Ref<T>::operator!=(const Ref<T>& c)const{
		return !(*this == c);
	}


//template <class T> bool Ref<T>::operator==(const RefCounted* obj)const{
//	return (m_ptRef == obj);
//}
//
//template <class T> bool Ref<T>::operator!=(const RefCounted* obj)const{
//	return (m_ptRef != obj);
//}
//
//template <class T> bool Ref<T>::operator==(const T* obj)const{
//		Ptr<T>* ref = NULL;
//	
//		try{	
//			ref = dynamic_cast<Ptr<T>*>(m_ptRef);
//		}catch(...){}
//
//		
//		if( ref != NULL) {
//			return (ref->ptObj() == obj);
//		}else{
//
//			T* tref = NULL;
//			try{	
//				tref = dynamic_cast<T*>(m_ptRef);
//			}catch(...){}
//
//			if(tref != NULL){
//				return (tref == obj);
//			}else{
//				return false;
//			}
//		}
//		return false;
//}
//
//template <class T> bool Ref<T>::operator!=(const T* obj)const{
//	return !(*this == obj);
//}


template <class T> Ref<T>::operator bool() const{     // cast to bool operator to allow  Ref<MyClass> ref; if(ref){ ...}
		return bIsValid();
	}

template <class T> bool Ref<T>::bIsValid() const{
	if(m_ptRef == NULL){
		return false;
	}

	/*	Ptr<T>* ptr = NULL; 
	try{
	ptr = dynamic_cast<Ptr<T>*>(m_ptRef);
	}catch(...){}

	if(ptr != NULL){
	return ptr->bIsValid();
	}*/

	return m_ptRef->bIsValid();
}

template <class T> template <class P> Ref<T>::operator Ref<P>() const{
	Ref<P> res;

	if(m_ptRef == NULL){
		return res;
	}

	if(bIsPtrCont(m_ptRef)){
		Ptr<T>* refT = static_cast<Ptr<T>*>(m_ptRef);
		P* typeTest = NULL;
		try{
			if(refT != NULL){
				typeTest = dynamic_cast<P*>(refT->ptObj());
			}
		}catch(...){}
		if( typeTest != NULL){
			Ptr<P>* newRef = static_cast<Ptr<P>*>(m_ptRef);
			res.ptAttachNew(newRef, m_eRefType);
		}else{

		}
	}else{
		try{
			P* newRef = dynamic_cast<P*>(m_ptRef);
			res.ptAttachNew(newRef, m_eRefType, false);                    /// TODO:
		}catch(...){}
	}

	return res;
}


/** Convenience function that automatically manages a Ptr<T> class. The type will be automatically SRI_REF.
* There are no seperate implementations such as  ptAttachNew(T* obj, bool takeOwnership) and ptAttachNew(RefCounted* ref, tRefType type)
* because it causes compiler errors as
* multiple implicit conversions match the function definition. For example,
* the compiler cannot decide between:
*          class MyClass: public RefCounted{};
*          MyClass* m= new MyClass();			
*          SRI::Ref<MyClass> ref;
*          ref.ptAttachNew(m, SRI_REF);
* The last line matches  (T*, true)  and (RefCounted*, SRI_REF)
* As a solution, the ptAttachNew(T*, SRI_REF, false) has three parameters that
* are evaluated on demand.
 */
template <class T> RefCounted** Ref<T>::ptAttachNew(T* obj, tRefType type, bool takeOwnership){
	RefCounted* old = m_ptRef;
	
	tRefType newType = type;

	// try if the object given casts to a Refcounted   -> if it does set the reference
	try{
		m_ptRef = dynamic_cast<RefCounted*>(obj);
	}catch(...){}
	//
	if(m_ptRef == NULL){
		if(obj != NULL){
			m_ptRef = new Ptr<T>(obj, takeOwnership);
			newType = SRI_REF;
		}
	}else{
		if((type == SRI_WEAK_REF) || (type ==SRI_COUNTER_REF)){  // increase one more so that container doesn't get released
			if(m_ptRef != NULL){
				m_ptRef->vIncContainerCount();
			}
		}
	}

	vIncRef(&m_ptRef, newType);
	vDecRef(&old, m_eRefType);
	m_eRefType = newType;

	return &m_ptRef;
}


template <class T> RefCounted** Ref<T>::ptAttachNew(Ptr<T>* obj, tRefType type){
	RefCounted* old = m_ptRef;
	m_ptRef = obj;
	vIncRef(&m_ptRef, type);
	if((type == SRI_WEAK_REF) || (type == SRI_COUNTER_REF)){
		if(m_ptRef != NULL){
			m_ptRef->vIncContainerCount(); //add one more because decref removes one
		}
	}
	vDecRef(&old, m_eRefType);
	m_eRefType = type;
	return &m_ptRef;
}

//The problem of the below implementation is that it causes compiler errors as
//multiple implicit conversions match the function definition. For example,
// the compiler cannot decide between:
//          class MyClass: public RefCounted{};
//          MyClass* m= new MyClass();			
//          SRI::Ref<MyClass> ref;
//          ref.ptAttachNew(m, SRI_REF);
// The last line matches  (T*, true)  and (RefCounted*, SRI_REF)
//As a solution, the ptAttachNew(T*, SRI_REF, false) has three parameters that
//are evaluated on demand.

//template <class T> RefCounted** Ref<T>::ptAttachNew(RefCounted* obj, tRefType type){
//	RefCounted* old = m_ptRef;
//	
//
//	T* typeTest = NULL;
//
//	if ((obj != NULL) && (bIsPtrCont(obj))){
//		Ptr<T>* ptr = static_cast<Ptr<T>*>(obj);
//		try{
//			if(ptr != NULL){
//				typeTest = dynamic_cast<T*>(ptr->ptObj());
//			}
//		}catch(...){}
//	}
//	if( typeTest == NULL){ 
//		try{
//			typeTest = dynamic_cast<T*>(obj);
//		}catch(...){}
//	}
//	if(typeTest == NULL){
//		//Type mismatch -> leave the current ref functional
//		return &m_ptRef;
//	}
//
//	m_ptRef = obj;
//
//	vIncRef(&m_ptRef, type);
//	if((type == SRI_WEAK_REF) || (SRI_COUNTER_REF)){
//		if(m_ptRef != NULL){
//			m_ptRef->vIncContainerCount(); //add one more because decref removes one
//		}
//	}
//	vDecRef(&old, m_eRefType);
//	m_eRefType = type;
//	return &m_ptRef;
//}

template <class T> Ref<T> Ref<T>::tGetCounterRef(){
	Ref<T> res = *this;
	res.vSetRefType(SRI_COUNTER_REF);
	if(m_eRefType == SRI_WEAK_REF){ //otherwise the copy constructor already increased refcount
		vIncRef(&m_ptRef, SRI_COUNTER_REF);
		vDecContainerRef(&m_ptRef);
	}
	return res;
}

template <class T> Ref<T> Ref<T>::tGetWeakRef(){
	Ref<T> res = *this;
	res.vSetRefType(SRI_WEAK_REF);
	if(m_eRefType != SRI_WEAK_REF){ // copy constructor increases refcount (not allowed for weak ref)
		vIncContainerRef(&m_ptRef); // offset the decref of the container
		vDecRef(&m_ptRef, SRI_REF);
	}
	return res;
}

template <class T> Ref<T> Ref<T>::tGetFullRef(){
	Ref<T> res = *this;
	res.vSetRefType(SRI_REF);
	if(m_eRefType == SRI_WEAK_REF){ // copy constructor didn't increase yet
		vIncRef(&m_ptRef, SRI_REF);
		vDecContainerRef(&m_ptRef);
	}
	return res;
}


template <class T> tRefType Ref<T>::eGetRefType() const{
	return m_eRefType;
}


template <class T> int Ref<T>::iRefCount() const{
		if(m_ptRef == NULL){
			return 0;
		}else{
			return m_ptRef->iRefCount();
		}
	}


template <class T> int Ref<T>::iContainerRefCount() const{
	if(m_ptRef == NULL){
			return 0;
		}else{
			return m_ptRef->iGetContainerCount();
	}
}









} // end namespace

#endif
