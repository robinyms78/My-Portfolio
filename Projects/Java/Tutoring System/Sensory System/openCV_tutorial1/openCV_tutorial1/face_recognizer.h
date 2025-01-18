#ifndef SRI_FACERECOGNIZER_H
#define SRI_FACERECOGNIZER_H

#include "SRI.h"
#include "SRIRegistryPlugin.h"

#include "opencv2/core/core.hpp"
#include "opencv2/contrib/contrib.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/objdetect/objdetect.hpp"

#include <iostream>
#include <fstream>
#include <sstream>

#include "Image.h"

using namespace cv;
using namespace std;


namespace SRI{


//INST_TEMPLATE SRI::Ref<cv::VideoCapture>;

class CVFaceRecognizer : public SRI::ReactiveComponent{


private:
	int im_width;
    int im_height;
	int face_ctr;
	vector<Mat> images;
    vector<int> labels;
	cv::Ptr<FaceRecognizer> model;
	CascadeClassifier haar_cascade;
	bool m_showImage;

	Logger m_tLog;
	bool m_Finished;
	
	void parseImage(cv::Mat mat);
	void CVFaceRecognizer::read_csv(const string& filename, vector<Mat>& images, vector<int>& labels, char separator = ';');

protected:
	IplImage* m_ptCapture;	// camera resource can be shared between multiple camera components
	SRI::Ref<Serializable> m_tFrame;
	SRI::Ref<Serializable> m_tResult;

public:
	CVFaceRecognizer(SRI::String name, 
		int algo_type, SRI::String faceHarrCascade, SRI::String faceCSV,bool showImage=true);
	virtual ~CVFaceRecognizer();

	CVFaceRecognizer(const CVFaceRecognizer& c);
	CVFaceRecognizer& operator=(const CVFaceRecognizer& c);
	

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