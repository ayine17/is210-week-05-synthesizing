#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sing multiple functions, chained together to reduce repetition."""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')



def fahrenheit_to_celsius(degrees):

    """ a function that convert temperature from fahrenheit to celsius.

    args:
        degrees (mixed):  fahrenheit value to be converted to celsius
    return:
        Return the temperature as a decimal in degrees celsius
    Example:
        >>> fahrenheit_to_celsius(212)
        decimal.Decimal('100')
        fahrenheit_to_celsius(200)
        Decimal('93')
        fahrenheit_to_celsius(373)
        Decimal('189')
    """
    celsius = ((decimal.Decimal(degrees) - 32) * 5) / 9

    return celsius


def celsius_to_kelvin(degrees):

    """ function that convert temperature from  celsius to kelvin.
    args:
        degrees (mixed): celsius value to be converted to kelvin
    return:
        Return the temperature as a decimal in degrees kelvin

    Example:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> celsius_to_kelvin(200)
        Decimal('473.15')
    """
    kelvin = decimal.Decimal(ABSOLUTE_DIFFERENCE) + degrees
    return kelvin


def fahrenheit_to_kelvin(degrees):

    """ a functionthat convert temperature from fahrenheit to kelvin
    Args:
        degrees (mixed): fahrenheit value to be converted to kelvin
    return:

    Examples:
       >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
       >>> fahrenheit_to_kelvin(100)
        Decimal('310.15')
    """
    celsius = fahrenheit_to_celsius(degrees)

    kelvin = celsius_to_kelvin(celsius)

    return kelvin
