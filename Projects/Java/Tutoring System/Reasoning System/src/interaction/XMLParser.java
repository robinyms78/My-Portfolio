package interaction;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

import reasoning.core.DataXMLDAO;
import reasoning.core.RsLogger;

public class XMLParser {
	private static RsLogger logger = RsLogger.getLogger(DataXMLDAO.class.getName());
	// XML Tags
	private static final String ACTION = "interaction";
	private static final String NAME = "name";

	private static final String PARALLEL = "parallel";
	private static final String SEQUENTIAL = "seq";
	private static final String REPEAT = "repeat";
	private static final String RANDOM = "random";
	private static final String SELECT = "select";

	private static final String SAY = "say";
	private static final String DISPLAY = "display";
	private static final String WAITFOR = "waitfor";
	private static final String DELAY = "delay";

	private static final String UTTERANCE = "utterance";
	private static final String EVENT = "event";
	private static final String TIME = "period";
	private static final String STRING = "string";

	private static final String EVENT_VOICE = "voice";
	private static final String EVENT_KEYBOARD = "keyboard";

	private XMLParser() {
		super();
	}

	public static HashMap<String, Action> loadInteractions(String location) {
		Element root = loadDocument(location);
		return getInteractions(root);
	}

	private static Element loadDocument(String location) {
		Document doc = null;
		try {
			DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder parser = docBuilderFactory.newDocumentBuilder();
			doc = parser.parse(new File(location));
			Element root = doc.getDocumentElement();
			root.normalize();
			return root;
		} catch (SAXParseException err) {
			logger.error("InitDataUtil ** Parsing error" + ", line " + err.getLineNumber() + ", uri " + err.getSystemId());
			logger.error("InitDataUtil error: " + err.getMessage());
		} catch (SAXException e) {
			logger.error("InitDataUtil error: " + e);
		} catch (java.net.MalformedURLException mfx) {
			logger.error("InitDataUtil error: " + mfx);
		} catch (java.io.IOException e) {
			logger.error("InitDataUtil error: " + e);
		} catch (Exception pce) {
			logger.error("InitDataUtil error: " + pce);
		}
		return null;
	}

	private static HashMap<String, Action> getInteractions(Element root) {
		HashMap<String, Action> allActions = new HashMap<String, Action>();
		NodeList actions = root.getElementsByTagName(ACTION);
		for (int loop = 0; loop < actions.getLength(); loop++) {
			Node node = actions.item(loop);
			if (!(node instanceof Element)) {
				continue;
			}
			logger.debug(node.getNodeName());
			try {
				Element element = ((Element) node);
				Action action = new Action();
				action.setName(element.getAttribute(NAME));
				allActions.put(action.getName(), action);

				NodeList subItems = element.getChildNodes();
				if (subItems == null || subItems.getLength() == 0) {
					continue;
				}

				for (int i = 0; i < subItems.getLength(); i++) {
					Node subNode = subItems.item(i);
					if (!(subNode instanceof Element)) {
						continue;
					}
					Element subAction = ((Element) subNode);
					if (PARALLEL.equalsIgnoreCase(subAction.getTagName())) {
						Parallel par = new Parallel();
						par.setObjects(createItems(subAction));
						action.setParal(par);
					} else if (SEQUENTIAL.equalsIgnoreCase(subAction.getTagName())) {
						Sequential seq = new Sequential();
						seq.setObjects(createItems(subAction));
						action.setSeq(seq);
					} else if (REPEAT.equalsIgnoreCase(subAction.getTagName())) {
						Repeat rep = new Repeat();
						rep.setObjects(createItems(subAction));
						action.setRepeat(rep);
					} else if (RANDOM.equalsIgnoreCase(subAction.getTagName())) {
						Random ran = new Random();
						ran.setObjects(createItems(subAction));
						action.setRand(ran);
					} else if (SELECT.equalsIgnoreCase(subAction.getTagName())) {
						Select sel = new Select();
						sel.setObjects(createItems(subAction));
						action.setSel(sel);
					}
				}
			} catch (Exception ex) {
				logger.error("Convert actions error: " + ex.getMessage());
			}
		}

		return allActions;
	}

	private static List<IAItem> createItems(Element element) {
		List<IAItem> items = new ArrayList<IAItem>();
		IAItem item = null;

		NodeList subItems = element.getChildNodes();
		if (subItems == null || subItems.getLength() == 0) {
			return items;
		}

		for (int i = 0; i < subItems.getLength(); i++) {
			Node subNode = subItems.item(i);
			if (!(subNode instanceof Element)) {
				continue;
			}
			Element subAction = ((Element) subNode);
			if (SAY.equalsIgnoreCase(subAction.getTagName())) {
				item = new Say();
				((Say) item).setUtterance(subAction.getAttribute(UTTERANCE));
				items.add(item);
			} else if (DISPLAY.equalsIgnoreCase(subAction.getTagName())) {
				item = new Display();
				((Display) item).setContent(subAction.getAttribute(STRING));
				items.add(item);
			} else if (WAITFOR.equalsIgnoreCase(subAction.getTagName())) {
				item = new WaitFor();
				((WaitFor) item).setEvent(convertEvent(subAction.getAttribute(EVENT)));
				items.add(item);
			} else if (DELAY.equalsIgnoreCase(subAction.getTagName())) {
				item = new Delay();
				((Delay) item).setSecs(Integer.parseInt(subAction.getAttribute(TIME)));
				items.add(item);
			}
		}

		return items;
	}

	private static Event convertEvent(String event) {
		if (EVENT_VOICE.equalsIgnoreCase(event)) {
			return Event.voice_input;
		} else if (EVENT_KEYBOARD.equalsIgnoreCase(event)) {
			return Event.keybord_input;
		}

		return Event.no_input;
	}
}
