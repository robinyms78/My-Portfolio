#ifndef SRI_EXTENSIONS_LIB_H
#define SRI_EXTENSIONS_LIB_H



#ifdef WIN32

#ifdef SRIEXTENSIONS_EXPORTS
#define SRI_EXT_API __declspec(dllexport)
#ifndef EXPIMP_EXT_TEMPLATE
#define EXPIMP_EXT_TEMPLATE
#endif
#else
#define SRI_EXT_API __declspec(dllimport)
#ifndef EXPIMP_EXT_TEMPLATE
#define EXPIMP_EXT_TEMPLATE extern
#endif
#pragma warning ( disable : 4231 )
#endif
#define INST_EXT_TEMPL EXPIMP_EXT_TEMPLATE template class SRI_EXT_API

#else
#define SRI_EXT_API
#ifndef EXPIMP_EXT_TEMPLATE
#define EXPIMP_EXT_TEMPLATE
#endif
#define INST_EXT_TEMPL template class
#endif



#endif // header already included