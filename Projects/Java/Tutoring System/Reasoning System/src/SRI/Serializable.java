package SRI;

public abstract class Serializable {

	//class SRIUTIL_API Serializable: public SRI::Cloneable{

		//public:
			//virtual Serializable* ptClone() const;
	public Serializable()
	{
		
	}
			//virtual ~Serializable();

	public abstract String szToString();
	public abstract int iFromString(String data);
			/** Returns a string identifying the object type that is serialized */
	public abstract String szGetObjType() ;
	//	};

	//	}

	//	#endif
	
}
