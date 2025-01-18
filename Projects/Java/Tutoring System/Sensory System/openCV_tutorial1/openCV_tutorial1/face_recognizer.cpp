#include "face_recognizer.h"
#include "ObjectMessage.h"

namespace SRI{


CVFaceRecognizer::CVFaceRecognizer(SRI::String name, int algo_type, 
	SRI::String faceHarrCascade, SRI::String faceCSV, bool showImage):
		ReactiveComponent(name),m_tLog(SRI::String("FaceRecogShow_") + name, SRI::LOG_DEBUG){
	m_showImage = showImage;
	m_Finished = false;
	iCreateInputPort("ImageInput", "cvImage");

	 // These vectors hold the images and corresponding labels:
    vector<Mat> images;
    vector<int> labels;
    // Read in the data (fails if no valid input filename is given, but you'll get an error message):
    try {
		read_csv(faceCSV.c_str(), images, labels);
    } catch (cv::Exception& e) {
     //   cerr << "Error opening file \"" << fn_csv << "\". Reason: " << e.msg << endl;
		string face_fileName = format("Error opening imageDB index file \,", faceCSV.c_str());
		m_tLog.error(face_fileName);
        // nothing more we can do
        m_Finished = true;
    }

	im_width = images[0].cols;
    im_height = images[0].rows;

	if(algo_type==0)
		model = createFisherFaceRecognizer(80);
	else if(algo_type==1)
		model = createLBPHFaceRecognizer();
	else
		model = createEigenFaceRecognizer(80);
	model->train(images, labels);

	if(!haar_cascade.load(faceHarrCascade.c_str()))
	{
		string face_fileName = format("Error opening faceHarrCascade xml \,", faceHarrCascade.c_str());
		m_tLog.error(face_fileName);
        // nothing more we can do
        m_Finished = true;
	}

	face_ctr =0;

}

CVFaceRecognizer::~CVFaceRecognizer(){

}


CVFaceRecognizer::CVFaceRecognizer(const CVFaceRecognizer& c): ReactiveComponent(c), m_tLog(c.m_tLog){
	m_Finished = false;
}


CVFaceRecognizer& CVFaceRecognizer::operator=(const CVFaceRecognizer& c){
	if(this == &c){
		return *this;
	}
	ReactiveComponent::operator=(c);
	m_tLog = c.m_tLog;
	m_Finished = false;

	return *this;
}



Component* CVFaceRecognizer::ptClone() const{
	CVFaceRecognizer* c = new CVFaceRecognizer(*this);
	return c;
}


void CVFaceRecognizer::vInit(){
	ReactiveComponent::vInit();
	if(m_showImage)
 		cv::namedWindow(m_szName.c_str());
}


void CVFaceRecognizer::vFinalize(){
	ReactiveComponent::vFinalize();
	m_Finished = true;
	if(m_showImage)
	 	cv::destroyWindow(m_szName.c_str());
}


bool CVFaceRecognizer::bHasMoreSteps(){
	ReactiveComponent::bHasMoreSteps();
	return !m_Finished;
}

void CVFaceRecognizer::parseImage(cv::Mat mat)
{
	Mat original = mat.clone();
	Mat gray;
        cvtColor(original, gray, CV_BGR2GRAY);
        // Find the faces in the frame:
        vector< Rect_<int> > faces;
        haar_cascade.detectMultiScale(gray, faces);
        // At this point you have the position of the faces in
        // faces. Now we'll get the faces, make a prediction and
        // annotate it in the video. Cool or what?
		Mat face_resized;

		for(int i = 0; i < faces.size(); i++) {
            // Process face by face:
            Rect face_i = faces[i];
            // Crop the face from the image. So simple with OpenCV C++:
            Mat face = gray(face_i);
            // Resizing the face is necessary for Eigenfaces and Fisherfaces. You can easily
            // verify this, by reading through the face recognition tutorial coming with OpenCV.
            // Resizing IS NOT NEEDED for Local Binary Patterns Histograms, so preparing the
            // input data really depends on the algorithm used.
            //
            // I strongly encourage you to play around with the algorithms. See which work best
            // in your scenario, LBPH should always be a contender for robust face recognition.
            //
            // Since I am showing the Fisherfaces algorithm here, I also show how to resize the
            // face you have just found:
         // Mat face_resized;
            cv::resize(face, face_resized, Size(im_width, im_height), 1.0, 1.0, INTER_CUBIC);
            // Now perform the prediction, see how easy that is:
        //    int prediction = model->predict(face_resized);
			int prediction;
			double dist;
			model->predict(face_resized,prediction,dist);
            // And finally write all we've found out to the original image!
            // First of all draw a green rectangle around the detected face:
            rectangle(original, face_i, CV_RGB(0, 255,0), 1);
            // Create the text we will annotate the box with:
        //    string box_text = format("Prediction = %d", prediction);
			dist/= 100.0;
			string box_text = format("Prediction = %d, confidence = %f", prediction,dist);
            // Calculate the position for annotated text (make sure we don't
            // put illegal values in there):
            int pos_x = std::max(face_i.tl().x - 10, 0);
            int pos_y = std::max(face_i.tl().y - 10, 0);
            // And now put it into the image:
		//	if(dist>1.0)
			{
				putText(original, box_text, Point(pos_x, pos_y), FONT_HERSHEY_PLAIN, 1.0, CV_RGB(0,255,0), 2.0);
			}
        }


		//send out parsed image with face recognition
		{
			//Image ptImg(original);
			//m_tFrame.ptAttachNew(&ptImg);
			//ObjectMessage* message = new ObjectMessage(m_tFrame);
			//m_mOutputPorts["CaptureImage"]->iSend(message);

			////pass PersonRecognized
			//m_tFrame.ptAttachNew(&ptImg);
			//ObjectMessage* message = new ObjectMessage(m_tFrame);
			//m_mOutputPorts["PersonRecognized"]->iSend(message);
			//
		}
		if(m_showImage)
		{
			// Show the result:
			imshow(m_szName.c_str(), original);
			// And display it:
			char key = (char) waitKey(20);
			if(key == 32)
			{
				//save face image
				string face_fileName = format("./image/face%d.jpg", face_ctr);
				face_ctr++;
				imwrite( face_fileName, face_resized );
				namedWindow( m_szName.c_str(), CV_WINDOW_AUTOSIZE );

				imshow( "face captured", face_resized );
			

				waitKey(0);
			}
		}
		
}

void CVFaceRecognizer::vStep(){
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
						//	cv::imshow(m_szName.c_str(), *img);
							parseImage(*img);
				//			cvWaitKey(0);
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
				}
			}else{
				m_tLog.error("Received wrong message type");

			}
		}
	}
}


void CVFaceRecognizer::vPreStep(){
	ReactiveComponent::vPreStep();
}

void CVFaceRecognizer::vPostStep(){
	ReactiveComponent::vPostStep();

}


void CVFaceRecognizer::read_csv(const string& filename, vector<Mat>& images, vector<int>& labels, char separator) {
    std::ifstream file(filename.c_str(), ifstream::in);
    if (!file) {
        string error_message = "No valid input file was given, please check the given filename.";
        CV_Error(CV_StsBadArg, error_message);
		m_tLog.error(error_message);
    }
    string line, path, classlabel;
    while (getline(file, line)) {
        stringstream liness(line);
        getline(liness, path, separator);
        getline(liness, classlabel);
        if(!path.empty() && !classlabel.empty()) {
            images.push_back(imread(path, 0));
            labels.push_back(atoi(classlabel.c_str()));
        }
    }
}




}