package day02;

public class OopTest {
	public static void main(String[] args) {		
//		Animal ani = new Animal();
		
		Human hum = new Human();
//		System.out.println(hum.);
		//점 찍고 ctrl + space 해보면, 상속받지 않은 것들도 포함되어 있다.
		// => 오브젝트를 상속 받았기 때문에 생기는 것들
		System.out.println(hum.age);
		System.out.println(hum.skill_speak);
		hum.aging();
		hum.learnSpeack(5);
		System.out.println(hum.age);
		System.out.println(hum.skill_speak);
	}
}
