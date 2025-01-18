#ifndef SRI_CAMERA_H
#define SRI_CAMERA_H

#include "SRI.h"
#include "SRIRegistryPlugin.h"

#pragma warning( disable : 4251 4996) 
#include "cv.h"
#include "highgui.h"
#include "Image.h"


namespace SRI{


//INST_TEMPLATE SRI::Ref<cv::VideoCapture>;

class Camera : public SRI::ReactiveComponent{


private:
	Logger m_tLog;

protected:
	Ref<cv::VideoCapture> m_ptCapture;  // camera resource can be shared between multiple camera components
	SRI::Ref<Serializable> m_tFrame;

public:
	Camera(SRI::String name);
	virtual ~Camera();

	Camera(const Camera& c);
	Camera& operator=(const Camera& c);

	int iOpenDevice(int devNum);


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