#ifndef SRI_COMPONENT_SERVER_H
#define SRI_COMPONENT_SERVER_H

#include "SRI/SRIEngine/Server.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIEngine/Component.h"

namespace Poco {
	namespace XML {
		class NamedNodeMap;
	}
}

/// The ComponentServer is a proxy service allowing remote access to a Component

namespace SRI {

	class SRI_E_API ComponentServer : public Server, public Component {

	private:
		Logger m_tLog;
		Ref<Component> m_ptComponent; 
		SRI::String m_szName;

	protected:
		//Component methods
		virtual void vSetId(SRI::String id); 
		virtual int iSetNameSpace(SRI::String name);

	public:
		
		//Server methods
		ComponentServer(Ref<Component> c); 
		virtual ~ComponentServer();
		//TODO: copy con, assignment op
		SRI::String szCallFunction(const ServerExecutorObject& execObj);



		//Component methods

		virtual Ref<EngineHandle> ptGetEngineHandle();
		virtual int iSetEngineHandle(Ref<EngineHandle> handle);

		virtual int iSetParent(Ref<Component> newParent);
		virtual int iAddChild(Ref<Component> comp);
		virtual Ref<Component> ptGetChild(SRI::String name);
		virtual Ref<Component> ptGetParent();
		virtual bool bHasChild(SRI::String name);
		/** returns reference to removed child. Child keeps its children*/
		virtual Ref<Component> ptRemoveChild(SRI::String name);
		virtual Ref<Component> ptRemoveChild(Ref<Component> comp);

		virtual SRI::String szGetID() const;
		virtual SRI::String szGetComponentType() const;
		virtual SRI::String szGetName() const;
		virtual SRI::String szGetNameSpace() const;
		virtual SRI::String szGetComponentName() const;
		virtual int iSetName(SRI::String name);
		virtual int iSetComponentType(SRI::String type);

		//virtual Component* ptClone() const;
		virtual ComponentStatus eGetStatus() const;
		virtual void vSetStatus(ComponentStatus status);

		virtual void vInit();
		virtual void vFinalize();
		virtual bool bHasMoreSteps();
		virtual void vStep();
		virtual void vPreStep();
		virtual void vPostStep();
	};
} //end namespace
#endif SRI_COMPONENT_SERVER_H