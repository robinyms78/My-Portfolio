#ifndef SRI_OPENAL_H
#define SRI_OPENAL_H

#include "SRI.h"
#include "SRIRegistryPlugin.h"


#include <conio.h>
#include <stdlib.h>
#include <stdio.h>			

#include <al.h>
#include <alc.h>
//#include <al/alut.h>	


#include <iostream>
#include <string>

#include <fstream>
#include <sstream>
#include <vector>

#define PlaySoundA PlaySound
#define PlaySoundW PlaySound


#define NUM_SOUND 100

namespace SRI{

	//sigleton?
class CV_VoicePlayer : public SRI::ReactiveComponent{


private:
	std::vector<std::pair<std::string,int>> fileList;

	ALuint      uiBuffer[NUM_SOUND];
	ALuint      uiSource[NUM_SOUND];
	ALint       iState[NUM_SOUND];

	Logger m_tLog;
	bool m_Finished;
	
	void PlaySound(std::string name);
//	void StopSound(int soundID);

	bool LoadSoundFile(std::string name);

	void read_csv(const std::string& filename, char separator = ';');
	
protected:
	

public:
	CV_VoicePlayer(SRI::String name, SRI::String voiceFileCSV);
	virtual ~CV_VoicePlayer();

	CV_VoicePlayer(const CV_VoicePlayer& c);
	CV_VoicePlayer& operator=(const CV_VoicePlayer& c);
	

	virtual Component* ptClone() const;
	virtual void vInit();
	virtual void vFinalize();
	virtual bool bHasMoreSteps();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();

};

}


#endif