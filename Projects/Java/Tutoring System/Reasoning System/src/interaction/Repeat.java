package interaction;

import java.util.List;

import reasoning.core.RsLogger;

public class Repeat implements IAItem {
	private int count;
	private List<IAItem> objects;
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());

	public List<IAItem> getObjects() {
		return objects;
	}

	public void setObjects(List<IAItem> objects) {
		this.objects = objects;
	}

	public int getCount() {
		return count;
	}

	public void setCount(int count) {
		this.count = count;
	}

	public boolean play() {
		// random sequence to play items
		for (IAItem item : objects) {
			logger.debug("play the sub item:" + item);
			item.play();
		}

		return true;
	}
}
