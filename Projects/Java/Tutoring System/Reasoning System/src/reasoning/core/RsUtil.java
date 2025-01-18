/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package reasoning.core;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

/**
 * 
 * @author xin.xin
 */
public class RsUtil {
	private static RsLogger logger = RsLogger.getLogger(RsUtil.class.getName());
	public static final String SEPARATOR = ",";

	public static boolean isSuitable(ArrayList<RsConditions> rules, RsFacts facts, RsLogic oper) {
		boolean result = true;

		for (RsConditions conds : rules) {
			boolean subResult;
			if (conds.getSubSection() != null && conds.getSubSection().size() > 0) {
				result = result && isSuitable(conds.getSubSection(), facts, conds.getLogic());
			}

			if (conds.getLogic() == RsLogic.NOT) {
				subResult = compareNOTCondtions(conds.getSubCondition(), facts);
			} else if (conds.getLogic() == RsLogic.OR) {
				subResult = compareORCondtions(conds.getSubCondition(), facts);
			} else {
				subResult = compareANDCondtions(conds.getSubCondition(), facts);
			}

			if (oper == RsLogic.NOT) {
				result = !subResult;
			} else if (oper == RsLogic.NOT) {
				result = result || subResult;
			} else {
				result = result && subResult;
			}
		}

		return result;
	}

	private static boolean compareANDCondtions(ArrayList<RsCondition> conds, RsFacts facts) {
		for (RsCondition cond : conds) {
			if (!compareValue(facts.getFact(cond.getName()), cond.getValue(), cond.getOper())) {
				return false;
			}
		}

		return true;
	}

	private static boolean compareORCondtions(ArrayList<RsCondition> conds, RsFacts facts) {
		for (RsCondition cond : conds) {
			if (compareValue(facts.getFact(cond.getName()), cond.getValue(), cond.getOper())) {
				return true;
			}
		}

		return false;
	}

	private static boolean compareNOTCondtions(ArrayList<RsCondition> conds, RsFacts facts) {
		boolean result = false;

		for (RsCondition cond : conds) {
			result = compareValue(facts.getFact(cond.getName()), cond.getValue(), cond.getOper());
		}

		return !result;
	}

	private static boolean compareValue(String str1, String str2, RsOperator oper) {
		boolean result = true;
		str1 += "";
		str2 += "";
		if (isInteger(str1) && isInteger(str2)) {
			int num1 = Integer.parseInt(str1);
			int num2 = Integer.parseInt(str2);
			if (oper == RsOperator.Greater) {
				if (!(num1 > num2)) {
					result = false;
				}
			} else if (oper == RsOperator.GreaterEquals) {
				if (!(num1 >= num2)) {
					result = false;
				}
			} else if (oper == RsOperator.Smaller) {
				if (!(num1 < num2)) {
					result = false;
				}
			} else if (oper == RsOperator.SmallerEquals) {
				if (!(num1 <= num2)) {
					result = false;
				}
			} else {
				if (!(num1 == num2)) {
					result = false;
				}
			}
		} else {
			if (oper == RsOperator.Greater) {
				if (!(str1.compareTo(str2) > 0)) {
					result = false;
				}
			} else if (oper == RsOperator.GreaterEquals) {
				if (!(str1.compareTo(str2) >= 0)) {
					result = false;
				}
			} else if (oper == RsOperator.Smaller) {
				if (!(str1.compareTo(str2) < 0)) {
					result = false;
				}
			} else if (oper == RsOperator.SmallerEquals) {
				if (!(str1.compareTo(str2) <= 0)) {
					result = false;
				}
			} else {
				if (!(str1.compareTo(str2) == 0)) {
					result = false;
				}
			}
		}

		return result;
	}

	public static boolean isSatisfy(RsPlan plan, RsFacts facts) {
		boolean result = false;

		for (RsCondition cond : plan.getPostcondition()) {
			if (cond.getOper() == RsOperator.Equals) {
				if (!facts.getFact(cond.getName()).equalsIgnoreCase(cond.getValue())) {
					result = false;
				}
			}
		}

		return result;
	}

	public static List<RsPlan> getPlanlist(RsGoal goal, HashMap<String, RsPlan> plans, RsFacts facts, List<RsRule> rules) {
		List<RsPlan> suitablePlans = new ArrayList<RsPlan>();
		logger.debug("goal plan is: " + goal);
		if (goal == null || goal.getPlan() == null) {
			return suitablePlans;
		}
		if (!plans.containsKey(goal.getPlan())) {
			return suitablePlans;
		}

		RsPlan plan = plans.get(goal.getPlan());
		if (plan == null) {
			return suitablePlans;
		}
		calSuitablePlans(suitablePlans, plans.values(), plan, facts, rules);

		return suitablePlans;
	}

	public static void updateFact(RsFacts facts, String factName, String factValue, List<RsRule> rules) {
		facts.setFact(factName, factValue);
		logger.debug("insert/update new fact: " + factName + " = " + factValue);
		// trigger rules
		ArrayList<RsRule> matched = new ArrayList<RsRule>();
		for (RsRule rule : rules) {
			if (isSuitable(rule.getLogicSections(), facts, RsLogic.AND)) {
				matched.add(rule);
			}
		}
		Collections.sort(matched, new RsRuleComparator());
		logger.debug("updateFact: matched rules are: " + matched);
		// update facts
		for (RsRule rule : matched) {
			for (RsCondition action : rule.getActions()) {
				facts.setFact(action.getName(), action.getValue());
			}
		}
		logger.debug("updateFact: " + facts);
	}

	// Note 1: compare the plan post condition mixed with current state
	// Note 2: Only get the first plan as the selection based on the 1. activity
	// value; 2. sequence in the plans.xml
	//
	private static void calSuitablePlans(List<RsPlan> suitablePlans, Collection<RsPlan> allPlans, RsPlan target, RsFacts facts, List<RsRule> rules) {
		logger.debug("calSuitablePlans: target plan is: " + target);
		logger.debug("calSuitablePlans: current facts is: " + facts);
		if (RsUtil.isSuitable(target.getPrecondition(), facts, RsLogic.AND)) {
			logger.debug("calSuitablePlans: target plan[" + target + "] is suitable already.");
			suitablePlans.add(0, target);
		} else {
			logger.debug("calSuitablePlans: target plan[" + target + "] is not suitable yet. Try to find plan in front of it.");
			List<RsPlan> selections = new ArrayList<RsPlan>();
			RsFacts assum = facts.clone();

			for (RsPlan plan : allPlans) {
				assum = facts.clone();
				for (RsCondition cond : plan.getPostcondition()) {
					updateFact(assum, cond.getName(), cond.getValue(), rules);
				}

				if (RsUtil.isSuitable(target.getPrecondition(), assum, RsLogic.AND)) {
					logger.debug("This plan " + plan + " may be candidate.");
					selections.add(plan);
				} else {
					// if assum plan is not suitable, need to clear assum facts
					assum = facts.clone();
				}
			}
			if (selections.size() > 0) {
				Collections.sort(selections, new RsPlanComparator());
				logger.debug("calSuitablePlans: candidatea are " + selections);
				suitablePlans.add(0, target);
				assum = facts.clone();
				for (RsCondition cond : selections.get(0).getPostcondition()) {
					updateFact(assum, cond.getName(), cond.getValue(), rules);
				}
				// suitablePlans.add(0, selctions.get(0));
				calSuitablePlans(suitablePlans, allPlans, selections.get(0), assum, rules);
			}
		}

	}

	private static boolean isInteger(String s) {
		return isInteger(s, 10);
	}

	private static boolean isInteger(String s, int radix) {
		if (s.isEmpty())
			return false;
		for (int i = 0; i < s.length(); i++) {
			if (i == 0 && s.charAt(i) == '-')
				continue;
			if (Character.digit(s.charAt(i), radix) < 0)
				return false;
		}
		return true;
	}

	static class RsPlanComparator implements Comparator<RsPlan> {
		public int compare(RsPlan plan1, RsPlan plan2) {
			return plan1.getActivity() - plan2.getActivity();
		}
	}

	static class RsRuleComparator implements Comparator<RsRule> {
		public int compare(RsRule plan1, RsRule plan2) {
			return plan2.getPiority() - plan1.getPiority();
		}
	}
}
