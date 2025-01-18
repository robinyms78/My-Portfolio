/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package reasoning.core;

import java.io.Serializable;
import java.util.ArrayList;

/**
 *
 * @author xin.xin
 */

public class RsRule implements Serializable {
    private static final long serialVersionUID = 1L;

    private Long id;
    
    private String name;
    private int piority;
    private ArrayList<RsCondition> actions = new ArrayList<RsCondition>();
    private ArrayList<RsConditions> logicSec = new ArrayList<RsConditions>();

    public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getPiority() {
		return piority;
	}

	public void setPiority(int piority) {
		this.piority = piority;
	}

	public ArrayList<RsCondition> getActions() {
		return actions;
	}

	public void setActions(ArrayList<RsCondition> actions) {
		this.actions = actions;
	}

	public void setLogicSections(ArrayList<RsConditions> conditions) {
		this.logicSec = conditions;
	}

	public ArrayList<RsConditions> getLogicSections() {
        return logicSec;
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
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof RsRule)) {
            return false;
        }
        RsRule other = (RsRule) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "reasoning.RsRule[ name=" + name + " ]";
    }
    
}
