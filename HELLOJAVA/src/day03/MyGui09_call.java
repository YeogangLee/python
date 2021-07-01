package day03;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

import javax.swing.SwingConstants;

public class MyGui09_call extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui09_call frame = new MyGui09_call();
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
	public MyGui09_call() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 422, 282);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(25, 41, 346, 28);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myDisplay(e);
			}
		});
		btn1.setBounds(25, 90, 97, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "2";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn2.setBounds(151, 90, 97, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "3";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn3.setBounds(274, 90, 97, 23);
		contentPane.add(btn3);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "6";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn6.setBounds(274, 123, 97, 23);
		contentPane.add(btn6);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "5";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn5.setBounds(151, 123, 97, 23);
		contentPane.add(btn5);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "4";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn4.setBounds(25, 123, 97, 23);
		contentPane.add(btn4);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "9";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn9.setBounds(274, 156, 97, 23);
		contentPane.add(btn9);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "8";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn8.setBounds(151, 156, 97, 23);
		contentPane.add(btn8);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "7";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn7.setBounds(25, 156, 97, 23);
		contentPane.add(btn7);
		
		JButton btnCall = new JButton("call");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JOptionPane.showMessageDialog(null, 
						"calling...\n" + tf.getText(), "Message", 
						JOptionPane.INFORMATION_MESSAGE); 
			}
		});
		btnCall.setBounds(274, 189, 97, 23);
		contentPane.add(btnCall);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				String str = tf.getText();
//				str += "0";
//				tf.setText(str);
				myDisplay(e);
			}
		});
		btn0.setBounds(151, 189, 97, 23);
		contentPane.add(btn0);
		
		JButton btnC = new JButton("C");
		btnC.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText("");
			}
		});
		btnC.setBounds(25, 189, 97, 23);
		contentPane.add(btnC);
	}
	
	//숫자만 줘도 되는데, 이벤트를 파라미터로 줘볼게요.
	public void myDisplay(MouseEvent e) {
		String str_old = tf.getText();
//		str += "1";
//		System.out.println(e);
//		System.out.println(e.getSource());
		
		JButton obj = (JButton) e.getSource(); 
//		System.out.println(obj.getText());
		String str_new = obj.getText();
		
		tf.setText(str_old + str_new);
	}
	
}
