
#ifndef SRI_CONSTMAP_ITERATOR_H
#define SRI_CONSTMAP_ITERATOR_H

#ifdef WIN32
//	#pragma warning (push)
//	#pragma warning (disable : 4702)
#endif

#include "SRI/SRIUtil/SRIMap.h"
#include <map>

namespace SRI
{
   // prototype of map class
   template<typename K, typename T> class Map;

   template<typename K, typename T> class ConstMapIterator {
	  friend class SRI::Map<K,T>;

	  typedef typename std::map<K, T>::const_iterator StdConstMapIterator;
	  typedef typename std::map<K, T> StdMap;

	  private:
		 StdConstMapIterator* m_ptStdIt;
		 ConstMapIterator (StdConstMapIterator* it); // only the map can generate an iterator
		 

	  public:
		 virtual ~ConstMapIterator (void);
		 ConstMapIterator (const ConstMapIterator& c);
		 ConstMapIterator<K,T>& operator=(const ConstMapIterator& c);
		 bool operator==(const ConstMapIterator& c);
		 bool operator!=(const ConstMapIterator& c);
		 ConstMapIterator<K,T>& operator++(void);
		 ConstMapIterator<K,T> operator++(int unused); // postfix

		 const K& first();
		 const T& second();
   };

   /** Memory is taken over */
   template<typename K, typename T>
   ConstMapIterator<K, T>::ConstMapIterator(StdConstMapIterator* it){
	   m_ptStdIt = it;
   }

   template<typename K, typename T>
   ConstMapIterator<K, T>::ConstMapIterator (const ConstMapIterator& c){
	   if(c.m_ptStdIt != NULL){
			m_ptStdIt = new StdConstMapIterator(*(c.m_ptStdIt));
	   }else{
		   m_ptStdIt = NULL;
	   }
   }

   template<typename K, typename T>
   ConstMapIterator<K, T>::~ConstMapIterator (void){
	   if(m_ptStdIt != NULL){
		   delete m_ptStdIt;
		   m_ptStdIt = NULL;
	   }
   }

   template<typename K, typename T>
   ConstMapIterator<K,T>& ConstMapIterator<K, T>::operator=(const ConstMapIterator<K,T>& c){
	   if(this == &c){
		   return *this;
	   }
	   if(m_ptStdIt != NULL){
		   delete m_ptStdIt;
		   m_ptStdIt = NULL;
	   }
	   if(c.m_ptStdIt != NULL){
			m_ptStdIt = new StdConstMapIterator(*(c.m_ptStdIt));
	   }else{
		   m_ptStdIt = NULL;
	   }
	   return *this;
   }

   template<typename K, typename T>
   bool ConstMapIterator<K, T>::operator==(const ConstMapIterator<K,T>& c){
	   return (m_ptStdIt->operator==(*(c.m_ptStdIt)));
   }

   template<typename K, typename T>
   bool ConstMapIterator<K, T>::operator!=(const ConstMapIterator<K,T>& c){
	   return ( m_ptStdIt->operator!=(*(c.m_ptStdIt)));
   }

	template<typename K, typename T>
	ConstMapIterator<K,T>& ConstMapIterator<K, T>::operator++(){
		(*m_ptStdIt)++;
		return *this;
	}

	template<typename K, typename T>
	ConstMapIterator<K,T> ConstMapIterator<K, T>::operator++(int unused){
		ConstMapIterator<K,T> it = *this;
		++(*m_ptStdIt);
		return it;
	}


   template<typename K, typename T>
   const K&  ConstMapIterator<K, T>::first(void){
		return (*m_ptStdIt)->first; 
   } 

   template<typename K, typename T>
   const T&  ConstMapIterator<K, T>::second(void){
		return (*m_ptStdIt)->second; 
   } 

} 

#ifdef WIN32
//	#pragma warning (pop)
#endif

#endif // include once
