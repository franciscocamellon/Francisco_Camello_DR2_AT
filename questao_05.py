# -*- coding: utf-8 -*-
"""
/******************************* ASSESMENT *********************************
*    Questao 05                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_05.py                                   *
***************************************************************************/
"""

from validation import Validate


class Questao_05():
    """
    Doscstring.
    """

    def __init__(self):
        """ Constructor. """

    def init_class(self):
        """ This function receives the input data from users. """

    def process_data(self):
        """ This function divides the input tuple by half. """

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 05'.center(75),
              '===' * 25, sep='\n')
        self.process_data()
        print(
            '---' * 25, 'ANULADA'.center(75),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_05().print_result()
