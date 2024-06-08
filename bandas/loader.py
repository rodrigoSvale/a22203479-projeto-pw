from bandas.models import *
import json

Banda.objects.all().delete()
Album.objects.all().delete()

with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)


    for banda in bandas:
        Banda.objects.create(
            nome = banda['nome'],
            nacionalidade = banda['nacionalidade'],
            ano = banda['ano_criacao'],
            genero = banda['genero'],
            foto = ""
            )

with open('bandas/json/albuns.json') as f:
    albuns = json.load(f)


    for album in albuns:
        Album.objects.create(
            titulo = album['titulo'],
            ano = album['ano_lancamento'],
            banda = Banda.objects.get(nome = album['banda']),
            capa = ""
            )
        for musica in album['musicas']:
            Musica.objects.create(
                album = Album.objects.get(titulo = album['titulo']),
                titulo = musica['titulo'],
                duracao = musica['duracao'],
                spotify_link = musica['spotify_link']
                )


# PERGUNTAS #

# 1 Lista os albuns ordenando pelo ano de lançamento

    print('Lista os albuns ordenando pelo ano de lançamento\n')

    albuns_ano = []
    albuns_ano = Album.objects.values_list('titulo', 'ano').order_by('ano')

    for album in albuns_ano:
        print(album)

    print('\n')

# 2 Lista as músicas que duram mais que 4 minutos e ordenados pela duração

    print('Lista as músicas que duram mais que 4 minutos e ordenados pela duração\n')

    musica_mais_4min = []
    musica_mais_4min = Musica.objects.filter(duracao__gt = '4:00').values_list('titulo', 'duracao').order_by('duracao')

    for musica in musica_mais_4min:
        print(musica)

    print('\n')

# 3 Devolve o número de músicas de uma banda

    print('Devolve o número de músicas de uma banda\n')

    print(Musica.objects.filter(album__banda__nome = 'The Beatles').count())
    print("\n")

# 4 Lista as bandas que foram criadas entre dois anos

    print('Lista as bandas que foram criadas entre dois anos\n')

    bandas_entre = []
    bandas_entre = Banda.objects.filter(ano__gt = 1960, ano__lt = 1980).values_list('nome', 'ano').order_by('ano')

    for banda in bandas_entre:
        print(banda)

    print('\n')

# 5 Lista todos os albuns de uma banda cronológicamente

    print('Lista todos os albuns de uma banda cronológicamente\n')

    albuns_banda = []
    albuns_banda = Album.objects.filter(banda__nome = 'Led Zeppelin').values_list('banda__nome','titulo').order_by('ano')

    for album in albuns_banda:
        print(album)

    print('\n')

# 6 Listar os albuns de todas as bandas

    print('Listar os albuns de todas as bandas\n')

    banda_albuns = []
    banda_albuns = Album.objects.values_list('banda__nome','titulo')

    for album in banda_albuns:
        print(album)

    print('\n')

# 7 Listar as músicas com duração entre 2:00 a 5:00 e ordenadas pela duração

    print('Listar as músicas com duração entre 2:00 a 5:00 e ordenadas pela duração\n')

    playlist = []

    playlist = Musica.objects.filter(duracao__gte = '2:00', duracao__lte= '5:00').values_list('album__titulo','titulo','duracao').order_by('duracao')

    for musica in playlist:
        print(musica)

    print('\n')

# 8 Listar as bandas por ordem alfabética

    print('Listar as bandas por ordem alfabética\n')

    bandas = []

    bandas = Banda.objects.values_list('nome',flat = True).order_by('nome')

    for banda in bandas:
        print(banda)

    print('\n')

# 9 Listar os albuns que começam com a letra 'A'

    print('Listar os albuns que começam com a letra A\n')

    albuns_start_with_A = []

    albuns_start_with_A = Album.objects.filter(titulo__startswith = 'A').values_list('titulo',flat = True)

    for album in albuns_start_with_A:
        print(album)

    print('\n')


# 10 Listar os links das músicas dos albuns

    print('Listar os links das músicas dos albuns\n')

    spotify_links = []

    spotify_links = Musica.objects.values_list('album__titulo','spotify_link')

    for link in spotify_links:
        print(link)

    print('\n')