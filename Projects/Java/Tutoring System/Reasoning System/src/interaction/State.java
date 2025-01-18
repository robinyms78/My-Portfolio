package interaction;

import java.util.List;

import reasoning.core.RsLogger;

public class State implements IAItem {
	private List<IAItem> objects;
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());

	public List<IAItem> getObjects() {
		return objects;
	}

	public void setObjects(List<IAItem> objects) {
		this.objects = objects;
	}

	public boolean play() {
		// TODO: how to state items
		for (IAItem item : objects) {
			logger.debug("play the sub item:" + item);
			item.play();
		}

		return true;
	}
}
