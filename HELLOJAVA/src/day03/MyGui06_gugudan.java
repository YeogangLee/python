package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui06_gugudan extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui06_gugudan frame = new MyGui06_gugudan();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyGui06_gugudan() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 260, 360);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단");
		lbl.setBounds(31, 31, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(100, 28, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(31, 92, 185, 216);
		contentPane.add(ta);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int dan = Integer.parseInt(tf.getText());
				String str = "";
				//선생님은 for문 쓰는거 안 좋아한다.
				for(int i=1; i<10; i++) {
					str += dan + " x " + i + " = " + dan*i + "\n";
				}
				ta.setText(str);
			}
		});
		
		btn.setBounds(31, 59, 185, 23);
		contentPane.add(btn);
		
	}
}
