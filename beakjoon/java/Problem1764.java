package backjoon;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.ArrayList;
import java.util.Collections;
import java.io.BufferedReader;

class Problem1764{
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String input = br.readLine();
		
		String[] inputString = input.split(" ");
		int n = Integer.parseInt(inputString[0]);
		int m = Integer.parseInt(inputString[1]);
		
		Set<String> set1 = new HashSet<>();
		Set<String> set2 = new HashSet<>();
		
		ArrayList<String> duplicates = new ArrayList<>();
		
		for (int i = 0;i< n; i++) {
			set1.add(br.readLine().trim());
		}
		for (int j = 0; j < m; j++) {
			String tmp = br.readLine().trim();
			if (set1.contains(tmp)) {
				duplicates.add(tmp);
			}
			set2.add(tmp);
		}
		
		Collections.sort(duplicates);
		
	       sb.append(duplicates.size()).append("\n");
	        for (String name : duplicates) {
	            sb.append(name).append("\n");
	        }
	        
	        System.out.println(sb.toString());

		
		
		
	}
}