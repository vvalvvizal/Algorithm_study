package backjoon;
import java.util.Scanner;

class Problem30802{
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		sc.nextLine();
		String inputString = sc.nextLine();
		
		String[] input = inputString.split(" ");
		int [] sizes = new int[6];
		for (int i=0;i<6;i++) {
			sizes[i] = Integer.parseInt(input[i]);
		}
		inputString = sc.nextLine();
		input = inputString.split(" ");
		
		int t = Integer.parseInt(input[0]);
		int p = Integer.parseInt(input[1]);
		int tResult=0;
		int pResult =0;
		int pResultOne = 0;
		for(int size:sizes) {
		if(size<1) {
			continue;
		}
		if(size>t) {
			tResult += (size/t)+1;
		}
		else {
		tResult++;	
		}
		
		pResult = n/p;
		pResultOne = n%p;
		}
		
		System.out.println(tResult);
		System.out.println(pResult +" "+pResultOne);
		
	}
}