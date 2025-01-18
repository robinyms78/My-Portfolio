#ifndef SRI_REMOTETASK_H
#define SRI_REMOTETASK_H

#include "SRI/SRIUtil/SRIString.h"

/** 
* The struct represents a task to be executed by a remote server. It contains 
* an XML string that represents:
* 1. the function to be executed and its arguments, if any
* 2. an identifier for the thread that caused the despatch of this task
* 3 a pointer to a Poco::Event, used to co-ordinate between the calling thread and the monitoring thread of the socket
* 4. a place for the monitoring thread to write the return value
*/ 

namespace SRI{

struct RemoteTask{

	SRI::String m_szCall; //function to be executed and its arguments
	SRI::String m_szCallerID; //id for the despatching thread
	Poco::Event *m_ptEvent; //pt to co-ordinating event, used by monitoring thread to wake up despatching thread
	SRI::String m_szRetVal; //return value, written by monitoring thread
	
};

}

#endif SRI_REMOTETASK_H