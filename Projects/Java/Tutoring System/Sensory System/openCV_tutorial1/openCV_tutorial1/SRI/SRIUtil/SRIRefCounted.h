#ifndef SRI_REFCOUNTED_H
#define SRI_REFCOUNTED_H

#include "SRI/SRIUtil/SRIUtilLib.h"

namespace SRI{

class SRIUTIL_API RefCounted{

public:
	typedef enum {
		COUNTED = 1,
		PTR_COUNTED
	} tRefType;

protected:	
	int m_iRefCount;
	int m_iContainerCount;
	tRefType m_eRefType;

public:
	RefCounted();
	RefCounted(const RefCounted& c);
	virtual ~RefCounted();

	RefCounted& operator=(const RefCounted& c);

	/** Explicit release of allocated resources but leaving the container intact*/
	virtual void vRelease();
	virtual void vIncRef();
	virtual int iDecRef();
	virtual int iRefCount()const;
	virtual void vResetCounter();
	virtual bool bIsValid()const;

	virtual void vIncContainerCount();
	virtual int iDecContainerCount();
	virtual int iGetContainerCount() const;
	virtual void vResetContainerCounter();
	virtual tRefType eGetContainerType() const;
};


} // end namespace


#endif


