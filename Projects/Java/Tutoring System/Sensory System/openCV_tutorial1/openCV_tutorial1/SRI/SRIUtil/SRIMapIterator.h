
#ifndef SRI_MAP_ITERATOR_H
#define SRI_MAP_ITERATOR_H

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

   template<typename K, typename T> class MapIterator {
	  friend class SRI::Map<K,T>;
	  typedef typename std::map<K, T>::iterator StdMapIterator;
	  typedef typename std::map<K, T> StdMap;

	  private:
		 StdMapIterator* m_ptStdIt;
		 MapIterator (StdMapIterator* it); // only the map can generate an iterator
		 

	  public:
		 virtual ~MapIterator (void);
		 MapIterator (const MapIterator& c);
		 MapIterator<K,T>& operator=(const MapIterator& c);
		 bool operator==(const MapIterator& c);
		 bool operator!=(const MapIterator& c);
		 MapIterator<K,T>& operator++(void);
		 MapIterator<K,T> operator++(int unused); // postfix

		 const K& first();
		 T& second();
   };

   /** Memory is taken over */
   template<typename K, typename T>
   MapIterator<K, T>::MapIterator(StdMapIterator* it){
	   m_ptStdIt = it;
   }

   template<typename K, typename T>
   MapIterator<K, T>::MapIterator (const MapIterator& c){
	   if(c.m_ptStdIt != NULL){
			m_ptStdIt = new StdMapIterator(*(c.m_ptStdIt));
	   }else{
		   m_ptStdIt = NULL;
	   }
   }

   template<typename K, typename T>
   MapIterator<K, T>::~MapIterator (void){
	   if(m_ptStdIt != NULL){
		   delete m_ptStdIt;
		   m_ptStdIt = NULL;
	   }
   }

   template<typename K, typename T>
   MapIterator<K,T>& MapIterator<K, T>::operator=(const MapIterator<K,T>& c){
	   if(this == &c){
		   return *this;
	   }
	   if(m_ptStdIt != NULL){
		   delete m_ptStdIt;
		   m_ptStdIt = NULL;
	   }
	   if(c.m_ptStdIt != NULL){
			m_ptStdIt = new StdMapIterator(*(c.m_ptStdIt));
	   }else{
		   m_ptStdIt = NULL;
	   }
	   return *this;
   }

   template<typename K, typename T>
   bool MapIterator<K, T>::operator==(const MapIterator<K,T>& c){
	   return (m_ptStdIt->operator==(*(c.m_ptStdIt)));
   }

   template<typename K, typename T>
   bool MapIterator<K, T>::operator!=(const MapIterator<K,T>& c){
	   return ( m_ptStdIt->operator!=(*(c.m_ptStdIt)));
   }

	template<typename K, typename T>
	MapIterator<K,T>& MapIterator<K, T>::operator++(){
		(*m_ptStdIt)++;
		return *this;
	}

	template<typename K, typename T>
	MapIterator<K,T> MapIterator<K, T>::operator++(int unused){
		MapIterator<K,T> it = *this;
		++(*m_ptStdIt);
		return it;
	}


   template<typename K, typename T>
   const K&  MapIterator<K, T>::first(void){
		return (*m_ptStdIt)->first; 
   } 

   template<typename K, typename T>
   T&  MapIterator<K, T>::second(void){
		return (*m_ptStdIt)->second; 
   } 

} 

#ifdef WIN32
//	#pragma warning (pop)
#endif

#endif // include once
