# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 03                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_03.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_03():
    """
    This function gets two numbers from user and calculates power
    between numbers.
    """

    def __init__(self):
        """ Constructor """
        self.power = 0
        self.components = {' Digite a base: ': 0, ' Digite o expoente: ': 0}

    def init_class(self):
        """ This function receives the input data from users. """
        for k in self.components.keys():
            self.components[k] = Validate().validate_values(k)

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()
        self.power = self.components[' Digite a base: ']**self.components[' Digite o expoente: ']

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 03'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print(
            '---' *
            25, ' A potência de {0} elevado a {1} é {2}!'.format(
                self.components[' Digite a base: '], self.components[' Digite o expoente: '], self.power),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_03().print_result()
