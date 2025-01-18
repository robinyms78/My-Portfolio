#ifndef SERVER_REPLY_STRUCT_H
#define SERVER_REPLY_STRUCT_H

#include "SRI\SRIUtil\SRIString.h"

namespace Poco {
	class Event;
} 

namespace SRI {
	struct ServerReplyStruct {
		Poco::Event* e;
		SRI::String reply;
	};

} //end namespace SRI

#endif SERVER_REPLY_STRUCT_H