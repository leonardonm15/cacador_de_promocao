from datetime import datetime as dt
from caçador_de_promoção import web_scraper
from calendar import monthrange
from caçador_de_promoção import tt_bot
from time import sleep
from caçador_de_promoção import menu_lib

while True:
    year = dt.today().year
    month = dt.today().month
    day = dt.today().day
    hour = dt.today().hour
    minutes = dt.today().minute
    seconds = dt.today().second

    if hour == 19 and minutes == 00 and seconds == 0:
        web_scraper.manual_menu = 0
        if day == monthrange(year=year, month=month):  # month routine
            web_scraper.get_promos(2)
            tt_bot.thread_maker(f'Reprise das melhores do mês {month} de {year}')
            web_scraper.get_promos(1)
            tt_bot.thread_maker(f'Melhores pomoções do dia {day}/{month}/{year}')
            sleep(10)

        elif day == monthrange(year=year, month=month) and year == 12:  # year routine
            web_scraper.get_promos(3)
            tt_bot.thread_maker(f'Reprise das melhores promoções do ano de {year}')
            web_scraper.get_promos(1)
            tt_bot.thread_maker(f'melhores promoções do dia {day}/{month}/{year}')
            sleep(10)

        else:
            web_scraper.get_promos(1)  # daily routine
            tt_bot.thread_maker(f'melhores promoções do dia {day}/{month}/{year}')
            sleep(10)

    else:
        menu = menu_lib.Menu('Tweet promos: Day', 'Tweet promos: month', 'Tweet promos: year', 'Quit program')
        menu.interface()
        number = int(menu.input())
        if number == 0:
            web_scraper.get_promos(1)
            tt_bot.thread_maker(f'melhores promoções do dia {day}/{month}/{year}')
        if number == 1:
            web_scraper.get_promos(2)
            tt_bot.thread_maker(f'Reprise das melhores do mês {month} de {year}')
        if number == 2:
            web_scraper.get_promos(3)
            tt_bot.thread_maker(f'Reprise das melhores promoções do ano de {year}')
        if number == 3:
            print('saindo do programa')
            manual_menu = 0
            break
