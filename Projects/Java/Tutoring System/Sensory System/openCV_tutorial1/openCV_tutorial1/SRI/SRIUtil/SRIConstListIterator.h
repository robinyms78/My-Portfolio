#ifndef SRI_CONSTLIST_ITERATOR_H
#define SRI_CONSTLIST_ITERATOR_H

#ifdef WIN32
//	#pragma warning (push)
//	#pragma warning (disable : 4702)
#endif


#include <List>

namespace SRI
{
   // prototype of List class
   template<typename T> class List;

   template<typename T> class ConstListIterator {
      friend class SRI::List<T>;
      typedef typename std::list<T>::const_iterator StdConstListIterator;
      typedef typename std::list<T> StdList;

      private:
         StdConstListIterator m_tStdIt;
		 ConstListIterator (StdConstListIterator it); // only the List can generate an iterator

		 const typename std::list<T>::iterator& tGetStdConstListIterator() const;

      public:
		 ConstListIterator();
         virtual ~ConstListIterator (void);
		 ConstListIterator<T>& operator=(const ConstListIterator& c);
		 bool operator==(const ConstListIterator& c);
		 bool operator!=(const ConstListIterator& c);
		 ConstListIterator<T>& operator++(void);
		 ConstListIterator<T> operator++(int unused); // postfix
		 ConstListIterator<T>& operator--(void);
		 ConstListIterator<T> operator--(int unused); // postfix

		 const T& operator->();
		 const T& operator*();
   };

    template<typename T>
    const typename std::list<T>::iterator& ConstListIterator<T>::tGetStdConstListIterator() const{
		return m_tStdIt;
	}


   /** The iterator can only be used once it is assigend a list
   * it = list.begin() or it=list.end();
   */
   template<typename T>
   ConstListIterator<T>::ConstListIterator():m_tStdIt(){
	   // TODO: warning if the iterator has not been assigend a list
   }

   template<typename T>
   ConstListIterator<T>::ConstListIterator(StdConstListIterator it):m_tStdIt(it){
   }

   template<typename T>
   ConstListIterator<T>::~ConstListIterator (void){
   }

   template<typename T>
   ConstListIterator<T>& ConstListIterator<T>::operator=(const ConstListIterator<T>& c){
	   if(this == &c){
		   return *this;
	   }
	   m_tStdIt = c.m_tStdIt;
	   return *this;
   }

   template<typename T>
   bool ConstListIterator<T>::operator==(const ConstListIterator<T>& c){
	   return (m_tStdIt == c.m_tStdIt);
   }

   template<typename T>
   bool ConstListIterator<T>::operator!=(const ConstListIterator<T>& c){
	   return (m_tStdIt != c.m_tStdIt);
   }

    template<typename T>
   	ConstListIterator<T>& ConstListIterator<T>::operator++(){
		m_tStdIt++;
		return *this;
	}

	template<typename T>
	ConstListIterator<T> ConstListIterator<T>::operator++(int unused){
		ConstListIterator<T> it = *this;
		++m_tStdIt;
		return it;
	}

	template<typename T>
	ConstListIterator<T>&  ConstListIterator<T>::operator--(void){
		m_tStdIt--;
		return *this;
	}

	template<typename T>
	ConstListIterator<T>  ConstListIterator<T>::operator--(int unused){
		ConstListIterator<T> it = *this;
		--m_tStdIt;
		return it;
	}

	template<typename T>
	const T&  ConstListIterator<T>::operator->(){
		return (*(m_tStdIt));
	}

	template<typename T>
	const T& ConstListIterator<T>::operator*(){
		return (*(m_tStdIt));
	}
   

} 

#ifdef WIN32
//	#pragma warning (pop)
#endif

#endif // include once
