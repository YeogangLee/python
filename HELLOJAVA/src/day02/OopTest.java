package day02;

public class OopTest {
	public static void main(String[] args) {		
//		Animal ani = new Animal();
		
		Human hum = new Human();
//		System.out.println(hum.);
		//�� ��� ctrl + space �غ���, ��ӹ��� ���� �͵鵵 ���ԵǾ� �ִ�.
		// => ������Ʈ�� ��� �޾ұ� ������ ����� �͵�
		System.out.println(hum.age);
		System.out.println(hum.skill_speak);
		hum.aging();
		hum.learnSpeack(5);
		System.out.println(hum.age);
		System.out.println(hum.skill_speak);
	}
}
