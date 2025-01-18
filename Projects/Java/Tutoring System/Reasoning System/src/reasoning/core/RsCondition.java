/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package reasoning.core;

import java.io.Serializable;

/**
 * 
 * @author xin.xin
 */

public class RsCondition implements Serializable {
	private static final long serialVersionUID = 1L;

	private Long id;

	public String getName() {
		return name;
	}

	public RsOperator getOper() {
		return oper;
	}

	public String getValue() {
		return value;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setOper(RsOperator oper) {
		this.oper = oper;
	}

	public void setValue(String value) {
		this.value = value;
	}

	private String name = "";
	private String value = "";
	private RsOperator oper = RsOperator.Equals;

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
		if (!(object instanceof RsCondition)) {
			return false;
		}
		RsCondition other = (RsCondition) object;
		if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
			return false;
		}
		return true;
	}

	@Override
	public String toString() {
		return "reasoning.RsCondition[ " + name + " " + oper + " " + value + " ]";
	}

}
