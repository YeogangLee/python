package day03;

import java.awt.Frame;

public class AwtTest {
	public static void main(String[] args) {
		//자바에서는 Frame이라고 한다, 윈도우가 아니라.
		Frame f = new Frame(); 
		f.setSize(300, 400);
		f.setVisible(true);
		
		//5번말해 : 생성, visible, size
		//옛날에는 c++로 개고생해서 만든 코드인데 3줄로 해결
	}
}
