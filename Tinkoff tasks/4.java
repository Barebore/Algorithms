import java.util.Scanner;

public class Solution4 {
    static double alfa;
    static double r;
    static double answer = 0;
    static int N;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        N = Integer.parseInt(in.nextLine());
        alfa = ((double) N-2)/ (double) N*180; //Угол правильного n-угольника (град)
        r = 1/(2*Math.sin(Math.PI/ (double) N));//Радиус описанной вокруг правильного n-угольника окружности
        task4(N);
        System.out.println(answer);
    }

    public static void task4(int n) {
        if (n <= 2) {
            return;
        }
        int part1;
        int part2;
        int part3;
        if (n == N) {
            part1 = n / 3 + 1;
            part2 = (n - part1) / 2 + 2;
            part3 = n - part1 - part2 + 3;
        } else {
            part1 = n;
            part2 = part1/2+1;
            part3 = part1-part2 + 1;
        }
        double a = lengthOfChord(part1);
        double b = lengthOfChord(part2);
        double c = lengthOfChord(part3);
        double s = a*b*c/4/r;
        task4(part1-2);
        task4(part2-2);
        task4(part3-2);
        answer += s;
    }
    public static double lengthOfChord(int angles) {
        if (angles == 2) {
            return 1;
        }
        double sumOfAngles = (angles-1)*180; //углов стало на 1 больше из за центрального угла (в каноничной формуле -2)
        double centerAlfa = sumOfAngles - (angles-1)*alfa ;
        return 2*r*Math.sin(centerAlfa*Math.PI/2/180);
    }
}
