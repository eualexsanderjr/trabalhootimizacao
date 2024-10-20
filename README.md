## Explicação das Funções e Estrutura

### Coleta de dados (`get_data`)
Usa a biblioteca `yfinance` para baixar os preços ajustados de fechamento dos ativos. Você pode substituir os tickers de exemplo pelos ativos de seu interesse.

### Cálculo de retorno e risco (`calculate_returns_and_risk`)
Calcula o retorno esperado e o risco (volatilidade) anualizados a partir dos dados históricos.

### Otimização da carteira (`portfolio_optimization`)
Resolve o problema de otimização para maximizar o retorno esperado, respeitando o limite de risco definido.

### Visualização da alocação de ativos (`plot_allocation`)
Exibe a alocação de pesos da carteira em um gráfico de barras.

### Fronteira eficiente (`plot_efficient_frontier`)
Mostra a relação risco-retorno do portfólio ótimo.

### Evolução dos retornos ao longo do tempo (`plot_return_risk_evolution`)
Mostra a evolução do retorno acumulado para cada ativo ao longo do período.

## Como Usar
O código é executado a partir da função `main()`. Ele baixa os dados dos ativos, calcula os retornos e o risco, otimiza a carteira e plota os gráficos.  Para rodar o script, basta executar o arquivo teste.py diretamente no terminal:

python teste.py

Ao rodar o script, você verá:

Os pesos ótimos calculados para cada ativo.
Três gráficos:
A alocação de ativos na carteira.
A fronteira eficiente (relação entre retorno e risco).
A evolução dos retornos acumulados ao longo do tempo.

