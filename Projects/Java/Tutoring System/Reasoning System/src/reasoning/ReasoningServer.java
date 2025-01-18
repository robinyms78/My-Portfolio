package reasoning;

import interaction.SRI.InteractionComponent;

import org.apache.log4j.PropertyConfigurator;

import reasoning.SRI.ReasonComponent;
import SRI.SRIEngineStub;
import attention.AttentionComponent;

public class ReasoningServer {
	private static String INTERACTION_NAME = "INTERACTION";
	private static String INTERACTION_PORT = "interaction";
	private static String PLANER_NAME = "PLANER";
	private static String PLANER_PORT = "planer";
	private static String ATTENTINO_NAME = "ATTENTION";
	private static String ATTENTINO_PORT = "attention";

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		PropertyConfigurator.configure("log4j.properties");
		// System.loadLibrary("CLIPSJNI");

		// create engine stub
		SRIEngineStub engine = new SRIEngineStub("localhost", 54321, "planer");

		// create own component
		ReasonComponent planer = new ReasonComponent(PLANER_NAME, PLANER_PORT);
		InteractionComponent interaction = new InteractionComponent(INTERACTION_NAME, INTERACTION_PORT);
		AttentionComponent attention = new AttentionComponent(ATTENTINO_NAME, ATTENTINO_PORT);

		// add component to engine stub
		engine.iAddComponent(planer, "engine");
		engine.iAddComponent(interaction, "engine");
		engine.iAddComponent(attention, "engine");

		// create connection between components
		engine.iConnect(PLANER_NAME, PLANER_PORT + "out", INTERACTION_NAME, INTERACTION_PORT + "in");
		engine.iConnect(PLANER_NAME, PLANER_PORT + "out", ATTENTINO_NAME, ATTENTINO_PORT + "in");

		// planer.vInit();
		// planer.updateFacts("face", "happy");
		// planer.getPlans("basicsentence");
		// planer.process("action=planer,goal=basicsentence,face=happy");

		// planer.vStep();
	}
}
