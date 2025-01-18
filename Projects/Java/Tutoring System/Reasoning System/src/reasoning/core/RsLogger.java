package reasoning.core;

import java.util.Hashtable;

import org.apache.log4j.Logger;

public class RsLogger {
	private Logger logger;
    private static Hashtable<String,RsLogger> instances = new Hashtable<String,RsLogger>();

    /**
     * Factory method to get the Log instance with the name.
     */
    public static RsLogger getLogger(String name)
    {
    	RsLogger log;
        if (instances.containsKey(name))
        {
            log = (RsLogger)instances.get(name);
        }
        else
        {
            log = new RsLogger(name);
            instances.put(name, log);
        }
        return log;
    }

    /**
     * Create a Log with the name.
//     * @deprecated Replaced by factory method getLog(String).
     */
    public RsLogger(String name)
    {
        logger = Logger.getLogger(name);
    }

    public void debug(Object message)
    {
        logger.debug(message);
    }

    public void info(Object message)
    {
        logger.info(message);
    }

    public void warn(Object message)
    {
        logger.warn(message);
    }

    public void error(Object message)
    {
        logger.error(message);
    }

    public void fatal(Object message)
    {
        logger.fatal(message);
    }
}
