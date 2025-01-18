#ifndef SRI_LIST_ITERATOR_H
#define SRI_LIST_ITERATOR_H

#ifdef WIN32
//	#pragma warning (push)
//	#pragma warning (disable : 4702)
#endif


#include <List>

namespace SRI
{
   // prototype of List class
   template<typename T> class List;

   template<typename T> class ListIterator {
      friend class SRI::List<T>;
      typedef typename std::list<T>::iterator StdListIterator;
      typedef typename std::list<T> StdList;

      private:
         StdListIterator m_tStdIt;
		 ListIterator (StdListIterator it); // only the List can generate an iterator

		 const typename std::list<T>::iterator& tGetStdListIterator() const;

      public:
		 ListIterator();
         virtual ~ListIterator (void);
		 ListIterator<T>& operator=(const ListIterator& c);
		 bool operator==(const ListIterator& c);
		 bool operator!=(const ListIterator& c);
		 ListIterator<T>& operator++(void);
		 ListIterator<T> operator++(int unused); // postfix
		 ListIterator<T>& operator--(void);
		 ListIterator<T> operator--(int unused); // postfix

		 T& operator->();
		 T& operator*();
   };

    template<typename T>
    const typename std::list<T>::iterator& ListIterator<T>::tGetStdListIterator() const{
		return m_tStdIt;
	}


   /** The iterator can only be used once it is assigend a list
   * it = list.begin() or it=list.end();
   */
   template<typename T>
   ListIterator<T>::ListIterator():m_tStdIt(){
	   // TODO: warning if the iterator has not been assigend a list
   }

   template<typename T>
   ListIterator<T>::ListIterator(StdListIterator it):m_tStdIt(it){
   }

   template<typename T>
   ListIterator<T>::~ListIterator (void){
   }

   template<typename T>
   ListIterator<T>& ListIterator<T>::operator=(const ListIterator<T>& c){
	   if(this == &c){
		   return *this;
	   }
	   m_tStdIt = c.m_tStdIt;
	   return *this;
   }

   template<typename T>
   bool ListIterator<T>::operator==(const ListIterator<T>& c){
	   return (m_tStdIt == c.m_tStdIt);
   }

   template<typename T>
   bool ListIterator<T>::operator!=(const ListIterator<T>& c){
	   return (m_tStdIt != c.m_tStdIt);
   }

    template<typename T>
   	ListIterator<T>& ListIterator<T>::operator++(){
		m_tStdIt++;
		return *this;
	}

	template<typename T>
	ListIterator<T> ListIterator<T>::operator++(int unused){
		ListIterator<T> it = *this;
		++m_tStdIt;
		return it;
	}

	template<typename T>
	ListIterator<T>&  ListIterator<T>::operator--(void){
		m_tStdIt--;
		return *this;
	}

	template<typename T>
	ListIterator<T>  ListIterator<T>::operator--(int unused){
		ListIterator<T> it = *this;
		--m_tStdIt;
		return it;
	}

	template<typename T>
	T&  ListIterator<T>::operator->(){
		return (*(m_tStdIt));
	}

	template<typename T>
	T& ListIterator<T>::operator*(){
		return (*(m_tStdIt));
	}
   

} 

#ifdef WIN32
//	#pragma warning (pop)
#endif

#endif // include once
