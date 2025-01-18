
package SRI;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Set;


import java.io.*;
import javax.swing.JFrame;
import javax.swing.JLabel;
//import java.net.*;

public class Component extends JFrame {

	//Socket echoSocket = null;
    //PrintWriter out = null;
    //BufferedReader in = null;
	protected String m_szID;
	protected String m_szType;
	protected String m_szName; // a human readable name for the component
	protected String m_szNameSpace;
	protected String m_szComponentType;
	protected Definition m_ptComponentDefinition;

	protected ComponentStatus m_eStatus;

	protected HashMap<String, Component> m_mChildComponents=new HashMap<String, Component>();
	protected Component m_ptParent;
	
	protected SRIEngineStub m_ptEngineHandle;//latest addin on 20121206
	//The engineHandle class is replace by enginestub in Java version
	//constructors 
	public Component()//default constructor
	{
		m_szNameSpace="SRI";
		m_szType="SRI.Component";
		
		m_szID="1";//temp put in for testing 2012/12/10
		//ComponentStatus cs=null;
		
	//	HelloWorldFrame();
		//try {
			//Thread.sleep(10000);
	//	} catch (InterruptedException e) {
			// TODO Auto-generated catch block
		//	e.printStackTrace();
		//}

		m_eStatus = ComponentStatus.SRI_STOPPED;
		
	}
	
	public void HelloWorldFrame() {
		JLabel jlbHelloWorld = new JLabel("Testing Done");
		add(jlbHelloWorld);
		this.setSize(100, 100);
		// pack();
		setVisible(true);
	}
	
	
	
	public Component(String name)
	{
		m_szName="";
		m_szNameSpace="";
		
		m_szType="SRI.Component";
		m_szID="1";//temp put in for testing 2012/12/10
		
		iSetName(name);
		//ComponentStatus cs=null;
		
		m_eStatus = ComponentStatus.SRI_STOPPED;
	}
	
	
	
	protected void vSetId(String id)
	{
		m_szID = id;
	}
	
	protected int iSetNameSpace(String name)
	{
		if(m_szNameSpace == name){
			return 0;//SRI_OK
		}
		int res = 0;//SRI_OK;
		//String oldName = szGetName();
		m_szNameSpace = name;
		/*if(m_ptEngineHandle.bIsValid() && m_ptEngineHandle->bIsValid()){
			res =  m_ptEngineHandle->iChangeName(oldName, szGetName());

			if(res != SRI_OK){
				m_tLog.error("Unable to set namespace of component %s to %s",oldName.c_str(), name);
				return res;
			}

			//set new namespace for all children
			for(SRI::MapIterator<SRI::String, SRI::Ref<SRI::Component>> it = m_mChildComponents.begin(); it != m_mChildComponents.end(); it++){
				Ref<Component>& child = it.second();
				if(child!=null){
					res = child.iSetNameSpace(szGetName());
				}
			}

		}else{
		
			// no handle set
			return 0;//SRI_OK
		}
		 */
		return res;
	}

	
	//ComponentDefinition m_tComponentDefinition;//this should be implemented in the future for the input and output port

	//private Component m_ptSelfRef;

	
		/** *
		*  */
		

	public int iSetParent(Component newParent)
	{
		
		int res = 0;//SRI_OK

		if(newParent == m_ptParent){
			return 0; // parent is already set
		}
		

		// check if component is child of different parent
		if(m_ptParent!=null && (newParent != m_ptParent)){
			if(m_ptParent.bHasChild(szGetName())){ // protect against double deletion
				Component oldParent = m_ptParent;
				m_ptParent = null;
				oldParent.ptRemoveChild(szGetComponentName());
			}
		}

		if(newParent==null){	
			m_ptParent = null;
			
			iSetNameSpace("");
		}else{
			m_ptParent = newParent;
			if(!newParent.bHasChild(szGetComponentName())){
				res = newParent.iAddChild( this);
			}
		}
		if(m_mChildComponents!=null)
		{
		 int count=0;
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
                // System.out.println(i.next());
        	 count++;
        	 if(count==2 && i.next()!=null&&m_mChildComponents.size()>1 )
        	 {	
        		 //Component comp1=(Component) i.next();
        		 ((Component) i.next().getValue()).iSetNameSpace(szGetName());
        	 }
         }
		}
		return res;
		
	}
	
	
	public int iAddChild(Component comp)
	{
		if(comp==null){
			System.out.println("Unable to add invalid component");
			return -2;
		}

		if(m_mChildComponents!=null && m_mChildComponents.containsKey( comp.szGetComponentName() )){
			System.out.println("Unable to add child component %s: Component with given name already exists! "+ comp.szGetComponentName());
			return -12; //SRI_ERR_NAMECONFLICT;
		}

		// should not be necessary (if not in local namespace no conflict possible)
		/*if(m_ptEngineHandle.bIsValid() && m_ptEngineHandle->bIsValid()){
			if( m_ptEngineHandle->bHasComponent(szGetName() + "+" + comp->szGetComponentName())){
				return SRI_ERR_NAMECONFLICT;
			}
		}
	*/
		//System.out.println(" COM NAME "+comp.szGetComponentName());
		m_mChildComponents.put(comp.szGetComponentName(),comp);

		comp.iSetNameSpace(szGetName());
		if(comp.ptGetParent() != this){
			comp.iSetParent(this);
		}
		
		/*
		int res = comp->iSetEngineHandle(m_ptEngineHandle);
		if (res != SRI_OK){
			m_tLog.error("Error adding child: %s", comp->szGetComponentName());
			this->ptRemoveChild(comp->szGetComponentName());
		} // implicitly also adds all children of comp to engine

	

		if(m_ptEngineHandle.bIsValid() && m_ptEngineHandle->bIsValid()){
			if( ! m_ptEngineHandle->bHasComponent(comp->szGetName())){
				m_ptEngineHandle->iAddComponent(comp, "embedded");
			}else{
				m_ptEngineHandle->iChangeLoop(comp->szGetName(), "embedded");
			}
		}
			*/
		return 0;//SRI_OK
		
	}
	
	public Component ptGetChild(String name)
	{
		if( ! m_mChildComponents.containsKey(name)){
			return null;
		}else{
			return (Component) m_mChildComponents.get(name);
		}
	}
	

	public Component ptGetParent()
	{
		return m_ptParent;
	}
	
	
	public boolean bHasChild(String name)
	{
		boolean containChild=false;
		if(m_mChildComponents!=null){
			System.out.println(" CHILD NAME "+m_mChildComponents.size());
			containChild= m_mChildComponents.containsKey(name);
		}
		return containChild;
	}
	
	
	/** returns reference to removed child. Child keeps its children*/
	public Component ptRemoveChild(String name)
	{
		
		Component child = null;
		if(m_mChildComponents.containsKey(name)){
			 child = m_mChildComponents.get(name);
			 m_mChildComponents.remove(name);
			 //SRI::Ref<Component>& child = m_mChildComponents[name];
			 if(child!=null){
				child.iSetParent(null); // implictly also removes the child from engine
			 }
			 //m_mChildComponents.erase(name);	 
		 }
		 return child;
	}
	
	public Component ptRemoveChild(Component comp)
	{
		
		 if(comp!=null){
			 return ptRemoveChild(comp.szGetComponentName());
		 }else{
			 return comp;
		 }
		
	}

	public  String  szGetID() 
	{
		return m_szID;
		
	}
		
	public String szGetType()
	{
		return m_szType;
	}
	
	/** \returns returns fully qualified name including namespace */
	public String szGetName()
	{
		if(m_szNameSpace == ""){
			return m_szName;
		}else{
			return m_szNameSpace + "." + m_szName;
		}
	}
		
	/** \returns returns only the current namespace */
	public String szGetNameSpace()
	{
		return m_szNameSpace;
	}
	
	/** \returns returns just the name of the component without the namespace */
	public String szGetComponentName()
	{
		return m_szName;
	}
		
	/** The function sets the fully qualified name of the component. The name is parsed
	* to seperate namespace from component name and sets both values accordingly*/
	public int iSetName(String name)
	{
		if(name.equals(m_szName)){
			return 0;//SRI_OK
		}

		//String oldName = szGetName();
		//String oldComponentName = m_szName;
		//String oldNameSpace = m_szNameSpace;

		// parse the new name
		String _name, _nameSpace;
		//int pos = name.indexOf('.');
		//if(pos != String::npos){
			//_name = name.substr(pos+1);
			//_nameSpace = name.substr(0, pos);
		//}else{
			_nameSpace = "";
			_name = name;
		//}

		m_szName = _name;
		m_szNameSpace = _nameSpace;

		//if(m_ptEngineHandle.bIsValid() && m_ptEngineHandle->bIsValid()){
			//m_ptEngineHandle->iChangeName(oldName, name);
		//}

		//set new namespace for all children
		if(m_mChildComponents!=null)
		{
		 int count=0;
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
                // System.out.println(i.next());
        	 count++;
        	 if(count==2 && i.next()!=null && m_mChildComponents.size()>1 )
        	 {
        		 ((Component) i.next().getValue()).iSetNameSpace(szGetName());
        	 }
         }
		}
		return 0;//SRI_OK
	}

	
	public int iSetComponentType(String type){
		m_szComponentType = type;
		//m_ptComponentDefinition=type;
		return 0;//SRI_OK;
	}
	
	/** Components should ALWAYS set their type in the constructor. The type sting should match the
	* type string that is given by the factory. The Factory can set the type
	* of the component during construction if a configuration deserves a specific type name. */
	public int iSetType(String type)
	{
			m_szType = type;
			//m_tComponentDefinition.vSetComponentType(type);
			return 0;//SRI_OK
	}

	public String szGetComponentType()
	{
		return m_szComponentType;
		
	}
		
	public ComponentStatus eGetStatus()
	{
		return m_eStatus;
			//ComponentStatus cs=null;
			//return cs;
	}
	
	public void vSetStatus(ComponentStatus status)
	{
		m_eStatus = status;	
	}
		
	// ComponentDefinition tGetDefinition();

	/** A component overwriting this function must call the base class implementation 
	* Baseclass implementation sets the status of the component to "INITIALIZED" and makes sure that all 
	* children initialize. (if this behaviour is not desired for children, the component can simply
	* maintain its own list of component children)
	*/
	public void vInit()
	{
		//ComponentStatus cs=null;
		
		m_eStatus = ComponentStatus.SRI_INITIALIZED;
		 //int count=0;
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
                // System.out.println(i.next());
        	// count++;
        	 if( i.next()!=null &&m_mChildComponents.size()>0 )
        	 {
        		 ((Component) i.next().getValue()).vInit();
        	 }
         }
		
		
	}
	
	/** A component overwriting this function must call the base class implementation.
	* Baseclass implementation sets the status of the component to "STOPPED" and makes sure that all 
	* children finalize.   (if this behaviour is not desired for children, the component can simply
	* maintain its own list of component children)
	*/
	public void vFinalize()
	{
		//ComponentStatus cs=null;
		m_eStatus = ComponentStatus.SRI_FINALIZED;
		 
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
                // System.out.println(i.next());
        	 
        	 if(i.next()!=null && m_mChildComponents.size()>0)
        	 {
        		 ((Component) i.next().getValue()).vFinalize();
        	 }
         }
			
	}
	
	
	public boolean bHasMoreSteps()
	{
		boolean res = true;
		
		Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
        Iterator<Entry<String, Component>> i = s.iterator();
        while (i.hasNext()) {
               // System.out.println(i.next());
       	
       	 if(i.next()!=null && m_mChildComponents.size()>0 )
       	 {
       		res = res || ((Component) i.next().getValue()).bHasMoreSteps();
       	 //System.out.println("running 1");
       		
       	 }
        }
		
		return res;
			
	}
	
	public boolean vStep()
	{
		boolean status=false;
		
		System.out.println("Going thru the Main Step");
		if (m_mChildComponents.size()>0){
		Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
        Iterator<Entry<String, Component>> i = s.iterator();
        while (i.hasNext()) {
               // System.out.println(i.next());
       
       	// if( i.next().getValue()==null )
       	// {
       		 //System.out.println(" NO OF TIME ");
       		((Component) i.next().getValue()).vStep();
       		 //c.vStep();
       		 status=true;
       	 //
       //	 }
        }
		}
		return status;//just check to see if there is any child for this component
	}
	
	
	public boolean vPreStep()
	{
		boolean status =false;
		System.out.println("Going thru the Pre Step");
		Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
        Iterator<Entry<String, Component>> i = s.iterator();
        while (i.hasNext()) {
               
       	 
       	 //if( i.next()!=null && m_mChildComponents.size()>0)
       //	 {
       		((Component) i.next().getValue()).vPreStep();
       		status=true;
       	 //
       //	 }
        }	
        return status;
	}
		
	
	public boolean vPostStep()
	{
		boolean status=false;
		System.out.println("Going thru the Post Step");
		
		Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
        Iterator<Entry<String, Component>> i = s.iterator();
        while (i.hasNext()) {
               // System.out.println(i.next());
       	 
       //	 if( i.next()!=null && m_mChildComponents.size()>0)
       //	 {
       		((Component) i.next().getValue()).vPostStep();
       		status =true;
       	 //
       	// }
        }	
        return status;
	}

	//Latest addition of EngineHandle function on 20121206
	public SRIEngineStub ptGetEngineHandle()
	{
		return m_ptEngineHandle;
	}
	
	public int iSetEngineHandle(SRIEngineStub handle)
	{
		int res = 0;//SRI_OK;
		if( m_ptEngineHandle!=null && handle!=null){
			if( m_ptEngineHandle == handle){
				return 0;//SRI_OK; // no change
			}
		}else{
			if( m_ptEngineHandle == handle){
				return 0;//SRI_OK; 
			}
		}

		if(m_ptEngineHandle!=null && m_ptEngineHandle!=null){
			if (  handle==null || m_ptEngineHandle != handle){
				if(m_ptEngineHandle.bHasComponent(szGetName(),"")){ // safe guard against double deletion
					SRIEngineStub tmp = m_ptEngineHandle;  
					//m_ptEngineHandle.vRelease();  
					tmp.vRemoveComponent(szGetName());
				}
			} 
		}

		m_ptEngineHandle = handle;
		ComponentDefinition def = (ComponentDefinition)m_ptComponentDefinition;
		if(def != null){
			if(m_ptEngineHandle!=null && m_ptEngineHandle!=null){
				def.vSetEngineName(m_ptEngineHandle.szGetName());
			}else{
				def.vSetEngineName(""); // set engine to nil
			}
		}
		Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
             Component child=i.next().getValue();
             if(child!=null){	
            	 if(m_ptEngineHandle!=null ){
            		 if (!m_ptEngineHandle.bHasComponent(child.szGetName(),"embedded")){
 						m_ptEngineHandle.iAddComponent(child, "embedded");
 					}else{
 						//child.ptGetEngineHandle().iChangeLoop(child.szGetName(), "embedded");
 					}
            		 
            	 }
            	 res = child.iSetEngineHandle(handle);
 				if(res != 0){
 					//m_tLog.error("Unable to set engine handle for child %s", child->szGetName().c_str());
 					System.out.println("Unable to set engine handle for child %s "+ child.szGetName());
 				}
             
             }
        
         }
		

		return res;
	}
	
	
	
	/** Convenience helper function to step children */
	public  void vInitChildren()
	{
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
             Component c=i.next().getValue();
        	 if(c!=null)
        	 {	
        		 c.vInit();
        	 }
         }
	}
	
	public void vStepChildren()
	{
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
             Component c=i.next().getValue();
        	 if(c!=null)
        	 {	
        		 c.vStep();
        	 }
         }
	}
	
	public void vPreStepChildren()
	{
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
             Component c=i.next().getValue();
        	 if(c!=null)
        	 {	
        		 c.vPreStep();
        	 }
         }
	}
	
	public void vPostStepChildren()
	{
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
             Component c=i.next().getValue();
        	 if(c!=null)
        	 {	
        		 c.vPostStep();
        	 }
         }
	}
	
	public void vFinalizeChildren()
	{
		 Set<Entry<String, Component>> s = m_mChildComponents.entrySet();
         Iterator<Entry<String, Component>> i = s.iterator();
         while (i.hasNext()) {
             Component c=i.next().getValue();
        	 if(c!=null)
        	 {	
        		 c.vFinalize();
        	 }
         }
	}
	
}
