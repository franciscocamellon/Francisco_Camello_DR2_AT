# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 04                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_04.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_04():
    """
    This function takes from the user a vector and prints your reverse order.
    """

    def __init__(self):
        """ Constructor. """
        self.input = []
        self.list = []

    def init_class(self):
        """ This function receives the input data from users. """
        while len(self.input) < 5:
            self.input.append(Validate().validate_values(
                ' Digite um número: ', zero=True))

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()
        self.list = self.input.copy()
        self.list.reverse()

    def print_result(self):
        """ This is a printer! It prints. """
        print('===' * 25, 'Questão 04'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print(
            '---' *
            25, '{0}A ordem inversa do vetor {1} é: {2}.'.format(
                ' '*2, self.input, self.list),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_04().print_result()
