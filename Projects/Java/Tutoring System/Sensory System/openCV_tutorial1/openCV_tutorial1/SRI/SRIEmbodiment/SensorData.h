#ifndef SRI_SENSOR_DATA_H
#define SRI_SENSOR_DATA_H

#include "SRI/SRIEmbodiment/SRIEmbodimentLib.h"
#include "SRI/SRIUtil/Cloneable.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIUtil/Serializable.h"
#include "SRI/SRIUtil/SRITime.h"

namespace SRI{

class EMBODIMENT_API SensorData: public Serializable{

protected:
	SRI::String m_szDataType;
	SRI::TimeStamp m_tTimeStamp;
	SRI::String m_szSourceName; // encodes the name of the component generating the data

public:
	SensorData();
	virtual ~SensorData();

	SensorData(const SensorData& c);
	virtual SensorData& operator=(const SensorData& c);
	virtual bool operator==(const SensorData& c);

	/** Sets the timeStamp of the sensor data to current time*/
	virtual int iCurrentTime();
	virtual void vSetTimeStamp(const SRI::TimeStamp& c);
	virtual SRI::TimeStamp tGetTimeStamp() const;

	virtual void vSetSourceName(SRI::String name);
	virtual SRI::String szGetSourceName() const;

	virtual SRI::String szGetDataType() const;

	//====== Interface from Serializable ==============================
	virtual SensorData* ptClone() const;
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	/** Returns a string identifying the object type is is serialized */
	virtual const char* szGetObjType() const;
};

}




#endif
