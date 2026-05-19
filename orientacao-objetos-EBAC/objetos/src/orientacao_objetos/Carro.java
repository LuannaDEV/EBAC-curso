package orientacao_objetos;

public class Carro extends Veiculo {

    private boolean temAirbag;
    private int quantidadeDePortas;
    private boolean temPortamalas;


    public Carro(String marca, String modelo, String cor,int quantidadeDePortas, double preco, boolean temAirbag, boolean temPortamalas) {

        super(marca, modelo, cor, preco);

        this.temAirbag = temAirbag;

        this.quantidadeDePortas = quantidadeDePortas;

        this.temPortamalas = temPortamalas;



    }

        public void exibirDetalhes(){

        super.exibirDetalhes();


            System.out.println("POSSUI AIRBAG: " + (this.temAirbag ? "SIM" : "NAO"));
            System.out.println("QUANTIDADE DE PORTAS : " + this.quantidadeDePortas);
            System.out.println("TEM PORTA MALAS: " + (this.temPortamalas ?  "SIM" : "NAO"));
        }




}
