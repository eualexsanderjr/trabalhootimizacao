import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import seaborn as sns

# Função para obter os dados históricos dos ativos via Yahoo Finance
def get_data(tickers, start_date, end_date):
    print("Baixando dados dos ativos de", tickers)
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Função para calcular os retornos esperados e o risco (desvio padrão)
def calculate_returns_and_risk(data):
    print("Calculando retornos e risco dos ativos.")
    returns = data.pct_change().mean() * 252  # Retorno anualizado
    risk = data.pct_change().std() * np.sqrt(252)  # Volatilidade anualizada (risco)
    return returns, risk

# Função de otimização (Maximizar retorno sujeito a um risco máximo)
def portfolio_optimization(returns, risk, max_risk):
    n = len(returns)
    
    # Função objetivo: maximizar o retorno (negativo para minimizar com scipy)
    def objective(weights):
        return -np.dot(weights, returns)
    
    # Restrição de risco
    def constraint(weights):
        return max_risk - np.sqrt(np.dot(weights.T, np.dot(np.diag(risk**2), weights)))
    
    # Restrições e limites dos pesos dos ativos
    constraints = {'type': 'ineq', 'fun': constraint}
    bounds = [(0, 1) for _ in range(n)]
    initial_weights = np.ones(n) / n  # Pesos iniciais iguais
    
    # Resolver problema de otimização
    result = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
    
    if result.success:
        print("Otimização concluída com sucesso.")
        return result.x
    else:
        raise ValueError("A otimização falhou:", result.message)

# Função para visualizar a alocação dos ativos em um gráfico de barras
def plot_allocation(weights, tickers):
    plt.figure(figsize=(10, 6))
    plt.bar(tickers, weights)
    plt.title('Alocação de Ativos na Carteira')
    plt.xlabel('Ativos')
    plt.ylabel('Pesos')
    plt.show()

# Função para exibir a fronteira eficiente (Retorno x Risco)
def plot_efficient_frontier(returns, risks, weights):
    portfolio_returns = np.dot(weights, returns)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(np.diag(risks**2), weights)))
    
    plt.figure(figsize=(10, 6))
    plt.scatter(portfolio_risk, portfolio_returns, color='red', marker='o', s=100, label='Portfólio Ótimo')
    plt.xlabel('Risco (Desvio Padrão)')
    plt.ylabel('Retorno Esperado')
    plt.title('Fronteira Eficiente - Risco vs Retorno')
    plt.legend()
    plt.show()

# Função para plotar a evolução dos retornos e riscos ao longo do tempo
def plot_return_risk_evolution(data, tickers):
    returns_over_time = data.pct_change().cumsum()
    plt.figure(figsize=(10, 6))
    for ticker in tickers:
        plt.plot(returns_over_time.index, returns_over_time[ticker], label=ticker)
    plt.title('Evolução dos Retornos ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Retorno Acumulado (%)')
    plt.legend()
    plt.show()

# Função principal para executar a otimização
def main():
    # Definir os ativos a serem analisados e o período
    tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']  # Exemplo de ativos
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    max_risk = 0.2  # Definir o limite de risco aceitável (20% de volatilidade)

    # Baixar os dados
    data = get_data(tickers, start_date, end_date)
    
    # Calcular retornos esperados e risco
    returns, risks = calculate_returns_and_risk(data)
    
    # Otimizar a carteira
    optimal_weights = portfolio_optimization(returns, risks, max_risk)
    
    # Exibir os resultados
    print("\nPesos Ótimos da Carteira:")
    for ticker, weight in zip(tickers, optimal_weights):
        print(f"{ticker}: {weight:.2%}")
    
    # Visualização dos resultados
    plot_allocation(optimal_weights, tickers)
    plot_efficient_frontier(returns, risks, optimal_weights)
    plot_return_risk_evolution(data, tickers)

# Execução do código principal
if __name__ == '__main__':
    main()