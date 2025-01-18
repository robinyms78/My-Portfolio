#ifndef SRI_ANIMATION_ENGINE_H
#define SRI_ANIMATION_ENGINE_H

#include "SRI/SRIAnimation/SRIAnimationLib.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "SRI/SRIEmbodiment/Embodiment.h"
#include "SRI/SRIUtil/SRIRef.h"
#include "SRI/SRIAnimation/AnimationHandle.h"
#include "SRI/Logger/Logger.h"
#include "SRI/SRIEmbodiment/Actuator.h"
#include "SRI/SRIEmbodiment/ActuatorDefinition.h"

#ifdef SRI_USE_LUA
#include "SRI/LuaEngine/LuaEngine.h"
#endif

namespace SRI{

INST_SRI_ANIMATION_TEMPL SRI::Ref<SRI::Embodiment>;
INST_SRI_ANIMATION_TEMPL SRI::Map<SRI::String, Ref<SRI::Animation>>;
INST_SRI_ANIMATION_TEMPL SRI::Map<SRI::String, SRI::AnimationHandle>;
INST_SRI_ANIMATION_TEMPL SRI::Map<SRI::String, SRI::List<SRI::Ref<SRI::Message>>>;

class SRI_ANIMATION_API AnimationEngine:public ReactiveComponent{

private:
	Logger m_tLog;
	SRI::Map<SRI::String, SRI::AnimationHandle> m_mLoadedAnimations;
	SRI::Map<SRI::String, SRI::AnimationHandle> m_mActiveAnimations;
	SRI::Map<SRI::String, SRI::Ref<SRI::Component>> m_mEmbActuators; // a list of actuator references of current embodiment
	SRI::Map<SRI::String, SRI::ActuatorDefinition> m_mEmbActuatorDefinitions; // to accsess port description

	SRI::Map<SRI::String, SRI::List<SRI::Ref<SRI::Message>>> m_mOutBuffer;  
	void vCollectInput(SRI::List<SRI::PortMapping>& portMappings);
	
	SRI::String m_szCurrentEmbodimentName;

	/** The setting of an embodiment creates output ports with type specifications to connect
	* to the actuators of the embodiment. This function uses the engine handle to establish
	* the required connections */
	int iConnectEmbodiment();
	int iConnectAnimation(SRI::List<SRI::PortMapping>& portMappings);

	TimeStamp m_tNow; //Current time for comparision in preStep, Step, postStep
	TimeStamp m_tCurrentTime;  //memorizes last steptime to calculate timeDiff between steps
	TimeStamp m_tMaxFrameRate; // control update speed of animation engine
	TimeStamp m_tCurrentEngineTime;

	bool m_bUseVirtualClock;

#ifdef SRI_USE_LUA
	SRI::String m_szScriptDir;
	SRI::LuaEngine m_tLua;
	void vSetScriptDir(SRI::String dir);
	void vInitLuaEngine();
#endif

	void vMergeAnimations();

	void vForwardAllInput();
	void vHandleAnimationCommand();

public:
	/** The flag initDefaultLua can be set to false to be able to
	* set the directory for the lua script extensions using vSetScriptDir() */
	AnimationEngine(SRI::String name, bool initDefaultLua = true);
	virtual ~AnimationEngine();

	AnimationEngine(const AnimationEngine& c);
	AnimationEngine& operator=(const AnimationEngine& c);

	virtual Component* ptClone() const;
	/** Give a duration of a frame. Animations will only be processed if more time than the given duration has passed*/
	void vSetMaxFrameRate(SRI::TimeStamp t);

	int iSetEmbodiment(Ref<Embodiment> emb);
	int iSetEmbodiment(SRI::EmbodimentDefinition embDef);
	int iSetEmbodiment(SRI::Ref<SRI::Definition> def);

	int iSetEmbodimentDef(SRI::String embodimentDef);
	
	int iSetEmbodimentByName(SRI::String name);
	
	
	void vSetUseVirtualClock(bool isEnabled);

	void vCloseEmbodiment();

	int iLoadAnimation(SRI::Ref<SRI::Animation> anim);
	int iLoadAnimationDef(SRI::String animDef);
	int iLoadAnimationByName(SRI::String name);
	int iCloseAnimation(SRI::String animName);
	void vCloseAllAnimations();

	int iPlayAnimation(SRI::String name);
	int iPauseAnimation(SRI::String name);
	int iStopAnimation(SRI::String name);

	virtual void vInit();
	virtual void vFinalize();

	virtual void vPreStep();
	virtual void vStep();
	virtual void vPostStep();

	virtual bool bHasMoreSteps();

};

} // end namespace


#endif