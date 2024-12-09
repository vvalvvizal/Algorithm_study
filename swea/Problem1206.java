package swea;

import java.util.Scanner;


class Problem1206
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            sc.nextLine();
            String input = sc.nextLine();
            String[] heightsString = input.split(" ");
            
          int[] heights = new int [n];
			for (int i=0;i<n;i++){
                heights[i] = Integer.parseInt(heightsString[i]);
            }
            int[][] board = new int [255][n];
            int count = 0;
            int max_height = 0;
            for (int i=2;i<n-2;i++){
             for(int j=0;j<heights[i];j++){
                 board[j][i] = 1;
               
             }
              max_height = Math.max(max_height,heights[i]);
            }
            for(int i=max_height-1;i>=0;i--){
             for (int j=2;j<n-2;j++){
                  if (board[i][j] == 1){
                        if(board[i][j - 2] == 0 && board[i][j - 1] == 0 &&
                        board[i][j + 1] == 0 && board[i][j + 2] == 0) {
                        count += 1;
                    }
                  }
             }
            }
                                             
           
           System.out.println("#"+test_case+" "+count);
		

		}
	}
}