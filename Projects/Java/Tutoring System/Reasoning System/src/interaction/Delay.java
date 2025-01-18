package interaction;

import reasoning.core.RsLogger;

public class Delay implements IAItem {
	private int secs = 0;
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());

	public Delay() {
	}

	public int getSecs() {
		return secs;
	}

	public void setSecs(int secs) {
		this.secs = secs;
	}

	public boolean play() {
		try {
			this.wait(secs * 1000);
		} catch (InterruptedException e) {
			logger.error("Exception thrown: " + e.getMessage());
		}
		return true;
	}

}
