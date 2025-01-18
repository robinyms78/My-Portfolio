#ifndef SRI_SERVEREXECUTOROBJECT_H
#define SRI_SERVEREXECUTOROBJECT_H

#include "SRI\SRIUtil\SRIString.h"
#include "SRI\SRIUtil\SRIRef.h"
#include "SRI\SRIUtil\SRIList.h"
#include "SRI\Logger\Logger.h"
#include <vector>

/** 

*/ 

namespace Poco {
	namespace Net{
	
		class StreamSocket;
	
	}
}

namespace SRI{

class ServerExecutorObject{
private:
	SRI::String m_szName; //function name
	SRI::List<SRI::String> args;
	SRI::String m_szCallerID; //id for the despatching thread
	
	SRI::String m_szRetVal; //return value, written by monitoring thread
	Logger m_tLog;
	Poco::Net::StreamSocket *m_ptStreamSocket;


	//SRI::Ref<SRI::List> 

public:

	ServerExecutorObject() : m_tLog("ServerExecutorObject", LOG_DEBUG) {
	}

	virtual ~ServerExecutorObject() { //this is just to make this class polymorphic so it'll work with SRI::Ref
	}

	void vSetName(const SRI::String& n) {
		m_szName = n;
	}

	SRI::String szGetName() const {
		return m_szName;
	}

	void vAddArg(const SRI::String& arg) {
		args.push_back(arg);
	}

	SRI::String szGetArg(int index) const {
		if (index >= args.size()) {
			m_tLog.error("Index out of bounds");
			return "";
		}
		
		SRI::String res;
		for (SRI::ConstListIterator<SRI::String> it = args.begin(); it != args.end(); it++) {
			if (index == 0) res = *it;
			index--;
		}
		return res;
	}

	int iNumArgs() const {
		return args.size();
	}

	void vSetCallerID(const SRI::String& id) {
		m_szCallerID = id;
	}

	SRI::String szGetCallerID() const {
		return m_szCallerID;
	}

	void vSetRetVal(const SRI::String& ret) {
		m_szRetVal = ret;
	}

	SRI::String szGetRetVal() const {
		return m_szRetVal;
	}

	void vSetStreamSocket(Poco::Net::StreamSocket *s) {
		m_ptStreamSocket = s;
	}

	Poco::Net::StreamSocket *ptGetStreamSocket() {
		return m_ptStreamSocket;
	}

	Poco::Net::StreamSocket *ptGetStreamSocket() const {
		return m_ptStreamSocket;
	}

	inline bool operator==(const ServerExecutorObject& rhs) const {
		//should be sufficient to check on these fields
		if (m_szName == rhs.m_szName &&
			m_szCallerID == rhs.m_szCallerID &&
			m_ptStreamSocket == rhs.m_ptStreamSocket) return true;
		return false;
	}



};

}

#endif SRI_SERVEREXECUTOROBJECT_H