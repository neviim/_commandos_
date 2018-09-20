# Fazendo um Web Scraping usando o BeautifulSoup

    ::: 1. Importe as bibliotecas necessárias:

        #importe a biblioteca usada para consultar uma URL
        import urllib.request
        #importe as funções BeautifulSoup para analisar os dados retornados do site
        from bs4 import BeautifulSoup
        #especifique o URL
        wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"
        #Consulte o site e retorne o html para a variável 'page'
        page = urllib.request.urlopen(wiki)
        #Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
        soup = BeautifulSoup(page, 'html5lib')


    ::: O BeautifulSoup pode nos ajudar a entrar nessas camadas e extrair o conteúdo com o find(). Nesse caso, eu pretendo simplesmente
        extrair uma lista de capitais de Estados do Brasil do Wikipédia, mas agora vamos simplesmente consultar <li class= "toclevel-2 tocsection-26">
        para pegar o Rio de Janeiro.

            #Insira a tag <li> e adicione sua classe
            list_item = soup.find('li', attrs={'class': 'toclevel-2 tocsection-26'})
            Depois que selecionarmos a tag, podemos obter os dados obtendo somente seu texto.

            #Separe o HTML do texto com o código abaixo
            name = list_item.text.strip()
            print(name)


    ::: Um teste usando BeautifulSoup

        import urllib.request
        from bs4 import BeautifulSoup

        wiki = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil'
        page = urllib.request.urlopen(wiki)
        soup = BeautifulSoup(page, 'html5lib')
        list_item = soup.find('li', attrs={'class': 'toclevel-2 tocsection-26'})
        name = list_item.text.strip()
        print(name)


    ::: Como fazer Web Scraping de uma Tabela?

        Primeiramente precisamos encontrar um site que contenha uma tabela com as capitais dos estados brasileiros. Por
        sorte achei outro site do Wikipédia com uma Tabela. Você vai precisar alterar somente essa parte do código, veja.

            Onde havia:

            wiki = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil'
            page = urllib.request.urlopen(wiki)
            Agora vai ser:

            wiki = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea'
            page = urllib.request.urlopen(wiki)
            Como estamos buscando uma tabela para extrair informações sobre as capitais dos estados brasileiros, devemos identificar tabela que contém no site da Wikipédia. Vamos escrever o comando para extrair informações em todas as tags da Tabela.

            all_table = soup.find_all('table')
            Para identificar a tabela correta, usaremos o atributo class da tabela para filtrar a tabela correta. No chrome, você pode verificar o nome da classe clicando com o botão direito do mouse na tabela desejada da página.

            Inspecione o elemento > Copie o nome da classe da lista.

            table = soup.find('table', class_='wikitable sortable')


            Agora, para acessar o valor de cada elemento, usaremos o método find (text = True para cada elemento. Vamos ver o código:

            A=[]
            B=[]
            C=[]
            D=[]
            E=[]


            for row in table.findAll("tr"): #para tudo que estiver em <tr>
                cells = row.findAll('td') #variável para encontrar <td>
                if len(cells)==5: #número de colunas
                    A.append(cells[0].find(text=True)) #iterando sobre cada linha
                    B.append(cells[1].find(text=True))
                    C.append(cells[2].find(text=True))
                    D.append(cells[3].find('a').text)
                    E.append(cells[4].find(text=True))
            Observação: Repare que na Coluna D eu tive que mudar o método, isso foi devido que nessa coluna contém a bandeira da capital (img) seguida de um link (a), tudo isso dentro de um <td>.

            Então tive que usar find('a').text para pegar somente o texto do link, que é a informação que eu desejo extrair, contém o nome da capital.

            import pandas as pd

            df = pd.DataFrame(index=A, columns=['Posição'])

            df['Posição']=A
            df['Estado']=B
            df['Código/IBGE']=C
            df['Capital']=D
            df['Área']=E

            df
            Por fim, temos a nossa Planilha toda organizada.
