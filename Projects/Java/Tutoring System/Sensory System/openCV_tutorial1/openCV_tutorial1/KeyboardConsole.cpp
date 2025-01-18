#include "KeyboardConsole.h"
#include "ObjectMessage.h"

namespace SRI{

KeyboardConsole::KeyboardConsole(SRI::String name):ReactiveComponent(name), m_tLog(SRI::String("KeyboardConsole_") + name, SRI::LOG_DEBUG)
{
	iCreateOutputPort("KeyboardInput", "String");
	//need event for scan input
	//and send out by SRI Message
}

KeyboardConsole::~KeyboardConsole(){

}



KeyboardConsole::KeyboardConsole(const KeyboardConsole& c):ReactiveComponent(c), m_tLog(c.m_tLog),m_tFrame(new Image()){
	m_ptCapture = c.m_ptCapture;
}


KeyboardConsole& KeyboardConsole::operator=(const KeyboardConsole& c){
	if(this == &c){
		return *this;
	}

	m_tLog = c.m_tLog;
	m_ptCapture = c.m_ptCapture;
	//m_tFrame.ptAttachNew(new Image()); just keep the current image object

	return *this;
}




 Component* KeyboardConsole::ptClone() const{
	 KeyboardConsole* c = new KeyboardConsole(*this);
	 return c;
}


int KeyboardConsole::iOpenDevice(int devNum){
	//close old one if new one is opened
	if(m_ptCapture.bIsValid() && m_ptCapture->isOpened()){
		m_ptCapture->release();
	}

	if(m_ptCapture.bIsValid()){
		m_ptCapture->open(devNum);
	}

	if(m_ptCapture.bIsValid() && m_ptCapture->isOpened()){
		return SRI_OK;
	}else{
		m_tLog.error("Unable to open device: %d", devNum);
		return SRI_ERR_LOAD;
	}
}


void KeyboardConsole::vInit(){
	ReactiveComponent::vInit();
}


void KeyboardConsole::vFinalize(){
	ReactiveComponent::vFinalize();
}


bool KeyboardConsole::bHasMoreSteps(){
	ReactiveComponent::bHasMoreSteps();
	return true;
}


void KeyboardConsole::vStep(){
	ReactiveComponent::vStep();
	if( m_ptCapture.bIsValid() && m_ptCapture->isOpened()){
		if(m_ptCapture->grab()){
			Image* ptImg = dynamic_cast<Image*>(m_tFrame.ptGetObj());
			if(ptImg != NULL){
				m_ptCapture->retrieve(*ptImg);

				Message* message = new Message(String("test string"));
				m_mOutputPorts["CaptureImage"]->iSend(message);
			}
		}
	}
}


void KeyboardConsole::vPreStep(){
	ReactiveComponent::vPreStep();
}


void KeyboardConsole::vPostStep(){
	ReactiveComponent::vPostStep();
}



}