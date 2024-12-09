package backjoon;
import java.io.*;
import java.util.*;

class Problem1541{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(),"-");
		
	    int sum = 0;
        if (st.hasMoreTokens()) {
            StringTokenizer firstGroup = new StringTokenizer(st.nextToken(), "+");
           
            while (firstGroup.hasMoreTokens()) {
                sum += Integer.parseInt(firstGroup.nextToken());
            }
        }
        //- 이후의 수식 
        while (st.hasMoreTokens()) {
            StringTokenizer nextGroup = new StringTokenizer(st.nextToken(), "+");
            int groupSum = 0;
            while (nextGroup.hasMoreTokens()) {
                groupSum += Integer.parseInt(nextGroup.nextToken());
            }
            sum -= groupSum;
        }
		
        System.out.println(sum);
		
		}
	
}