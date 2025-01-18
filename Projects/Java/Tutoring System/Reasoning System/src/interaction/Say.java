package interaction;

import reasoning.core.RsLogger;

import com.sun.speech.freetts.Voice;
import com.sun.speech.freetts.VoiceManager;

public class Say implements IAItem {
	private String utterance = "";
	private VoiceManager voiceManager;
	private Voice voice;
	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());

	public boolean play() {
		logger.debug("Try to read content:" + utterance);
		read();

		return true;
	}

	private void read() {
		voiceManager = VoiceManager.getInstance();
		voice = voiceManager.getVoice("kelvin");
		if (this.voice != null && this.utterance != "") {
			voice.setPitch((float) 4.00);
			voice.setPitchShift((float) .005);
			voice.setPitchRange((float) 0.01);
			// "business", "casual", "robotic", "breathy"
			voice.setStyle("robotic");

			// allocate the resources for the voice
			voice.allocate();

			voice.speak(getUtterance());

			voice.deallocate();
		}
	}

	public String getUtterance() {
		return utterance;
	}

	public void setUtterance(String utterance) {
		this.utterance = utterance;
	}
}
