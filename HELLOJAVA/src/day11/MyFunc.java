package day11;

public class MyFunc {
	public static void printNum() {
		for(int i=0; i<100000; i++) {
			if(i%100 == 0) {
				System.out.println();
			}
			System.out.print(i + " ");
		}
	}
	
	public static void printChar() {
		for(int i=0; i<100000; i++) {
			System.out.print((char)i + " ");
			if(i%100 == 0) {
				System.out.println();
			}
		}
	}
	
	public static void main(String[] args) {
		printNum();
		printChar();
	}
}
