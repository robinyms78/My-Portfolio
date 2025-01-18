package reasoning.core;

public class RsGoal {
	private String name;
	private String plan;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getPlan() {
		return plan;
	}

	public void setPlan(String plan) {
		this.plan = plan;
	}

	public String toString() {
		return "reasoning.RsGoal[ goal name=" + name + " plan=" + plan + "]";
	}
}
