////////////////////////////////////////////////////////////////////////
//
// hello-world.cpp
//
// This is a simple, introductory OpenCV program. The program reads an
// image from a file, inverts it, and displays the result. 
//
////////////////////////////////////////////////////////////////////////
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <cv.h>
#include <highgui.h>
#include "SRI.h"
#include "CVImageLoader.h"
#include "ImageShow.h"
#include "Camera.h"
#include "face_recognizer.h"
#include "SRI_openAL.h"

using namespace SRI;

class Counter : public SRI::ReactiveComponent{
private:
	int counter;
	SRI::Logger log;

	SRI::Ref<SRI::Message> message;
public:
	Counter():SRI::ReactiveComponent("Counter"), counter(0), log("Counter", SRI::LOG_DEBUG){
		iCreateOutputPort("VoiceCmdInput", "voiceEnum");
	}
	virtual ~Counter(){}

	virtual void vInit(){
		Component::vInit();
		counter = 5;
		log.debug("Counter init");
	}

	virtual void vSetCounter(int val){
		counter = val;	
	}

	virtual void vStep(){
		Component::vStep();

		char num[2];
		itoa(counter,num,10);
		SRI::String str(num);
		
		message = new SRI::Message(str);
		m_mOutputPorts["VoiceCmdInput"]->iSend(message);


		log.debug("Counter at: %d\n", counter);
		--counter;
		Sleep(1000);
		
	}

	virtual bool bHasMoreSteps(){
		bool res = Component::bHasMoreSteps();
		return (counter >= 0);
	}
};

int main(int argc, char *argv[])
{

	SRI::Logger log("SRIMinApplication", SRI::LOG_DEBUG);
	log.info("Start demo application");

	SRI::SRIEngine* engine = new SRI::SRIEngine("MinApplication");

	/*CVImageLoader* loader = new CVImageLoader("loader1","C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.JPG");

	if(engine->iAddComponent(loader) != SRI::SRI_OK){
		log.error("Unable to add loader to engine");
	}else{
		log.debug("Added loader to engine");
	}

	ImageShow* imgShow = new ImageShow("show1");
	if(engine->iAddComponent(imgShow) != SRI::SRI_OK){
		log.error("Unable to add imgShow to engine");
	}else{
		log.debug("Added imgShow to engine");
	}

	
	if(engine->iConnect("loader1", "LoadedImage", "show1", "ImageInput") != SRI::SRI_OK)
	{
		log.error("Unable to connect imgLoader and imgShow to engine");
	}else{
		log.debug("Connect imgLoader and imgShow success");
	}
*/
	

	int mode = 2;
	if(mode == 0)//show face
	{
		Camera* cam = new Camera("webcam");
	if(engine->iAddComponent(cam) != SRI::SRI_OK){
		log.error("Unable to add cam to engine");
	}else{
		log.debug("Added cam to engine");
	}
		ImageShow* imgShow2 = new ImageShow("show2");
		if(engine->iAddComponent(imgShow2) != SRI::SRI_OK){
			log.error("Unable to add imgShow2 to engine");
		}else{
			log.debug("Added imgShow2 to engine");
		}
		if(engine->iConnect("webcam", "CaptureImage", "show2", "ImageInput") != SRI::SRI_OK)
		{
			log.error("Unable to connect webcam and imgShow to engine");
		}else{
			log.debug("Connect imgLoader and imgShow success");
		}
	}
	else if(mode ==1)
	{

		Camera* cam = new Camera("webcam");
	if(engine->iAddComponent(cam) != SRI::SRI_OK){
		log.error("Unable to add cam to engine");
	}else{
		log.debug("Added cam to engine");
	}
		CVFaceRecognizer* imgShow2 = new CVFaceRecognizer("show2",3,
			"C:\\Users\\mht\\Desktop\\visual-control\\haarcascades\\haarcascade_frontalface_alt.xml",
			"C:\\FYP\\workingDir_Debug/image.csv");

		if(engine->iAddComponent(imgShow2) != SRI::SRI_OK){
			log.error("Unable to add imgShow2 to engine");
		}else{
			log.debug("Added imgShow2 to engine");
		}

		if(engine->iConnect("webcam", "CaptureImage", "show2", "ImageInput") != SRI::SRI_OK)
		{
			log.error("Unable to connect webcam and imgShow to engine");
		}else{
			log.debug("Connect imgLoader and imgShow success");
		}
	}
	else if(mode ==2)
	{

		CV_VoicePlayer* imgShow2 = new CV_VoicePlayer("voiceTest","C:\\FYP\\workingDir_Debug\\voice.csv");

		if(engine->iAddComponent(imgShow2) != SRI::SRI_OK){
			log.error("Unable to add imgShow2 to engine");
		}else{
			log.debug("Added imgShow2 to engine");
		}

		Counter* counter = new Counter();

		if(engine->iAddComponent(counter) != SRI::SRI_OK){
			log.error("Unable to add counter to engine");
		}else{
			log.debug("Added counter to engine");
		}


		if(engine->iConnect("Counter", "VoiceCmdInput", "voiceTest", "VoiceCmdInput") != SRI::SRI_OK)
		{
			log.error("Unable to connect webcam and imgShow to engine");
		}else{
			log.debug("Connect imgLoader and imgShow success");
		}
	}

	engine->vInit();
	log.info("Starting Application");
	engine->vRun();
	log.info("Application finished");
	engine->vFinalize();

	delete engine;

	/*
  IplImage* img = 0; 
  int height,width,step,channels;
  uchar *data;
  int i,j,k;

  //if(argc<2){
  //  printf("Usage: main <image-file-name>\n\7");
  //  exit(0);
  //}

  // load an image  
  img=cvLoadImage("C:\\Documents and Settings\\haotian\\My Documents\\My Pictures\\main_rotate.JPG");
  if(!img){
    printf("Could not load image file: %s\n",argv[1]);
    exit(0);
  }

  // get the image data
  height    = img->height;
  width     = img->width;
  step      = img->widthStep;
  channels  = img->nChannels;
  data      = (uchar *)img->imageData;
  printf("Processing a %dx%d image with %d channels\n",height,width,channels); 

  // create a window
  cvNamedWindow("mainWin", CV_WINDOW_AUTOSIZE); 
  cvMoveWindow("mainWin", 100, 100);

  // invert the image
  for(i=0;i<height;i++) for(j=0;j<width;j++) for(k=0;k<channels;k++)
    data[i*step+j*channels+k]=255-data[i*step+j*channels+k];

  // show the image
  cvShowImage("mainWin", img );

  // wait for a key
  cvWaitKey(0);

  // release the image
  cvReleaseImage(&img );

  */
  return 0;
}