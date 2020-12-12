# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 11                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_11.py                                   *
***************************************************************************/
"""
import requests
from bs4 import BeautifulSoup


class Questao_12():
    """ This function draws a triangle with side size given by the user. """

    def __init__(self):
        """ Constructor. """
        self.request = requests.get(
            'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html')
        self.states = ['df', 'mt', 'go', 'ms']
        self.data = ''
        self.usr_choice = ''

    def init_class(self):
        """ This function receives the input data from users. """

        self.request.encoding = self.request.apparent_encoding
        bs = BeautifulSoup(self.request.text, "lxml")
        self.table = bs.html.body.find('div', {'class': 'tabela'})
        self.lines = bs.html.body.article.find_all('div', {'class': 'linha'})

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()
        finish = False
        while not finish:
            self.data = input("Informe a sigla de um estado do Centro Oeste: ")
            for line in self.lines:
                _state = line.find_all('div', {'class': 'celula'})[0].text
                if self.data == _state.lower():
                    self.usr_choice = line.text
                    finish = True
                # else:
                #     finish = True
                #     print(
                #     'A sigla informada não corresponde a nenhum estado do centro oeste!')
                #     break

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 11'.center(75), '===' * 25, sep='\n')
        self.init_class()
        print('Conteúdo da tabela:\n {} '.format(
            self.table.get_text()), '---' * 25, sep='\n')
        self.process_data()
        print('---' * 25,
              ' {} '.format(self.usr_choice),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_12().print_result()
