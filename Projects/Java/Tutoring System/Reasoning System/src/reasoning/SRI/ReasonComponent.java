package reasoning.SRI;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import reasoning.core.DataXMLDAO;
import reasoning.core.RsFacts;
import reasoning.core.RsGoal;
import reasoning.core.RsLogger;
import reasoning.core.RsPlan;
import reasoning.core.RsRule;
import reasoning.core.RsUtil;
import SRI.Message;
import SRI.ReactiveComponent;

@SuppressWarnings("serial")
public class ReasonComponent extends ReactiveComponent {
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());
	private String m_portName = "planer";
	private String m_outPort = m_portName + "out";
	private String m_inPort = m_portName + "in";

	public ReasonComponent(String name, String portName) {
		super(name);
		m_portName = portName;
		m_outPort = m_portName + "out";
		m_inPort = m_portName + "in";
		iCreateOutputPort(m_outPort, "string");
		iCreateInputPort(m_inPort, "string");
	}

	private HashMap<String, RsPlan> plans = new HashMap<String, RsPlan>();
	private static RsFacts facts = new RsFacts();
	private ArrayList<RsRule> rules = new ArrayList<RsRule>();
	private HashMap<String, RsGoal> goals = new HashMap<String, RsGoal>();

	/**
	 * A component overwriting this function must call the base class
	 * implementation Baseclass implementation sets the status of the component
	 * to "INITIALIZED" and makes sure that all children initialize. (if this
	 * behaviour is not desired for children, the component can simply maintain
	 * its own list of component children)
	 */
	public void vInit() {
		super.vInit();
		// import all rules, plans and static facts
		plans = DataXMLDAO.loadPlans("data/plans.xml");
		rules = DataXMLDAO.loadRules("data/rules.xml");
		goals = DataXMLDAO.loadGoals("data/goals.xml");
	}

	/**
	 * A component overwriting this function must call the base class
	 * implementation. Baseclass implementation sets the status of the component
	 * to "STOPPED" and makes sure that all children finalize. (if this
	 * behaviour is not desired for children, the component can simply maintain
	 * its own list of component children)
	 */
	public void vFinalize() {

	}

	public void updateFacts(String factName, String factValue) {
		RsUtil.updateFact(facts, factName, factValue, rules);
	}

	public List<RsPlan> getPlans(String goalName) {
		RsGoal goal = goals.get(goalName);
		List<RsPlan> suitablePlans = RsUtil.getPlanlist(goal, plans, facts, rules);
		logger.debug("Plan list: " + suitablePlans);
		return suitablePlans;
	}

	public boolean vStep() {
		Message m = null;
		String msg = "";
		while ((m = m_mInputPorts.get(m_inPort).ptReceive()) != null) {
			msg = m.szGetContent() + "";
			logger.debug("Got message: \t" + msg);
		}
		msg = "action=planer,goal=basicsentence,face=happy";
		if ("".equals(msg)) {
			return true;
		}

		return process(msg);
	}
	
	public boolean process(String msg){
		String[] infos = msg.split(",");
		String focus = "";
		String goalName = "";
		for (String info : infos) {
			String[] action = info.split("=");
			if (action != null && action.length == 2) {
				if ("action".equals(action[0])) {
					focus = action[1];
				} else if ("goal".equals(action[0])) {
					goalName = action[1];
				} else {
					updateFacts(action[0], action[1]);
				}
			}
		}

		if ("planer".equalsIgnoreCase(focus)) {
			// fetch plan
			List<RsPlan> rs = new ArrayList<RsPlan>();
			if (goals.containsKey(goalName)) {
				rs = getPlans(goalName);
				StringBuilder sb = new StringBuilder();
				for (RsPlan plan : rs) {
					sb.append(plan.getName());
					sb.append(RsUtil.SEPARATOR);
				}
				m_mOutputPorts.get(m_outPort).iSend(new Message(sb.toString()));
				logger.debug("Sent message already: " + sb.toString());
			}
		}
		
		return true;
	}
}
