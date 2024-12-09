package swea;

import java.util.Scanner;
import java.io.FileInputStream;
import java.util.Arrays;

class Problem1208
{
	public static void main(String args[]) throws Exception
	{	Scanner sc = new Scanner(System.in);

	 for (int test_case = 1; test_case <= 10; test_case++) {
         int dumpNum = sc.nextInt();
         sc.nextLine(); 
         
         String input = sc.nextLine();
         String[] inputString = input.split(" "); 
         int[] boxHeight = new int[100]; 

         for (int i = 0; i < 100; i++) {
             boxHeight[i] = Integer.parseInt(inputString[i]);
         }

         while (dumpNum-- > 0) {
             if (Arrays.stream(boxHeight).distinct().count() == 1) {
                 break; 
             }

             int maxHeight = Arrays.stream(boxHeight).max().getAsInt();
             int minHeight = Arrays.stream(boxHeight).min().getAsInt();
             
             for (int i = 0; i < 100; i++) {
                 if (boxHeight[i] == maxHeight) {
                     boxHeight[i]--; 
                     break;
                 }
             }
             for (int i = 0; i < 100; i++) {
                 if (boxHeight[i] == minHeight) {
                     boxHeight[i]++;  
                     break;
                 }
             }
             
             maxHeight = Arrays.stream(boxHeight).max().getAsInt();
             minHeight = Arrays.stream(boxHeight).min().getAsInt();
             if (maxHeight - minHeight <= 1) {
                 break;
             }
         }

         int diff = Arrays.stream(boxHeight).max().getAsInt() - Arrays.stream(boxHeight).min().getAsInt();
         System.out.println("#" + test_case + " " + diff);
     }
    }
} 