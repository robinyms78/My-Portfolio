
#ifndef SRI_ENGINE_PLUGIN_H
#define SRI_ENGINE_PLUGIN_H


#include "SRI/SRIEngine/SRIPlugin.h"

//#ifdef WIN32
//
//#include <SDKDDKVer.h>
//#define WIN32_LEAN_AND_MEAN             // Selten verwendete Teile der Windows-Header nicht einbinden.
//// Windows-Headerdateien:
//#include <windows.h>
//
//
//#ifdef SRIENGINE_PLUGIN_EXPORTS  
//#define SRIENGINE_PLUGIN_API __declspec(dllexport)
//#define SRIENGINE_EXPORT_IMPORT_TEMPLATE
//#else
//#define SRIENGINE_PLUGIN_API __declspec(dllimport)
//#define SRIENGINE_EXPORT_IMPORT_TEMPLATE extern
//#pragma warning ( disable : 4231 )
//#endif
//#define SRIENGINE_INST_TEMPLATE SRIENGINE_EXPORT_IMPORT_TEMPLATE template class SRI_API
//
//#else   // here the non windows part
//#define SRIENGINE_PLUGIN_API
//#define SRIENGINE_EXPORT_IMPORT_TEMPLATE
//#define SRIENGINE_INST_TEMPLATE template class
//#endif
//



#define SRIENGINE_PLUGIN_INIT_FNC_NAME "InitSRIEnginePlugin"
#define SRIENGINE_PLUGIN_FREE_FNC_NAME "FreeSRIEnginePlugin"
#define SRIENGINE_PLUGIN_EXTENSION ".dll"

#include "SRI/SRIGlobals.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIString.h"

namespace SRI{

class SRIEngine;

typedef int (*SRIEnginePluginInitFnc)(SRI::Ref<SRI::SRIEngine> engine, SRI::String pluginName, SRI::String pluginPath, SRI::String config);
typedef void (*SRIEnginePluginFreeFnc)(SRI::Ref<SRI::SRIEngine> engine, SRI::String pluginName, SRI::String pluginPath, SRI::String config);

}



#endif