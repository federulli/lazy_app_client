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

cli = Client('192.168.99.100', 5000)
tv_show = cli.add_tv_show("arrow")
print (cli.add_season(1, 1))
