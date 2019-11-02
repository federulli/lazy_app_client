from gql import gql, Client as gql_client
from gql.transport.requests import RequestsHTTPTransport


class Client:
    def __init__(self, url, port):
        _transport = RequestsHTTPTransport(
            url=f'http://{url}:{port}/graphql',
            use_json=True
        )
        self._client = gql_client(
            transport=_transport,
            fetch_schema_from_transport=True,
        )

    def add_tv_show(self, name):
        query = gql("""
            mutation CreateTVShow($name: String!){
                createTvShow(name:$name){
                    tvShow{name id}
                }
            }
        """)
        return self._client.execute(query, {'name': name})

    def add_season(self, tv_show_id, season_number):
        mutation = gql("""
            mutation CreateTVShow($show_id: ID! $number: Int!){
                createSeason(tvShowId:$show_id, number: $number){
                    season{number}
                }
            }
        """)
        return self._client.execute(
            mutation,
            {'show_id': tv_show_id, 'number': season_number}
        )

    def add_movie(self, name, year=None):
        mutation = gql("""
            mutation CreateMovie($name: String! $year: Int){
                createMovie(name:$name, year: $year){
                    movie{name}
                }
            }
        """)
        return self._client.execute(
            mutation,
            {'name': name, 'year': year}
        )

    def search_movies(self):
        mutation = gql("""
            mutation {
                searchMovies{
                    msg
                }
            }
        """)
        return self._client.execute(mutation)

    def search_chapters(self):
        mutation = gql("""
            mutation {
                searchChapters{
                    msg
                }
            }
        """)
        return self._client.execute(mutation)

    def delete_completed_torrents(self):
        mutation = gql("""
            mutation {
                deleteCompleted{
                    msg
                }
            }
        """)
        return self._client.execute(mutation)

    def delete_all_torrents(self):
        mutation = gql("""
            mutation {
                deleteAllTorrents{
                    msg
                }
            }
        """)
        return self._client.execute(mutation)

    def reload_chapter_count(self):
        mutation = gql("""
            mutation {
                reloadChapterCount{
                    msg
                }
            }
        """)
        return self._client.execute(mutation)

    def get_tv_shows(self, id=None):
        query = gql("""
            query GetTvShows($show_id: ID) {
              tvShows(id: $show_id) {
                id
                name
                seasons {
                  id
                  number
                  completed
                  chapterCount
                }
              }
            }
        """)
        return self._client.execute(query, {"show_id": id})

    def get_movies(self, id=None):
        query = gql("""
            query GetMovies($movie_id: ID) {
                  movies(id: $movie_id) {
                    id
                    name
                    year
                    torrent{id magnet downloadPath}
                  }
                }
        """)
        return self._client.execute(query, {"movie_id": id})
