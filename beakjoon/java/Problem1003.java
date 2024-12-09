

package backjoon;
import java.io.InputStreamReader;
import java.io.BufferedReader;


class Problem1003{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine().trim());
		StringBuilder sb = new StringBuilder();
		
		int[][] tabulation = new int[41][2];//1~40, 0~1
		
		for (int j = 0; j < t ; j ++) {
			int n = Integer.parseInt(br.readLine().trim());
			
			tabulation[0][0] = 1;
			tabulation[1][1] = 1;
			tabulation[0][1] = 0;
			tabulation[1][0] = 0;
			for(int i =2 ;i<=40;i++) {
				tabulation[i][0] = tabulation[i-1][0]+tabulation[i-2][0];
				tabulation[i][1] = tabulation[i-1][1]+tabulation[i-2][1];
			}
			sb.append(tabulation[n][0]).append(" ").append(tabulation[n][1]).append("\n");
			
		
		
			

		
		}
		
		System.out.println(sb);
		br.close();
		
	}
	

}