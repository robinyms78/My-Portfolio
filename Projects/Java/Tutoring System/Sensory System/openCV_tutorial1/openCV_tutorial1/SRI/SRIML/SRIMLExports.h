#ifndef SRIML_EXPORTS_H
#define SRIML_EXPORTS_H


#ifdef WIN32

#ifdef SRIML_EXPORTS
#define SRIML_API __declspec(dllexport)
#define EXPIMP_SRIML_TEMPLATE
#else
#define SRIML_API __declspec(dllimport)
#define EXPIMP_SRIML_TEMPLATE extern
#endif
#define INST_SRIML_TEMPL EXPIMP_SRIML_TEMPLATE template class SRIML_API

#else // Win32
#define SRIML_API
#define EXPIMP_SRIML_TEMPLATE
#define INST_SRIML_TEMPL template class

#endif // WIN32






#endif // SRIML_EXPORTS_H