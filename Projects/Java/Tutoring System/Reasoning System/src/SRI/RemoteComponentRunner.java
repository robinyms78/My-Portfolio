package SRI;

public class RemoteComponentRunner extends Thread{

	
		
		private Component m_ptComponent;
		private Server m_ptServer;


	

			public RemoteComponentRunner(Component c, Server s) 
			 {
				m_ptComponent=c;
				m_ptServer=s;
			}

			

			public void run() {

				m_ptServer.vJoinServerThread();
				
			}
		

	} 
