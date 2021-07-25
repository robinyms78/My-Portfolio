package pkg;

// Fig. 4.20: DrawPanel.java
// Using drawLine to connect the corners of a panel.

import java.awt.Graphics;
import javax.swing.JPanel;

public class DrawPanel extends JPanel 
{
	// draws an X from the corners of the panel
	public void paintComponent(Graphics g)
	{
		// call paintComponent to ensure the panel displays correctly
		super.paintComponent(g);

		int width = getWidth(); // total width
		int height = getHeight(); // total height
		int w_start = 0;
		int h_start = 0;
		int h_end = height;
		int verticalStep = height / 15;
		int horizontalStep = width / 15;
		int counter = 1;

		while (counter <= 15)
		{
			// draw a line from the lower-left to the upper-right starting from upper right corner
			g.drawLine(0, 0, w_start, h_end);

		    // draw a line from the lower-right to the upper-left starting from upper left corner
			g.drawLine(width, 0, w_start, h_start);

			// draw a line from the lower-right to the upper-left starting from lower left corner
			g.drawLine(0, height, w_start, h_start);
			
			// draw a line from the lower-right to the upper-left starting from lower right corner
			g.drawLine(width, height, w_start, h_end);

			w_start += horizontalStep;
			h_end -= verticalStep;
			h_start += verticalStep;
			counter += 1;
		}
	} // end method paintComponent
} // end class DrawPanel


