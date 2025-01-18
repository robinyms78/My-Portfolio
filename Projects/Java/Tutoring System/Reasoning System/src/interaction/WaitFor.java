package interaction;

import reasoning.core.RsLogger;

public class WaitFor implements IAItem {
	private Event event = null;
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());

	public Event getEvent() {
		return event;
	}

	public void setEvent(Event event) {
		this.event = event;
	}

	public boolean play() {
		// TODO: wait for event
		logger.debug("wait for event: " + event);

		return true;
	}

}
