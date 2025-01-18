package interaction;

import java.util.List;

import reasoning.core.RsLogger;

public class Select implements IAItem {
	private List<IAItem> objects;
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());

	public List<IAItem> getObjects() {
		return objects;
	}

	public void setObjects(List<IAItem> objects) {
		this.objects = objects;
	}

	public boolean play() {
		// Need to define how to select here
		for (IAItem item : objects) {
			logger.debug("select the sub item:" + item);
			item.play();
		}
		return true;
	}
}
