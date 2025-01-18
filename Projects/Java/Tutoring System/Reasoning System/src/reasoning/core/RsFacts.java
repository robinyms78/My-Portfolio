/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package reasoning.core;

import java.io.Serializable;
import java.util.HashMap;

/**
 * 
 * @author xin.xin
 */

public class RsFacts implements Serializable {
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());
	private static final long serialVersionUID = 1L;

	private Long id;

	private HashMap<String, String> facts;

	public RsFacts() {
		facts = new HashMap<String, String>();
	}

	private RsFacts(HashMap<String, String> facts) {
		this.facts = facts;
	}

	public void setFact(String name, String value) {
		facts.put(name, value);
	}

	public String getFact(String name) {
		if (facts.containsKey(name)) {
			return facts.get(name);
		}
		return "";
	}

	@SuppressWarnings("unchecked")
	public RsFacts clone() {
		HashMap<String, String> temp;
		try {
			temp = (HashMap<String, String>) this.facts.clone();
		} catch (Exception ex) {
			logger.error(ex.getMessage());
			temp = new HashMap<String, String>();
		}
		RsFacts newFacts = new RsFacts(temp);
		return newFacts;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	@Override
	public int hashCode() {
		int hash = 0;
		hash += (id != null ? id.hashCode() : 0);
		return hash;
	}

	@Override
	public boolean equals(Object object) {
		// TODO: Warning - this method won't work in the case the id fields are
		// not set
		if (!(object instanceof RsFacts)) {
			return false;
		}
		RsFacts other = (RsFacts) object;
		if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
			return false;
		}
		return true;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("reasoning.core.RsFacts: [");
		for (String key : facts.keySet()) {
			sb.append("name=");
			sb.append(key);
			sb.append(" value=");
			sb.append(facts.get(key));
			sb.append("|");
		}
		sb.append("]");

		return sb.toString();
	}
}
