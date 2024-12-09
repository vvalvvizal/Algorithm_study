package backjoon;

import java.util.*;
import java.io.*;

class Problem2630{
	static int blueOne = 0;
	static int whiteOne=  0;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] board = new int[n][n];

		for(int i =0; i< n ; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=0;j<n;j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		divide( board, 0,0,n);
		//System.out.println(Arrays.deepToString(board));
		
		System.out.println(whiteOne);
		System.out.println(blueOne);
	}
	
	//분할 정복의 병합정렬 
	public static void divide(int[][] board,int x, int y, int size) {

		if(check(board, x, y, size)) {
			if(board[y][x]==0) {
				whiteOne++;
			}
			else {
				blueOne++;
			}
			return;
		}
		
		int newSize = size/2;
		
		divide(board, x,y,newSize);
		divide(board,x+newSize, y,newSize);
		divide(board,x,y+newSize, newSize);
		divide(board, x+newSize, y+newSize, newSize );
	
	}
	public static boolean check(int[][] board, int x, int y, int size) {
		
		int color = board[y][x]; 
		for(int i = y;i< y + size;i++) {
			for(int j = x;j<x+size;j++) {
				if(board[i][j]!=color) {
					return false;
				}
			}
		}
		return true;
	}

}