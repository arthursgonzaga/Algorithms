public class NovoSorte {
        public static void main(String[] args) {
            Produto produtos[] = {
                    new Produto("Lamborghini", 1000000),
                    new Produto("Jipe", 46000),
                    new Produto("Brasília", 16000),
                    new Produto("Smart", 46000),
                    new Produto("Fusca", 17000)
            };
            
            // selectionSort(produtos, produtos.length);
            novoSort(produtos, produtos.length);
        
            imprime(produtos);
            
        }
    
        private static void novoSort(Produto[] produtos, int quantidadeDeElementos) {
            for(int atual = 0; atual < quantidadeDeElementos; atual++){
                int analise = atual;
                while(analise > 0 &&produtos[analise].getPreco() < produtos[analise-1].getPreco()){
                    Produto produtoAnalise = produtos[analise];
                    Produto produtoAnaliseMenos1 = produtos[analise - 1];
                    produtos[analise] = produtoAnaliseMenos1;
                    produtos[analise - 1] = produtoAnalise;
                    analise--;
                }
            }
        }
    
        private static void imprime(Produto[] produtos) {
            for(Produto produto : produtos) {
                System.out.println(produto.getNome() + " custa " +
                        produto.getPreco());
            }
        }
    
        private static void troca(Produto[] produtos, int primeiro, int segundo) {		
            Produto primeiroProduto = produtos[primeiro];
            Produto segundoProduto = produtos[segundo];
            
            produtos[primeiro] = segundoProduto;
            produtos[segundo] = primeiroProduto;
        }
    
        private static void selectionSort(Produto[] produtos, int quantidadeDeElementos) {
            for(int atual = 0; atual < quantidadeDeElementos - 1; atual++) {
                
                int menor = buscaMenor(produtos, atual, quantidadeDeElementos - 1);
                troca(produtos, atual, menor);
            }		
        }
                                                                                                                                                                                  
    
        private static int buscaMenor(Produto[] produtos, int inicio, int termino) {
            int maisBarato = inicio;
            for(int atual = inicio; atual <= termino; atual++){
                if(produtos[atual].getPreco() < produtos[maisBarato].getPreco()) {
                    maisBarato = atual;
                }
            }
            return maisBarato;
        }
}
