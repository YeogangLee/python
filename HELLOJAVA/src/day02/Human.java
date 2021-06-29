package day02;

public class Human extends Animal {
	int skill_speak = 0;
//	int step = 0; //얘를 learnSpeak 메서드 내부에서 쓰려면 this.step
	
	public void learnSpeack() {
		int a = 0;		// 지역변수 : 갈색
		skill_speak++;	// 전역변수 : 파란색
	}
	
	//오버로드 : 과중시키다, 파라미터를 여러 개 실어도 상관없다.
	//옛날 스타일 요즘 시대에는 조금 병맛...
	//면접에서 오버로드와 오버라이딩 비교 질문 많이 했었다
	//오버라이딩 
	//: 내 메서드가 있고, 아빠 메서드가 있을 때,
	//  둘 다 같은 메서드일 때 내 메서드가 실행되는 것
	public void learnSpeack(int step) {
		skill_speak += step; 
	}
	
}
