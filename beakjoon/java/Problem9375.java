package backjoon;
import java.util.*;
import java.io.*;

class Problem9375{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0 ; i < t ; i ++) {
			Map<String, Integer> items = new HashMap<>();
			int n = Integer.parseInt(br.readLine().trim());
			
			for (int j = 0 ; j < n ; j ++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				String name = st.nextToken();
				String type = st.nextToken();
				
				items.put(type, items.getOrDefault(type, 0)+1); //value는 의상 종류 개수 
			}
			
			int combinations = 1;
			
			for (int item : items.values()) {
				combinations *= (item+1); //종류마다 모든종류 + 1 (아예아무것도안함)의 경우의수가 존재 

			}
			
			sb.append(combinations-1).append("\n");
		
			
		}
		System.out.println(sb);
	}
	
}

