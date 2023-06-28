'''GraphQL queries as strings

'''

__all__ = [
    'FRAGMENT_LOG',
    'FRAGMENT_LOG_CONNECTION',
    'MUTATION_CREATE_LOG',
    'MUTATION_DELETE_LOG',
    'QUERY_ALL_LOGS',
    'QUERY_LOG',
]


from .fragments import FRAGMENT_LOG, FRAGMENT_LOG_CONNECTION
from .mutations import MUTATION_CREATE_LOG, MUTATION_DELETE_LOG
from .queries import QUERY_ALL_LOGS, QUERY_LOG
