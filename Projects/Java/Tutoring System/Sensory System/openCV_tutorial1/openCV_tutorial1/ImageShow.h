#ifndef SRI_IMAGESHOW_H
#define SRI_IMAGESHOW_H

#include "SRI.h"
#include "SRIRegistryPlugin.h"

#pragma warning( disable : 4251 4996) 
#include "cv.h"
#include "highgui.h"
#include "Image.h"


namespace SRI{


//INST_TEMPLATE SRI::Ref<cv::VideoCapture>;

class ImageShow : public SRI::ReactiveComponent{


private:
	Logger m_tLog;
	bool m_Finished;

public:
	ImageShow(SRI::String name);
	virtual ~ImageShow();
	ImageShow(const ImageShow& c);
	ImageShow& operator=(const ImageShow& c);

	virtual Component* ptClone() const;
	virtual void vInit();
	virtual void vFinalize();
	virtual bool bHasMoreSteps();
	virtual void vStep();
	virtual void vPreStep();
	virtual void vPostStep();

};


}// end namespace


#endif