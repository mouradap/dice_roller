from utils.roller import Roller
import sys


if __name__ == "__main__":
    n_lados = int(sys.argv[1])
    n_jogadas = int(sys.argv[2])

    dado1 = Roller(n_lados = n_lados)
    print(f"O dado possui {len(dado1.lados)} lados.")

    dado1.jogar(n_jogadas)