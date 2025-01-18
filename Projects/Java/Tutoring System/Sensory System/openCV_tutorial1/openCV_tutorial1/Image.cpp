
#include "Image.h"
#include "SRIGlobals.h"
#ifdef USE_TINYXML
#include "xpath_processor.h"
#else
#include "rapidxml.hpp"
#include "rapidxml_print.hpp"
#endif
#include <sstream>
#include <string>
#include "SRIUtil.h"
#include "core/types_c.h"

//TinyXPath::

namespace SRI{
	namespace cvUtil{
		static const char TypeSymbol[] = "ucwsifdr";

		
		bool bIsdigit(char c){
			return '0' <= c && c <= '9';
		}

		char* pszEncodeFormat(int type, char* ptr){
			if(ptr == NULL){
				return NULL;
			}
			sprintf(ptr, "%d%c", CV_MAT_CN(type), TypeSymbol[CV_MAT_DEPTH(type)] );
			return ptr + ( ptr[2] == '\0' && ptr[0] == '1' );
		}

		int iDecodeFormat( const char* dt, int* fmt_pairs, int max_len ){
			int fmt_pair_count = 0;
			int i = 0, k = 0, len = dt ? (int)strlen(dt) : 0;

			if( !dt || !len )
				return 0;

			assert( fmt_pairs != 0 && max_len > 0 );
			fmt_pairs[0] = 0;
			max_len *= 2;

			for( ; k < len; k++ )
			{
				char c = dt[k];

				if( bIsdigit(c) )
				{
					int count = c - '0';
					if( bIsdigit(dt[k+1]) )
					{
						char* endptr = 0;
						count = (int)strtol( dt+k, &endptr, 10 );
						k = (int)(endptr - dt) - 1;
					}

					if( count <= 0 )
						CV_Error( CV_StsBadArg, "Invalid data type specification" );

					fmt_pairs[i] = count;
				}
				else
				{
					const char* pos = strchr( TypeSymbol, c );
					if( !pos )
						CV_Error( CV_StsBadArg, "Invalid data type specification" );
					if( fmt_pairs[i] == 0 )
						fmt_pairs[i] = 1;
					fmt_pairs[i+1] = (int)(pos - TypeSymbol);
					if( i > 0 && fmt_pairs[i+1] == fmt_pairs[i-1] )
						fmt_pairs[i-2] += fmt_pairs[i];
					else
					{
						i += 2;
						if( i >= max_len )
							CV_Error( CV_StsBadArg, "Too long data type specification" );
					}
					fmt_pairs[i] = 0;
				}
			}

			fmt_pair_count = i/2;
			return fmt_pair_count;
		}



		

	}
	//	extern int icvDecodeFormat( const char* dt, int* fmt_pairs, int max_len );
	//	extern char* icvEncodeFormat( int elem_type, char* dt );
}


#ifdef USE_TINYXML
#else
	using namespace rapidxml;


namespace SRI{

	void vAddIntAttribute(xml_document<>& doc, xml_node<>* node, const char* name, int value){
		xml_attribute<>* attr = doc.allocate_attribute(name);
		char* szValue = doc.allocate_string(NULL, 32);
		sprintf_s(szValue, 32, "%d", value);
		attr->value(szValue);
		node->append_attribute(attr);
	}
}

#endif


namespace SRI{



Image::Image():m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(int _rows, int _cols, int _type):cv::Mat(_rows,_cols,_type),m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(int _rows, int _cols, int _type, const cv::Scalar& _s):cv::Mat(_rows, _cols,_type, _s),m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(cv::Size _sz, int _type):cv::Mat(_sz, _type),m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(cv::Size _sz, int _type, const cv::Scalar& _s):cv::Mat(_sz, _type, _s),m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(int _dims, const int* _sz, int _type):cv::Mat(_dims, _sz, _type),m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(int _dims, const int* _sz, int _type, const cv::Scalar& _s):cv::Mat(_dims, _sz,_type, _s),m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(const Mat& m):cv::Mat(m),m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(int _rows, int _cols, int _type, void* _data, size_t _step):cv::Mat(_rows, _cols, _type, _data, _step),m_tLog("Image", SRI::LOG_DEBUG){

}

Image::Image(cv::Size _sz, int _type, void* _data, size_t _step):cv::Mat(_sz, _type, _data, _step),m_tLog("Image", SRI::LOG_DEBUG){

}

//Image::Image(const cv::CvMat* m, bool copyData):cv::Mat(m, copyData),m_tLog("Image", SRI::LOG_DEBUG){
//
//}
//
//Image::Image(const cv::vector<_Tp>& vec, bool copyData):cv::Mat(vec, copyData),m_tLog("Image", SRI::LOG_DEBUG){
//
//}
//
//Image::Image(const cv::Vec<_Tp, n>& vec, bool copyData):cv::Mat(vec, copyData),m_tLog("Image", SRI::LOG_DEBUG){
//
//}
//
//Image::Image(const cv::Matx<_Tp,m,n>& M, bool copyData):cv::Mat(M, copyData),m_tLog("Image", SRI::LOG_DEBUG){
//
//}
//
//Image::Image(const cv::Point_<_Tp>& pt, bool copyData):cv::Mat(pt, copyData),m_tLog("Image", SRI::LOG_DEBUG){
//
//}
//
//Image::Image(const cv::Point3_<_Tp>& pt, bool copyData): cv::Mat(pt, copyData),m_tLog("Image", SRI::LOG_DEBUG){
//
//}
//
//Image::Image(const cv::MatCommaInitializer_<_Tp>& commaInitializer):cv::Mat(commaInitializer),m_tLog("Image", SRI::LOG_DEBUG){
//
//}


Image::Image(const Image& c):cv::Mat(c),m_tLog("Image", SRI::LOG_DEBUG){

}

Image& Image::operator=(const Image& c){
	if(this == &c){
		return *this;
	}
	cv::Mat::operator=(c);

	return *this;
}

Image& Image::operator=(const cv::Scalar& s){
	
	cv::Mat::operator=(s);

	return *this;
}

Image::~Image(){

}




SRI::String Image::szToString() const{

#ifdef USE_TINYXML
	TiXmlDocument doc;

	//doc.InsertEndChild(TiXmlDeclaration("1.0", "UTF-8", "yes"));
	TiXmlElement img("Image");
	
	char dt[16];
	img.SetAttribute("format", cvUtil::pszEncodeFormat(CV_MAT_TYPE(type()), dt ));

	TiXmlElement txDims("Dimension");
	txDims.SetAttribute("dims", dims);
	txDims.SetAttribute("rows", rows);
	txDims.SetAttribute("cols", cols);
	for(int i = 0; i < dims; i++){
		TiXmlElement txSize("Size");
		txSize.SetAttribute("dim", i);
		txSize.SetAttribute("dimSize", size[i]);
		txDims.InsertEndChild(txSize);
	}
	img.InsertEndChild(txDims);

	//char typeBuf[16];
	//cv::icvEncodeFormat( CV_MAT_TYPE(type()), typeBuf);
	img.SetAttribute("type", type());
	
	TiXmlElement txData("Data");
	TiXmlText txRaw("");
	txRaw.SetCDATA(true);
	std::stringstream xmlMem;

	/** If dimensions are less then 2 rows and coloums can be used. Otherwise
	* the size array needs to be used. 
	* Example of creating a cube matric:
	* \code{.cpp}
	* // create a 100x100x100 8-bit array
	* int sz[] = {100, 100, 100};
	* Mat bigCube(3, sz, CV_8U, Scalar::all(0));
	* \endcode
	**/
	if(this->dims <= 2){
		img.SetAttribute("cvType", CV_TYPE_NAME_MAT);   //CV_TYPE_NAME_MATND 
		 if( rows > 0 && cols > 0 ){
			 const unsigned char* imgPtr = NULL;
			 size_t step = this->step[0];
			 unsigned char* encoded = new unsigned char[step * 3 + 1];

			 int nRows = rows;
			 for(int i = 0; i < nRows; i++){
				 imgPtr = this->ptr<unsigned char>(i);
				 SRI::vEncodeBytes(encoded, imgPtr, step);
				 xmlMem.write((char*)encoded, step*3);
			 }
			 delete[] encoded;
		 }
		 txRaw.SetValue(xmlMem.str());
	}else{
		img.SetAttribute("cvType", CV_TYPE_NAME_MATND);
		if(total() != 0){
			const Mat* arrays[] = {this, 0 };
			Mat planes[1];
			cv::NAryMatIterator it(arrays, planes);
			size_t size = it.size*elemSize();
			unsigned char* encoded = new unsigned char[size * 3 + 1];
			const unsigned char* imgPtr = NULL;
			for(size_t i = 0; i < it.nplanes; i++, ++it){
				imgPtr = (it.planes[0]).ptr<unsigned char>(0);
				SRI::vEncodeBytes(encoded, imgPtr, size);
				xmlMem.write((char*)encoded,size*3);
			}
			delete[] encoded;
		}
		txRaw.SetValue(xmlMem.str());
	}

	/*size = cvGetSize(this);
	if( (size.height > 0) && (size.width > 0) && (this->data.ptr != NULL) ){
		 if( CV_IS_MAT_CONT(type()) ){
            size.width *= size.height;
            size.height = 1;
        }

        for( y = 0; y < size.height; y++ )
            cvWriteRawData( fs, mat->data.ptr + y*mat->step, size.width, dt );
	}*/
	/*
	cv::MatConstIterator it(this);
	for(it = this->begin(); it
*/

	txData.InsertEndChild(txRaw);
	img.InsertEndChild(txData);

	doc.InsertEndChild(img);
	TiXmlPrinter printer;
	printer.SetIndent("\t");
	printer.SetLineBreak("\n");
	doc.Accept(&printer);


	return printer.CStr();
#else
	int msgSize = 0;
	xml_document<> doc;

	xml_node<>* rxImage = doc.allocate_node(node_element, "Image");
	char* dt = doc.allocate_string(NULL, 16);
	cvUtil::pszEncodeFormat(CV_MAT_TYPE(type()),dt);
	
	xml_attribute<>* rxaFormat = doc.allocate_attribute("format", dt);
	rxImage->append_attribute(rxaFormat);
	vAddIntAttribute(doc, rxImage, "type", type());

	xml_node<>* rxDim = doc.allocate_node(node_element, "Dimension"); 
	vAddIntAttribute(doc, rxDim, "dims", dims);
	vAddIntAttribute(doc, rxDim, "rows", rows);
	vAddIntAttribute(doc, rxDim, "cols", cols);

	msgSize += 512;

	/*xml_attribute<>* rxaDims = doc.allocate_attribute("dims");
	char* szDims = doc.allocate_string(NULL, 32);
	sprintf_s(szDims, 32, "%d", dims);
	rxaDims->value(szDims);
	rxDim->append_attribute(rxaDims);

	xml_attribute<>* rxaRows = doc.allocate_attribute("rows");
	char* szRows = doc.allocate_string(NULL, 32);
	sprintf_s(szRows, 32, "%d", rows);
	rxaRows->value(szRows);
	rxDim->append_attribute(rxaRows);

	xml_attribute<>* rxaCols = doc.allocate_attribute("cols");
	char* szCols = doc.allocate_string(NULL, 32);
	sprintf_s(szCols, 32, "%d", cols);
	rxaRows->value(szCols);
	rxDim->append_attribute(rxaCols);*/

	for(int i = 0; i < dims; i++){
		xml_node<>* rxSize = doc.allocate_node(node_element, "Size"); 
		vAddIntAttribute(doc, rxSize, "dim", i);
		vAddIntAttribute(doc, rxSize, "dimSize", size[i]);
		rxDim->append_node(rxSize);
		msgSize += 64;
	}
	rxImage->append_node(rxDim);

	xml_node<>* rxData = doc.allocate_node(node_element, "Data");
	xml_node<>* rxRaw = doc.allocate_node(node_cdata);
	


	/** If dimensions are less then 2 rows and coloums can be used. Otherwise
	* the size array needs to be used. 
	* Example of creating a cube matric:
	* \code{.cpp}
	* // create a 100x100x100 8-bit array
	* int sz[] = {100, 100, 100};
	* Mat bigCube(3, sz, CV_8U, Scalar::all(0));
	* \endcode
	**/
	if(this->dims <= 2){
		xml_attribute<>* rxaCvType = doc.allocate_attribute("cvType", CV_TYPE_NAME_MAT);
		rxImage->append_attribute(rxaCvType);
		if( rows > 0 && cols > 0 ){
			const unsigned char* imgPtr = NULL;
			size_t step = this->step[0];
			char* encoded = doc.allocate_string(NULL, rows * step * 3 + 1);
			unsigned char* encPtr = (unsigned char*) encoded;

			int nRows = rows;
			for(int i = 0; i < nRows; i++){
				imgPtr = this->ptr<unsigned char>(i);
				SRI::vEncodeBytes(encPtr, imgPtr, step);
				encPtr += step*3;
			}
			rxRaw->value(encoded, rows*step*3);
			msgSize += rows * step * 3;
		}
	}else{
		xml_attribute<>* rxaCvType = doc.allocate_attribute("cvType", CV_TYPE_NAME_MATND);
		rxImage->append_attribute(rxaCvType);

		if(total() != 0){
			const Mat* arrays[] = {this, 0 };
			Mat planes[1];
			cv::NAryMatIterator it(arrays, planes);
			size_t size = it.size*elemSize();
			char* encoded = doc.allocate_string(NULL, it.nplanes* size * 3 + 1);
			unsigned char* encPtr = (unsigned char*)encoded;
			const unsigned char* imgPtr = NULL;
			for(size_t i = 0; i < it.nplanes; i++, ++it){
				imgPtr = (it.planes[0]).ptr<unsigned char>(0);
				SRI::vEncodeBytes(encPtr, imgPtr, size);
				encPtr += size * 3;
			}
			rxRaw->value(encoded, it.nplanes* size * 3 + 1);
			msgSize += it.nplanes* size * 3;
		}
		
	}

	rxData->append_node(rxRaw);
	rxImage->append_node(rxData);
	doc.append_node(rxImage);



	char* xmlBuffer = new char[msgSize];
	char *end = print(xmlBuffer, doc, 0);     
	*end = 0;                         
	
	SRI::String res(xmlBuffer, end-xmlBuffer);
	delete[] xmlBuffer;

	return res;
	//std::string xml;
	//rapidxml::print(std::back_inserter(xml), doc, 0);
	//return xml;


#endif
}

int Image::iFromString(SRI::String data){
#ifdef USE_TINYXML
	TiXmlDocument doc;
	doc.Parse(data.c_str());
	if(doc.Error()){
		m_tLog.error("Unable to parse image xml: (Row:%d, Col:%d) %s", doc.ErrorRow(), doc.ErrorCol(), doc.ErrorDesc());
		return SRI::SRI_ERR_SYNTAX;
	}

	TiXmlElement* txImage = doc.RootElement();
	if( (txImage == NULL) || (txImage->ValueTStr() != "Image")){
		m_tLog.debug("Unable to parse image from XML");
		return SRI::SRI_ERR_TYPE;
	}

	TiXmlElement* txDimension = txImage->FirstChildElement("Dimension");
	TiXmlElement* txData = txImage->FirstChildElement("Data");

	if(( txDimension == NULL) || (txData == NULL)){
		m_tLog.error("Unable to parse Image Dimension or Data field from xml");
	}

	int dims = 0;
	int type = 0;
	const char* format = txImage->Attribute("format");
	if(format == NULL){
		m_tLog.error("Unable to parse the format attribute");
		return SRI::SRI_ERR_SYNTAX;
	}

	if (txDimension->QueryIntAttribute("dims", &dims) != TIXML_SUCCESS){
		m_tLog.error("Unable to read dims attribute");
		return SRI::SRI_ERR_SYNTAX;
	}
	
	if (txImage->QueryIntAttribute("type", &type) != TIXML_SUCCESS){
		m_tLog.error("Unable to  read type attribute");
		return SRI::SRI_ERR_SYNTAX;
	}
	
	if(dims <= 2){
		int rows = 0, cols = 0;
		if (txDimension->QueryIntAttribute("rows", &rows) != TIXML_SUCCESS){
			m_tLog.error("Unable to read rows attribute");
			return SRI::SRI_ERR_SYNTAX;
		}
		if (txDimension->QueryIntAttribute("cols", &cols) != TIXML_SUCCESS){
			m_tLog.error("Unable to read cols attribute");
			return SRI::SRI_ERR_SYNTAX;
		}

		this->create(rows, cols, type);
		const char* dataPtr = txData->GetText();
		if(dataPtr != NULL){
			unsigned char* imgPtr = NULL;
			size_t step = this->step[0];
			size_t codedStep = step * 3;
			for(int i = 0; i < rows; i++){
				imgPtr = this->ptr<unsigned char>(i);		
				SRI::vDecodeBytes(imgPtr, (unsigned char*)(dataPtr + (i * codedStep)), codedStep);
				//memcpy(imgPtr, dataPtr + (i * step), step);
			}
		}
	}else{
		int* sz = new int[dims];

		TiXmlElement* txSize = txDimension->FirstChildElement("Size");
		while(txSize != NULL){
			int dim = 0;
			if(txSize->QueryIntAttribute("dim", &dim) != TIXML_SUCCESS){
				m_tLog.error("Unable to read dimension information");
				return SRI::SRI_ERR_SYNTAX;
			}
			int dimSize = 0;
			if(txSize->QueryIntAttribute("dimSize", &dimSize) != TIXML_SUCCESS){
				m_tLog.error("Unable to read dimension size information");
				return SRI::SRI_ERR_SYNTAX;
			}

			if( (dim >= 0) && (dim < dims) ){
				sz[dim] = dimSize;
			}
			txSize = txSize->NextSiblingElement("Size");
		}
		
		this->create(dims, sz, type);

		const char* dataPtr = txData->GetText();
		if(( total() != 0) && (dataPtr != NULL)){
			const Mat* arrays[] = {this, 0 };
			Mat planes[1];
			cv::NAryMatIterator it(arrays, planes);
			size_t size = it.size*elemSize();
			size_t codedSize =  size *3;
			unsigned char* imgPtr = NULL;
			for(size_t i = 0; i < it.nplanes; i++, ++it){
				imgPtr = (it.planes[0]).ptr<unsigned char>(0);
				SRI::vDecodeBytes(imgPtr, (unsigned char*)(dataPtr + (i * codedSize)), codedSize);
				//memcpy(imgPtr, dataPtr + (i * size), size);
			}
		}

		delete[] sz;
	}




	return SRI::SRI_OK;
#else
	xml_document<> doc;
	try{
		doc.parse<rapidxml::parse_non_destructive>(const_cast<char*>(data.c_str()));
	}catch(rapidxml::parse_error& e){
		m_tLog.error("Unable to parse image xml: %s", e.what());
		return SRI::SRI_ERR_SYNTAX;
	}
	
	xml_node<>* rxImage = doc.first_node("Image");
	if(rxImage == NULL){
		m_tLog.debug("Unable to parse image from XML");
		return SRI::SRI_ERR_TYPE;
	}

	int type = 0;
	xml_attribute<>* rxaType = rxImage->first_attribute("type");
	if(rxaType == NULL){
		m_tLog.error("Unable to read type attribute");
		return SRI::SRI_ERR_SYNTAX;
	}
	std::string szType(rxaType->value(), rxaType->value_size());
	type = atoi(szType.c_str());


	xml_node<>* rxDimension = rxImage->first_node("Dimension");
	if(rxDimension == NULL){
		m_tLog.debug("Unable to parse Dimension from XML");
		return SRI::SRI_ERR_TYPE;
	}

	xml_node<>* rxData = rxImage->first_node("Data");
	if(rxData == NULL){
		m_tLog.debug("Unable to parse Data from XML");
		return SRI::SRI_ERR_TYPE;
	}

	xml_node<>* rxRaw = rxData->first_node();
	if(rxRaw == NULL){
		m_tLog.debug("Unable to parse raw data from XML");
		return SRI::SRI_ERR_TYPE;
	}

	int dims = 0;
	xml_attribute<>* rxaDims = rxDimension->first_attribute("dims");
	if(rxaDims == NULL){
		m_tLog.error("Unable to read dims attribute");
		return SRI::SRI_ERR_SYNTAX;
	}
	std::string szDims(rxaDims->value(), rxaDims->value_size());
	dims = atoi(szDims.c_str());

	
	if(dims <= 2){
		int rows = 0, cols = 0;
	
		xml_attribute<>* rxarows = rxDimension->first_attribute("rows");
		if(rxarows == NULL){
			m_tLog.error("Unable to read rows attribute");
			return SRI::SRI_ERR_SYNTAX;
		}
		std::string szrows(rxarows->value(), rxarows->value_size());
		rows = atoi(szrows.c_str());

		xml_attribute<>* rxacols = rxDimension->first_attribute("cols");
		if(rxacols == NULL){
			m_tLog.error("Unable to read cols attribute");
			return SRI::SRI_ERR_SYNTAX;
		}
		std::string szcols(rxacols->value(), rxacols->value_size());
		cols = atoi(szcols.c_str());


		this->create(rows, cols, type);
		const char* dataPtr = rxRaw->value();
		if(dataPtr != NULL){
			unsigned char* imgPtr = NULL;
			size_t step = this->step[0];
			size_t codedStep = step * 3;
			for(int i = 0; i < rows; i++){
				imgPtr = this->ptr<unsigned char>(i);		
				SRI::vDecodeBytes(imgPtr, (unsigned char*)(dataPtr + (i * codedStep)), codedStep);
			}
		}
	}else{
		int* sz = new int[dims];

		xml_node<>* rxSize = rxDimension->first_node("Size");

		while(rxSize != NULL){
			int dim = 0;

			xml_attribute<>* rxadim = rxDimension->first_attribute("dim");
			if(rxadim == NULL){
				m_tLog.error("Unable to read dim attribute");
				return SRI::SRI_ERR_SYNTAX;
			}
			std::string szdim(rxadim->value(), rxadim->value_size());
			dim = atoi(szdim.c_str());

			int dimSize = 0;
			xml_attribute<>* rxadimSize = rxDimension->first_attribute("dimSize");
			if(rxadimSize == NULL){
				m_tLog.error("Unable to read dimSize attribute");
				return SRI::SRI_ERR_SYNTAX;
			}
			std::string szdimSize(rxadimSize->value(), rxadimSize->value_size());
			dimSize = atoi(szdimSize.c_str());

			
			if( (dim >= 0) && (dim < dims) ){
				sz[dim] = dimSize;
			}
			rxSize = rxSize->next_sibling("Size");
		}
		
		this->create(dims, sz, type);

		const char* dataPtr = rxRaw->value();
		if(( total() != 0) && (dataPtr != NULL)){
			const Mat* arrays[] = {this, 0 };
			Mat planes[1];
			cv::NAryMatIterator it(arrays, planes);
			size_t size = it.size*elemSize();
			size_t codedSize =  size *3;
			unsigned char* imgPtr = NULL;
			for(size_t i = 0; i < it.nplanes; i++, ++it){
				imgPtr = (it.planes[0]).ptr<unsigned char>(0);
				SRI::vDecodeBytes(imgPtr, (unsigned char*)(dataPtr + (i * codedSize)), codedSize);
			}
		}

		delete[] sz;
	}

	return SRI::SRI_OK;

#endif
}

Image* Image::ptClone() const{
	Image* c = new Image(*this);
	return c;
}

const char* Image::szGetType() const{
	return "cvImage";
}


}