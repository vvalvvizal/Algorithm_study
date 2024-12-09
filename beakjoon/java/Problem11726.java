package backjoon;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Problem11726{
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine().trim());
		
		int[] dp = new int[n+1];
	        if (n >= 1) dp[1] = 1;
	        if (n >= 2) dp[2] = 2;

	        System.out.println(dpFunc(dp, n));
		
	}
	
	public static int dpFunc(int[]dp, int n) {
		  if (dp[n] != 0) return dp[n];
		
		  dp[n] = (dpFunc(dp, n - 1) + dpFunc(dp, n - 2))%10007;
		  
		  return dp[n];
	}
	
}

//동적계획법. tabulation?상향 memoization?하향 -> memoization이좋겠다