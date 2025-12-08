import java.util.Scanner;

public class exercicio_Matriz_2 {
    public static void main (String[] args) {

        String[][]        produtos = new String[3][3];
        produtos [0][0] = "110";
        produtos [0][1] = "TELEVISAO";
        produtos [0][2] = "5.300";

        produtos [1][0] = "444";
        produtos [1][1] = "CELULAR";
        produtos [1][2] = "3.500";


        produtos [2][0] = "550";
        produtos [2][1] = "FONE";
        produtos [2][2] = "600.00";

        for (String[] p : produtos) {
            for (String dadoDoProduto : p) {
                System.out.print(dadoDoProduto + " ");
            }

            System.out.println();
        }

        Scanner sc = new Scanner(System.in);

        System.out.println("Digite o codigo do produto que deseja buscar:");

        String codigo = sc.nextLine();

        boolean existe = false;

        for (String[] p : produtos) {
            if (p[0].equals(codigo)){
                System.out.println("Codigo encontrado");
            existe = true;
                break;
        }

        }
        if  (existe==false){
            System.out.println("Produto nao encontrado");
        }
}
}