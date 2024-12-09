package backjoon;

import java.util.*;
import java.io.*;

class Problem1927{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		PriorityQueue<Integer> minHeap = new PriorityQueue<>();
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n ; i++) {
			int num = Integer.parseInt(br.readLine());
			if(num>0) {
				minHeap.add(num);
			}
			else{//0
				
				if(!minHeap.isEmpty()) {
					sb.append(minHeap.peek()).append("\n");
					minHeap.poll();
				}
				else {
					sb.append(0).append("\n");
				}
				
			}
		}
		
		System.out.println(sb);
	}
}