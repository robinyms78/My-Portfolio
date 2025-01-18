#ifndef SRI_CVImageLoader_H
#define SRI_CVImageLoader_H

#include "SRI.h"
#include "SRIRegistryPlugin.h"

#pragma warning( disable : 4251 4996) 
#include "cv.h"
#include "highgui.h"
#include "Image.h"


namespace SRI{


//INST_TEMPLATE SRI::Ref<cv::VideoCapture>;

class CVImageLoader : public SRI::ReactiveComponent{


private:
	Logger m_tLog;
	bool sentFlag;
protected:
 	IplImage* m_ptCapture;  // camera resource can be shared between multiple camera components
	SRI::Ref<Serializable> m_tFrame;

public:
	CVImageLoader(SRI::String name, SRI::String path);
	virtual ~CVImageLoader();

	CVImageLoader(const CVImageLoader& c);
	CVImageLoader& operator=(const CVImageLoader& c);

//	int iOpenDevice(int devNum);
	int iLoadImage(SRI::String path);


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