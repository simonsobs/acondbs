"""GraphQL queries as strings

"""

from .fragments import (  # noqa: F401
    FRAGMENT_PRODUCT,
    FRAGMENT_PRODUCT_SHALLOW,
    FRAGMENT_PRODUCT_CONNECTION,
    FRAGMENT_PRODUCT_CONNECTION_SHALLOW
)

from .product import (  # noqa: F401
    FRAGMENT_PRODUCT_SHALLOW,
    FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
    MUTATION_CREATE_PRODUCT,
    MUTATION_DELETE_PRODUCT,
    MUTATION_UPDATE_PRODUCT,
)

from .product_relation_type import (  # noqa: F401
    FRAGMENT_PRODUCT_RELATION_TYPE,
    FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
    CREATE_PRODUCT_RELATION_TYPES,
    UPDATE_PRODUCT_RELATION_TYPE,
    DELETE_PRODUCT_RELATION_TYPES,
)

from .product_relation import (  # noqa: F401
    FRAGMENT_PRODUCT_RELATION,
    FRAGMENT_PRODUCT_RELATION_CONNECTION,
    CREATE_PRODUCT_RELATION,
    DELETE_PRODUCT_RELATION,
)

from .product_type import (  # noqa: F401
    FRAGMENT_PRODUCT_TYPE,
    FRAGMENT_PRODUCT_TYPE_CONNECTION,
    CREATE_PRODUCT_TYPE,
    UPDATE_PRODUCT_TYPE,
    DELETE_PRODUCT_TYPE,
)
