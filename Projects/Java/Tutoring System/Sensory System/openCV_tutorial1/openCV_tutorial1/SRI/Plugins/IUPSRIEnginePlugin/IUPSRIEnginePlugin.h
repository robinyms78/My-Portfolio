
#ifndef IUP_SRI_ENGINE_PLUGIN_H
#define IUP_SRI_ENGINE_PLUGIN_H

#include "SRI/Logger/Logger.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIEngine/SRIEnginePlugin.h"



namespace SRI{

/** This class implements the component interface and calls
 * the functions as defined in Lua 
 * A lua component might be generated using a C++ factory or a Lua factory
 */
class SRI_PLUGIN_API IUPSRIEnginePlugin: public SRI::ReactiveComponent{ 

private:
	Logger m_tLog;
	

protected:


public:
	IUPSRIEnginePlugin(SRI::String name);
	virtual ~IUPSRIEnginePlugin();
	IUPSRIEnginePlugin(const IUPSRIEnginePlugin& c);
	IUPSRIEnginePlugin& operator=(const IUPSRIEnginePlugin& c);


	virtual Component* ptClone();

	virtual void vInit();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();
	virtual bool bHasMoreSteps();
	virtual void vFinalize();
};



}




#endif