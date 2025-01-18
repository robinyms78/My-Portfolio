/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package reasoning.core;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Comparator;


/**
 *
 * @author xin.xin
 */

public class RsPlan implements Serializable {
    private static final long serialVersionUID = 1L;

    private Long id;
    
    private int activity;
    
    private String name;

    public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getActivity() {
        return activity;
    }

    public void setActivity(int activity) {
        this.activity = activity;
    }

    public ArrayList<String> getAction() {
        return action;
    }

    public void setAction(ArrayList<String> action) {
        this.action = action;
    }

    public ArrayList<RsCondition> getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(ArrayList<RsCondition> postcondition) {
        this.postcondition = postcondition;
    }

    public ArrayList<RsConditions> getPrecondition() {
        return precondition;
    }

    public void setPrecondition(ArrayList<RsConditions> precondition) {
        this.precondition = precondition;
    }
    
    private ArrayList<RsConditions> precondition = new ArrayList<RsConditions>();
    private ArrayList<RsCondition> postcondition = new ArrayList<RsCondition>();
    private ArrayList<String> action = new ArrayList<String>();

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
        if (!(object instanceof RsPlan)) {
            return false;
        }
        RsPlan other = (RsPlan) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "reasoning.RsPlan[ plan name=" + name + " ]";
    }
    
    class RsPlanComparator implements Comparator<RsPlan> {
        public int compare(RsPlan plan1, RsPlan plan2) {
            return plan1.getActivity() - plan2.getActivity();
        }
    }
    
}
