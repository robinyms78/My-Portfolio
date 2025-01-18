#ifndef SRI_COMPONENT_FACTORY_SERVER_H
#define SRI_COMPONENT_FACTORY_SERVER_H

#include "SRI/SRIEngine/Server.h"
#include "SRI/SRIEngine/ComponentFactory.h"
#include "SRI/Logger/Logger.h"
#include "SRI/ConfigReader/ConfigNode.h"
#include "SRI/SRIUtil/SRIRef.h"


namespace Poco {

	class ThreadPool;

	namespace XML {
		class NamedNodeMap;
	}
}

namespace SRI {

	class ComponentFactory;
	class Component;


	/// A ComponentFactoryServer is a proxy service allowing remote access to a ComponentFactory
	/** NOTE: In the current framework, all components created by the proxied ComponentFactory
		exist in the same address space as the ComponentFactoryServer and the proxied ComponentFactory,
		as opposed to running as a separate process.
		The ComponentFactoryServer is responsible for providing remote access to created
		Components by creating an accompanying ComponentServer/ReactiveComponentServer. The
		ComponentServer/ReactiveComponentServer runs in a separate thread, and cleans up
		after itself when it shuts down.
	*/

	class SRI_E_API ComponentFactoryServer : public Server, public ComponentFactory {

	private:
		Poco::ThreadPool *m_ptThreadPool;

		Logger m_tLog;
		Ref<ComponentFactory> m_ptComponentFactory;

		SRI::String szGetComponentType(Component *c);
		SRI::String szGetComponentType(SRI::Ref<SRI::Component> c);

	public:
		ComponentFactoryServer(Ref<ComponentFactory> f); 
		virtual ~ComponentFactoryServer();
		//TODO: copy con, assignment op
		SRI::String szCallFunction(const ServerExecutorObject& execObj);

	};
} //end namespace
#endif SRI_COMPONENT_FACTORY_SERVER_H