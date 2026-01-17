import java.util.Scanner;
import ReservaHotel.Reserva;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Reserva[] reservas = new Reserva[10];
        int total = 0;
        int escolha;

        do {
            System.out.println("\nO que deseja fazer?");
            System.out.println("1 - Cadastrar nova reserva");
            System.out.println("2 - Listar reservas");
            System.out.println("3 - Buscar reserva por nome do hóspede");
            System.out.println("4 - Ordenar reservas por número de dias");
            System.out.println("5 - Sair");

            escolha = sc.nextInt();
            sc.nextLine();


            if (escolha == 1) {

                if (total >= 10) {
                    System.out.println("Limite máximo de reservas atingido!");
                    continue;
                }

                System.out.print("Nome do hóspede: ");
                String nome = sc.nextLine();

                System.out.print("Número de dias: ");
                int dias = sc.nextInt();
                sc.nextLine();

                System.out.println("Tipo de quarto (Standard / Luxo / Presidencial): ");
                String tipo = sc.nextLine();



                double diaria;

                if (tipo.equalsIgnoreCase("Standard")) diaria = 800;
                else if (tipo.equalsIgnoreCase("Luxo")) diaria = 3000;
                else if (tipo.equalsIgnoreCase("Presidencial")) diaria = 7000;
                else {
                    System.out.println("Tipo inválido.");
                    continue;
                }


                double totalValor = diaria * dias;

                System.out.println("\n--- CONFIRMAÇÃO DA RESERVA ---");
                System.out.println("Hóspede: " + nome);
                System.out.println("Quarto: " + tipo);
                System.out.println("Dias: " + dias);
                System.out.println("Valor da diária: R$ " + diaria);
                System.out.println("Valor total: R$ " + totalValor);

                System.out.print("\nDeseja confirmar a reserva? (Sim/Nao): ");
                String confirmar = sc.nextLine();

                if (confirmar.equalsIgnoreCase("Nao")) {
                    System.out.println("Reserva cancelada.");
                    continue; 
                }
                else if (!confirmar.equalsIgnoreCase("Sim")) {
                    System.out.println("Opção inválida. Reserva cancelada.");
                    continue;
                }




                reservas[total] = new Reserva(nome, tipo, dias, diaria);
                total++;

                System.out.println("Reserva cadastrada com sucesso!");
            }


            else if (escolha == 2) {

                if (total == 0) {
                    System.out.println("Nenhuma reserva cadastrada.");
                }

                for (int i = 0; i < total; i++) {
                    reservas[i].exibirDetalhes();
                }
            }


            else if (escolha == 3) {

                System.out.print("Digite o nome do hóspede: ");
                String busca = sc.nextLine();
                boolean encontrado = false;

                for (int i = 0; i < total; i++) {
                    if (reservas[i].getNomeHospede().equalsIgnoreCase(busca)) {
                        reservas[i].exibirDetalhes();
                        encontrado = true;
                    }
                }

                if (!encontrado) {
                    System.out.println("Reserva não encontrada.");
                }
            }


            else if (escolha == 4) {

                for (int i = 0; i < total - 1; i++) {
                    for (int j = 0; j < total - 1 - i; j++) {
                        if (reservas[j].getNumeroDias() < reservas[j + 1].getNumeroDias()) {
                            Reserva temp = reservas[j];
                            reservas[j] = reservas[j + 1];
                            reservas[j + 1] = temp;
                        }
                    }
                }

                System.out.println("Reservas ordenadas por número de dias.");
            }

        } while (escolha != 5);

        System.out.println("Programa encerrado.");
    }
}
