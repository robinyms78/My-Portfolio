#ifndef SRI_STRING_H
#define SRI_STRING_H

#include <string>
#include <stdarg.h>
#include "SRIUtilLib.h"
#include "SRIRef.h"

namespace SRI{



/** This is a string class wrapper to allow it being exported from a microsoft dll
*/
class SRIUTIL_API String{

private:
	
	SRI::Ptr<std::string>* m_ptString;

	void vDecRef(Ptr<std::string>** ref);
	void vAttachNew(std::string* obj);

public:
	static size_t npos;

	String();
	String(const char* str);
	String(const String& c);
	String(const std::string& c);
	String(const char* str, size_t n);
	virtual ~String();

	String& operator=(const String& c);
	int size() const ;
	const char* c_str() const;
	std::string sz_str() const;

	const char& at(size_t pos) const;
	char& at(size_t pos);

	const char& operator[](size_t pos) const;
	char& operator[](size_t pos);

	bool operator==(const char str[]) const;
	bool operator==(const String& c) const;
	bool operator!=(const char str[]) const;
	bool operator!=(const String& c) const;
	String operator+(const String& c) const;
	String& operator+=(const String& c);
	bool operator<(const String& c) const;
	bool operator<(const char* str) const;
	bool operator>(const char* str) const ;
	bool operator>(const String& c) const;

	/** Sets the string to a value using the given format string
	* \param length the length of the expanded string
	* \param fmt Format string containing for example %d
	* \param ... parameters to match the format string
	*/
	void vFormat_s(const char* fmt, size_t length, ...);
	void vFormat_s(const char *fmt, size_t length, va_list argPtr);

	/** Same as vFormat_s but tries to calculate the length of resulting string automatically */
	void vFormat(const char* fmt, ...);
	void vFormat(const char *fmt, va_list argPtr);

	String& append(const char* str);
	String& append(const String& c);

	size_t find ( const String& str, size_t pos = 0 ) const;
	size_t find ( const char* s, size_t pos, size_t n ) const;
	size_t find ( const char* s, size_t pos = 0 ) const;
	size_t find ( char c, size_t pos = 0 ) const;

	size_t rfind ( const String& str, size_t pos = -1 ) const;
	size_t rfind ( const char* s, size_t pos, size_t n ) const;
	size_t rfind ( const char* s, size_t pos = -1 ) const;
	size_t rfind ( char c, size_t pos = -1 ) const;

	String substr ( size_t pos = 0, size_t n = -1 ) const;

	/** \returns a converted copy of the string. The original remains unchanged.*/
	String szToLower() const;
	/** \returns a converted copy of the string. The original remains unchanged.*/
	String szToUpper() const;

	std::string::iterator begin();
	std::string::iterator end();

	std::string::const_iterator begin() const;
	std::string::const_iterator end() const;


	String& assign ( const char* s, size_t n );
	
};


}




#endif // include once