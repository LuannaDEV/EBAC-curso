package ReservaHotel;

public class Reserva {

    private String nomeHospede;
    private String tipoQuarto;
    private int numeroDias;
    private double valorDiaria;

    public Reserva(String nomeHospede, String tipoQuarto, int numeroDias, double valorDiaria) {
        this.nomeHospede = nomeHospede;
        this.tipoQuarto = tipoQuarto;
        this.numeroDias = numeroDias;
        this.valorDiaria = valorDiaria;
    }

    public String getNomeHospede() {
        return nomeHospede;
    }

    public int getNumeroDias() {
        return numeroDias;
    }

    public double getValorTotal() {
        return numeroDias * valorDiaria;
    }

    public void exibirDetalhes() {
        System.out.println("Hóspede: " + nomeHospede);
        System.out.println("Quarto: " + tipoQuarto);
        System.out.println("Dias: " + numeroDias);
        System.out.println("Total: R$ " + getValorTotal());
        System.out.println("------------------------");
    }
}
