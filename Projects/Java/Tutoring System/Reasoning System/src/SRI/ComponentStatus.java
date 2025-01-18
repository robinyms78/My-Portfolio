package SRI;

public enum ComponentStatus  {
	 SRI_FAILED (-1),
	 SRI_STOPPED (0),
	 SRI_RUNNING (1),
	 SRI_INITIALIZED(2),
	 SRI_PAUSED(3),
	 SRI_FINALIZED(4)
	 ;
	 
	 private int b;
	 ComponentStatus(){} 
	 ComponentStatus(int b) 
	  { this.b = b; 
	  }
	 
	
	 
	 

}