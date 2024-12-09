package backjoon;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;

class Problem17219{
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		Map<String, String> sites = new HashMap<>();
		for (int i = 0; i < n ; i++) {
			st = new StringTokenizer(br.readLine());
			
			String url = st.nextToken();
			String value = st.nextToken();
			sites.put(url, value);
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i =0 ;i < m;i++) {
			String targetURL = br.readLine().trim();
			sb.append(sites.get(targetURL)).append("\n");
		}
		
		System.out.println(sb);
	}
}