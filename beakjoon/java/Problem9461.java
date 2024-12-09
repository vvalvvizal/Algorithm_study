package backjoon;
import java.util.*;
import java.io.*;

class Probelm9461{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		for (int i =0 ; i< t ; i++) {
			int n = Integer.parseInt(br.readLine());
			
			long[] dp = new long[101];
			
			dp[1] = 1;
			dp[2] = 1;
			dp[3] = 1;
			dp[4] = 2;
			dp[5] = 2;
			
			
			
			for (int j =6;j<=n;j++) {
				dp[j] = dp[j-1]+dp[j-5];
											
			}
			
			System.out.println(dp[n]);
			
		}
	}
}