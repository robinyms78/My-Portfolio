#ifndef LIB_HANDLE_H
#define LIB_HANDLE_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/ConfigReader/ConfigNode.h"


namespace SRI{

/** Wrapper class to make sure that the DLL does not get not released as long as it is referenced
* To be used with Ref<LibHandle> dllRef;   The smart pointer takes care that the library
* is only released when there are no more references. 
*/
class SRI_E_API LibHandle: public RefCounted{
private:
	HMODULE m_hHandle;
	Logger m_tLog;

	

	//access to library handles by Ref<LibHandle> and not by implicit copy
	LibHandle(const LibHandle& c);
	LibHandle& operator=(const LibHandle& c);


public:
	LibHandle();
	LibHandle(HMODULE h);
	
	virtual ~LibHandle();

	void vSetHandle(HMODULE h);
	HMODULE tGetHandle();

	virtual void vCloseLibrary();
	virtual bool bIsValid()const;
};


} // end namespace




#endif