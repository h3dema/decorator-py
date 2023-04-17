from datetime import datetime
import uuid
import time
import os


def log_parametros(func):

    def wrapper(*args, **kwargs):
        print("*" * 40, "\n")
        print(f"Função iniciada em {datetime.now().strftime('%H:%M:%S')}")
        t0 = time.time()
        ret = func(*args, **kwargs)
        _dur = time.time() - t0
        print(f"Execução em {_dur} segundos.\n")
        print("*" * 40)
        return ret

    return wrapper

@log_parametros
def gen_unique_fname(fname: str) -> str:
    """
        esta função recebe um nome de arquivo no formato "nome_arquivo.extensao"
        e retorna "nome_arquivo_xxxx-xxxx--xxxx.extensao"
    """
    _id = str(uuid.uuid1())
    dirname, basename = os.path.dirname(fname), os.path.basename(fname)
    idx = basename.rfind(".")
    basename = basename[:idx] + "-" +_id + basename[idx:] if idx >= 0 else basename + "-" + _id
    new_fname = os.path.join(dirname, basename)
    return new_fname


if __name__ == "__main__":
    # passamos em fname a base do nome do arquivo
    print("Nome do arquivo:", gen_unique_fname(fname="image.png"))

    print("Nome do arquivo:", gen_unique_fname(fname="image"))
