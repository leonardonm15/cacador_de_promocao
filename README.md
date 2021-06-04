# cacador_de_promo-ao
web scraper que recolhe informação das 5 melhores promoções do dia e joga no twitter

web_crapper -> retira as informações usando selenium, cria 2 listas, uma com nome e outra com os links das melhores promoções, zipa as listas(cria uma relação de paralelismo entre elas), e faz um arquivo json(data.json) com as 5 melhores

tt_bot -> faz uma thread no twitter com base na iteração do arquivo json

schedule -> sistema de verificação de horario para post no twitter e menu

menu_lib -> menu no terminal para operação manual do script caso necessário

as chaves da api foram mudadas | 
@promocaoBOT no twitter, pra ver como ficou o resultado final | 
qualquer coisa chama no discord ai Léu#1575 | 

---------------------------------------------------------------------------------------------

web scrapper that grabs information at pelando.com and show it on twitter

files: 

  web_scrapper -> grabs the information and create 2 lists, une with the links and the other with the best promotions, zips it togueder and creates a json file with it
  
  tt_bot -> makes the thread based on the json
  
  schedule -> makes sure everything will work at the right time
 
  menu_lib -> manual terminal in case something goes wrong
  
  the api key was changed | 
  acess @pomocaoBOT to check it out | 
  anything u want to talk about the project ? reach me out on discord Léu#1575 | 
