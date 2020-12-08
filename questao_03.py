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
        self.num = 0

    def init_class(self):
        """ This function receives the input data from users. """
        number = Validate().validate_values(' Digite um número: ')
        return number

    def process_data(self, a, b):
        """ This function process the input data from init_class. """
        self.num = a**b

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 03'.center(75), '===' * 25, sep='\n')
        a = self.init_class()
        b = self.init_class()
        self.process_data(a, b)
        print(
            '---' *
            25, ' A potência de {0} por {1} é {2}!'.format(a, b, self.num),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_03().print_result()
