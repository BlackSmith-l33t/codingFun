import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class KeyMoveFrame extends JFrame {
	
	private class MyPanel extends JPanel {
		public MyPanel() {
			
		}
	}
	
	
	public KeyMoveFrame() {
		setSize(400, 400);
		setTitle("화살표키로 원 이동하기");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		add(new MyPanel());
		
		JButton reset = new JButton("GO");	
		
		reset.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				
			}
		});
		
		add(reset);	
	}	
	
	

	public static void main(String[] args) {
		(new KeyMoveFrame()).setVisible(true);
	}
}
