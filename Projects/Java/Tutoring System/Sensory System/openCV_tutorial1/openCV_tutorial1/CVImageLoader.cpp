#include "CVImageLoader.h"
#include "ObjectMessage.h"

namespace SRI{

CVImageLoader::CVImageLoader(SRI::String name, SRI::String path):ReactiveComponent(name), m_tLog(SRI::String("ImageLoader_") + name, SRI::LOG_DEBUG),
	m_tFrame(new Image()){
	iCreateOutputPort("LoadedImage", "cvImage");

	sentFlag = true;
	//For now use default 0 TODO: reand from config file
 	m_ptCapture = new IplImage();
	iLoadImage(path);
}

CVImageLoader::~CVImageLoader(){

}



CVImageLoader::CVImageLoader(const CVImageLoader& c):ReactiveComponent(c), m_tLog(c.m_tLog),m_tFrame(new Image()){
	m_ptCapture = c.m_ptCapture;
}


CVImageLoader& CVImageLoader::operator=(const CVImageLoader& c){
	if(this == &c){
		return *this;
	}

	m_tLog = c.m_tLog;
	m_ptCapture = c.m_ptCapture;
	//m_tFrame.ptAttachNew(new Image()); just keep the current image object

	return *this;
}




 Component* CVImageLoader::ptClone() const{
	 CVImageLoader* c = new CVImageLoader(*this);
	 return c;
}

 /*
int CVImageLoader::iOpenDevice(int devNum){
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
}*/
 
 int CVImageLoader::iLoadImage(SRI::String path){
	m_ptCapture =cvLoadImage(path.c_str());

	if( m_ptCapture!=NULL()){
		sentFlag = false;
		return SRI_OK;
	}else{
		m_tLog.error("Unable to load Image: %s", path.c_str());
		return SRI_ERR_LOAD;
	}
}


void CVImageLoader::vInit(){
	ReactiveComponent::vInit();
}


void CVImageLoader::vFinalize(){
	ReactiveComponent::vFinalize();
}


bool CVImageLoader::bHasMoreSteps(){
	ReactiveComponent::bHasMoreSteps();
	return true;
}


void CVImageLoader::vStep(){
	ReactiveComponent::vStep();
//	if( m_ptCapture.bIsValid() && m_ptCapture->isOpened())
	if(!sentFlag)
	{
//		if(m_ptCapture->grab())
		{
			m_tLog.info("Start to set SRI::Image");
		//	Image* ptImg = dynamic_cast<Image*>(m_tFrame.ptGetObj());
			//convert CvMat cvmat = img
			cv::Mat imgMat(m_ptCapture);  //Construct an Mat image "img" out of an IplImage
			Image* ptImg = new Image(imgMat);
			//Image* ptImg = new Image(m_ptCapture->height,m_ptCapture->width,CV_32FC3,m_ptCapture->imageData,m_ptCapture->widthStep);
			m_tLog.info("SRI::Image set successful");

		 	ObjectMessage* message = new ObjectMessage(*ptImg);
		//	message->vSetContent(m_ptCapture->imageData,m_ptCapture->nSize);
			
			m_mOutputPorts["LoadedImage"]->iSend(message);
			sentFlag = true;
			delete ptImg;
		}
	}
}


void CVImageLoader::vPreStep(){
	ReactiveComponent::vPreStep();
}


void CVImageLoader::vPostStep(){
	ReactiveComponent::vPostStep();
}



}