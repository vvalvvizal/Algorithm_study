package backjoon;
import java.util.*;
import java.io.*;

class Problem11279{
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int x = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> maxheap = new PriorityQueue<>(Collections.reverseOrder()); //최대힙 
		
		for (int i =0;i<x;i++) {
			int n = Integer.parseInt(br.readLine());
			if(n==0) {
				if(!maxheap.isEmpty())
				{
				sb.append(maxheap.poll()).append("\n"); //값을 꺼내고 배열에서 제거 
				}
				else {
					sb.append(0).append("\n");
				}
			}
			else {
			maxheap.add(n);
			}
		}
		System.out.println(sb);
	}
}