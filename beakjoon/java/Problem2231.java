package backjoon;
import java.util.Scanner;


class Problem2231{
	
public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);

	int n = sc.nextInt();
	
	int min = n - (9*Integer.toString(n).length());
	if(min<0)min=0;


	for (int j=min;j<n;j++) {
		int sum = j;
		int temp = j;
		
		while(temp>0) {
			sum += temp%10; //각 자리수를 합하기 
			temp /= 10; //10으로 나눈 몫. 자리수 
			//한 자리수일때 temp는 0이 되고 그 다음에 끝남. 
		}
		
		if(sum==n) {
			System.out.println(j);
			return;
		}
	}
	System.out.println(0);
}

}