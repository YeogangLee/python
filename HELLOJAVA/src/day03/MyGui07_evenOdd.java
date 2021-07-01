package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MyGui07_evenOdd extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;
	private JLabel lblMine;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui07_evenOdd_sem frame = new MyGui07_evenOdd_sem();
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
	public MyGui07_evenOdd() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 271, 241);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lblMine = new JLabel("\uB098 : ");
		lblMine.setBounds(25, 24, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("\uCEF4\uD4E8\uD130 : ");
		lblCom.setBounds(25, 62, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("\uACB0\uACFC : ");
		lblResult.setBounds(25, 102, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {

				if(tfMine.getText().equals("")) {
					tfCom.setText("");
					tfResult.setText("");
					
				}else {			
					if(tfMine.getText().equals("È¦") || tfMine.getText().equals("Â¦")) {	
						String mine = tfMine.getText();
						
						double rnd = Math.random();
						if(rnd > 0.5) {
							tfCom.setText("È¦");
						}else {
							tfCom.setText("Â¦");
						}
		
						if(tfCom.getText().equals(tfMine.getText())) {
							tfResult.setText("½Â¸®ÇÏ¼Ì½À´Ï´Ù!");
						}else {
							tfResult.setText("ÆÐ¹èÇÏ¼Ì½À´Ï´Ù...");
						}
					}
				}
			}
		});
		tfMine.setText("\uD640 / \uC9DD");
		tfMine.setBounds(110, 21, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(110, 59, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(110, 99, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("\uAC8C\uC784\uD558\uAE30");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String mine = tfMine.getText();
				
				double rnd = Math.random();
				if(rnd > 0.5) {
					tfCom.setText("È¦");
				}else {
					tfCom.setText("Â¦");
				}

				if(tfCom.getText().equals(tfMine.getText())) {
					tfResult.setText("½Â¸®ÇÏ¼Ì½À´Ï´Ù!");
				}else {
					tfResult.setText("ÆÐ¹èÇÏ¼Ì½À´Ï´Ù...");
				}
			}
		});
		
		btn.setBounds(25, 147, 201, 23);
		contentPane.add(btn);
	}

}
