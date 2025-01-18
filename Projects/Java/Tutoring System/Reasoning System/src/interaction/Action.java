package interaction;

import reasoning.core.RsLogger;

public class Action {
	private String name;
	private Parallel paral;
	private Random rand;
	private Repeat repeat;
	private Sequential seq;
	private Select sel;

	public Parallel getParal() {
		return paral;
	}

	public void setParal(Parallel paral) {
		this.paral = paral;
	}

	public Random getRand() {
		return rand;
	}

	public void setRand(Random rand) {
		this.rand = rand;
	}

	public Repeat getRepeat() {
		return repeat;
	}

	public void setRepeat(Repeat repeat) {
		this.repeat = repeat;
	}

	public Sequential getSeq() {
		return seq;
	}

	public void setSeq(Sequential seq) {
		this.seq = seq;
	}

	public Select getSel() {
		return sel;
	}

	public void setSel(Select sel) {
		this.sel = sel;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	private RsLogger logger = RsLogger.getLogger(this.getClass().getName());

	public boolean execute() {
		if (paral!=null)
		{
			logger.debug("Execute paral items.");
			paral.play();
		}
		
		if (rand!=null)
		{
			logger.debug("Execute rand items.");
			rand.play();
		}
		
		if (repeat!=null)
		{
			logger.debug("Execute repeat items.");
			repeat.play();
		}
		
		if (seq!=null)
		{
			logger.debug("Execute seq items.");
			seq.play();
		}
		
		if (sel!=null)
		{
			logger.debug("Execute sel items.");
			sel.play();
		}
		
		return true;
	}

}
