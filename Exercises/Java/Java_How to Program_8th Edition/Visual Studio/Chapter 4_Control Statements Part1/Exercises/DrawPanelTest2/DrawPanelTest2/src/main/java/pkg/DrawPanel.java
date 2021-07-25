package pkg;

// Fig. 4.21: DrawPanel.java
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
		int w_end = width;
		int verticalStep = height / 15;
		int horizontalStep = width / 15;
		int counter = 1;

		while (counter <= 15)
		{
			// draw a line from the upper-left to the lower-left starting from lower left corner
			g.drawLine(0, h_start, w_start, height);
			
			// draw a line from the upper-left to the lower-right starting from upper left corner
			g.drawLine(w_start, 0, width, h_start);

			// draw a line from the upper-right to the lower-left starting from lower right corner
			g.drawLine(width, h_start, w_end, height);

            // draw a line from the upper-right to the lower-left starting from upper left corner
			g.drawLine(w_end, 0, 0, h_start);
			
		    w_start += horizontalStep;
			h_start += verticalStep;
			w_end -= horizontalStep;
			counter += 1;
		}
	} // end method paintComponent
} // end class DrawPanel

