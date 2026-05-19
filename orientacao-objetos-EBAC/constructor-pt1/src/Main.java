import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args)  {


        System.out.println("Quantos alunos no sistema voce deseja criar?");
        Scanner sc = new Scanner(System.in);
        int quantidade = sc.nextInt();

        Aluno[] alunosVetor = new Aluno[quantidade];



        double[] vetornotas  = new double[3];

        double nota;

        double notaFinal;

        double soma = 0;

        for (int i = 0; i < alunosVetor.length; i++) {
            System.out.println("Digite o nome do aluno " + (i+1) + ":");
            String nome = sc.next();

            System.out.println("Digite a idade do aluno: ");
            int idade = sc.nextInt();

            alunosVetor[i] = new Aluno(nome, idade);


            for (int j = 0; j < vetornotas.length; j++) {


               do {
                   System.out.println("Digite a nota numero " + (j + 1) + " do aluno " + (i + 1) + ":");
                   nota = sc.nextDouble();
                   soma = +nota;

                   if (nota < 0 || nota > 10) {
                       throw new IllegalArgumentException("Nota deve ser entre 0 e 10!");
                   }

               } while (nota < 0 || nota > 10);


            }
            notaFinal = soma / 3;
            System.out.println("Dados do aluno " + i + ":");
            System.out.println("Nome: " + nome);
            System.out.println("Idade: " + idade);
            System.out.println("Nota final: " + notaFinal);


        }











    }



}