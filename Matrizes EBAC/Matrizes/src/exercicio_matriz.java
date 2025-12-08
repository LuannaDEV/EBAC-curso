import java.sql.SQLOutput;
import java.util.Arrays;
import java.util.Scanner;

public class exercicio_matriz {
    public static void main(String[] args) {


        System.out.println("Digite quantas linhas voce quer na matriz");
        Scanner sc = new Scanner(System.in);
        int linhas = sc.nextInt();

        System.out.println("Digite quantas colunas voce quer na matriz");
        int colunas = sc.nextInt();

        int[][] matriz = new int[linhas][colunas];

                for ( int i=0; i< matriz.length; i++) {
                    for (int j = 0; j < matriz[i].length;j++ ) {

                        System.out.println("Digite o valor");
                        matriz[i][j] = sc.nextInt();


                    }
                }

        System.out.println(Arrays.deepToString(matriz));



                int maior = matriz[0][0];

                for ( int i=0; i< matriz.length; i++) {
                        for (int j=0; j< matriz[i].length; j++) {

                            if (matriz[i][j] > maior) {

                                maior = matriz[i][j];

                            }


                        }


                }


        System.out.println("O numero maior eh :" + maior);


    }
}
