#ifndef SRI_TIME_H
#define SRI_TIME_H

#include "SRI/SRIUtil/SRIUtilLib.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/Serializable.h"

namespace SRI{

class SRIUTIL_API TimeStamp: public Serializable{

private:
	long m_lSec;
	long m_lMSec;
	short m_sSign;

public:
	TimeStamp();
	/** Creates timeStamp from given milliseconds (e.g. 83000 = 8sec, 300msec) */
	TimeStamp(long msec);  
	TimeStamp(long sec, long msec); 
	virtual ~TimeStamp();
	TimeStamp(const TimeStamp& c);

	TimeStamp& operator=(const TimeStamp& c);

	/** Sets the values of the TimeStamp to current system time. It returns 0 in case of success
	* or -1 in case of failure */
	int iCurrentTime();

	/** Creates a new timeStamp object and initializes it with current system time */
	static TimeStamp tGetTime();
	/** Puts the current thread to sleep for specified milliseconds */
	static void Sleep(long msec);
	static void Sleep(const SRI::TimeStamp& t);

	/** \returns seconds component */
	long lGetSec() const;
	/** \returns milli seconds component*/
	long lGetMSec() const;
	short sGetSign() const;
	
	/** adds the milliseconds as fraction to the seconds  e.g. 8.234  means 8 seconds, 234 milliseconds*/
	double dGetAbsSec() const;
	/** Gives a combined msec: e.g. 8300 for 8sec + 300 msec */
	long lGetAbsMSec() const; 

	void vSetSign(short s);

	/** Sets the second component of the time value */
	void vSetSec(long val);
	/** Sets the millisecond value. The given value is capped at 1000 */
	void vSetMSec(long val);
	void vSetTime(long sec, long msec);

	TimeStamp operator+(const TimeStamp& c) const;
	TimeStamp operator-(const TimeStamp& c) const;

	TimeStamp& operator+=(const TimeStamp& c);
	TimeStamp& operator-=(const TimeStamp& c);

	bool operator==(const TimeStamp& c) const;
	bool operator!=(const TimeStamp& c) const;

	bool operator<(const TimeStamp& c) const;
	bool operator<=(const TimeStamp& c) const;
	bool operator>(const TimeStamp& c) const;
	bool operator>=(const TimeStamp& c) const;

	bool operator==(const long absMSec) const;
	bool operator!=(const long absMSec) const;

	bool operator<(const long absMSec) const;
	bool operator<=(const long absMSec) const;
	bool operator>(const long absMSec) const;
	bool operator>=(const long absMSec) const;

	virtual TimeStamp* ptClone() const;

	/** Generates a human readable string for console */
	virtual SRI::String szFormatTime() const;
	
	//=========== from serializable interface =====================
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	/** This returns a class type for serialization */
	virtual const char* szGetObjType() const;

	static const char* szGetClassType();
};

}

#endif