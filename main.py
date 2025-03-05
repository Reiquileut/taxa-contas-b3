import pandas as pd

TAXA_CORRETAGEM = 0.40

def calcular_corretagem_por_conta(df, taxa=TAXA_CORRETAGEM):
    """
    Agrupa as ordens por conta e calcula a corretagem:
    para cada ordem (linha), cobra-se a taxa definida.
    """
    # Conta o número de ordens por conta
    ordens_por_conta = df.groupby('Conta').size()
    # Calcula a corretagem multiplicando o número de ordens pela taxa
    corretagem = ordens_por_conta * taxa
    return corretagem

def main():
    print("===== Cálculo de Corretagem =====")
    caminho_arquivo = input("Informe o caminho do arquivo CSV (ex: /mnt/data/ordens.csv): ").strip()
    
    try:
        # Lê o arquivo CSV utilizando a codificação 'latin1'
        df = pd.read_csv(caminho_arquivo, encoding='latin1')
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
        return
    
    print("\nArquivo carregado com sucesso!")
    print("Colunas encontradas:", df.columns.tolist())
    
    # Verifica se a coluna 'Conta' está presente
    if 'Conta' not in df.columns:
        print("A coluna 'Conta' não foi encontrada no arquivo. Verifique o cabeçalho do CSV.")
        return

    # Converte a coluna 'Conta' para string para evitar discrepâncias com a entrada do usuário
    df['Conta'] = df['Conta'].astype(str)
    
    # Permite filtrar as contas se desejado
    contas_input = input("\nDigite os números das contas separados por vírgula (ou pressione ENTER para processar todas): ").strip()
    if contas_input:
        contas = [conta.strip() for conta in contas_input.split(',')]
        df = df[df['Conta'].isin(contas)]
    
    if df.empty:
        print("Nenhuma ordem encontrada para as contas informadas.")
        return

    # Calcula a corretagem por conta
    corretagem_por_conta = calcular_corretagem_por_conta(df)

    print("\n===== Resumo da Corretagem por Conta =====")
    for conta, valor in corretagem_por_conta.items():
        print(f"Conta: {conta} - Corretagem: R$ {valor:.2f}")

if __name__ == "__main__":
    main()
