#ifndef SRI_LIST_H
#define SRI_LIST_H

#ifdef WIN32
//	#pragma warning (push)
//	#pragma warning (disable : 4702)
#endif


#include "SRI_ListIterator.h"
#include "SRI_ConstListIterator.h"
#include <List>


namespace SRI{

   // prototype of ListIterator
   template<typename T>   class ListIterator;

   /** This is a wrapper to allow STL classes to be exported from a dll */
   template<typename T> class List {

      friend class SRI::ListIterator<T>;
	  typedef typename std::list<T> StdList;
	  typedef typename std::list<T>::iterator StdListIterator;
	  typedef typename std::list<T>::const_iterator StdConstListIterator;

   private:
	   StdList *m_ptStdList; // pointer to an original STL class

   protected:
	   std::list<T>* ptGetStdList() const;

   public:
	   List (void);
	   virtual ~List (void);
	   List(const List& c);
	   List& operator=(const List& c);

	   T& front();
	   T& back();

	   const T& front() const;
	   const T& back() const;

	   void push_back(const T& t);
	   void push_front(const T& t);
	   void pop_back();
	   void pop_front();

	   ListIterator<T> find(const T& t);
	   ConstListIterator<T> find(const T& t) const;
	   ListIterator<T> insert(const ListIterator<T>& pos, const T& t);
	   ListIterator<T> erase(const ListIterator<T>& pos);


       unsigned int size(void) const;
       void clear(void);

	   ListIterator<T> begin();
	   ListIterator<T> end();

	   ConstListIterator<T> begin() const;
	   ConstListIterator<T> end() const;

   };

   template<typename T>  List<T>::List (void){
	   m_ptStdList = new StdList;
   } 

   template<typename T> List<T>::~List (void) {  
	   if (m_ptStdList != NULL){
		   m_ptStdList->clear();
		   delete m_ptStdList;
		   m_ptStdList = NULL;
	   }
   }

   template<typename T> List<T>::List(const List<T>& c){
	   m_ptStdList = new StdList(*(c.ptGetStdList()));
   }

   template<typename T> List<T>& List<T>::operator=(const List<T>& c){
	   if(this == &c){
		   return *this;
	   }

	   if(m_ptStdList != NULL){
		   delete m_ptStdList;
		   m_ptStdList = NULL;
	   }
	   m_ptStdList = new StdList(*(c.ptGetStdList()));

	   return *this;
   }

   template<typename T> std::list<T>* List<T>::ptGetStdList() const{
	   return m_ptStdList;
   }


   template<typename T>
   T& List<T>::front(){
	   return m_ptStdList->front();
   }

	template<typename T>
	T& List<T>::back(){
		return m_ptStdList->back();
	}

	template<typename T>
	const T& List<T>::front() const{
		return m_ptStdList->front();
	}

	template<typename T>
	const T& List<T>::back() const{
		return m_ptStdList->back();
	}

	template<typename T>
	void List<T>::push_back(const T& t){
		m_ptStdList->push_back(t);
	}
	
	template<typename T>
	void List<T>::push_front(const T& t){
		m_ptStdList->push_front(t);
	}

	template<typename T>
	void List<T>::pop_back(){
		m_ptStdList->pop_back(); 
	}
	
	template<typename T>
	void List<T>::pop_front(){
		m_ptStdList->pop_front();
	}

	template<typename T>
	ListIterator<T> List<T>::find(const T& t){
		 StdListIterator b = m_ptStdList->begin();
		 while(	b != m_ptStdList->end()){
			if ( *b == t ){
				break;
			}
			++b;
		 }
		 return ListIterator<T>(b);
	}

	template<typename T>
	ConstListIterator<T> List<T>::find(const T& t) const{
		StdConstListIterator b = m_ptStdList->begin();
		 while(	b != m_ptStdList->end()){
			if ( *b == t ){
				break;
			}
			++b;
		 }
		 return ConstListIterator<T>(b);
	}


	template<typename T>
	ListIterator<T> List<T>::insert(const ListIterator<T>& pos, const T& t){
		 StdListIterator b = m_ptStdList->insert(pos.tGetStdListIterator(), t);
		 return ListIterator<T>(b);
	}

	template<typename T>
	ListIterator<T> List<T>::erase(const ListIterator<T>& pos){
		StdListIterator b = m_ptStdList->erase(pos.tGetStdListIterator());
		return ListIterator<T>(b);
	}

   template<typename T>
   unsigned int List<T>::size(void) const{
      return m_ptStdList->size();
   } 

   template<typename T>
   void List<T>::clear (void){
      m_ptStdList->clear();
      return;
   }

   template<typename T>
   ListIterator<T> List<T>::begin(){
	   StdListIterator b = m_ptStdList->begin();
	   return ListIterator<T>(b);
   }

   template<typename T>
   ListIterator<T> List<T>::end(){
	   StdListIterator e = m_ptStdList->end();
	   return ListIterator<T>(e);
   }

   template<typename T>
   ConstListIterator<T> List<T>::begin() const{
	   StdConstListIterator b = m_ptStdList->begin();
	   return ConstListIterator<T>(b);
   }

   template<typename T>
   ConstListIterator<T> List<T>::end() const{
	   StdConstListIterator e = m_ptStdList->end();
	   return ConstListIterator<T>(e);
   }

} 

#ifdef WIN32
//	#pragma warning (pop)
#endif

#endif // one inclusion
