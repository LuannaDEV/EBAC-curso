import orientacao_objetos.Carro;
import orientacao_objetos.Veiculo;

import java.sql.SQLOutput;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);


        int quantidadeDeCarros;

        do {
            System.out.println("Quantos carros voce deseja? (maximo 50)");
            quantidadeDeCarros = sc.nextInt();

            if (quantidadeDeCarros > 50) {
                System.out.println("A quantidade maxima é 50. Tente novamente!");
            }


        } while  (quantidadeDeCarros > 50);

        Carro[] vetorDeCarros = new Carro[quantidadeDeCarros];

        boolean portaMalas  = false;
        boolean airbag = false;

        for (int i = 0; i < vetorDeCarros.length; i++) {
            sc.nextLine();
            System.out.println("-Cadastrando o carro-\n");
            System.out.println("\nDigite a marca do carro :");
            String marca = lerString(sc);


            System.out.println("\nDigite o modelo do carro :");
            String modelo = lerString(sc);


            String cor = lerCor(sc);


            System.out.println("\nDigite a quantidade de portas: ");
            int quantidadeDePortas = lerPortas(sc);

            System.out.println("\nDigite o preco do carro :");
            double preco = sc.nextDouble();

            System.out.println("\nTem airbag? Digite 1 para sim e 2 para não: ");
            int temAirbag = lerInt(sc);

            if (temAirbag == 1) {
                airbag = true;


            }

            System.out.println("Tem porta malas? Digite 1 para sim e 2 para não: ");
            int temPortamalas = lerInt(sc);

            if (temPortamalas == 1) {
                portaMalas = true;
            }

            vetorDeCarros[i] = new Carro(marca, modelo, cor, quantidadeDePortas, preco, airbag, portaMalas);
        }



        double soma = 0.0;
        for (int i = 0; i < vetorDeCarros.length; i++) {


            System.out.println("\n carro numero " + (i+1) + ":");
          vetorDeCarros[i].exibirDetalhes();

            soma += vetorDeCarros[i].getPreco();

        }
        System.out.println("\n soma final do preco de todos os carros: " + soma);

    }






    public static int lerInt(Scanner scanner) {


        int numeroLido = 0;
        boolean entradaValida = false;

        do{
            if (scanner.hasNextInt()) {

                numeroLido = scanner.nextInt();


                if (numeroLido > 2 || numeroLido < 1) {
                    System.out.println("Valor invalido!");
                } else {

                    entradaValida = true;
                }


            } else  {
                System.out.println("Valor invalido!");
            }

        } while (!entradaValida);


 return numeroLido;

    }

    public static int lerPortas(Scanner scanner) {
        int numeroLido = 0;
        boolean entradaValida = false;

        do {
            if (scanner.hasNextInt()) {

                numeroLido = scanner.nextInt();

                if (numeroLido > 4)  {
                    System.out.println("Valor invalido!");
                } else {
                    entradaValida = true;
                }

            }



        } while (!entradaValida);

        return numeroLido;


    }




    public static String lerString (Scanner scanner) {

        String stringLida = "";
        int maxCaracteres = 50;

        boolean entradaInvalida = false;

        do {
            if (scanner.hasNextLine()) {
                stringLida = scanner.nextLine();

                if (stringLida.length() > maxCaracteres) {
                    System.out.println("ERRO! Quantidade maxima de caracteres: " + maxCaracteres + ". Tente novamente.");
                }

               if (stringLida.trim().isEmpty()) {
                   entradaInvalida = true;
               }

               if (entradaInvalida == true) {
                   System.out.println("ERRO! O campo nao pode estar vazio! Tente novamente.");

                   return stringLida = scanner.nextLine();
               }


            }
        } while (stringLida.length() > maxCaracteres || entradaInvalida );


        return stringLida;



    }

    public static String lerCor (Scanner scanner) {

        String[] coresDisponiveis = {"1 - Branco(White) ", "2 - Preto(Black) ", "3 - Prata(Silver)","4 - Cinza(Gray/Grey) ", "5 - Vermelho(Red) ", "6 - Azul(Blue) ", "7 - Verde(Green) ", "8 - Marrom/Bege(Brown/Beige) "};

        for (int i = 0; i < coresDisponiveis.length; i++) {

            System.out.print(coresDisponiveis[i]);


        }


        int escolha = 0;
        boolean valido = false;

        do{
            System.out.println("\nDigite o numero correspondente a cor do veiculo :");

        if (scanner.hasNextInt()) {
            escolha = scanner.nextInt();


            if (escolha >= 1 && escolha <= coresDisponiveis.length) {
                valido = true;
            } else {
                System.out.println("ERRO! Opcao invalida.");
            }



        }





        } while (!valido);


        return coresDisponiveis[escolha];
    }



}



