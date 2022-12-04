//В моем алгоритме получилось что количество букв n в названии отдела вообще не используется) Может и не особо оптимально, ну да пофиг

import java.util.Scanner;

public class Solution1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = Integer.parseInt(in.nextLine());//Количество букв без учета пробелов
        String [] str = in.nextLine().split(" ");//Формируем массив из слов
        String schema = in.nextLine();//Цветовая схема
        int counterLength = 0;//Счетчик для синхронизации номера буквы в слове названия отдела и номера буквы в цветовой схеме
        int answer = 0; //Количество некрасивых слов
        for (int i = 0; i < str.length; i++) {// Цикл по словам в названии
            String word = str[i];
            for (int j = 0; j < word.length()-1; j ++) {//Цикл по буквам в слове
                char prevSymb = schema.charAt(counterLength + j);
                char symb = schema.charAt(counterLength + j + 1);
                if (symb == prevSymb) {//Сравниваем равенство соседний символов в цветовой схеме
                    answer ++;
                    break;
                }
            }
            counterLength += word.length()+1;//Устанавливаем значение для корретного указания номера символа в цветовой схеме
        }
        System.out.println(answer);
    }
}
