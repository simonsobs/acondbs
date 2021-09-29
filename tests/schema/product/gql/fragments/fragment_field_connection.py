from .fragment_field import FRAGMENT_FIELD

FRAGMENT_FIELD_CONNECTION = '''
fragment fragmentFieldConnection on FieldConnection {
  edges {
    node {
     ...fragmentField
    }
  }
}
''' + FRAGMENT_FIELD
