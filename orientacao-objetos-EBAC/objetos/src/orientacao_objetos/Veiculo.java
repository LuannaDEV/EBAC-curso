package orientacao_objetos;

public class Veiculo {


    private String marca;
     private String modelo;
    private String cor;
    private double preco;



   public String getMarca() {
       return marca;
   }

   public void setMarca(String marca) {
        this.marca = marca;
   }

 public String getModelo() {
       return modelo;
 }


 public void setModelo(String modelo) {
       this.modelo = modelo;
 }

 public String getCor() {
       return cor;
 }

 public void setCor(String cor) {
       this.cor = cor;
 }

 public double getPreco() {
       return preco;
 }
 public void setPreco(double preco) {
       this.preco = preco;
 }








   public Veiculo(String marca, String modelo, String cor, double preco) {

        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
        this.preco = preco;




   }


   public void exibirDetalhes() {
       System.out.println("Detalhes do veiculo");
       System.out.println("MARCA: " + this.marca.toUpperCase());
       System.out.println("MODELO: " + this.modelo.toUpperCase());
       System.out.println("COR: " + this.cor.toUpperCase());




   }

    public String toString() {

        return marca + modelo + cor;
    }


}

