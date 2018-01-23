# Teste para desenvolvedor backend Imaginie
Neste teste, você deverá implementar uma api para um sistema de playlist de músicas, seguindo os seguintes passos:

## 1)
Completar o código das 4 classes no arquivo de models: Gênero, Artista, Música e Playlist. O diagrama estará no arquivo diagrama.png.

## 2)
Criar uma nova migration para popular o seu banco, a partir do arquivo load.csv.

## 3)
Implementar as requisições REST de retrieve, list, create, update e delete para todas as tabelas.


- O usuário normal poderá fazer todas as requisições apenas em sua playlist.
Nas demais (incluindo playlists de terceiros), apenas as requisições GET.

- O admin tem acesso livre a todas as requisições para todas as tabelas.

- GET /api/playlist/[id]/music retorna uma lista de todas as musicas de uma playlist.

- Em todas as listagens, deverá ter o parâmetro search, que retornará uma lista com os termos da busca.

- POST /api/playlist/[id_in]/add/[id_out] adiciona todas as músicas de uma playlist para outra playlist.

## Notas:
- Utilize o sistema de usuários do Django
- Poderá utilizar o sqlite

# Boa sorte!
