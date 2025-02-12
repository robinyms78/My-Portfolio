#ifndef SRI_ERROR_CODES_H
#define SRI_ERROR_CODES_H

#define SRI_SMALLEST_ERR_VALUE -17

namespace SRI{

typedef enum{
	SRI_ERR_TIMEOUT = SRI_SMALLEST_ERR_VALUE,
	SRI_ERR_NETWORK,
	SRI_ERR_FILE,
	SRI_ERR_IUP,
	SRI_ERR_SYNTAX,
	SRI_ERR_NAMECONFLICT,
	SRI_ERR_CALL,
	SRI_ERR_LOAD,
	SRI_ERR_NOT_DEFINED,
	SRI_ERR_INCOMPLETE,
	SRI_ERR_ABORT,
	SRI_ERR_CONNECTION,
	SRI_ERR_NA,
	SRI_ERR_TYPE,
	SRI_ERR_MEM, 
	SRI_ERR_NULL,
	SRI_ERR,
	SRI_OK=0
} SRIErrorCode;


}

#endif