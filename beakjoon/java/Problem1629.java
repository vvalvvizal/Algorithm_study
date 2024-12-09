package backjoon;

import java.util.*;
import java.io.*;

class Problem1629{
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		
		System.out.print(divide(a,b,c));
		
		
		
	}
	public static long divide(int a,int b, int c) {
		if(b==0)return 1;
		if (b%2==0) {//짝수 
			long tmp =divide(a,b/2,c);
			return (tmp*tmp)%c;
		}
		else {//홀수 
			return (a*divide(a,b-1,c))%c;
		}

}
}