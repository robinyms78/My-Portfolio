#ifndef SRI_MUTEXSTACK_H
#define SRI_MUTEXSTACK_H

#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIList.h"
#include "Poco/Mutex.h"

/** Class that encapsulates a stack and its mutex. Caller is responsible for 
 *  acquiring and releasing the mutex
 *
 *  The stack is implemented with an SRIList
 */ 

namespace SRI{

template <typename T> class SRIMutexStack{
private:
	
	SRI::List<T> m_lList;
	Poco::Mutex m_mutMutex;

public:

	bool isEmpty() const {
		if (m_lList.size() == 0) return true;
		return false;
	}

	unsigned int size() const {
		return m_lList.size();
	}

	T& top() {
		return m_lList.front();
	}

	void push(const T& t) {
		m_lList.push_front(t);
	}

	void pop() {
		m_lList.pop_front();
	}

	
	void vLock() {
		m_mutMutex.lock();
	}

	bool bTryLock() {
		return m_mutMutex.tryLock();
	}

	void vUnlock() {
		m_mutMutex.unlock();
	}

	Poco::Mutex* ptGetLock() {
		return &m_mutMutex;
	}
	
};

}

#endif SRI_MUTEXLIST_H