
#ifndef SRI_EXCEPTION
#define SRI_EXCEPTION


#include "SRIUtilLib.h"


namespace SRI{



#define SRI_MAX_EXCEPTION_MESSAGE 128


class SRIUTIL_API Exception{

private:

protected:
	int m_eErrorCode;
	char* m_szMessage;

public:
	Exception();
	Exception(const char* message);
	virtual ~Exception();
	Exception(const Exception& c);
	Exception& operator=(const Exception& c);
	const char* szMessage() const;

};


class SRIUTIL_API NullException: public Exception{

public:
	NullException();
	NullException(const char* message);
	virtual ~NullException();
	NullException(const NullException& c);
	NullException& operator=(const NullException& c);

};



}// end namespace

#endif