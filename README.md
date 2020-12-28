# cacador_de_promo-ao
web scraper que recolhe informação das 5 melhores promoções do dia e joga no twitter

web_crapper -> retira as informações usando selenium, cria 2 listas, uma com nome e outra com os links das melhores promoções, zipa as listas(cria uma relação de paralelismo entre elas), e faz um arquivo json(data.json) com as 5 melhores

tt_bot -> faz uma thread no twitter com base na iteração do arquivo json

schedule -> sistema de verificação de horario para post no twitter e menu

menu_lib -> menu no terminal para operação manual do script caso necessário

as chaves da api foram mudadas
@promocaoBOT
qualquer coisa chama no discord ai Léu#1575
