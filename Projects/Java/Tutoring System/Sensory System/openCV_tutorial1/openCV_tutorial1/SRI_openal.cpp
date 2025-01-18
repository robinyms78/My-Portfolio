#include"SRI_openAL.h"
#include "Framework.h"

#define	TEST_WAVE_FILE		"C:\\Program Files (x86)\\OpenAL 1.1 SDK\\samples\\media/Footsteps.wav"


namespace SRI{



CV_VoicePlayer::CV_VoicePlayer(SRI::String name,  SRI::String voiceFileCSV):ReactiveComponent(name), m_tLog(SRI::String("ALDevice_") + name, SRI::LOG_DEBUG)
{
	iCreateInputPort("VoiceCmdInput", "voiceEnum");

	// Initialize Framework
	ALFWInit();

//	ALFWprintf("PlayStatic Test Application\n");
	m_tLog.info("Start to initialize OpenAL");

	if (!ALFWInitOpenAL())
	{
		m_tLog.error("Failed to initialize OpenAL");
		ALFWShutdown();
		return;
	}

	// Generate an AL Buffer
			alGenBuffers( NUM_SOUND, &uiBuffer[0] );

			// Generate a Source to playback the Buffer
			alGenSources( NUM_SOUND, &uiSource[0] );

	read_csv(voiceFileCSV.c_str());
	


	

	

	return ;
}

/*
void CV_VoicePlayer::read_csv(const string& filename, std::string name, int ID) {
    std::ifstream file(filename.c_str(), ifstream::in);
    if (!file) {
        string error_message = "No valid input file was given, please check the given filename.";
        CV_Error(CV_StsBadArg, error_message);
		m_tLog.error(error_message);
    }
    string line, path, classlabel;
    while (getline(file, line)) {
        stringstream liness(line);
        getline(liness, path, separator);
        getline(liness, classlabel);
        if(!path.empty() && !classlabel.empty()) {
            images.push_back(imread(path, 0));
            labels.push_back(atoi(classlabel.c_str()));
        }
    }
}*/

CV_VoicePlayer::~CV_VoicePlayer(){
	// Clean up by deleting Source(s) and Buffer(s)
	alSourceStop(uiSource[0]);
    alDeleteSources(NUM_SOUND, &uiSource[0]);
	alDeleteBuffers(NUM_SOUND, &uiBuffer[0]);

	ALFWShutdownOpenAL();

	ALFWShutdown();
}

void CV_VoicePlayer::read_csv(const std::string& filename, char separator) {
    std::ifstream file(filename.c_str(), std::ifstream::in);
    if (!file) {
        std::string error_message = "No valid voice csv file was given, please check the given filename.";
		m_tLog.error(error_message);
    }
    std::string line, path, classlabel;
    while (getline(file, line)) {
        std::stringstream liness(line);
        getline(liness, path, separator);
        getline(liness, classlabel);
        if(!path.empty() && !classlabel.empty()) {

			int enum_ID = atoi(classlabel.c_str());

			enum_ID--;

			std::pair<std::string,int> pair(path,enum_ID);
			fileList.push_back(pair);
			
			if(enum_ID<0||enum_ID>100)
			{
				m_tLog.error("voice file enum should be within 1--100");
				return;
			}

			
	

			// Load Wave file into OpenAL Buffer
			if (!ALFWLoadWaveToBuffer((char*)ALFWaddMediaPath(path.c_str()), uiBuffer[enum_ID]))
			{
				ALFWprintf("Failed to load %s\n", ALFWaddMediaPath(path.c_str()));
			}

			

			// Attach Source to Buffer
			alSourcei( uiSource[enum_ID], AL_BUFFER, uiBuffer[enum_ID] );

        }
    }
}


CV_VoicePlayer::CV_VoicePlayer(const CV_VoicePlayer& c):ReactiveComponent(c), m_tLog(c.m_tLog){

}


CV_VoicePlayer& CV_VoicePlayer::operator=(const CV_VoicePlayer& c){
	if(this == &c){
		return *this;
	}

	m_tLog = c.m_tLog;
	
	//m_tFrame.ptAttachNew(new Image()); just keep the current image object

	return *this;
}




 Component* CV_VoicePlayer::ptClone() const{
	 CV_VoicePlayer* c = new CV_VoicePlayer(*this);
	 return c;
}



void CV_VoicePlayer::vInit(){
	ReactiveComponent::vInit();
}


void CV_VoicePlayer::vFinalize(){
	ReactiveComponent::vFinalize();
}


bool CV_VoicePlayer::bHasMoreSteps(){
	ReactiveComponent::bHasMoreSteps();
	return true;
}


void CV_VoicePlayer::vStep(){
	ReactiveComponent::vStep();
	//ALFWprintf(".");
	//	// Get Source State
	//alGetSourcei( uiSource[0], AL_SOURCE_STATE, &iState[0]);

	if(m_mInputPorts["VoiceCmdInput"].bIsValid()){
		SRI::Ref<SRI::Message> m = m_mInputPorts["VoiceCmdInput"]->ptReceive();
		
		if(m.bIsValid()){
			std::string str(m->szGetContent().c_str());
			int num = atoi(str.c_str());
			bool match =false;
			{
				for(int i =0;i<fileList.size();i++)
				{
					printf("/n i %d num %d /\ %d",i,fileList[i].second,num);
					if(fileList[i].second==num)
					{

						// Play Source
						alSourcePlay( uiSource[num] );
						ALFWprintf("Playing Source ");
	
						do
						{
							//Sleep(100);
							ALFWprintf(".");
							// Get Source State
							alGetSourcei( uiSource[num], AL_SOURCE_STATE, &iState[num]);
						} while (iState[num] != AL_PLAYING);

						ALFWprintf("\n");
						match = true;

					}
				}
				if(!match)
				{
					m_tLog.error("voice file enum not found");
					return;
				}
			}
		
		}
	}
		/*	if(m->szGetType() == "objectMessage"){
				SRI::ObjectMessage* om = dynamic_cast<ObjectMessage*>(m.ptGetObj());
				if(om != NULL){
			//		SRI::Ref<Serializable> ptImg = om->ptGetObjectRef(new Image());
				 	SRI::Ref<Serializable> ptImg = om->ptGetObjectRef<String>();
					m->szGetContent()
				 */
	
}


void CV_VoicePlayer::vPreStep(){
	ReactiveComponent::vPreStep();
}


void CV_VoicePlayer::vPostStep(){
	ReactiveComponent::vPostStep();
}



}