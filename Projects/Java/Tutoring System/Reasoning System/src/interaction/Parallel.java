package interaction;

import java.util.ArrayList;
import java.util.List;

import reasoning.core.RsLogger;

public class Parallel implements IAItem {
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());
	List<IAItem> objects = new ArrayList<IAItem>();

	public List<IAItem> getObjects() {
		return objects;
	}

	public void setObjects(List<IAItem> objects) {
		this.objects = objects;
	}

	public boolean play() {
		// Parallel to play items
		for (IAItem item : objects) {
			// Need to create multiple thread here
			logger.debug("play the sub item:" + item);
			item.play();
		}

		return true;
	}

}
