#ifndef SRI_SENSOR_H
#define SRI_SENSOR_H

#include "SRI/SRIEmbodiment/SRIEmbodimentLib.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEmbodiment/SensorData.h"

namespace SRI{

INST_EMBODIMENT_TEMPL SRI::Ref<SensorData>;

class EMBODIMENT_API Sensor: public ReactiveComponent{

private:
	SRI::Logger m_tLog;

protected:
	SRI::Ref<SensorData> m_ptSensorData;

public:
	Sensor(SRI::String name = "SRI.DefaultSensor");
	virtual ~Sensor();

	Sensor(const Sensor& c);
	Sensor& operator=(const Sensor& c);

	virtual SRI::Component* ptClone() const;

	virtual void vSetSensingType(SRI::String sensingType);

	virtual void vSetSensorData(SRI::Ref<SensorData> data);

	virtual bool operator==(const Sensor& c);

	SRI::Ref<SensorData> ptGetSensorData();

};



}// end namespace


#endif
