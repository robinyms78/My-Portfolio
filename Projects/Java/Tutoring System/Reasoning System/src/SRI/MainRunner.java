package SRI;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;

public class MainRunner {
	public static HashMap<String,ComponentFactory> FactoryMap;
	public static void main(String args[])
	{


			//SRI::Logger logger("RemotePluginLoader", SRI::LOG_DEBUG);
			
			//logger.debug("Starting remote plugin %s", argv[1]);

			//SRI::Ref<SRI::RegistryPluginHandle> plug = new SRI::RegistryPluginHandle();

			//int err = plug->iLoadLibrary(argv[1]); //TODO add other args

			//if(err != SRI::SRI_OK) {
			//	logger.error("unable to load plugin");
			//	return -1;
			//}
			
			System.out.println("Connecting to registry server @ ip: %s:%s"+ args[2]+ args[3]);

			String ip=args[2];
			
			//std::stringstream ss(argv[3]);
			StringBuffer ss=new StringBuffer();
			ss.append(args[3]);
			int port = 0;
			ss.append(port);
			//TODO: change to explicit creation of registry stub
			SRIRegistry.vMakeRemote(ip, port);

			SRIRegistry registry = new SRIRegistry();
			
			RegistryHandle regHandle=new RegistryHandle(registry);

			//err = plug->iInitPlugin(regHandle);

			//if(err != SRI::SRI_OK) {
			//	logger.error("unable to initialise plugin");
			//	return -1;
			//}

			//SRI::FactoryMap facts = plug->mGetFactories();

			//if(facts.size() <= 0) {
				//logger.error("empty factory map");
				//return -1;
			//}

			List<ComponentFactoryServer > factServerList=new ArrayList<ComponentFactoryServer>();

		//	SRI::SRIRegistryStub *regStub = dynamic_cast<SRI::SRIRegistryStub *>(registry.ptGetObj());
			//if (regStub == NULL)
				//logger.error("in remote environment yet did not obtain registrystub");

			
			//for(SRI::FactoryMapIterator it = facts.begin(); it != facts.end(); it++) {
				//ComponentFactory g = it.second();
			Set<Entry<String, ComponentFactory>> s = FactoryMap.entrySet();
		         Iterator<Entry<String, ComponentFactory>> i = s.iterator();
		         while (i.hasNext()) {
		                // System.out.println(i.next());
		        	// count++;
		        	 if( i.next()!=null &&FactoryMap.size()>0 )
		        	 {
		        		 ComponentFactory g = ((ComponentFactory) i.next().getValue());
		        		 
		        	 }
		         }	
				//new SRI::ComponentFactoryServer(it.second());
				//SRI::ComponentFactoryServer *fs = new SRI::ComponentFactoryServer(it.second());
				//SRI::Ref<SRI::ComponentFactoryServer> factServ;
				//factServ = new SRI::ComponentFactoryServer(it.second());
				//SRI::Ref<SRI::ComponentFactoryServer> factServ = new SRI::ComponentFactoryServer(it.second());
//				factServ->vStartServer(0);
				//
				//regStub->iRegisterComponentFactory(SRI::Ref<SRI::ComponentfactServ, factServ->iGetServerPort());
				//factServerList.push_back(factServ);
			//}

		         
		         Iterator<ComponentFactoryServer> it= factServerList.iterator();
					ComponentFactoryServer c; 
					while(it.hasNext()) {
						c=it.next();
						c.vJoinServerThread();
			//for(SRI::ListIterator<SRI::ComponentFactoryServer *> it = factServerList.begin(); it != factServerList.end(); it++) {
				//it->vJoinServerThread();
			}

			System.out.println("Shutting down");

			//return 0;
		}


	}
	
//}
