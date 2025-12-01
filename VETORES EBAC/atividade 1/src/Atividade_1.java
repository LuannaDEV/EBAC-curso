import java.util.Arrays;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Atividade_1 {
    public static void main(String[] args) {


            int[] vetor = new int[] {5 , 10, 8, 23};

            for(int i = 0; i < vetor.length; i++){

                for(int j = 0; j < vetor.length; j++){


                    if (vetor[j] > vetor[i]){
                    int aux  = vetor[i];
                    vetor[i] = vetor[j];
                    vetor[j] = aux;
                    }

                }

            }


        System.out.println(Arrays.toString(vetor));


        System.out.println("Digite um nome ");
        Scanner sc = new Scanner(System.in);
        String nome = sc.nextLine();

        char[] letras = nome.toCharArray();
        int quantidadeVogais = 0;


        String vogais = "aeiouAEIOU";
        for(int i = 0; i < letras.length; i++){

            if (vogais.contains(String.valueOf(letras[i]))){

                quantidadeVogais++;


            }

            }

        System.out.println("Esta palavra tem: " + quantidadeVogais + " vogais");

        sc.close();
        }













    }

