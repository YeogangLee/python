package day02;

public class Human extends Animal {
	int skill_speak = 0;
//	int step = 0; //�긦 learnSpeak �޼��� ���ο��� ������ this.step
	
	public void learnSpeack() {
		int a = 0;		// �������� : ����
		skill_speak++;	// �������� : �Ķ���
	}
	
	//�����ε� : ���߽�Ű��, �Ķ���͸� ���� �� �Ǿ �������.
	//���� ��Ÿ�� ���� �ô뿡�� ���� ����...
	//�������� �����ε�� �������̵� �� ���� ���� �߾���
	//�������̵� 
	//: �� �޼��尡 �ְ�, �ƺ� �޼��尡 ���� ��,
	//  �� �� ���� �޼����� �� �� �޼��尡 ����Ǵ� ��
	public void learnSpeack(int step) {
		skill_speak += step; 
	}
	
}
