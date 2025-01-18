#ifndef SRI_UTIL_LIB_H
#define SRI_UTIL_LIB_H



#ifdef WIN32

#ifdef SRIUTIL_EXPORTS
#define SRIUTIL_API __declspec(dllexport)
#ifndef EXPIMP_SRI_TEMPLATE
#define EXPIMP_SRI_TEMPLATE
#endif
#else
#define SRIUTIL_API __declspec(dllimport)
#ifndef EXPIMP_SRI_TEMPLATE
#define EXPIMP_SRI_TEMPLATE extern
#endif
#pragma warning ( disable : 4231 )
#endif
#define INST_SRI_TEMPL EXPIMP_SRI_TEMPLATE template class SRIUTIL_API

#else
#define SRIUTIL_API
#ifndef EXPIMP_SRI_TEMPLATE
#define EXPIMP_SRI_TEMPLATE
#endif
#define INST_SRI_TEMPL template class
#endif



#endif // header already included