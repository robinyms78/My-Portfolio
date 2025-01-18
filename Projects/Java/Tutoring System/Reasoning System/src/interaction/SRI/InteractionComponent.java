package interaction.SRI;

import interaction.Action;
import interaction.XMLParser;

import java.util.HashMap;

import reasoning.core.RsLogger;
import reasoning.core.RsUtil;
import SRI.Message;
import SRI.ReactiveComponent;

@SuppressWarnings("serial")
public class InteractionComponent extends ReactiveComponent {
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());
	private String m_portName = "interaction";
	private String m_outPort = m_portName + "out";
	private String m_inPort = m_portName + "in";

	public InteractionComponent(String name, String portName) {
		super(name);
		m_portName = portName;
		m_outPort = m_portName + "out";
		m_inPort = m_portName + "in";
		iCreateOutputPort(m_outPort, "string");
		iCreateInputPort(m_inPort, "string");
	}

	private HashMap<String, Action> actions = new HashMap<String, Action>();

	/**
	 * A component overwriting this function must call the base class
	 * implementation Baseclass implementation sets the status of the component
	 * to "INITIALIZED" and makes sure that all children initialize. (if this
	 * behaviour is not desired for children, the component can simply maintain
	 * its own list of component children)
	 */
	public void vInit() {
		super.vInit();
		// import all interactions
		actions = XMLParser.loadInteractions("data/interactions.xml");
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

	public boolean vStep() {
		Message m = null;
		String msg = "";
		while ((m = m_mInputPorts.get(m_inPort).ptReceive()) != null) {
			msg = m.szGetContent() + "";
			logger.debug("Got message: \t" + msg);
		}

		// get plan list
		String[] plans = null;
		if (!"".equals(msg)) {
			plans = msg.split(RsUtil.SEPARATOR);
			for (String planName : plans) {
				if (!"".equals(planName)) {
					Action act = actions.get(planName);
					if (act != null) {
						logger.debug("Execute interaction: " + act.getName());
						act.execute();
					}
				}
			}
		}

		return true;
	}
}
