#include "Camera.h"
#include "ObjectMessage.h"

namespace SRI{

Camera::Camera(SRI::String name):ReactiveComponent(name), m_tLog(SRI::String("Camera_") + name, SRI::LOG_DEBUG),
	m_tFrame(new Image()){
	iCreateOutputPort("CaptureImage", "cvImage");

	//For now use default 0 TODO: reand from config file
	m_ptCapture.ptAttachNew(new cv::VideoCapture(0));
}

Camera::~Camera(){

}



Camera::Camera(const Camera& c):ReactiveComponent(c), m_tLog(c.m_tLog),m_tFrame(new Image()){
	m_ptCapture = c.m_ptCapture;
}


Camera& Camera::operator=(const Camera& c){
	if(this == &c){
		return *this;
	}

	m_tLog = c.m_tLog;
	m_ptCapture = c.m_ptCapture;
	//m_tFrame.ptAttachNew(new Image()); just keep the current image object

	return *this;
}




 Component* Camera::ptClone() const{
	 Camera* c = new Camera(*this);
	 return c;
}


int Camera::iOpenDevice(int devNum){
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


void Camera::vInit(){
	ReactiveComponent::vInit();
}


void Camera::vFinalize(){
	ReactiveComponent::vFinalize();
}


bool Camera::bHasMoreSteps(){
	ReactiveComponent::bHasMoreSteps();
	return true;
}


void Camera::vStep(){
	ReactiveComponent::vStep();
	if( m_ptCapture.bIsValid() && m_ptCapture->isOpened()){
		if(m_ptCapture->grab()){
			Image* ptImg = dynamic_cast<Image*>(m_tFrame.ptGetObj());
			if(ptImg != NULL){
				m_ptCapture->retrieve(*ptImg);

				ObjectMessage* message = new ObjectMessage(m_tFrame);
				m_mOutputPorts["CaptureImage"]->iSend(message);
			}
		}
	}
}


void Camera::vPreStep(){
	ReactiveComponent::vPreStep();
}


void Camera::vPostStep(){
	ReactiveComponent::vPostStep();
}



}