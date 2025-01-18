package interaction;

import reasoning.core.RsLogger;

public class Display implements IAItem{
	private String content;
	private RsLogger logger = RsLogger.getLogger(Display.class.getName());

	public boolean play() {
		logger.info("Display Message: " + this.content);
		return true;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}
}
