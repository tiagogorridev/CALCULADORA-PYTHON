#importar

import flet as ft
from flet import colors
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.WHITE, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.BLACK, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE}
]

#criar função

def main(page: ft.Page):
    page.bgcolor = '#000' #cor preta
    page.windowresizable = False #não permite redirecionamento da tela
    page.window_width = 250
    page.window_height = 380
    page.window_always_on_top = True
    page.title = 'Calculadora'

    result = ft.Text(value = '0', color = colors.WHITE, size = 20)

    def calculate(operator, value_at):
        
        try:
            value = eval(value_at) #eval = calcula

            if operator == '%':
                value /= 100
            elif operator == '±':
                value = -value
        except:
            return 'ERROR'
        
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')

    def select(e): #mudar o cursor como elemento clicavel
        value_at = result.value if result.value != '0' else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value #contatenar numeros
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/','*','-','+','.'):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=','%','±'):
                value = calculate(operator=value[-1], value_at=value_at)

        result.value = value
        result.update()
    

    display = ft.Row(
        width = 250,
        controls = [result],
        alignment = 'end' #numero no canto direito
    )

    #criação do botão

    btn = [ft.Container( 
            content = ft.Text(value=btn['operador'], color=btn['fonte']),
            width = 50,
            height = 50,
            bgcolor = btn['fundo'],
            border_radius = 100,
            alignment = ft.alignment.center,
            on_click = select
        ) for btn in botoes]


    keyboard = ft.Row(
        width = 250,
        wrap = True, #quebra pra linha de baixo
        controls = btn,
        alignment = 'end'
    )

    page.add(display, keyboard)
ft.app(target = main)