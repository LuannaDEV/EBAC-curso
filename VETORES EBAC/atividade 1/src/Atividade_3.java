import java.util.Arrays;
import java.util.Scanner;

public class Atividade_3 {
    public static void main(String[] args) {


        System.out.println("Digite um nome qualquer");
        Scanner sc = new Scanner(System.in);
        String nome = sc.nextLine();


        char[]letras = nome.toCharArray();




        for (int i = 0; i < letras.length / 2; i++) {

         char aux = letras[i];

         letras[i] = letras[letras.length - i - 1];
        letras[letras.length - i - 1] = aux;

        }

        System.out.println(Arrays.toString(letras));


    }
}
