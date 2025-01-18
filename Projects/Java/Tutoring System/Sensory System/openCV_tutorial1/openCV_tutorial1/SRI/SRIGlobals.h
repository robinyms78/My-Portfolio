#ifndef SRI_GLOBALS_H
#define SRI_GLOBALS_H

#ifdef WIN32
#define DIRSEP "\\"
#else
#define DIRSEP "//"
#endif

#include "SRI/SRIUtil/SRIErrorCodes.h"
#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIString.h"


namespace SRI{


extern SRI_E_API Logger SRILog;

extern SRI_E_API SRI::String SRIComponentNameString;
extern SRI_E_API SRI::String SRIReactiveComponentNameString;  


}// end namespace





#endif