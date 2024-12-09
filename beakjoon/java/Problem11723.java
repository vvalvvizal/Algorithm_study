package backjoon;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.HashSet;
import java.util.StringTokenizer;


class Problem11723{
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int m = Integer.parseInt(br.readLine());
		
		Set<Integer> set = new HashSet<>();

		while(m-->0) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			String calc = st.nextToken();
			
			int num  =0;
			
			if(st.hasMoreTokens()) {
				num = Integer.parseInt(st.nextToken());
			}
			switch(calc) {

			case "add":
				set.add(num);
				break;
			
			case "remove":
				set.remove(num);
				break;
			case "check":
				if(set.contains(num)) {
					sb.append(1).append('\n');
					break;
				}
				else {
					sb.append(0).append('\n');
					break;
				}
			case "toggle":
				if(set.contains(num)) {
					set.remove(num);
					break;
				}
				else {
					set.add(num);
					break;
				}
			case "all":
				for(int i=1;i<=20;i++) {
					set.add(i);
				}
				break;
			case "empty":
				set.clear();
				break;
		}
		
	}
		System.out.println(sb);

}
}