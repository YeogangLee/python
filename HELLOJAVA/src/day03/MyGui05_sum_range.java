package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui05_sum_range extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui05_sum_range frame = new MyGui05_sum_range();
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
	public MyGui05_sum_range() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(27, 35, 51, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl = new JLabel("에서");
		lbl.setBounds(90, 38, 37, 15);
		contentPane.add(lbl);
		
		tf2 = new JTextField();
		tf2.setBounds(121, 35, 63, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JButton btn = new JButton("까지 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int start = Integer.parseInt(tf1.getText());
				int end = Integer.parseInt(tf2.getText());
				int sum = 0;
				for(int i=start; i<=end; i++) {
					sum += i;
				}
				tf3.setText(String.valueOf(sum));
			}
		});
		btn.setBounds(196, 34, 116, 23);
		contentPane.add(btn);
		
		tf3 = new JTextField();
		tf3.setBounds(324, 35, 78, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
	}

}
