package reasoning.core;

import java.util.ArrayList;

public class RsConditions {
	private RsLogic logic = RsLogic.AND;
	private ArrayList<RsCondition> sub_cond = new ArrayList<RsCondition>();
	public ArrayList<RsCondition> getSubCondition() {
		return sub_cond;
	}
	public void setSubCondition(ArrayList<RsCondition> sub_cond) {
		this.sub_cond = sub_cond;
	}
	private ArrayList<RsConditions> sub_sec = new ArrayList<RsConditions>();
	
	public RsLogic getLogic() {
		return logic;
	}
	public void setLogic(RsLogic logic) {
		this.logic = logic;
	}
	public ArrayList<RsConditions> getSubSection() {
		return sub_sec;
	}
	public void setSubSection(ArrayList<RsConditions> sub_sec) {
		this.sub_sec = sub_sec;
	}
	
}
