import argparse
import logging
import os
from utils import load_csv

def setup_logging(verbose: bool):
    os.makedirs("../logs", exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("../logs/execucao.log", mode='w'),
            logging.StreamHandler()
        ]
    )

def parse_args():
    parser = argparse.ArgumentParser(description="Script para análise de CSVs")
    
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Caminho para o arquivo CSV de entrada."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Se definido, mostrará logs de debug mais detalhados."
    )

    return parser.parse_args()

def main():
    args = parse_args()
    setup_logging(args.verbose)

    logging.info("Início da execução")
    df = load_csv(args.input)
    # Outras operações aqui
    logging.info("Fim da execução")

if __name__ == "__main__":
    main()
