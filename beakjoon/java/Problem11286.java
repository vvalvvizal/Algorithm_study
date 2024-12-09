package backjoon;
import java.io.*;
import java.util.*;

class Problem11286{
	
	public static void main(String[] args) throws Exception {
		//queue 니까 선입선출 FIFO 
		//그럼 작<-> 큰으로 세워야 함
		//최소힙 
		
		//절대값이 작으려면 숫자 자체가 작아야함. 
		
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	int n = Integer.parseInt(br.readLine());
	PriorityQueue<Integer> minHeap = new PriorityQueue<>((a,b)->{
		int absA = Math.abs(a);
		int absB = Math.abs(b);
		if(absA==absB) {//절대값이 같으면 
			return Integer.compare(a,b);//원래 수가 더 작은거를 출력 
			}
		return Integer.compare(absA, absB);// 절댓값 오름차순 
	});
	StringBuilder sb = new StringBuilder();
	
	for (int i =0 ; i< n ; i++) {
		int x = Integer.parseInt(br.readLine());
		if(x==0) {
			if(!minHeap.isEmpty()) {
				sb.append(minHeap.poll()).append("\n");
			}
			else {
				sb.append(0).append("\n");
			}
		}
		else {
			minHeap.add(x); //그냥 저장하고 
		}
	}
	
	System.out.println(sb);
	}
}