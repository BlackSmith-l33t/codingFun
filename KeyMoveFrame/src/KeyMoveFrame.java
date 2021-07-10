import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class KeyMoveFrame extends JFrame {
	
	private JButton reset;
	
	
	private class MyPanel extends JPanel {
		public MyPanel() {
			reset = new JButton("GO");
			add(reset);			
			
		}
	}
	
	
	
	public KeyMoveFrame() {
		setSize(400, 400);
		setTitle("화살표키로 원 이동하기");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		add(new MyPanel());
		
	}	
	public static void main(String[] args) {
		(new KeyMoveFrame()).setVisible(true);
	}
}
