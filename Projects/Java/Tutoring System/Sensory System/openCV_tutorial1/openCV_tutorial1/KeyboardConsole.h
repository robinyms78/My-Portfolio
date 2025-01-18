#ifndef SRI_KEYBOARD_CONSOLE_H
#define SRI_KEYBOARD_CONSOLE_H

#include "SRI.h"
#include "SRIRegistryPlugin.h"

#pragma warning( disable : 4251 4996) 
//#include "cv.h"
//#include "highgui.h"
//#include "Image.h"


namespace SRI{


//INST_TEMPLATE SRI::Ref<cv::VideoCapture>;

class KeyboardConsole : public SRI::ReactiveComponent{


private:
	Logger m_tLog;

protected:
	//use message(string)
//	SRI::Ref<Serializable> m_tFrame;

public:
	KeyboardConsole(SRI::String name);
	virtual ~KeyboardConsole();

	KeyboardConsole(const KeyboardConsole& c);
	KeyboardConsole& operator=(const KeyboardConsole& c);

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