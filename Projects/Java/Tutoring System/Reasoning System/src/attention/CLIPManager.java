package attention;

import interaction.Action;
import reasoning.core.RsLogger;
import CLIPSJNI.Environment;
import CLIPSJNI.PrimitiveValue;

public class CLIPManager {
	private static Environment clips = new Environment();
	private static RsLogger log = RsLogger.getLogger(Action.class.getName());

	public static void loadClipsProgram(String program) {
		// clips = new Environment();
		clips.clear();
		clips.load(program);
		clips.reset();
	}

	public static void resetClips() {
		clips.reset();
	}

	public static void clearClips() {
		clips.clear();
	}

	public static void assertString(String str) {
		log.debug(str);
		clips.assertString(str);
	}

	public static void runClips() {
		clips.run();
	}

	public static String runClips(String evalStr, String[] names) {
		clips.run();

		PrimitiveValue pv = clips.eval(evalStr);
		String result = "";
		try {
			for (int i = 0; i < pv.size(); i++) {
				PrimitiveValue fv = pv.get(i);
				result = fv.getFactSlot("Result").toString();
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			clips.clear();
			// clips = null;
		}
		return result;
	}

}
