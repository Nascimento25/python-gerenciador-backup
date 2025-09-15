import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta

# --- Configuração de Teste ---
HOME_DIR = Path.home()
TEST_BASE_DIR = HOME_DIR / "ambiente_de_teste_automação"

SOURCE_DIR = TEST_BASE_DIR / "backupsFrom"
DEST_DIR = TEST_BASE_DIR / "backupsTo"
LOG_DIR = TEST_BASE_DIR
DAYS_THRESHOLD = 3

def main():
    print("Iniciando o script de automação de backups...")

    SOURCE_DIR.mkdir(exist_ok=True)
    DEST_DIR.mkdir(exist_ok=True)

    log_from_path = LOG_DIR / "backupsFrom.log"
    log_to_path = LOG_DIR / "backupsTo.log"

    from_log_entries = []
    to_log_entries = []
    
    time_threshold = datetime.now() - timedelta(days=DAYS_THRESHOLD)

    print(f"Analisando arquivos em: {SOURCE_DIR}")
    for file_path in SOURCE_DIR.iterdir():
        if file_path.is_file():
            try:
                stats = file_path.stat()
                file_name = file_path.name
                file_size = stats.st_size
                creation_time = datetime.fromtimestamp(stats.st_ctime)
                mod_time = datetime.fromtimestamp(stats.st_mtime)

                log_entry = (
                    f"Nome: {file_name}, Tamanho: {file_size} bytes, "
                    f"Criação: {creation_time.strftime('%Y-%m-%d %H:%M:%S')}, "
                    f"Modificação: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
                from_log_entries.append(log_entry)

                if creation_time < time_threshold:
                    print(f"  -> Removendo arquivo antigo: {file_name}")
                    file_path.unlink()
                else:
                    print(f"  -> Copiando arquivo recente: {file_name} para {DEST_DIR}")
                    shutil.copy2(file_path, DEST_DIR)
                    to_log_entries.append(f"Arquivo copiado: {file_name}\n")

            except Exception as e:
                print(f"Ocorreu um erro ao processar o arquivo {file_path}: {e}")

    print(f"Salvando log de listagem em: {log_from_path}")
    with open(log_from_path, 'w', encoding='utf-8') as f:
        f.writelines(from_log_entries)

    print(f"Salvando log de cópias em: {log_to_path}")
    with open(log_to_path, 'w', encoding='utf-8') as f:
        f.writelines(to_log_entries)

    print("Script finalizado com sucesso!")

if __name__ == "__main__":
    main()