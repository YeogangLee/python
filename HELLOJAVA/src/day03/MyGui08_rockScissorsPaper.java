package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui08_rockScissorsPaper extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui08_rockScissorsPaper_sem frame = new MyGui08_rockScissorsPaper_sem();
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
	public MyGui08_rockScissorsPaper() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 279, 245);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("\uB098 : ");
		lblMine.setBounds(30, 33, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("\uCEF4\uD4E8\uD130 :");
		lblCom.setBounds(30, 72, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("\uACB0\uACFC : ");
		lblResult.setBounds(30, 111, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {

				if(tfMine.getText().equals("")) {
					tfCom.setText("");
					tfResult.setText("");
					
				}else {			
					if(tfMine.getText().equals("가위") 
							|| tfMine.getText().equals("바위")
							|| tfMine.getText().equals("보")) {
						
						double rnd = Math.random();
						if(rnd > 0.66) {
							tfCom.setText("가위");
						}else if(rnd > 0.33) {
							tfCom.setText("바위");
						}else {
							tfCom.setText("보");
						}
						
						String mine = tfMine.getText();
						String com = tfCom.getText();
						
						if(mine.equals(com)) {
							tfResult.setText("== 무승부 ==");
						}else if(mine.equals("가위") && com.equals("보")
								|| mine.equals("바위") && com.equals("가위")
								|| mine.equals("보") && com.equals("바위") ){
							
							tfResult.setText("승리하셨습니다!");
							
						}else if(mine.equals("가위") && com.equals("바위")
								|| mine.equals("바위") && com.equals("보")
								|| mine.equals("보") && com.equals("가위") ){
							
							tfResult.setText("패배하셨습니다...");
						}
					}
				}
			}
		});
		tfMine.setText("\uAC00\uC704 / \uBC14\uC704 / \uBCF4");
		tfMine.setBounds(118, 30, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setBounds(118, 69, 116, 21);
		contentPane.add(tfCom);
		tfCom.setColumns(10);
		
		tfResult = new JTextField();
		tfResult.setBounds(118, 108, 116, 21);
		contentPane.add(tfResult);
		tfResult.setColumns(10);
		
		JButton btn = new JButton("\uAC8C\uC784\uD558\uAE30");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				if(tfMine.getText().equals("")) {
					tfCom.setText("");
					tfResult.setText("");
					
				}else {			
					if(tfMine.getText().equals("가위") 
							|| tfMine.getText().equals("바위")
							|| tfMine.getText().equals("보")) {
						
						double rnd = Math.random();
						if(rnd > 0.66) {
							tfCom.setText("가위");
						}else if(rnd > 0.33) {
							tfCom.setText("바위");
						}else {
							tfCom.setText("보");
						}
						
						String mine = tfMine.getText();
						String com = tfCom.getText();
						
						if(mine.equals(com)) {
							tfResult.setText("== 무승부 ==");
						}else if(mine.equals("가위") && com.equals("보")
								|| mine.equals("바위") && com.equals("가위")
								|| mine.equals("보") && com.equals("바위") ){
							
							tfResult.setText("승리하셨습니다!");
							
						}else if(mine.equals("가위") && com.equals("바위")
								|| mine.equals("바위") && com.equals("보")
								|| mine.equals("보") && com.equals("가위") ){
							
							tfResult.setText("패배하셨습니다...");
						}
					}
				}
			}
		});
		btn.setBounds(30, 160, 204, 23);
		contentPane.add(btn);
	}

}
