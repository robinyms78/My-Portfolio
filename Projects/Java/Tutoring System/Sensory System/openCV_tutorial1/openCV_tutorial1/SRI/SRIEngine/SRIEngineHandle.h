#ifndef SRI_ENGINE_HANDLE_H
#define SRI_ENGINE_HANDLE_H

#include "SRI/SRIEngine/SRIEngineLib.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIEngine/SRIEngine.h"

namespace SRI{

class Component;


INST_SRI_E_TEMPL SRI::Ref<SRI::SRIEngine>;

class SRI_E_API EngineHandle{

private:
	SRI::Logger m_tLog;
	
protected:
	SRI::Ref<SRI::SRIEngine> m_ptEngine;
	SRI::String m_szConfig;


public:
	EngineHandle(SRI::String config = "");
	EngineHandle(SRI::Ref<SRI::SRIEngine> engine);
	EngineHandle(const EngineHandle& c);
	EngineHandle& operator=(const EngineHandle& c);
	virtual ~EngineHandle();

	virtual void vSetEngine(SRI::Ref<SRI::SRIEngine> engine);
	virtual Ref<SRIEngine> ptGetEngine();
	/** Checks if there is a valid engine associated (either real engine or connected engien stub) */
	virtual bool bIsValid() const;

	/** This function takes over the memory even on failure (which directly deletes the component) */
	virtual int iAddComponent(SRI::Component* comp, SRI::String loopLabel = "simulation");
	virtual int iAddComponent(SRI::Ref<SRI::Component> comp, SRI::String loopLabel = "simulation");
	virtual void vRemoveComponent(SRI::String compName);
	virtual int iChangeName(SRI::String oldName, SRI::String newName);
	virtual bool bHasComponent(SRI::String name, SRI::String loopLabel = "*");
	virtual int iChangeLoop(SRI::String componentName, SRI::String newLoopLabel);

	virtual int iConnect(SRI::String sender, SRI::String outport, SRI::String receiver, SRI::String inport);
	virtual int iDisconnect(SRI::String sender, SRI::String outport, SRI::String receiver, SRI::String inport);

	virtual SRI::String szGetLoopLabel(SRI::String name);
	/** Compares of engine handle points to same engine */
	virtual bool operator==(const EngineHandle& c) const;
	virtual bool operator!=(const EngineHandle& c) const;

	virtual SRI::Ref<SRI::Component> ptGetComponent(SRI::String name, SRI::String loopLabel="*");

	virtual SRI::String szGetEngineName() const;

	/** Asks the engine to give the registry address. \returns either real or RegistryStub*/
	virtual SRI::Ref<SRIRegistry> ptGetSRIRegistry();

	// Returns the ip and port address of the engine if it has a server running, otherwise an empty string
	virtual SRI::String szGetEngineAddress();

	// for exmaple needed to allow a remote luaConsole to step the engine
	virtual void vStop();
	virtual void vInit();
	virtual void vStep();
	virtual void vFinalize();

	virtual bool bEngineStopped();
};

} //end namespace

#endif