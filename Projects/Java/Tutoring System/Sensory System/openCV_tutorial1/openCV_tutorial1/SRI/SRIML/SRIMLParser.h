#ifndef SRI_SRIML_SRIMLPARSER_H
#define SRI_SRIML_SRIMLPARSER_H


#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIML/SRIMLExports.h"
#include "SRI/SRIEngine/SRIRegistry.h"

namespace SRI{

class Component;
class MLComponent;


class SRIML_API SRIMLParser{
	
private:
	Logger m_tLog;
	SRI::Ref<SRIRegistry> m_ptRegistry;

	
public:
	//constructors & destructors
	SRIMLParser(SRI::Ref<SRIRegistry> reg);
	//virtual ~SRIMLParser();
	//SRIMLParser(const SRIMLParser& c);
	
	//SRIMLParser& operator=(const SRIMLParser& c);

	SRI::Ref<Component> ptParseSRIML(SRI::String sriMLScript);
			
};

} // end namepspace

#endif SRI_SRIML_SRIMLPARSER_H

