package backjoon;
import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

class Problem1931{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int count = 0 ;
		List<Pair> list = new ArrayList<>();
		

		
		for ( int i = 0 ; i < n ; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			
			Pair pair = new Pair(s,e);
			
			list.add(pair);
			}
		
		list = list.stream()
			    .sorted((p1, p2) -> Integer.compare(p1.getEnd(), p2.getEnd()) 
			        == 0 ? Integer.compare(p1.getStart(), p2.getStart())  // End 값이 같으면 Start 값으로 정렬
			        : Integer.compare(p1.getEnd(), p2.getEnd()))  // End 값으로 정렬
			    .collect(Collectors.toList());
		int nowStart = 0;
		int nowEnd = 0;

		
		
		for (Pair pair: list) {
			if(pair.getStart()>=nowEnd) {
				nowStart = pair.getStart();
				nowEnd = pair.getEnd();
				count +=1;
			}
		}
		
		System.out.println(count);
		
	}
}

class Pair{
private int start;
private int end;
	
	Pair(int start, int end){
		this.start = start;
		this.end = end;
		
	}
	public int getStart(){
		return this.start;
	}
	public int getEnd(){
		return this.end;
	}

}
