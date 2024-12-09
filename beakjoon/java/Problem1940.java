package backjoon;
import java.util.*;
import java.io.*;


class Problem1940 {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		
		int n = Integer.parseInt(br.readLine());
		
		int m = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		Set set = new HashSet();
		
		int[] numbers = new int[n];
		
		for (int i =0;i<n;i++) {
			if(st.hasMoreTokens()) {
				numbers[i] = Integer.parseInt(st.nextToken());
			}
		}
		
		 for (int i = 0; i < n; i++) {
	            for (int j = i + 1; j < n; j++) { 
	                if (numbers[i] + numbers[j] == m) {
	                    List<Integer> pair = Arrays.asList(numbers[i], numbers[j]);
	                    set.add(pair);  
	                }
	            }
	        }
		
		System.out.println(set.size());
	}
}