import java.util.ArrayList;

public class ProjetoArrayList3 {
    public static void main (String[] args) {


        ArrayList<Produto> lista = new ArrayList<>();



      Produto camiseta = new Produto(444, "Roupas", 199.00, "Renner");

        lista.add(camiseta);


        camiseta.precoSet(177.99);

        for (Produto p : lista) {

            p.exibirDetalhes();
        }


    }




    public static class Produto {

        private int codigo;
        private String categoria;
        private double preco;
        private String nome;



        public String getCategoria() {
            return this.categoria;
        }

        public int getCodigo() {
            return this.codigo;
        }

        public String getNome() {
            return this.nome;
        }

        public double getPreco(){
            return  this.preco;
        }



        public Produto(int codigo, String categoria, double preco, String nome) {

            this.codigo = codigo;
            this.categoria = categoria;
            this.preco = preco;
            this.nome = nome;



        }


        public void exibirDetalhes () {

            System.out.println("Detalhes do Produto");
            System.out.println("Codigo: " + this.codigo);
            System.out.println("Categoria: " + this.categoria);
            System.out.println("Preco: " + this.preco);
            System.out.println("Nome: " + this.nome);







        }



            public void precoSet(double novoPreco) {

            this.preco = novoPreco;


            }





    }





}
