# CONTEÚDO CORRETO PARA O ARQUIVO: preparar_ambiente.py
from pathlib import Path
from datetime import datetime, timedelta
import os
import shutil

# Define o diretório base para todos os testes.
TEST_BASE_DIR = Path.home() / "ambiente_de_teste_automação"

# Define os diretórios específicos que o script principal vai usar.
SOURCE_DIR = TEST_BASE_DIR / "backupsFrom"
DEST_DIR = TEST_BASE_DIR / "backupsTo"

def criar_estrutura():
    """Cria a estrutura de diretórios necessária para os testes."""
    print(f"Criando estrutura de teste em: {TEST_BASE_DIR}")
    # parents=True cria os diretórios-pai se necessário.
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    print("-> Estrutura criada com sucesso.")

def criar_arquivos_de_teste():
    """Cria uma massa de dados de teste com datas variadas."""
    print("Criando arquivos de teste...")
    arquivos_para_criar = {
        "arquivo_recente_1.txt": datetime.now(), "log_de_hoje.log": datetime.now(),
        "dados_de_ontem.csv": datetime.now() - timedelta(days=1),
        "backup_antigo_1.zip": datetime.now() - timedelta(days=5),
        "relatorio_semanal.pdf": datetime.now() - timedelta(days=10),
    }
    for nome_arquivo, data in arquivos_para_criar.items():
        caminho_arquivo = SOURCE_DIR / nome_arquivo
        caminho_arquivo.touch()
        timestamp = data.timestamp()
        os.utime(caminho_arquivo, (timestamp, timestamp))
        print(f" -> Criado: {nome_arquivo} com data {data.strftime('%Y-%m-%d')}")

def limpar_ambiente():
    """Remove todos os arquivos e diretórios de teste para começar do zero."""
    if TEST_BASE_DIR.exists():
        print(f"Limpando ambiente de teste anterior em: {TEST_BASE_DIR}")
        shutil.rmtree(TEST_BASE_DIR)

if __name__ == "__main__":
    limpar_ambiente()
    criar_estrutura()
    criar_arquivos_de_teste()
    print("\nAmbiente de teste pronto!")