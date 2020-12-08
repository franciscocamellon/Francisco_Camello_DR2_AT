# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 06                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_06.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_06():
    """ This fuction draws the angles by 15° from a circle. """

    def __init__(self):
        """ Constructor. """
        self.input = []
        self.list = []
        self.tuple = ()

    def init_class(self):
        """ This function receives the input data from users. """
        finish = False
        while not finish:
            _input = (Validate().validate_values(
                ' Digite um número ou 00 para sair: ', zero=True))
            if _input == 00:
                finish = True
            else:
                self.input.append(_input)

    def process_data(self):
        """ This function process the input data from init_class. """
        even_index = []
        self.init_class()
        for i in self.input:
            if i % 2 != 0:
                self.list.append(i)
        for i in self.input:
            if self.input.index(i) % 2 == 0:
                even_index.append(i)
        self.tuple = tuple(even_index)

    def print_result(self):
        """ This is a printer! It prints. """
        print('===' * 25, 'Questão 04'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print(
            '---' *
            25, '{0}Lista de números ímpares {1}\n \
            {0} Tupla com os números nas posições pares: {2}.'.format(' '*2, self.list, self.tuple),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_06().print_result()
