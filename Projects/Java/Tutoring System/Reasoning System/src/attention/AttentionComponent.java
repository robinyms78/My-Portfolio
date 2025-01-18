package attention;

import reasoning.core.RsLogger;
import SRI.Message;
import SRI.ReactiveComponent;

@SuppressWarnings("serial")
public class AttentionComponent extends ReactiveComponent {
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());
	private String m_portName = "attention";
	private String m_outPort = m_portName + "out";
	private String m_inPort = m_portName + "in";

	public AttentionComponent(String name, String portName) {
		super(name);
		m_portName = portName;
		m_outPort = m_portName + "out";
		m_inPort = m_portName + "in";
		iCreateOutputPort(m_outPort, "string");
		iCreateInputPort(m_inPort, "string");
	}

	/**
	 * A component overwriting this function must call the base class
	 * implementation Baseclass implementation sets the status of the component
	 * to "INITIALIZED" and makes sure that all children initialize. (if this
	 * behaviour is not desired for children, the component can simply maintain
	 * its own list of component children)
	 */
	public void vInit() {
		super.vInit();
		CLIPManager.loadClipsProgram("");
	}

	public boolean vStep() {
		Message m = null;
		String msg = "";
		while ((m = m_mInputPorts.get(m_inPort).ptReceive()) != null) {
			msg = m.szGetContent() + "";
			logger.debug("Got message: \t" + msg);
		}

		if (!"".equals(msg)) {
			CLIPManager.loadClipsProgram("data/Attention System_Final.CLP");
			CLIPManager.runClips("", new String[10]);
		}

		return true;
	}

}
