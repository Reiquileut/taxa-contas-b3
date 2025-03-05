# Cálculo de Corretagem

Este projeto é uma aplicação Python com interface gráfica (GUI) desenvolvida com Tkinter e Pandas. A aplicação permite calcular a corretagem de ordens de clientes contidas em um arquivo CSV, com as seguintes funcionalidades:

- **Upload de Arquivo:** Permite importar um arquivo CSV de qualquer diretório.
- **Filtro de Contas:** Possibilita filtrar as ordens por números de contas (informados manualmente, separados por vírgula).
- **Taxa Dinâmica:** Permite alterar a taxa de corretagem por ordem (valor padrão de R$ 0,40, mas editável).
- **Visualização:** Exibe o resumo da corretagem por conta na interface.
- **Exportação:** Permite salvar os resultados em um arquivo Excel (.xlsx).

## Funcionalidades

- **Upload do Arquivo CSV:** Selecione o arquivo que contém as ordens.
- **Filtro de Contas:** Informe os números das contas para filtrar os dados.
- **Taxa de Corretagem Personalizável:** Insira a taxa de corretagem a ser aplicada em cada ordem.
- **Visualização dos Resultados:** Exibição do resumo da corretagem por conta diretamente na interface.
- **Exportação para Excel:** Salve os resultados em um arquivo Excel (.xlsx).

## Requisitos

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- Tkinter (geralmente incluído na instalação padrão do Python)
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/) (para exportar arquivos .xlsx)
- [PyInstaller](https://pyinstaller.org/) (opcional, para gerar um executável)

## Instalação

1. **Clone ou Baixe o Projeto**

   Faça o download dos arquivos do projeto para uma pasta no seu computador.

2. **Crie um Ambiente Virtual (Opcional, mas recomendado)**

   No terminal, navegue até o diretório do projeto e execute:

   ```bash
   python -m venv venv
Em seguida, ative o ambiente virtual:

Windows:
bash
Copiar
venv\Scripts\activate
Linux/Mac:
bash
Copiar
source venv/bin/activate
Crie o Arquivo de Dependências

Se você ainda não possui o arquivo requirements.txt, gere-o automaticamente com o comando:

bash
Copiar
pip freeze > requirements.txt
Ou crie manualmente um arquivo requirements.txt com o seguinte conteúdo:

plaintext
Copiar
pandas
openpyxl
pyinstaller
Instale as Dependências

No terminal, execute:

bash
Copiar
pip install -r requirements.txt
Uso da Aplicação
Execute o Script:

No terminal, dentro do diretório do projeto, execute:

bash
Copiar
python main.py
Utilize a Interface:

Selecionar Arquivo: Clique no botão "Selecionar" para fazer upload do arquivo CSV contendo as ordens.
Filtrar Contas: Insira os números das contas no campo "Contas (separadas por vírgula)" se desejar filtrar os dados.
Taxa de Corretagem: Informe a taxa de corretagem a ser aplicada (o valor padrão é 0.40).
Processar: Clique no botão "Processar" para calcular a corretagem por conta. O resultado será exibido na área de texto.
Exportar para Excel: Se desejar salvar os resultados, clique no botão "Salvar como Excel" e escolha o local para salvar o arquivo .xlsx.
Gerando Executável (.exe)
Para converter a aplicação em um executável Windows, utilize o PyInstaller:

bash
Copiar
python -m pyinstaller --onefile --noconsole main.py
Após a execução, o executável será gerado na pasta dist.

Estrutura do Projeto
A estrutura básica do projeto pode ser a seguinte:

css
Copiar
taxa-contas-b3/
├── main.py
├── README.md
└── requirements.txt
Considerações Finais
Esta aplicação foi desenvolvida para facilitar o cálculo da corretagem para operações de ordens em mini contratos. Sinta-se à vontade para modificar e aprimorar o código conforme suas necessidades.
