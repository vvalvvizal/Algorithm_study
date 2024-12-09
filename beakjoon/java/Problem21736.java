package backjoon;
import java.util.*;
import java.io.*;

class Problem21736{
	static int count =0;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		char[][] board = new char[n][m];
		boolean[][] visited = new boolean[n][m];
		
		int x = 0;
		int y = 0;
		
		for(int i =0 ;i<n;i++) {
			String line = br.readLine(); //일단 한 줄 문자열로 받기 
			for(int j =0 ;j<m;j++) {
			board[i][j] = line.charAt(j);
			if(board[i][j]=='I') {//도연이의 시작위치라면 
				//i는 행, j는 열  
				//2차원 좌표계로 접근할때는 반대로 되어야함. 
				x = j;//열
				y = i; //행 
			}
				
			}
		}
		
		dfs(board, visited, x,y);//깊이 우선 탐색 
		
		if(count>0) {
			System.out.println(count);
			
		}
		else {
			System.out.println("TT");
		}
		//System.out.println(Arrays.deepToString(board));
	}
	
	public static void dfs(char[][] board, boolean[][] visited, int x, int y) {
		if(x<0||x>=board[0].length || y<0 || y>=board.length) {
			return;
		}
		if(visited[y][x]) {
			return;
		}
		if(board[y][x]=='X') {
			return;
		}
		if(board[y][x]=='P') {
			count += 1;
		}
		
		visited[y][x] = true;
		
		int[] x_pos = {1,0,-1,0};
		int[] y_pos = {0,1,0,-1};
		for(int i =0 ; i < 4; i++) {
			
			int newX = x+x_pos[i];
			int newY = y+y_pos[i];
			if( newX>=0&&newX<board[0].length && newY>=0&& newY<board.length) {
				dfs(board, visited , newX, newY);
			}
		}
	}
}

	