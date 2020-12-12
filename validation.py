# -*- coding: utf-8 -*-
""" Validate exceptions """
import re


class Custom_Error(Exception):
    """ Handle custom exceptions. """

    def __init__(self):
        super().__init__()


class Less_Than_Zero(Custom_Error):
    """ Raised when the input value is less than zero. """
    pass


class Zero(Custom_Error):
    """ Raised when the input value is equal zero. """
    pass


class Equal_Length(Custom_Error):
    """ Raised when the input value is not an integer. """
    pass


class String(Custom_Error):
    """ Raised when the error involves strings. """
    pass


class Not_Found(Custom_Error):
    """ Raised when the input value is not found. """
    pass


class Validate(Custom_Error):

    def validate_value_tuple(self, title, _tuple):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = input(title)
                for i in range(len(_tuple)):
                    if re.search(value, _tuple[i], re.IGNORECASE):
                        return value
                else:
                    raise Not_Found
                break
            except ValueError:
                print('{}Erro desconhecido, tente novamente!'.format(' '*3))
            except Not_Found:
                print('{}Erro! O elemento digitado não pertence à tupla!'.format(' '*3))

    def validate_values(self, title, zero=True):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = int(input(title))
                if value < 0:
                    raise Less_Than_Zero
                elif value == 0 and zero == False:
                    raise Zero
                else:
                    return value
                break
            except ValueError:
                print('{}Erro! Digite um número inteiro!'.format(' '*3))
            except Less_Than_Zero:
                print('{}Erro! Digite um número maior que zero!'.format(' '*3))
            except Zero:
                print('{}Erro! Digite um número diferente de zero!'.format(' '*3))

    def validate_strings(self, title, length):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = str(input(title))
                if len(value) == length:
                    raise Equal_Length
                elif len(value) < length:
                    raise String
                else:
                    return value
                break
            except ValueError:
                print('{}Erro! Digite uma string!'.format(' '*3))
            except String:
                print('{}Erro! String tem menos de {} caracteres!'.format(
                    length, ' '*3))
            except Equal_Length:
                print(
                    '{}Aviso! Tamanho da string igual ao número, nenhuma mudança será percebida!', sep="\n".format(' '*3))
