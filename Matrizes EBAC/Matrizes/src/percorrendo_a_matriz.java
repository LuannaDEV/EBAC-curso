import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class percorrendo_a_matriz {
    public static void main(String[] args) {


        System.out.println("Digite a quantidade de linhas ");
        Scanner scanner = new Scanner(System.in);
        int linhas = scanner.nextInt();

        System.out.println("Digite a quantidade de colunas");
        int colunas = scanner.nextInt();



        int[][] matriz = new int[linhas][colunas];




       for (int i=0; i< matriz.length; i++){

            for (int j=0; j< matriz[i].length; j++){
                System.out.println("Digite o valor da coluna : " + (j+1) + " da linha: " + (i+1));

                Scanner sc = new Scanner(System.in);

                matriz[i][j] = lerInt(sc);


            }


        }
        System.out.println();

        for (int i=0; i< matriz.length; i++){
            for (int j=0; j< matriz[i].length; j++){

                System.out.print(matriz[i][j] + " ");


            }

            System.out.println();
        }



    }






    public static int lerInt(Scanner scanner) {

      while (!scanner.hasNextInt()) {
          System.out.println("Valor invalido! digite apenas numeros.");
          scanner.next();
      }

        return scanner.nextInt();


    }




}