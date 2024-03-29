from acondbs.models import FieldType, saEnumFieldType


def test_attribute_class() -> None:
    for name, type_ in FieldType.__members__.items():
        # e.g., name = 'UnicodeText', type_ = FieldType.UnicodeText
        assert type_.attribute_class.__name__ == f'Attribute{name}'


def test_import_sa_enum() -> None:
    assert saEnumFieldType


def test_example() -> None:
    # can be instantiated with an int
    type_ = FieldType(1)

    # the same object
    assert type_ is FieldType(1)
    assert type_ is FieldType.UnicodeText

    # access to name and value
    assert type_.name == 'UnicodeText'
    assert type_.value == 1
