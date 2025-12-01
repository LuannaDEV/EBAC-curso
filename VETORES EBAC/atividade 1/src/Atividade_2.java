import java.util.Arrays;
import java.util.Scanner;

public class Atividade_2 {
    public static void main(String[] args) {


        System.out.println("Digite o tamanho do vetor");
        Scanner sc = new Scanner(System.in);
        int tamanho = sc.nextInt();

        int[] vetor  = new int[tamanho];

        for (int i = 0; i < vetor.length; i++) {
            System.out.println("Digite o numero: ");
            vetor[i] = sc.nextInt();


            if (vetor[i] % 2 == 0) {

                vetor[i] =  vetor[i] * 2;
            } else {
                vetor[i] = (int) Math.pow(vetor[i], vetor[i]);
            }


        }

        System.out.println("Vetor atualizado: " + Arrays.toString(vetor));

        sc.close();

    }
}
