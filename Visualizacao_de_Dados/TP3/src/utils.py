import logging
import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    """Carrega um arquivo CSV e realiza alguns logs básicos."""
    try:
        df = pd.read_csv(filepath)
        logging.info(f"Arquivo {filepath} carregado com sucesso.")
        logging.debug(f"Shape: {df.shape}")
        logging.debug(f"Colunas: {df.columns.tolist()}")
        logging.debug(f"Resumo:\n{df.describe(include='all')}")
        return df
    except Exception as e:
        logging.error(f"Erro ao carregar {filepath}: {e}")
        raise
