#ifndef LUA_POINTER_HANDLE_H
#define LUA_POINTER_HANDLE_H

namespace SRI{

/** In order to be able to control memory allocation and deallocation the LuaPointerHandle class is used.
* The handle class only stores the pointer to an allocated object. The handle itself is made a USERDATA
* object in Lua. As a result, the memory for the handle is managed by Lua. The handle mediates
* if on deletion also the stored object should be freed*/
template<class T> class LuaPointerHandle{
 private:
  T* m_ptr;
  bool m_bIsLuaHandled;

 public:
  LuaPointerHandle(){    
    m_ptr = NULL;
    m_bIsLuaHandled = false;
  }
  
  LuaPointerHandle(T* ptr, bool isLuaHandled = false){
    m_ptr = ptr;
    m_bIsLuaHandled = isLuaHandled;
  }

  virtual ~LuaPointerHandle(){
	  vReleaseHandle();
  }

  void vSetPointer(T* ptr, bool isLuaHandled = false){
	  vReleaseHandle(); // in case there was already one set
	  m_ptr = ptr;
	  m_bIsLuaHandled = isLuaHandled;
  }

  /** Frees the associated C++ object (if it is handled by this class) */
  virtual void vReleaseHandle(){
	  if( (m_bIsLuaHandled) && (m_ptr != NULL)){
		  delete m_ptr;
		  m_ptr = NULL;
	  }
  }

  /** This function releases the associated object, regardles of the isLuaHandled flag*/
  virtual void vForceRelease(){
	  if(m_ptr != NULL){
		  delete m_ptr;
		  m_ptr = NULL;
	  }
  }

  /** Can be used to change if the pointer is going to be freed or not*/
  virtual void vSetIsLuaHandeled(bool isLuahandled){
    m_bIsLuaHandled = isLuahandled;
  }

  T* ptGetObj(){
    return m_ptr;
  }

   bool bIsLuaHandeled(){
    return m_bIsLuaHandled;
  }

};


}



#endif

