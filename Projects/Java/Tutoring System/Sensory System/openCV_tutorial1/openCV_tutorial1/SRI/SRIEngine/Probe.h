#ifndef SRI_PROBE_H
#define SRI_PROBE_H


#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIUtil/Serializable.h"
#include "SRI/Logger/Logger.h"

namespace SRI{

class SRI_E_API Probe: public SRI::ReactiveComponent{

private:
	Logger m_tLog;

protected:

public:
	Probe(SRI::String name);
	virtual ~Probe();

	Probe(const Probe& c);
	Probe& operator=(const Probe& c);


	virtual SRI::Component* ptClone() const;


	SRI::Ref<SRI::Message> ptRead(SRI::String inPortName);
	int iSend(SRI::String outPortName, SRI::Ref<SRI::Message> m);

	SRI::String szRead(SRI::String inPortName);
	/** Takes over the memory */
	int iSend(SRI::String outPortName, SRI::Message* m);
	int iSend(SRI::String outPortName, SRI::String message);
	int iSend(SRI::String outPortName, const Serializable& obj);

	/** [targetPort, targetComponentName] */
	SRI::Map<SRI::String, SRI::String> mGetConnections(SRI::String portName);

	virtual void vPreStep();
	virtual void vPostStep();
	virtual bool bHasMoreSteps();

};

} // end namespace SRI


#endif