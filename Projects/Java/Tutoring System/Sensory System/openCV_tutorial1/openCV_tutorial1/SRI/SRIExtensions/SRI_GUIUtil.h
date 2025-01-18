
#ifndef SRI_GUI_UTIL_H
#define SRI_GUI_UTIL_H

#include "SRI_ExtensionsLib.h"

#include "SRI/SRIGlobals.h"

#ifdef SRI_USE_IUP
#include "iup.h"
#endif


namespace SRI{


#ifdef SRI_USE_IUP
SRI_EXT_API int iInitIUP(int nargs, char** argv);

SRI_EXT_API void vCloseIUP();

#endif



} // end namespace


#endif