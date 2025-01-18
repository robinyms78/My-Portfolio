
#ifndef SRI_MAP_H
#define SRI_MAP_H

#ifdef WIN32
//	#pragma warning (push)
//	#pragma warning (disable : 4702)
#endif


#include "SRI_MapIterator.h"
#include "SRI_ConstMapIterator.h"
#include <map>


namespace SRI{

   // prototype of MapIterator
   template<typename K, typename T>   class MapIterator;

   /** This is a wrapper to allow STL classes to be exported from a dll */
   template<typename K, typename T> class Map {

	  friend class SRI::MapIterator<K, T>;
	  typedef typename std::map<K, T> StdMap;
	  typedef typename std::map<K, T>::iterator StdMapIterator;
	  typedef typename std::map<K, T>::const_iterator StdConstMapIterator;
	  typedef typename std::pair<K, T> StdMapPair;
	  typedef typename std::pair<StdMapIterator,bool> StdMapRes;

   private:
	   StdMap *m_ptStdMap; // pointer to an original STL class

   public:
	   Map (void);
	   virtual ~Map (void);
	   Map (const Map& c);
	   Map& operator=(const Map& c);

	   /** Because map containers do not allow for duplicate key values, 
	   * the insertion operation checks for each element inserted whether 
	   * another element exists already in the container with the same key 
	   *value, if so, the element is not inserted and its mapped value is 
	   * not changed in any way. 
	   * \returns 0 on successful insertion (new element); 
	   * \returns -1 if key was already in use and new element was not inserted 
	   */
	   int  insert(const K& index, const T& value);

	   /** This function tests if a given index already exists in the map without modifying the size of the map
		* \param index Idex to test
		* \returns true in case the index is already in use, otherwise it returns false.
	   */
	   bool exists(const K& index) const;

	   /** \returns 1 if one element was erased
	   * \returns 0 if no element was erased
	   */
	   int  erase(const K& index);
	   
	   /** Creates a copy of the element at given index, removes the element from the map and returns the copy*/
	   T cremove(const K& index);

	   unsigned int size(void) const;
	   void clear(void);

	   MapIterator<K,T> begin();
	   MapIterator<K,T> end();

	   ConstMapIterator<K,T> begin() const;
	   ConstMapIterator<K,T> end() const;

	   /** If index does not match the key of any element in the container, the 
	   * function inserts a new element with that key and returns a reference 
	   * to its mapped value. Notice that this always increases the map size 
	   * by one, even if no mapped value is assigned to the element (the element
	   * is constructed using its default constructor).
	   */
	   T& operator[] (const K& index);

	   MapIterator<K,T> findValue(const T& value);

	   T* first();
   };

   template<typename K, typename T>  Map<K, T>::Map (void){
	  m_ptStdMap = new StdMap;
   } 

   template<typename K, typename T> Map<K, T>::~Map (void) {  
	  if (m_ptStdMap != NULL){
		 m_ptStdMap->clear();
		 delete m_ptStdMap;
		 m_ptStdMap = NULL;
	  }
   }

   template<typename K, typename T> Map<K, T>::Map(const Map& c){
	   m_ptStdMap = new StdMap(*(c.m_ptStdMap));
   }

  template<typename K, typename T>  Map<K,T>& Map<K, T>::operator=(const Map& c){
	   if(this == &c){
		   return *this;
	   }

	   m_ptStdMap->clear();
	   m_ptStdMap->operator=(*(c.m_ptStdMap));
		
	  return *this;
   }

   template<typename K, typename T>
   int Map<K, T>::insert (const K& index, const T& value)
   {
	  StdMapRes res;
	  res = m_ptStdMap->insert(StdMapPair(index, value));

	  if (res.second == false){
		  return -1;
	  }else{
		  return 0;
	  }
   }

   template<typename K, typename T>
   bool Map<K, T>::exists(const K& index) const{
	   bool res = false;
	   res = (m_ptStdMap->find(index) != m_ptStdMap->end());
	   return res;
   }
   
   template<typename K, typename T>
   int Map<K, T>::erase (const K& index){

	  int res = m_ptStdMap->erase(index);
	  return res;
   }

   template<typename K, typename T>
    T Map<K, T>::cremove(const K& index){
		T t= m_ptStdMap->operator[](index);
		m_ptStdMap->erase(index);
		return t;
	}

   template<typename K, typename T>
   unsigned int Map<K,T>::size(void) const{
	  return m_ptStdMap->size();
   } 

   template<typename K, typename T>
   void Map<K,T>::clear (void){
	  m_ptStdMap->clear();
	  return;
   }

   template<typename K, typename T>
   MapIterator<K,T> Map<K,T>::begin(){
	   StdMapIterator* b = new StdMapIterator(m_ptStdMap->begin());
	   return MapIterator<K,T>(b);
   }

   template<typename K, typename T>
   MapIterator<K,T> Map<K,T>::end(){
	   StdMapIterator* e = new StdMapIterator(m_ptStdMap->end());
	   return MapIterator<K,T>(e);
   }

   template<typename K, typename T>
   ConstMapIterator<K,T> Map<K,T>::begin() const{
	   StdConstMapIterator* e = new StdConstMapIterator(m_ptStdMap->begin());
	   return ConstMapIterator<K,T>(e);
   }

   template<typename K, typename T>
   ConstMapIterator<K,T> Map<K,T>::end() const{
	   StdConstMapIterator* e = new StdConstMapIterator(m_ptStdMap->end());
	   return ConstMapIterator<K,T>(e);
   }


   /** If x matches the key of an element in the container, the function returns a reference to its mapped value.
   * If x does not match the key of any element in the container, the function inserts a new element with that 
   * key and returns a reference to its mapped value. Notice that this always increases the map size by one, 
   * even if no mapped value is assigned to the element (the element is constructed using its default constructor).
   */
   template<typename K, typename T>
   T& Map<K,T>::operator[] (const K& index)
   {
	  return ((*m_ptStdMap)[index]);
   } 
  
  template<typename K, typename T>
   MapIterator<K,T>  Map<K,T>::findValue(const T& value){
	   MapIterator<K,T> ret = this->begin();
	   
	   while(ret != this->end()){
		   if(ret.second() == value){
			   break;
		   }
		   ret++;
	   }
	   return ret;
   }

   /** \returns the value of the first key */
   template<typename K, typename T>
   T*  Map<K,T>::first(){
	   MapIterator<K,T> ret = this->begin();
	   if(ret != this->end()){
		   return &(ret.second());
	   }else{
		   return NULL;
	   }
   }

} 

#ifdef WIN32
//	#pragma warning (pop)
#endif

#endif // one inclusion
