
#ifndef SRI_PLUGIN_H
#define SRI_PLUGIN_H


#ifdef WIN32

#include <SDKDDKVer.h>
#define WIN32_LEAN_AND_MEAN             // Selten verwendete Teile der Windows-Header nicht einbinden.
// Windows-Headerdateien:
#include <windows.h>


#ifdef SRI_PLUGIN_EXPORTS  
#define SRI_PLUGIN_API __declspec(dllexport)
#define EXPORT_IMPORT_TEMPLATE
#else
#define SRI_PLUGIN_API __declspec(dllimport)
#define EXPORT_IMPORT_TEMPLATE extern
#pragma warning ( disable : 4231 )
#endif
#define INST_TEMPLATE EXPORT_IMPORT_TEMPLATE template class SRI_PLUGIN_API

#else   // here the non windows part
#define SRI_PLUGIN_API
#define EXPORT_IMPORT_TEMPLATE
#define INST_TEMPLATE template class
#endif




#define PLUGIN_INIT_FNC_NAME "InitSRIPlugin"
#define PLUGIN_FREE_FNC_NAME "FreeSRIPlugin"
#define PLUGIN_EXTENSION ".dll"

//#include "SRI/SRI.h"
#include "SRI/SRIUtil/SRIString.h"



#endif