#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" extra credut five, temperation conversion"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def celsius_to_fahrenheit(degrees):
    """ a function that convert temperature from celsius to fahrenheit .

    args:
        degrees (mixed):  fahrenheit value to be converted to fahrenheit
    return:
        Return the temperature as a decimal in degrees fahrenheit
    Example:
        >>> celsius_to_fahrenheit(100)
        decimal.Decimal('212')
        >>> celsius_to_fahrenheit(93)
        Decimal('200')
        >>>celsius_to_fahrenheit(189)
        Decimal(373)
    """
    # C  x  9/5 + 32 = °F

    fahrenheit = ((decimal.Decimal(degrees) * 9) / 5) + 32

    return fahrenheit


def kelvin_to_celsius(degrees):
    """ function that convert temperature from  celsius to celsius.
    args:
        degrees (mixed): celsius value to be converted to celsius
    return:
        Return the temperature as a decimal in degrees celsius

    Example:
        >>> kelvin_to_celsius(372.15)
        Decimal('100')

        >>> kelvin_to_celsius(473.15)
        Decimal('200')
    """
    celsius = decimal.Decimal(degrees) - ABSOLUTE_DIFFERENCE
    return celsius


def kelvin_fahrenheit(degrees):
    """ a functionthat convert temperature from kelvin to fahrenheit
    Args:
        degrees (mixed): fahrenheit value to be converted to fahrenheit
    return:
         Return the temperature as a decimal in degrees fahrenheit

    Examples:
       >>> fahrenheit_to_kelvin(373.15)
        Decimal('212')
       >>> fahrenheit_to_kelvin(310.15)
        Decimal('100')
    """

    celsiu = kelvin_to_celsius(degrees)

    fahrenheit = celsius_to_fahrenheit(celsiu)
    return fahrenheit
