import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd

global_output_df = None  # Variável global para armazenar o resultado

def calcular_corretagem_por_conta(df, taxa):
    """
    Agrupa as ordens por conta e calcula a corretagem,
    multiplicando o número de ordens pela taxa informada.
    """
    ordens_por_conta = df.groupby('Conta').size()
    corretagem = ordens_por_conta * taxa
    return corretagem

def selecionar_arquivo():
    """
    Abre um diálogo para selecionar o arquivo CSV.
    """
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if arquivo:
        arquivo_entry.delete(0, tk.END)
        arquivo_entry.insert(0, arquivo)

def processar():
    """
    Lê o arquivo CSV, filtra pelas contas (se informado), 
    lê a taxa de corretagem informada pelo usuário, calcula a corretagem 
    e exibe o resultado na área de texto.
    """
    caminho_arquivo = arquivo_entry.get()
    if not caminho_arquivo:
        messagebox.showerror("Erro", "Selecione um arquivo CSV.")
        return

    # Recupera a taxa de corretagem informada
    taxa_str = taxa_entry.get().strip()
    try:
        taxa = float(taxa_str)
    except ValueError:
        messagebox.showerror("Erro", "Taxa de corretagem inválida. Insira um valor numérico.")
        return

    try:
        df = pd.read_csv(caminho_arquivo, encoding='latin1')
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o arquivo:\n{e}")
        return

    if 'Conta' not in df.columns:
        messagebox.showerror("Erro", "A coluna 'Conta' não foi encontrada no arquivo.")
        return

    # Converte a coluna 'Conta' para string para evitar discrepâncias com a entrada do usuário
    df['Conta'] = df['Conta'].astype(str)
    
    # Filtra as contas, se informado
    contas_input = contas_entry.get().strip()
    if contas_input:
        contas = [conta.strip() for conta in contas_input.split(',')]
        df = df[df['Conta'].isin(contas)]
    
    if df.empty:
        messagebox.showinfo("Informação", "Nenhuma ordem encontrada para as contas informadas.")
        return

    # Calcula a corretagem usando a taxa informada
    corretagem_por_conta = calcular_corretagem_por_conta(df, taxa)
    
    # Cria um DataFrame para o output
    output_df = pd.DataFrame(corretagem_por_conta).reset_index()
    output_df.columns = ['Conta', 'Corretagem']
    
    # Exibe o resultado na área de texto
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, "===== Resumo da Corretagem por Conta =====\n")
    for index, row in output_df.iterrows():
        resultado_text.insert(tk.END, f"Conta: {row['Conta']} - Corretagem: R$ {row['Corretagem']:.2f}\n")
    
    global global_output_df
    global_output_df = output_df

def salvar_excel():
    """
    Salva o resultado do processamento em um arquivo Excel (.xlsx).
    """
    global global_output_df
    if global_output_df is None or global_output_df.empty:
        messagebox.showerror("Erro", "Nenhum resultado para salvar. Execute o processamento primeiro.")
        return

    arquivo_salvar = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")],
        title="Salvar arquivo Excel"
    )
    if arquivo_salvar:
        try:
            global_output_df.to_excel(arquivo_salvar, index=False)
            messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{arquivo_salvar}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o arquivo:\n{e}")

# Criação da interface gráfica com tkinter
root = tk.Tk()
root.title("Cálculo de Corretagem")

# Frame para seleção do arquivo
frame_file = tk.Frame(root)
frame_file.pack(padx=10, pady=10, fill='x')

arquivo_label = tk.Label(frame_file, text="Arquivo CSV:")
arquivo_label.pack(side=tk.LEFT)

arquivo_entry = tk.Entry(frame_file, width=50)
arquivo_entry.pack(side=tk.LEFT, padx=5)

arquivo_btn = tk.Button(frame_file, text="Selecionar", command=selecionar_arquivo)
arquivo_btn.pack(side=tk.LEFT, padx=5)

# Frame para informar as contas
frame_contas = tk.Frame(root)
frame_contas.pack(padx=10, pady=10, fill='x')

contas_label = tk.Label(frame_contas, text="Contas (separadas por vírgula):")
contas_label.pack(side=tk.LEFT)

contas_entry = tk.Entry(frame_contas, width=30)
contas_entry.pack(side=tk.LEFT, padx=5)

# Frame para informar a taxa de corretagem
frame_taxa = tk.Frame(root)
frame_taxa.pack(padx=10, pady=10, fill='x')

taxa_label = tk.Label(frame_taxa, text="Taxa de Corretagem (R$):")
taxa_label.pack(side=tk.LEFT)

taxa_entry = tk.Entry(frame_taxa, width=10)
taxa_entry.insert(0, "0.40")  # valor padrão
taxa_entry.pack(side=tk.LEFT, padx=5)

# Botão para processar
processar_btn = tk.Button(root, text="Processar", command=processar)
processar_btn.pack(pady=10)

# Área de texto para exibir o resultado
resultado_text = scrolledtext.ScrolledText(root, width=60, height=15)
resultado_text.pack(padx=10, pady=10)

# Botão para salvar em Excel
salvar_btn = tk.Button(root, text="Salvar como Excel", command=salvar_excel)
salvar_btn.pack(pady=5)

root.mainloop()
