package SRI;

import java.util.HashMap;

public class ConfigNodeSet {
	


		protected HashMap<Integer, ConfigNode> m_mConfigNodes;
		protected int m_iNodeSetSize;


		public ConfigNodeSet()
		{
			m_iNodeSetSize = 0;
		}
		
		public ConfigNode ptGetNode(int pos)
		{
			ConfigNode res=new ConfigNode();
			if(m_mConfigNodes.containsKey(pos)){
				return res = m_mConfigNodes.get(pos);
			}
			return res;
		}

		/** \returns the number of nodes in the nodeset */
		public int iGetSize()
		{
			return m_iNodeSetSize;
		}



}
