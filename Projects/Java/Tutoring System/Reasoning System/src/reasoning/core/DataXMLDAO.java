package reasoning.core;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

public class DataXMLDAO {
	private static RsLogger logger = RsLogger.getLogger(DataXMLDAO.class.getName());
	// constants
	private static final String PLAN = "plan";
	private static final String PLAN_NAME = "name";
	private static final String ACTIVITY = "activity";
	private static final String PRE_COND = "precondition";
	private static final String POST_COND = "postcondition";
	private static final String COND = "condition";
	private static final String COND_LOGIC = "logic";
	private static final String SUB_SEC = "section";

	private static final String COND_NAME = "name";
	private static final String COND_OPER = "operator";
	private static final String COND_VALUE = "value";

	private static final String ACTIONS = "actions";
	private static final String ACTION = "action";
	private static final String ACTION_NAME = "name";

	private static final String RULE = "rule";
	private static final String RULE_COND = "conditions";
	private static final String RULE_NAME = "name";
	private static final String RULE_PRIO = "priority";

	private static final String GOAL = "goal";
	private static final String GOAL_NAME = "name";

	private DataXMLDAO() {
		super();
	}

	private static Element loadDocument(String location) {
		Document doc = null;
		try {
			DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder parser = docBuilderFactory.newDocumentBuilder();
			doc = parser.parse(new File(location));
			Element root = doc.getDocumentElement();
			root.normalize();
			return root;
		} catch (SAXParseException err) {
			logger.error("InitDataUtil ** Parsing error" + ", line " + err.getLineNumber() + ", uri " + err.getSystemId());
			logger.error("InitDataUtil error: " + err.getMessage());
		} catch (SAXException e) {
			logger.error("InitDataUtil error: " + e);
		} catch (java.net.MalformedURLException mfx) {
			logger.error("InitDataUtil error: " + mfx);
		} catch (java.io.IOException e) {
			logger.error("InitDataUtil error: " + e);
		} catch (Exception pce) {
			logger.error("InitDataUtil error: " + pce);
		}
		return null;
	}

	public static HashMap<String, RsPlan> loadPlans(String location) {
		Element root = loadDocument(location);
		return getPlans(root);
	}

	private static HashMap<String, RsPlan> getPlans(Element root) {
		HashMap<String, RsPlan> allPlans = new HashMap<String, RsPlan>();
		NodeList plans = root.getElementsByTagName(PLAN);
		for (int loop = 0; loop < plans.getLength(); loop++) {
			Node node = plans.item(loop);
			if (!(node instanceof Element)) {
				continue;
			}
			logger.debug(node.getNodeName());
			try {
				Element element = ((Element) node);
				RsPlan plan = new RsPlan();
				ArrayList<RsConditions> precondition = new ArrayList<RsConditions>();
				ArrayList<RsCondition> postcondition = new ArrayList<RsCondition>();
				ArrayList<String> actions = new ArrayList<String>();
				setCondtions(precondition, element.getElementsByTagName(PRE_COND));
				plan.setPrecondition(precondition);
				NodeList postCondNodes = element.getElementsByTagName(POST_COND);
				if (postCondNodes != null && postCondNodes.getLength() > 0) {
					for (int m = 0; m < postCondNodes.getLength(); m++) {
						Node postCondNode = postCondNodes.item(m);
						if (!(postCondNode instanceof Element)) {
							continue;
						}
						Element postCondElement = ((Element) postCondNode);
						setCondtion(postcondition, postCondElement.getElementsByTagName(COND));
					}
				}
				plan.setPostcondition(postcondition);
				plan.setActivity(Integer.parseInt(element.getAttribute(ACTIVITY)));
				plan.setName(element.getAttribute(PLAN_NAME));
				plan.setAction(actions);
				NodeList actionNodes = element.getElementsByTagName(ACTION);
				for (int n = 0; n < actionNodes.getLength(); n++) {
					Node actionNode = actionNodes.item(n);
					if (!(actionNode instanceof Element)) {
						continue;
					}
					actions.add(((Element) actionNode).getAttribute(ACTION_NAME));
				}
				allPlans.put(plan.getName(), plan);
			} catch (Exception ex) {
				logger.error("Convert plan error: " + ex.getMessage());
			}
		}
		return allPlans;
	}

	private static void setCondtion(ArrayList<RsCondition> condition, NodeList nodes) {
		for (int i = 0; i < nodes.getLength(); i++) {
			Node node = nodes.item(i);
			if (!(node instanceof Element)) {
				continue;
			}
			Element element = ((Element) node);
			RsCondition cond = new RsCondition();
			cond.setName(element.getAttribute(COND_NAME));
			cond.setOper(convertOper(element.getAttribute(COND_OPER)));
			cond.setValue(element.getAttribute(COND_VALUE));
			condition.add(cond);
		}
	}

	private static void setCondtion(ArrayList<RsCondition> condition, ArrayList<Element> elements) {
		for (Element element : elements) {
			RsCondition cond = new RsCondition();
			cond.setName(element.getAttribute(COND_NAME));
			cond.setOper(convertOper(element.getAttribute(COND_OPER)));
			cond.setValue(element.getAttribute(COND_VALUE));
			condition.add(cond);
		}
	}

	private static void setCondtions(ArrayList<RsConditions> condition, NodeList nodes) {
		for (int i = 0; i < nodes.getLength(); i++) {
			Node node = nodes.item(i);
			if (!(node instanceof Element)) {
				continue;
			}
			Element element = ((Element) node);
			RsConditions conds = new RsConditions();
			conds.setLogic(convertLogic(element.getAttribute(COND_LOGIC)));
			ArrayList<RsCondition> subCond = new ArrayList<RsCondition>();
			setCondtion(subCond, getChildrenByTagName(element, COND));
			conds.setSubCondition(subCond);
			NodeList subSecNodes = element.getElementsByTagName(SUB_SEC);
			condition.add(conds);
			if (subSecNodes != null && subSecNodes.getLength() > 0) {
				ArrayList<RsConditions> subSec = new ArrayList<RsConditions>();
				setCondtions(subSec, subSecNodes);
				conds.setSubSection(subSec);
			}
		}
	}

	private static ArrayList<Element> getChildrenByTagName(Element parent, String name) {
		ArrayList<Element> nodeList = new ArrayList<Element>();
		for (Node child = parent.getFirstChild(); child != null; child = child.getNextSibling()) {
			if (child.getNodeType() == Node.ELEMENT_NODE && name.equals(child.getNodeName())) {
				nodeList.add((Element) child);
			}
		}

		return nodeList;
	}

	private static RsLogic convertLogic(String oper) {
		if ("not".equals(oper)) {
			return RsLogic.NOT;
		} else if ("or".equals(oper)) {
			return RsLogic.OR;
		} else {
			return RsLogic.AND;
		}
	}

	private static RsOperator convertOper(String oper) {
		if (">".equals(oper)) {
			return RsOperator.Greater;
		} else if (">=".equals(oper)) {
			return RsOperator.GreaterEquals;
		} else if ("<".equals(oper)) {
			return RsOperator.Smaller;
		} else if ("<=".equals(oper)) {
			return RsOperator.SmallerEquals;
		} else {
			return RsOperator.Equals;
		}
	}

	public static ArrayList<RsRule> loadRules(String location) {
		Element root = loadDocument(location);
		return getRules(root);
	}

	private static ArrayList<RsRule> getRules(Element root) {
		ArrayList<RsRule> allRules = new ArrayList<RsRule>();
		NodeList rules = root.getElementsByTagName(RULE);
		for (int loop = 0; loop < rules.getLength(); loop++) {
			Node node = rules.item(loop);
			if (!(node instanceof Element)) {
				continue;
			}
			try {
				Element element = ((Element) node);
				RsRule rule = new RsRule();
				ArrayList<RsConditions> conditions = new ArrayList<RsConditions>();
				ArrayList<RsCondition> actions = new ArrayList<RsCondition>();
				setCondtions(conditions, element.getElementsByTagName(RULE_COND));
				rule.setLogicSections(conditions);
				rule.setPiority(Integer.parseInt(element.getAttribute(RULE_PRIO)));
				rule.setName(element.getAttribute(RULE_NAME));
				NodeList actionNodes = element.getElementsByTagName(ACTIONS);
				if (actionNodes != null && actionNodes.getLength() > 0) {
					for (int actNum = 0; actNum < actionNodes.getLength(); actNum++) {
						Node actNode = actionNodes.item(actNum);
						if (!(actNode instanceof Element)) {
							continue;
						}
						Element actEle = ((Element) actNode);
						setCondtion(actions, actEle.getElementsByTagName(ACTION));
					}
				}
				rule.setActions(actions);
				allRules.add(rule);
			} catch (Exception ex) {
				logger.error("Convert rule error: " + ex.getMessage());
			}
		}
		return allRules;
	}

	public static HashMap<String, RsGoal> loadGoals(String location) {
		Element root = loadDocument(location);
		return getGoals(root);
	}

	private static HashMap<String, RsGoal> getGoals(Element root) {
		HashMap<String, RsGoal> allGoals = new HashMap<String, RsGoal>();
		NodeList goalNodes = root.getElementsByTagName(GOAL);
		for (int loop = 0; loop < goalNodes.getLength(); loop++) {
			Node node = goalNodes.item(loop);
			if (!(node instanceof Element)) {
				continue;
			}
			try {
				Element element = ((Element) node);
				RsGoal goal = new RsGoal();
				goal.setName(element.getAttribute(GOAL_NAME));
				goal.setPlan(element.getAttribute(PLAN));
				allGoals.put(goal.getName(), goal);
			} catch (Exception ex) {
				logger.error("Convert goal error: " + ex.getMessage());
			}
		}
		return allGoals;
	}

}
