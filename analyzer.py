from syntax_analyzer import SintaxAnalyzer
import lexical_analyzer as la
from os import error
import os, os.path


def main():
    folder_out = os.getcwd() + '/output/'
    # apaga arquivos da pasta de output, se houver
    for file in os.listdir(folder_out):
        file_path = os.path.join(folder_out, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(e)
            
    index = 1
    folder_in = os.getcwd() + '/input/'
    while os.path.isfile(folder_in + f'entrada{index}.txt'):
        #sub-rotina lexico
        tokens = la.scanner(folder_in, folder_out, index)
        #print(tokens)

        # execução do analisador sintatico
        print(f'\nentrada{index}.txt')
        ans = SintaxAnalyzer(tokens).run()
        print(f'resultado analise sintatica: {ans}')
        index = index+1


__init__ = main()