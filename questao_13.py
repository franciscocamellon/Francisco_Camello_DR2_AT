# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 13                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_13.py                                   *
***************************************************************************/
"""
import requests
import re
from collections import Counter
from bs4 import BeautifulSoup as bs


class Questao_13():
    """ This function draws squares side by side. """

    def __init__(self):
        """ Constructor. """
        self.words = 0
        self.ladies = 0
        self.words_list = []
        self.only_once = []

    def init_class(self):
        """ This function receives the input data from users. """
        self.request = requests.get('http://brasil.pyladies.com/about')
        self.request.encoding = self.request.apparent_encoding
        self.soup = bs(self.request.text, 'lxml')
        for item in self.soup.html.body.article.find_all('div'):
            self.words_list = [re.sub('\W+', '', word).lower()
                               for word in item.text.split()]
        self.words = len(self.words_list)

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()
        word_dict = dict(Counter(self.words_list))
        self.ladies = word_dict['ladies']
        for key, value in word_dict.items():
            if value == 1:
                self.only_once.append(key)

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 13'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25,
              '{}Existem {} palavras no conteúdo sobre as PyLadies, das quais\n {} aparecem uma única vez, enquanto que a palavra ladies é\n repetida {} vezes.\n'.format(
                  ' ', self.words, len(self.only_once), self.ladies),
              'Esta é a lista das palavras que ocorrem uma única vez no conteúdo:', sep="\n")
        for word in self.words_list:
            print(word)

        print('---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_13().print_result()
