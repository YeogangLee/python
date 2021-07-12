package day11;

public class MyThre {
	
	public static void printNum() {
		new Thread(new Runnable() {
			@Override
			public void run() {
				for(int i=0; i<100000; i++) {
					if(i%100 == 0) {
						System.out.println();
					}
					System.out.print(i + " ");
				}
			}
		}).start();
	}
	
	public static void printChar() {
		new Thread(new Runnable() {
			@Override
			public void run() {
				for(int i=0; i<100000; i++) {
					System.out.print((char)i + " ");
					if(i%100 == 0) {
						System.out.println();
					}
				}
			}
		}).start();
	}
	
	public static void main(String[] args) {
		printNum();
		printChar();
	}
}
