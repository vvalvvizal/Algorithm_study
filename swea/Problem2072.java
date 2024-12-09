package swea;

import java.util.Scanner;
import java.io.FileInputStream;
public class Problem2072 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
        sc.nextLine();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			String input = sc.nextLine();
            String[] numbers = input.split(" ");
            int sum = 0;
 
            for (int i=0;i<numbers.length;i++){
                int num = Integer.parseInt(numbers[i]);
             	if(num%2!=0){
                    sum += num;
                }
            }
            System.out.println("# "+test_case+" "+sum);
		}
	}

	}
	
