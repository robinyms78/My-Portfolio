#include "ImageShow.h"
#include "ObjectMessage.h"

namespace SRI{


ImageShow::ImageShow(SRI::String name):ReactiveComponent(name),m_tLog(SRI::String("ImageShow_") + name, SRI::LOG_DEBUG){
	m_Finished = false;
	iCreateInputPort("ImageInput", "cvImage");
}

ImageShow::~ImageShow(){

}


ImageShow::ImageShow(const ImageShow& c): ReactiveComponent(c), m_tLog(c.m_tLog){
	m_Finished = false;
}


ImageShow& ImageShow::operator=(const ImageShow& c){
	if(this == &c){
		return *this;
	}
	ReactiveComponent::operator=(c);
	m_tLog = c.m_tLog;
	m_Finished = false;

	return *this;
}



Component* ImageShow::ptClone() const{
	ImageShow* c = new ImageShow(*this);
	return c;
}


void ImageShow::vInit(){
	ReactiveComponent::vInit();
	cv::namedWindow(m_szName.c_str());
}


void ImageShow::vFinalize(){
	ReactiveComponent::vFinalize();
	m_Finished = true;
	cv::destroyWindow(m_szName.c_str());
}


bool ImageShow::bHasMoreSteps(){
	ReactiveComponent::bHasMoreSteps();
	return !m_Finished;
}


void ImageShow::vStep(){
	ReactiveComponent::vStep();
	if(m_mInputPorts["ImageInput"].bIsValid()){
		SRI::Ref<SRI::Message> m = m_mInputPorts["ImageInput"]->ptReceive();
		SRI::Ref<SRI::Message> tmp =  m_mInputPorts["ImageInput"]->ptReceive();
		while(tmp.bIsValid()){
			m= tmp;
			tmp =  m_mInputPorts["ImageInput"]->ptReceive();
		}

		if(m.bIsValid()){
			if(m->szGetType() == "objectMessage"){
				SRI::ObjectMessage* om = dynamic_cast<ObjectMessage*>(m.ptGetObj());
				if(om != NULL){
			//		SRI::Ref<Serializable> ptImg = om->ptGetObjectRef(new Image());
				 	SRI::Ref<Serializable> ptImg = om->ptGetObjectRef<Image>();
				 	if(ptImg.bIsValid())
					{
						m_tLog.info("SRI::Image received");
						Image* img = dynamic_cast<Image*>(ptImg.ptGetObj());
						if( (img != NULL) && ( img->dims <= 2) && img->total() > 0){
							cv::imshow(m_szName.c_str(), *img);
				//			cvWaitKey(0);
							// Show the result:
        
							// And display it:
							char key = (char) cv::waitKey(20);
							
							
						}
						
					}
					//Image img;
					//img.iFromString(om->szGetContent());
					//if(( img.dims <= 2) && img.total() > 0){
					//	m_tLog.info("show Image");
					//	cv::imshow(m_szName.c_str(), img);
					//	 

					//	  // wait for a key
					//	  cvWaitKey(0);

					//	  
					//}
				}
			}else if(m->szGetTypeId() == "cvImage"){
				Image img;
				img.iFromString(m->szGetContent());
				if(( img.dims <= 2) && img.total() > 0){
					cv::imshow(m_szName.c_str(), img);
					cv::waitKey(20);
				}
			}else{
				m_tLog.error("Received wrong message type");

			}
		}
	}
}


void ImageShow::vPreStep(){
	ReactiveComponent::vPreStep();
}

void ImageShow::vPostStep(){
	ReactiveComponent::vPostStep();

}




}