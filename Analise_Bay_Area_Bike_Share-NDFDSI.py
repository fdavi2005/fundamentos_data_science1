
# coding: utf-8

# # Análise da Bay Area Bike Share
# 
# ## Introdução
# 
# > **Dica**: Seções citadas como esta fornecerão instruções úteis sobre como navegar e usar um notebook do iPython.
# 
# [Bay Area Bike Share](http://www.bayareabikeshare.com/) é uma empresa que oferece aluguel de bicicletas on-demand para clientes em San Francisco, Redwood City, Palo Alto, Mountain View e San Jose. Os usuários podem desbloquear bicicletas de uma variedade de estações em cada cidade, e devolvê-las em qualquer estação dentro da mesma cidade. Os usuários pagam o serviço por meio de assinatura anual ou pela compra de passes de 3 dias ou 24 horas. Os usuários podem fazer um número ilimitado de viagens. Viagens com menos de trinta minutos de duração não têm custo adicional; Viagens mais longas incorrem em taxas de horas extras.
# 
# Neste projeto, você vai se colocar no lugar de um analista de dados realizando uma análise exploratória sobre os dados. Você vai dar uma olhada em duas das principais partes do processo de análise de dados: limpeza de dados e análise exploratória. Mas antes que você comece a olhar os dados, pense algumas perguntas que você pode querer fazer sobre os dados. Considere, por exemplo, se você estivesse trabalhando para Bay Area Bike Share: que tipo de informação você gostaria de saber a fim de tomar decisões de negócios mais inteligentes? Ou você pode pensar se você fosse um usuário do serviço de compartilhamento de bicicletas. Que fatores podem influenciar a maneira como você gostaria de usar o serviço?

# # Sobre este projeto
# 
# Este é o seu primeiro projeto com a Udacity. Queremos fazer com que você treine os conhecimentos aprendidos durante o curso e que entenda algumas das dificuldades que pode ter quando for aplicar os mesmos. 
# 
# Os principais pontos que serão verificados neste trabalho:
# 
# - Criação de dicionários e mapeamento de variáveis
# - Uso de lógica com o `if`
# - Manipulação de dados e criação de gráficos simples com o `Pandas`
# 
# *Como conseguir ajuda*: Sugerimos que tente os seguintes canais, nas seguintes ordens:
# 
# | Tipo de dúvida\Canais         	| Google 	| Fórum 	| Slack 	| Email 	|
# |-------------------------------	|--------	|-------	|-------	|-------	|
# | Programação Pyhon e Pandas    	| 1      	| 2     	| 3     	|       	|
# | Requisitos do projeto         	|        	| 1     	| 2     	| 3     	|
# | Partes específicas do Projeto 	|        	| 1     	| 2     	| 3     	|
# 
# Os endereços dos canais são:
# 
# - Fórum: https://discussions.udacity.com/c/ndfdsi-project
# - Slack: [udacity-br.slack.com](https://udacity-br.slack.com/messages/C5MT6E3E1)
# - Email: data-suporte@udacity.com
# 
# **Espera-se que o estudante entregue este relatório com:**
# 
# - Todos os TODO feitos, pois eles são essenciais para que o código rode corretamente
# - Todas as perguntas respondidas. Elas estão identificadas como PERGUNTA em letras grandes.
# 
# Para entregar este projeto, vá a [sala de aula](https://classroom.udacity.com/nanodegrees/nd110/parts/05e3b1e2-ff23-488f-aaec-caba12ad8ed3/modules/519425b3-ee26-4ecd-a952-f689decef51c/lessons/47133342-a203-4df9-9b9e-69b04408e089/project) e submeta o seu `.ipynb` e um pdf, zipados.

# # Pergunta 1
# Escreva pelo menos duas perguntas que você acha que poderiam ser respondidas usando os dados.

# **Resposta**:  
# 
# 1 - As estações do ano influenciam na utilização dos serviços?
# 
# 2 - Qual a frequência média de utilização do serviço pelo mesmo usuário?
# 
# > **Dica**: Se você clicar duas vezes nesta célula, você verá o texto se alterar removendo toda a formatação. Isso permite editar este bloco de texto. Este bloco de texto é escrito usando [Markdown](http://daringfireball.net/projects/markdown/syntax), que é uma forma de formatar texto usando cabeçalhos, links, itálico e muitas outras opções. Pressione **Shift** + **Enter** ou **Shift** + **Retorno** para voltar a mostrar o texto formatado.

# ## Usando visualizações para comunicar resultados em dados
# 
# Como um analista de dados, a capacidade de comunicar eficazmente resultados é uma parte fundamental do trabalho. Afinal, sua melhor análise é tão boa quanto sua capacidade de comunicá-la.
# 
# Em 2014, Bay Area Bike Share realizou um [Open Data Challenge](http://www.bayareabikeshare.com/datachallenge-2014) para incentivar os analistas de dados a criar visualizações com base em seu conjunto de dados aberto. Você criará suas próprias visualizações neste projeto, mas primeiro, dê uma olhada no [vencedor de inscrições para Melhor Análise](http://thfield.github.io/babs/index.html) de Tyler Field. Leia todo o relatório para responder à seguinte pergunta:

# # Pergunta 2
# Que visualizações você acha que fornecem as idéias mais interessantes? 
# 
# Selecione duas visualizações de Tyler que forneçam idéias interessantes e que respondam alguma das perguntas da análise de Tyler.

# ** Resposta **: 
# 
# 1 - Gráfico que mostra a comparação por dia entre tipos de usuários e os dias da semana ("Rides by Weekday")
# 
# 2 - Mapa de calor que mostra a quantidade de viagem por rotas (Estação de partida e de chegada - "Heatmap diagram of systemwide rides")

# # Pergunta 2.1
# 
# Quais são as perguntas que foram respondidas com suas visualizações? Porque você as escolheu?

# ** Resposta **: 
# 
# 1 - Respondeu claramente qual o tipo de usuário que mais utiliza o serviço durante a semana e qual a finalidade de uso. Ficou claro que grande parte dos usuários registrados usa os serviços para ir e voltar para o trabalho diariamente. Eu escolhi essa visualização porque ela é simples e comunica diretamente os resultados da análise
# 
# 2 - Respondeu claramanet as rotas mais utilizadas e complementou a visualização anterior. Através dessa visualização foi possível identificar as estações e rotas mais utilizadas e dessa forma inferir o objetivo do cliente no uso do serviço. Escolhi essa visualização pois através dessa análise Tyler foi capaz de sugerir melhorias para o serviço prestado.

# ## Data Wrangling (Limpeza de Dados)
# 
# Agora é a sua vez de explorar os dados. Os [dados abertos](http://www.bayareabikeshare.com/open-data) do Ano 1 e do Ano 2 da página Bay Area Bike Share já foram fornecidos com os materiais do projeto; você não precisa baixar nada extra. O dado vem em três partes: a primeira metade do Ano 1 (arquivos a partir de `201402`), a segunda metade do Ano 1 (arquivos a partir de `201408`) e todo o Ano 2 (arquivos a partir de `201508`). Existem três arquivos de dados principais associados a cada parte: dados de viagem que mostram informações sobre cada viagem no sistema (`*_trip_data.csv`), informações sobre as estações no sistema (`*_station_data.csv`) e dados meteorológicos diários para cada cidade no sistema (`*_weather_data.csv`).
# 
# 
# Ao lidar com muitos dados, pode ser útil começar trabalhando com apenas uma amostra dos dados. Desta forma, será muito mais fácil verificar se nossos passos da limpeza de dados (Data Wrangling) estão funcionando, pois nosso código demorará menos tempo para ser concluído. Uma vez que estamos satisfeitos com a forma como funcionam as coisas, podemos configurar o processo para trabalhar no conjunto de dados como um todo.
# 
# Uma vez que a maior parte dos dados está contida na informação de viagem, devemos segmentar a procura de um subconjunto dos dados da viagem para nos ajudar a seguir em frente. Você começará olhando apenas o primeiro mês dos dados da viagem de bicicleta, de 2013-08-29 a 2013-09-30. O código abaixo selecionará os dados da primeira metade do primeiro ano, então escreverá o valor do primeiro mês de dados para um arquivo de saída. Este código explora o fato de que os dados são classificados por data (note que os dois primeiros dias são classificados por tempo de viagem, em vez de serem completamente cronológicos).
# 
# Primeiro, carregue todos os pacotes e funções que você usará em sua análise executando a primeira célula de código abaixo. Em seguida, execute a segunda célula de código para ler um subconjunto do primeiro arquivo de dados de viagem e escrever um novo arquivo contendo apenas o subconjunto em que inicialmente estamos interessados.
# 
# > **Dica**: Você pode executar uma célula de código ou renderizar um texto em Markdown clicando na célula e usando o atalho do teclado **Shift** + **Enter** ou **Shift** + **Return**. Alternativamente, uma célula de código pode ser executada usando o botão **Play** na barra de ferramentas (a cima no IPython Notebook) depois de selecioná-la. Enquanto a célula estiver em execução, você verá um asterisco na mensagem à esquerda da célula, ou seja, `In [*]:`. O asterisco mudará para um número para mostrar que a execução foi concluída, Ex: `In [1]`. Se houver saída, ele aparecerá como `Out [1]:`, com um número apropriado para coincidir com o número de "In".

# In[1]:


# Importa todas as bibliotecas necessárias
get_ipython().run_line_magic('matplotlib', 'inline')
import csv
from datetime import datetime
import numpy as np
import pandas as pd
from babs_datacheck import question_3
from babs_visualizations import usage_stats, usage_plot
from IPython.display import display
import matplotlib.pyplot as plt


# In[2]:


# definição dos arquivos
file_in  = '201402_trip_data.csv'
file_out = '201309_trip_data.csv'

with open(file_out, 'w') as f_out, open(file_in, 'r') as f_in:
    # configura o leitor de csv
    in_reader = csv.reader(f_in)
    out_writer = csv.writer(f_out)

    # escreve os dados no arquivo de saída até que a data limite seja atingida
    while True:
        datarow = next(in_reader)
        # data de início de das viagens na terceira coluna no formato 'm/d/yyyy HH:MM'
        if datarow[2][:9] == '10/1/2013':
            break
        out_writer.writerow(datarow)


# ### Condensando os Dados de Viagem
# 
# O primeiro passo é analisar a estrutura do conjunto de dados para ver se há alguma limpeza de dados que devemos realizar. A célula abaixo irá ler o arquivo de dados amostrado que você criou na célula anterior. Você deve imprimir as primeiras linhas da tabela.

# In[3]:


sample_data = pd.read_csv('201309_trip_data.csv')

# TODO: escreva o código para visualizar as primeiras linhas
sample_data.head()


# Nesta exploração, vamos nos concentrar nos fatores nos dados da viagem que afetam o número de viagens realizadas. Vamos focar em algumas colunas selecionadas: a duração da viagem (trip duration), hora de início (start time), terminal inicial (start terminal), terminal final (end terminal) e tipo de assinatura. O tempo de início será dividido em componentes de ano, mês e hora. Também adicionaremos uma coluna para o dia da semana e resumiremos o terminal inicial e final para ser a _cidade_ de início e fim.
# 
# Vamos primeiro abordar a última parte do processo de limpeza. Execute a célula de código abaixo para ver como as informações da estação estão estruturadas e observe como o código criará o mapeamento estação-cidade. Observe que o mapeamento da estação está configurado como uma função, `create_station_mapping()`. Uma vez que é possível que mais estações sejam adicionadas ou removidas ao longo do tempo, esta função nos permitirá combinar as informações da estação em todas as três partes dos nossos dados quando estivermos prontos para explorar tudo.

# In[4]:


# Mostra as primeiras linhas do arquivo de dados das estações
station_info = pd.read_csv('201402_station_data.csv')
station_info.head()


# Preencha a função abaixo de forma que a função retorne um mapeamento entre o id da estação (`station_id`) e a cidade em que ela se encontra (`landmark`).

# In[5]:


# esta função será usada mais tarde para criar o mapeamento entre station e cidade
def create_station_mapping(station_data):
    """
    Cria um mapeamento (também conhecido como de-para) entre a estação 
    e a cidade
    """
    # TODO: Inicie esta variável de maneira correta.
    station_map = {}
    for data_file in station_data:
        with open(data_file, 'r') as f_in:
            # configura o objeto csv reader - note que está sendo usado o DictReader,
            # que usa a primeira linha do arquivo como cabeçalho e cria as chaves
            # do dicionário com estes valores.
            weather_reader = csv.DictReader(f_in)

            for row in weather_reader:
                # TODO: faça o mapeamento aqui
                station_map[int(row['station_id'])]= row['landmark']
    return station_map


# In[6]:


test_file = ['201402_station_data.csv']
test_station_map = create_station_mapping(test_file)
test_station_map


# In[7]:


#sample_data['Start Terminal'][0]
test_station_map[sample_data['Start Terminal'][0]]


# Você pode agora usar o mapeamento para condensar as viagens para as colunas selecionadas acima. Isto acontecerá na função abaixo `summarise_data()`. Nela o módulo `datetime` é usado para fazer o **p**arse do tempo (timestamp) em formato de strings no arquivo original para um objeto usando a função `strptime`. Este objeto permitirá a conversão para outros **f**ormatos de datas usando a função `strftime`. O objeto possui também outras funções que facilitam a manipulação dos dados. Veja [este tutorial](http://usandopython.com.br/manipulando-data-hora-python-datetime/) para entender um pouco melhor como trabalhar com a biblioteca.
# 
# Você precisa concluir duas tarefas para completar a função `summarise_data()`. Inicialmente, você deverá realizar a operação de converter a duração das viagens de segundos para minutos. Esta é muito fácil, pois existem 60 segundos em um minuto!
# 
# Na sequência, você deve criar colunas para o ano, mês, hora e dia da semana. Verifique o tutorial acima ou a [documentação para o objeto de datetime no módulo datetime](https://docs.python.org/2/library/datetime.html#datetime-objects). 
# 
# ** TODO: Encontre os atributos e métodos necessários para poder completar o código abaixo **
# 
# *Dica*: Você pode abrir uma nova caixa para testar um pedaço do código ou verificar uma variável que seja global. Caso ela esteja dentro da função, você também pode usar o comando `print()` para imprimi-la e ajudar no Debug.

# In[8]:


sample_data.head()


# In[9]:


sample_data.groupby('Subscription Type')['Duration'].count()


# In[10]:


def summarise_data(trip_in, station_data, trip_out):
    """
    Esta função recebe informações de viagem e estação e produz um novo
    arquivo de dados com um resumo condensado das principais informações de viagem.Os 
    argumentos trip_in e station_data serão listas de arquivos de dados para
    as informações da viagem e da estação enquanto trip_out especifica o local
    para o qual os dados sumarizados serão escritos.
    """
    # gera o dicionário de mapeamento entre estações e cidades
    station_map = create_station_mapping(station_data)
    
    with open(trip_out, 'w') as f_out:
        # configura o objeto de escrita de csv       
        out_colnames = ['duration', 'start_date', 'start_year',
                        'start_month', 'start_hour', 'weekday',
                        'start_city', 'end_city', 'subscription_type']        
        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        trip_writer.writeheader()
        
        for data_file in trip_in:
            with open(data_file, 'r') as f_in:
                # configura o leitor do csv
                trip_reader = csv.DictReader(f_in)

                # processa cada linha lendo uma a uma
                for row in trip_reader:
                    new_point = {}
                    
                    # converte a duração de segundos para minutos.
                    ### TODO: Pergunta 3a: Adicione uma operação matemática       ###
                    ### para converter a duração de segundos para minutos.  ###
                    new_point['duration'] = int(row['Duration'])/60
                                     
                    
                    # reformate strings com datas para múltiplas colunas
                    ### TODO: Pergunta 3b: Preencha os __ abaixo para criar os        ###
                    ### campos experados nas colunas (olhe pelo nome da coluna) ###
                    trip_date = datetime.strptime(row['Start Date'], '%m/%d/%Y %H:%M')
                    new_point['start_date']  = trip_date.date()
                    new_point['start_year']  = trip_date.year
                    new_point['start_month'] = trip_date.month
                    new_point['start_hour']  = trip_date.hour
                    new_point['weekday']     = trip_date.weekday()
                    
                    # TODO: mapeia o terminal de inicio e fim com o a cidade de inicio e fim
                    new_point['start_city'] = station_map[int(row['Start Terminal'])]
                    new_point['end_city'] = station_map[int(row['End Terminal'])]
                    
                    # TODO: existem dois nomes diferentes para o mesmo campo. Trate cada um deles.
                    if 'Subscription Type' in row:
                        new_point['subscription_type'] = row['Subscription Type']
                    else:
                        new_point['subscription_type'] = row['Subscriber Type']

                    # escreve a informação processada para o arquivo de saída.
                    trip_writer.writerow(new_point)


# # Pergunta 3: 
# Execute o bloco de código abaixo para chamar a função `summarise_data()` que você terminou na célula acima. Ela usará os dados contidos nos arquivos listados nas variáveis `trip_in` e `station_data` e escreverá um novo arquivo no local especificado na variável `trip_out`. Se você executou a limpeza de dados corretamente, o bloco de código abaixo imprimirá as primeiras linhas do DataFrame e uma mensagem que verificando se as contagens de dados estão corretas.

# In[11]:


# processe os dados usando a função criada acima
station_data = ['201402_station_data.csv']
trip_in = ['201309_trip_data.csv']
trip_out = '201309_trip_summary.csv'
summarise_data(trip_in, station_data, trip_out)


# In[12]:


# Carregue os dados novamente mostrando os dados
## TODO: Complete o código para leitura dos dados no arquivo criado na função acima
sample_data = pd.read_csv('201309_trip_summary.csv')
display(sample_data.head())


# In[13]:


# Verifica o DataFrame contando o número de pontos de dados com as características de 
# tempo corretas.
question_3(sample_data)


# > **Dica**: se você salvar um notebook do jupyter, a saída dos blocos de código em execução também será salva. No entanto, o estado do seu arquivo será reiniciado uma vez que uma nova sessão será iniciada. Certifique-se de que você execute todos os blocos de código necessários da sessão anterior para restabelecer variáveis e funções antes de continuar de onde você deixou na última vez.

# ## Análise Exploratória de Dados 
# 
# Agora que você tem alguns dados salvos em um arquivo, vejamos algumas tendências iniciais nos dados. Algum código já foi escrito para você no script [babs_visualizations.py](babs_visualizations.py) para ajudar a resumir e visualizar os dados; Isso foi importado como as funções `usage_stats()` e `usage_plot()`. Nesta seção, vamos percorrer algumas das coisas que você pode fazer com as funções, e você usará as funções para você mesmo na última parte do projeto. Primeiro, execute a seguinte célula para carregar os dados. Depois preencha a célula abaixo com os comandos para verificar os dados básicos sobre os dados.

# In[14]:


trip_data = pd.read_csv('201309_trip_summary.csv')


# In[15]:


points = trip_data.shape[0]
points


# In[16]:


meantrip = trip_data['duration'].mean()
meantrip


# In[17]:


duration_qtiles = trip_data['duration'].quantile([.25, .5, .75]).as_matrix()


# In[18]:


durationqtiles0 = duration_qtiles[0]
durationqtiles0


# In[19]:


durationqtiles1 = duration_qtiles[1]
durationqtiles1


# In[20]:


durationqtiles2 = duration_qtiles[2]
durationqtiles2


# In[21]:


# TODO: preencha os campos com os dados de acordo com o print
print('Existem {:d} pontos no conjunto de dados'.format(points))
print('A duração média das viagens foi de {:.2f} minutos'.format(meantrip))
print('A mediana das durações das viagens foi de {:.2f} minutos'.format(durationqtiles1))

# TODO: verificando os quartis
duration_qtiles = trip_data['duration'].quantile([.25, .5, .75]).as_matrix()
print('25% das viagens foram mais curtas do que {:.2f} minutos'.format(durationqtiles0))
print('25% das viagens foram mais compridas do que {:.2f} minutos'.format(durationqtiles2))


# In[22]:


# execute este campo para verificar os seu processamento acima.
usage_stats(trip_data)


# Você deve ver que há mais de 27.000 viagens no primeiro mês e que a duração média da viagem é maior do que a duração mediana da viagem (o ponto em que 50% das viagens são mais curtas e 50% são mais longas). Na verdade, a média é maior que as durações de 75% das viagens mais curtas. Isso será interessante para ver mais adiante.
# 
# Vamos começar a ver como essas viagens são divididas por tipo de inscrição. Uma maneira fácil de construir uma intuição sobre os dados é traçá-los. 
# 
# Lembre-se que o Pandas possui maneiras de plotar os gráficos diretamente de um DataFrame. Para cada tipo de dados/análises se pode usar um tipo diferente de gráfico mais apropriado para a análise que se está fazendo.
# 
# Na caixa abaixo, faça um gráfico de viagens x tipo de subscrição do tipo barras.

# In[23]:


# TODO: plote um gráfico de barras que mostre quantidade de viagens por subscription_type
# lembrando que quando o comando .plot é usado, se pode escolher o tipo de gráfico usando 
# o parâmetro kind. Ex: plot(kind='bar')
trip_data.groupby('subscription_type')['duration'].count().plot(kind='bar',figsize=(8, 8));


# Para que você possa conferir se os seus gráficos estão corretos, usaremos a função `use_plot()`. O segundo argumento da função nos permite contar as viagens em uma variável selecionada, exibindo as informações em um gráfico. A expressão abaixo mostrará como deve ter ficado o seu gráfico acima.

# In[24]:


# como o seu gráfico deve ficar. Descomente a linha abaixo caso queira rodar este comando
usage_plot(trip_data, 'subscription_type')


# >*Nota*: Perceba que provavelmente o seu gráfico não ficou exatamente igual, principalmente pelo título e pelo nome dos eixos. Lembre-se, estes são detalhes mas fazem toda a diferença quando você for apresentar os gráficos que você analisou. Neste Nanodegree não focaremos nestas questões, mas tenha em mente que ter os gráficos acertados é de extrema importância.

# Parece que existe 50% mais viagens feitas por assinantes (subscribers) no primeiro mês do que outro tipos de consumidores. Vamos tentar uma outra variável. Como é a distribuição da duração das viagens (trip duration)?

# In[25]:


# TODO: Faça um gráfico baseado nas durações
trip_data['duration'].hist(figsize=(8, 8));


# In[26]:


# rode este comando abaixo caso esteja em dúvida quanto ao resultado esperado
usage_plot(trip_data, 'duration')


# Parece muito estranho, não é? Dê uma olhada nos valores de duração no eixo x. A maioria dos passeios deve ser de 30 minutos ou menos, uma vez que há taxas de excesso de tempo extra em uma única viagem. A primeira barra abrange durações de até 1000 minutos, ou mais de 16 horas. Com base nas estatísticas que obtivemos do `use_stats()`, deveríamos ter esperado algumas viagens com durações muito longas que levem a média a ser muito superior à mediana: o gráfico mostra isso de forma dramática, mas inútil.
# 
# Ao explorar os dados, muitas vezes você precisará trabalhar com os parâmetros da função de visualização para facilitar a compreensão dos dados. É aqui que os filtros vão ajudar você. Comecemos por limitar as  viagens de menos de 60 minutos.

# In[27]:


# TODO: faça um gráfico de barras para os dados com duração inferior a 60 minutos.
trip_data_60min = trip_data.query('duration < 60')
trip_data_60min['duration'].hist(figsize=(8, 8));


# In[28]:


# descomente a linha abaixo para verificar o gráfico esperado.
usage_plot(trip_data, 'duration', ['duration < 60'])


# Isso está bem melhor! Você pode ver que a maioria das viagens têm menos de 30 minutos de duração, mas que você pode fazer mais para melhorar a apresentação. Uma vez que a duração mínima não é 0, a barra da esquerda está ligeiramente acima de 0. Nós queremos saber onde existe um limite perto dos 30 minutos, então ficará mais agradável se tivermos tamanhos de intervalos (bin sizes) e limites dos intervalos que correspondam a alguns minutos. 
# 
# Felizmente, o Pandas e o Matplotlib te dão a opção de resolver ester problemas. Uma das maneiras de fazê-lo é definindo qual o intervalo no eixo x (parâmetro range) e quantos intervalos desejamos (bins).
# 
# No campo abaixo, faça o ajuste do gráfico para que os limites das barras se encontrem nas extremidades e que as barras tenham tamanho 5 (0, 5, 10, 15, etc). Se precisar, use a [documentação](http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist).

# In[29]:


# faça o gráfico ajustado que começará no 0 e terá o bin size de 5
trip_data_60min['duration'].hist(bins=12,range=(0,60),figsize=(8, 8));


# In[30]:


# rode esta linha para verificar como deve ficar o seu gráfico
usage_plot(trip_data, 'duration', ['duration < 60'], boundary = 0, bin_width = 5)


# Pequenos ajustes como este podem ser pequenos mas fazem toda a diferença na entrega de um trabalho de qualidade e com atenção aos detalhes.
# 

# # Pergunta 4
# 
# Analise o histograma do exercicio anterior e responda:
# 
# Qual o intervalo de duração com maior quantidade de viagens?
# 
# 
# **Reposta**: O intervalo de duração que tem maior quantidades de viagens é o intervalo entre 5 a 10 minutos.

# In[31]:


trip_data_morethan60min = trip_data.query('duration > 60')


# In[32]:


trip_data_morethan60min


# In[33]:


trip_data_morethan5min = trip_data.query('duration > 5')
trip_data_morethan5min


# In[34]:


trip_data_between5and10 = trip_data_morethan5min.query('duration < 10')
trip_data_between5and10


# In[35]:


trip_data_between5and10.groupby('start_city').count()


# In[36]:


trip_data_between5and10.groupby('end_city').count()


# # Pergunta 4.1
# 
# Com base na sua resposta da pergunta anterior, conte quantas viagens existem para cada origem e destino desse intervalo de tempo. Monte uma tabela que demonstre isso. 
# 
# Qual origem e destino tem a maior quantidade de viagens?  Aproximadamente quantas viagens foram feitas nesta faixa de tempo?
# 
# 
#  **Reposta**: A origem e destino que tem a maior quantidade de viagens é São Francisco (San Francisco - 8086) com 8975 viagens. O número total de viagens realizadas entre 5 e 10 min foi de 8975, sendo que São Francisco corresponde com aproximadamente 90% das viagens.

# ## Fazendo suas Próprias Análises
# 
# Agora que você fez alguma exploração em uma pequena amostra do conjunto de dados, é hora de avançar e reunir todos os dados em um único arquivo e ver quais tendências você pode encontrar. O código abaixo usará a mesma função `summarise_data()` para processar dados. Depois de executar a célula abaixo, você terá processado todos os dados em um único arquivo de dados. Observe que a função não exibirá qualquer saída enquanto ele é executado, e isso pode demorar um pouco para ser concluído, pois você tem muito mais dados do que a amostra com a qual você trabalhou.

# In[37]:


station_data = ['201402_station_data.csv',
                '201408_station_data.csv',
                '201508_station_data.csv' ]
trip_in = ['201402_trip_data.csv',
           '201408_trip_data.csv',
           '201508_trip_data.csv' ]
trip_out = 'babs_y1_y2_summary.csv'

# Esta função irá ler as informações das estações e das viagens
# e escreverá um arquivo processado com o nome trip_out
summarise_data(trip_in, station_data, trip_out)


# Já que a função `summarise_data()` escreveu um arquivo de saída, a célula acima não precisa ser rodada novamente mesmo que este notebook seja fechado e uma nova sessão seja criada. Você pode simplesmente ler os dados novamente e fazer a exploração deste ponto (não esqueça de executar a parte das funções no começo do notebook caso esteja em uma nova sessão)

# In[38]:


trip_data = pd.read_csv('babs_y1_y2_summary.csv')
display(trip_data.head())


# #### Agora é a SUA vez de fazer a exploração do dataset (do conjunto de dados) completo.
# 
# Aproveite para fazer filtros nos dados e tentar encontrar padrões nos dados.

# Explore algumas variáveis diferentes usando o mesmo racional acima e tome nota de algumas tendências que você encontra. Sinta-se livre para criar células adicionais se quiser explorar o conjunto de dados de outras maneiras ou de várias maneiras.
# 
# > **Dica**: para adicionar células adicionais a um notebook, você pode usar as opções "Inserir célula acima" (Insert Cell Above) e "Insert Cell Below" na barra de menu acima. Há também um ícone na barra de ferramentas para adicionar novas células, com ícones adicionais para mover as células para cima e para baixo do documento. Por padrão, as novas células são do tipo de código; Você também pode especificar o tipo de célula (por exemplo, Código ou Markdown) das células selecionadas no menu Cell ou no menu dropdown na barra de ferramentas.
# 
# Um feito com suas explorações, copie as duas visualizações que você achou mais interessantes nas células abaixo e responda as seguintes perguntas com algumas frases descrevendo o que você encontrou e por que você selecionou os números. Certifique-se de que você ajusta o número de caixas ou os limites da bandeja para que efetivamente transmitam os resultados dos dados. Sinta-se livre para complementar isso com quaisquer números adicionais gerados a partir de `use_stats()` ou coloque visualizações múltiplas para suportar suas observações.

# Para ver alguns outros tipos de gráficos que o matplotlib (padrão do Pandas) possui, leia [este artigo](https://www.labri.fr/perso/nrougier/teaching/matplotlib/#other-types-of-plots). 
# 
# Para entender um pouco mais como e quais gráficos podem ser úteis, leia [este documento](https://www.tableau.com/sites/default/files/media/Whitepapers/which_chart_v6_ptb.pdf). Ele lhe dará um pouco de idéia de como mostrar os dados de forma mais acertada

# In[39]:


# Quais horas do dia em que as bicicletas são mais utilizadas? Número de viagens por hora de início.
trip_data.groupby('start_hour')['duration'].count()


# In[40]:


trip_data.groupby('start_hour')['duration'].count().plot(kind='bar');


# #### Claramente existe uma maior utilização das bicicletas durante as horas início da jornada de trabalho (de 7 as 9 horas) e do fim da jornada de trabalho (de 16 as 18 horas)

# In[41]:


# Quais horas do dia em que as bicicletas são utilizadas por mais tempo? Média da duração por hora de início. 
trip_data.groupby('start_hour')['duration'].mean().plot(kind='bar')


# #### A média de duração não parece ser um bom indicador, horários com poucas utilizações podem criar desvios. 
# Verficando os detalhes em relação as viagens que ocorreram as 3 da manhã abaixo.

# In[42]:


trip_data_3am = trip_data.query('start_hour == 3')
trip_data_3am['duration'].describe()


# #### O desvio padrão e o valor máximo demonstram que algumas viagens muito longas estão descaracterizando a base de dados
# **std = 1113.1757** e **max = 10932.3166**

# In[43]:


trip_data_3am_outlier = trip_data_3am[trip_data_3am['duration'] > 10000]
trip_data_3am_outlier


# #### Existem 3 viagens que ocorreram as 3 horas da manhã com valores muito discrepantes acima de 10000 minutos ou mais de 166 horas. Isso pode indicar esquecimento de devolução, roubo de bicicletas, ou erros nos dados.

# In[44]:


trip_data_2am = trip_data.query('start_hour == 2')
trip_data_2am['duration'].describe()


# In[45]:


trip_data_2am_outlier = trip_data_2am[trip_data_2am['duration'] > 3000]
trip_data_2am_outlier


# #### O mesmo parece acontecer para viagens que começam as 2 am. 2 viagens com mais de 4000 minutos ou seja mais de 66 horas.

# In[46]:


trip_data_1am = trip_data.query('start_hour == 1')
trip_data_1am['duration'].describe()


# In[47]:


trip_data_1am_outlier = trip_data_1am[trip_data_1am['duration'] > 3000]
trip_data_1am_outlier


# In[48]:


# Limapando a base desses outliers de durações maiores que 2 horas (120 minutos);
trip_data_clean = trip_data[trip_data['duration'] < 120]
trip_data_clean.groupby('start_hour')['duration'].mean().plot(kind='bar');


# #### Percebe-se que as maiores médias das durações são viagens que se iniciam na madrugada.   

# In[49]:


# As bicicletas são mais utilizadas nos dias de semana ou nos fins de semana? 
trip_data.groupby('weekday')['duration'].count()


# In[50]:


trip_data_week = trip_data.groupby('weekday')['duration'].count()
trip_data_week.describe()


# In[51]:


# As bicicletas são mais utilizadas nos dias de semana ou nos fins de semana? Contagem das utilizações durante os dias da semana.
trip_data.groupby('weekday')['duration'].count().plot(kind='bar');


# #### Fica claro que as bicicletas são mais utilizadas nos dias de semana. Sendo a média de utilizações por dia das semana 95708, todos os dias da semana tem mais utilização que a média enquanto os fins de semana tem menos utilização que a média.

# In[52]:


trip_data_week2 = trip_data.groupby('weekday')['duration'].mean()
trip_data_week2.describe()


# In[53]:


# As bicicletas são mais utilizadas por mais tempo nos dias de semanda ou nos fins de semana? Média da duração das utilizações durante os dias da semana.
trip_data.groupby('weekday')['duration'].mean().plot(kind='bar');


# #### Por outro lado as bicicletas são utilizadas por mais tempo durante o fim de semana. Sendo a média de tempo de utilzação por dia da semana igual a 23,34 minutos, todos os dias de semana tempo de utilização inferior a média enquanto nos fins de semana o tempo de utilização é superior a média.

# In[54]:


# Nos dias da semana quais as horas em que as bicicletas são mais utilizadas?
trip_data_weekday = trip_data[trip_data['weekday'] < 5]
trip_data_weekday.groupby('start_hour')['duration'].count().plot(kind='bar');


# #### Nos dias de semana os horários mais utilizados são os de 7 a 9 da manhã e de 16 a 19 da tarde. Confirmando a tese de que se trata de pessoas indo e voltando das suas atividades profissionais.

# In[55]:


# Nos dias da semana qual o tipo de cliente utiliza mais o serviço?
trip_data_weekday.groupby('subscription_type')['duration'].count().plot(kind='bar');


# In[56]:


# Quais as horas preferidas para os clientes do tipo "Subscriber" nos dias de semana?
trip_data_weekday_sub = trip_data_weekday[trip_data_weekday['subscription_type'] == 'Subscriber']
trip_data_weekday_sub.groupby(['start_hour'])['duration'].count().plot(kind='bar');


# #### Percebe-se que o tipo de cliente "Subscriber" prefere utilizar o serviço nas horas de 7 as 9 da manhã e de 16 as 18 da tarde.

# In[57]:


# Quais as horas preferidas para os clientes do tipo "Customer" nos dias de semana?
trip_data_weekday_cus = trip_data_weekday[trip_data_weekday['subscription_type'] == 'Customer']
trip_data_weekday_cus.groupby(['start_hour'])['duration'].count().plot(kind='bar');


# #### Percebe-se que o cliente "Customer" prefere utilizar o serviço entre 11 da manhã as 17 da tarde nos dias de semana.

# In[58]:


# Nos fins de semana quais as horas em que as bicicletas são mais utilizadas?
trip_data_weekend = trip_data[trip_data['weekday'] > 4]
trip_data_weekend.groupby('start_hour')['duration'].count().plot(kind='bar');


# #### Nos fins de semana os horários mais utilizados são os entre 10 as 17.

# In[59]:


trip_data_weekend.groupby('subscription_type')['duration'].count()


# In[60]:


# Nos finais da semana qual o tipo de cliente utiliza mais o serviço?
trip_data_weekend.groupby('subscription_type')['duration'].count().plot(kind='bar');


# #### Nos finais de semana tanto os clientes "Subscriber" quanto os clientes "Customer" utilizam o serviço com uma pequena utilização a mais pelos clientes do tipo "Customer"

# In[61]:


# Quais as horas preferidas para os clientes do tipo "Subscriber" nos finais de semana?
trip_data_weekend_sub = trip_data_weekend[trip_data_weekend['subscription_type'] == 'Subscriber']
trip_data_weekend_sub.groupby(['start_hour'])['duration'].count().plot(kind='bar');


# In[62]:


# Quais as horas preferidas para os clientes do tipo "Customer" nos finais de semana?
trip_data_weekend_cus = trip_data_weekend[trip_data_weekend['subscription_type'] == 'Subscriber']
trip_data_weekend_cus.groupby(['start_hour'])['duration'].count().plot(kind='bar');


# #### Ambos os tipos de cliente no fim de semana tem a mesma preferência de horário entre 10 as 13 e entre 15 e 16 horas.

# In[63]:


# Existe algum mês em que as bicicletas são mais utilizadas, existe algum mês em que elas são menos utilizadas?
trip_data.groupby('start_month')['duration'].count()


# In[64]:


trip_data.groupby('start_month')['duration'].count().plot(kind='bar');


# #### O mês de fevereiro, novembro e dezembro são os meses aos quais tem menos utilização do serviço. O serviço é mais utilizado no mês de agosto. 

# In[65]:


trip_data.groupby('start_year')['duration'].count()


# In[66]:


# A utilização vem aumentando ou diminuindo ao longo dos anos?
trip_data.groupby('start_year')['duration'].count().plot(kind='line',figsize=(10,10));


# #### A utilização dos serviços teve um pico em 2014 e se reduziu em 2015

# In[67]:


trip_data_subscriber = trip_data[trip_data['subscription_type'] == 'Subscriber']
trip_data_subscriber.groupby('start_year')['duration'].count()


# In[68]:


# A utilização por clientes "Subscriber" vem aumentando ou diminuindo ao longo dos anos?
trip_data_subscriber = trip_data[trip_data['subscription_type'] == 'Subscriber']
trip_data_subscriber.groupby('start_year')['duration'].count().plot(kind='line',figsize=(10,10));


# In[69]:


trip_data_subscriber = trip_data[trip_data['subscription_type'] == 'Customer']
trip_data_subscriber.groupby('start_year')['duration'].count()


# In[70]:


# A utilização por clientes "Customer" vem aumentando ou diminuindo ao longo dos anos?
trip_data_subscriber = trip_data[trip_data['subscription_type'] == 'Customer']
trip_data_subscriber.groupby('start_year')['duration'].count().plot(kind='line',figsize=(10,10));


# #### Ocorreu um pico de utilização no ano de 2014 e uma subsequente redução no ano de 2015, esse tendência foi observada para ambos os tipos de clientes.

# In[71]:


# Cria uma função para recolher os resultados do dicionário e transformar numa lista de valores.
def make_list(dictionary):
    list_make = []
    for i in dictionary:
        list_make.append(i)
    return list_make


# In[72]:


# Verifica a contagem de valores de horas de partida apenas para dias de semana de clientes "Subscriber"
start_hour_weekday_sub = trip_data_weekday_sub.groupby(['start_hour'])['duration'].count()
start_hour_weekday_sub


# In[73]:


# Cria uma lista de valores para criação do gráfico
subcount = make_list(start_hour_weekday_sub)
subcount


# In[74]:


# Verifica a contagem de valores de horas de partida apenas para dias de semana de clientes "Customer"
start_hour_weekday_cus = trip_data_weekday_cus.groupby(['start_hour'])['duration'].count()
start_hour_weekday_cus


# In[75]:


# Cria uma lista de valores para criação do gráfico
cuscount = make_list(start_hour_weekday_cus)
cuscount


# In[76]:


# Verifica a contagem de valores de horas de partida apenas para dias de fim de semana de clientes "Subscriber"
start_hour_weekend_sub = trip_data_weekend_sub.groupby(['start_hour'])['duration'].count()
start_hour_weekend_sub


# In[77]:


# Cria uma lista de valores para criação do gráfico
subcountweekend = make_list(start_hour_weekend_sub)
subcountweekend


# In[78]:


# Verifica a contagem de valores de horas de partida apenas para dias de semana de clientes "Customer"
start_hour_weekend_cus = trip_data_weekend_cus.groupby(['start_hour'])['duration'].count()
start_hour_weekend_cus


# In[79]:


# Cria uma lista de valores para criação do gráfico
cuscountweekend = make_list(start_hour_weekend_cus)
cuscountweekend


# # Pergunta 5a
# Explore os dados e faça um gráfico que demonstre alguma particularidade dos dados:

# In[80]:


# Gráfico final 1
# Utilização de subscribers x customers durante a semana.
N = start_hour_weekday_cus.count()
ind = np.arange(N)    # the x locations for the groups
width = 0.8       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots(figsize=(20, 10))
p1 = plt.bar(ind, subcount, width)
p2 = plt.bar(ind, cuscount, width, bottom=subcount)

plt.ylabel('Número de Utilizações')
plt.title('Número de Utilizações em Dias de Semana')
plt.xticks(ind, ('0 hrs', '1 hrs', '2 hrs', '3 hrs', '4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '10 hrs', '11 hrs', '12 hrs', '13 hrs', '14 hrs', '15 hrs', '16 hrs', '17 hr', '18 hrs', '19 hrs', '20 hrs', '21 hrs', '22 hrs', '23 hrs'))
plt.yticks(np.arange(0, 90000, 10000))
plt.legend((p1[0], p2[0]), ('Subscriber', 'Customer'))


# O que é interessante na visualização acima? Por que você a selecionou?
# 
# **Answer**: A visualização acima nos permite ver com clareza o perfil de uso durante um dia de semana típico e o interesse relativo entre os diferentes tipos de usuários. O gráfico demonstra que durante a semana o serviço é utilizado em sua grande maioria pelos clientes do tipo "Subscriber" que utilizam o serviço principalmente nos horários típicos de entrada e saída de trabalho (entre 7 as 9, pela manhã, e entre 16 as 19, pela noite). É possível interpretar por esse resultado que o serviço é utilizado como meio de transporte para a jornada de trabalho (ainda que possivelmnete de forma complementar). Ainda é perceptível que existe uma pequena predileção pelo uso dos serviços por estes usuários pela manhã em relação a noite. Por outro lado, os usuários "Customers" tem uma utilização mais uniforme e concentram mais sua utilização nos horários típicos de lazer (de 10 as 18 horas). 

# # Pergunta 5b
# Faça um gráfico que demonstre alguma particularidade dos dados:

# In[81]:


# Gráfico Final 2
# Utilização de subscribers x customers durante o fim de semana.
N = start_hour_weekend_cus.count()
ind = np.arange(N)    # the x locations for the groups
width = 0.8       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots(figsize=(20, 10))
p1 = plt.bar(ind, subcountweekend, width)
p2 = plt.bar(ind, cuscountweekend, width, bottom=subcountweekend)

plt.ylabel('Número de Utilizações')
plt.title('Número de Utilizações em Fins de Semana')
plt.xticks(ind, ('0 hrs', '1 hrs', '2 hrs', '3 hrs', '4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '10 hrs', '11 hrs', '12 hrs', '13 hrs', '14 hrs', '15 hrs', '16 hrs', '17 hr', '18 hrs', '19 hrs', '20 hrs', '21 hrs', '22 hrs', '23 hrs'))
plt.yticks(np.arange(0, 10000, 1000))
plt.legend((p1[0], p2[0]), ('Subscriber', 'Customer'))


# O que é interessante na visualização acima? Por que você a selecionou?
# 
# **Answer**: A visualização acima nos permite contrabalancear a visualização anterior mostrando outro aspecto igualmente interessante dos dados. Enquando durante a semana o perfil "Subcriber" é dominante, não se pode afirmar o mesmo para os fins de semana. Nos fins de semana a divisão entre perfis é praticamente a mesma. É perceptível na visualização acima que a preferência de horários para utilização do serviço também é equivalente entre os dois perfis (em contrário com a utilização durante a semana). É possível inferir portanteo que durante os fins de semana o serviço é utilizado majoritariamente para atividades de recreação que costuma acontecer entre 10 as 18 horas. 

# ## Conclusões
# 
# Parabéns pela conclusão do projeto! Esta é apenas uma amostragem do processo de análise de dados: gerando perguntas, limpando e explorando os dados. Normalmente, neste momento no processo de análise de dados, você pode querer tirar conclusões realizando um teste estatístico ou ajustando os dados a um modelo para fazer previsões. Há também muitas análises potenciais que podem ser realizadas se evoluirmos o código fornecido. Em vez de apenas olhar para o número de viagens no eixo de resultados, você pode ver quais recursos afetam coisas como a duração da viagem. Nós também não analisamos como os dados meteorológicos se encaixam no uso de bicicletas.

# # Pergunta 6
# Pense em um tópico ou campo de interesse onde você gostaria de poder aplicar as técnicas da ciência dos dados. O que você gostaria de aprender com o assunto escolhido?
# 
# **Responda**: 
# Gostaria de aplicar as técnicas da ciências dos dados a dois tópicos de interesse. 
# 
# **Escolha de produtos (escolhas do consumidor)**. É interessante utilizar essa abordagem para esse assunto pois permite a criação de produtos e serviços mais adequados aos clientes. A partir da análise de dados é possível prever tendências e descobrir insights tanto de novos serviços e produtos como para melhorar os já existentes. Seria interessante encontrar formas de ampliar a escala de certos produtos sem perder a conexão "premium" de clientes com marcas feitas sobre medida. Acredito que a análise de dados somada com outras técnicas nos permite se aproximar desse objetivo.
# 
# **Decisões políticas**. As nossas eleições estão chegando e é interessante utilizar as técnicas de análise de dados para descobrir o que influencia nas decisões políticas dos individuos. Historicamente temos a sensação de nossas decisões políticas como população não estão nos direcionando para os objetivos que nós queremos (uma sociedade mais justa, igualitária, com liberdade e solidariedade). Seria interessante utilizar as técnicas de análise de dados para descobrir insights interessantes de porque as pessoas decidem por um ou por outro candidato, e por que após eleitos eles não satisfazem as expectativas depositadas pela população.

# > **Dica**: se quisermos compartilhar os resultados de nossa análise com os outros, existe uma outra opção que não é enviar o arquivo jupyter Notebook (.ipynb). Também podemos exportar a saída do Notebook de uma forma que pode ser aberto mesmo para aqueles sem o Python instalado. No menu **File** na parte superior esquerda, vá para o submenu **Download as**. Você pode então escolher um formato diferente que pode ser visto de forma mais geral, como HTML (.html) ou PDF (.pdf). Você pode precisar de pacotes adicionais ou software para executar essas exportações.
