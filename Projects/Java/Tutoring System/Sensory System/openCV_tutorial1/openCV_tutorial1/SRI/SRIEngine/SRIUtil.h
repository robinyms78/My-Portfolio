
#ifndef SRI_UTIL_H
#define SRI_UTIL_H

#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIGlobals.h"
#include "SRI/SRIUtil/SRIString.h"

namespace SRI{


SRI_E_API SRI::String szErrCodeToString(int errorCode);


/** The dest buffer must have the size = sourceSize * 3 + 1; */
SRI_E_API void vEncodeBytes(unsigned char* dest, const unsigned char* source, int sourceSize);

/** the dest buffer must have the size = (sourceSize - 1) / 3; */
SRI_E_API void vDecodeBytes(unsigned char* dest, const unsigned char* source, int sourceSize);

/** Creates a string formated timestamp */
SRI_E_API SRI::String szCreateTimeStamp();


};



#endif







