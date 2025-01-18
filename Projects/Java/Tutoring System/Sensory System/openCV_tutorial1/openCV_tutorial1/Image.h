#ifndef SRI_IMAGE_H
#define SRI_IMAGE_H

#pragma warning( disable : 4251 4996 4275) 

#include "Serializable.h"
#include "cv.h"
#include "SRI.h"
#include "SRIRegistryPlugin.h"
#include "Logger.h"

namespace SRI{

class Image: public cv::Mat, public Serializable{

private:
	SRI::Logger m_tLog;
	/** The destidantion must be 3 times as big as source*/


public:
	Image();
	Image(int rows, int cols, int type);
	Image(int _rows, int _cols, int _type, const cv::Scalar& _s);
	Image(cv::Size _sz, int _type);
	Image(cv::Size _sz, int _type, const cv::Scalar& _s);
	Image(int _dims, const int* _sz, int _type);
	Image(int _dims, const int* _sz, int _type, const cv::Scalar& _s);
	Image(const Mat& m);
	Image(int _rows, int _cols, int _type, void* _data, size_t _step);
	Image(cv::Size _sz, int _type, void* _data, size_t _step);
	/*Image(const cv::CvMat* m, bool copyData);
	Image(const vector<_Tp>& vec, bool copyData);
	Image(const cv::Vec<_Tp, n>& vec, bool copyData);
	Image(const cv::Matx<_Tp,m,n>& M, bool copyData);
	Image(const cv::Point_<_Tp>& pt, bool copyData);
	Image(const cv::Point3_<_Tp>& pt, bool copyData);
	Image(const cv::MatCommaInitializer_<_Tp>& commaInitializer);
*/



	Image(const Image& c);
	virtual ~Image();
	Image& operator=(const Image& c);
	Image& operator=(const cv::Scalar& s);


// serializable interface
	virtual SRI::String szToString() const;
	virtual int iFromString(SRI::String data);
	virtual Image* ptClone() const;
	virtual const char* szGetType() const;

};


}



#endif