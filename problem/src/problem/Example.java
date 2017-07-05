package problem;
import java.util.Scanner;

public class Example {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int num= sc.nextInt();
		int i = 0;
		int sum=0;
		while (i<num) {
			if(i%3==0 || i%5==0) {
				sum+=i;
			}
			i++;
		}
		System.out.println(sum);

	}

}
