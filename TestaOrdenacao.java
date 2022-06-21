public class TestaOrdenacao {
<<<<<<< HEAD
    public static void main(String[] args){
        Produto produtos[] = {
            new Produto("Lamborghini", 1000000),
=======

    public static void main(String[] args) {

        Produto produtos[] = {
            new Produto("Lamborguini", 1000000),
>>>>>>> 82917afe5f3cd6e82f0648203edc2997bf6966c9
            new Produto("Jipe", 46000),
            new Produto("Brasília", 16000),
            new Produto("Smart", 46000),
            new Produto("Fusca", 17000)
        };

<<<<<<< HEAD
        for(int atual=0; atual < produtos.length; atual++){
            int menor = buscaMenor(produtos, atual, produtos.length - 1);
            Produto produtoAtual = produtos[atual];
            Produto produtoMenor = produtos[menor];
=======
        for (int atual = 0; atual < produtos.length; atual++) {

            int menor = buscaMenor(produtos, atual, produtos.length - 1);

            Produto produtoAtual = produtos[atual];
            Produto produtoMenor = produtos[menor];

>>>>>>> 82917afe5f3cd6e82f0648203edc2997bf6966c9
            produtos[atual] = produtoMenor;
            produtos[menor] = produtoAtual;
        }

<<<<<<< HEAD
        for(Produto produto: produtos){
            System.out.println("O carro " + produto.getNome() + " custa: " + produto.getPreco());
        }

    };


    private static int buscaMenor(Produto[] produtos, int inicio, int termino){
        int maisBarato = 0;
        for(int atual=inicio; atual <= termino; atual++){
            if(produtos[atual].getPreco() < produtos[maisBarato].getPreco()){
                maisBarato = atual;
            }
        }
        return maisBarato;
    }
}
=======
        for (Produto produto : produtos) {
            System.out.println(produto.getNome() + " custa " + produto.getPreco());
        }
    }

    private static int buscaMenor(Produto[] produtos, int inicio, int termino) {

        int maisBarato = inicio;

        for (int atual = inicio; atual <= termino; atual++) {
            if (produtos[atual].getPreco() < produtos[maisBarato].getPreco()) {
                maisBarato = atual;
            }
        }

        return maisBarato;
    }
}
>>>>>>> 82917afe5f3cd6e82f0648203edc2997bf6966c9
