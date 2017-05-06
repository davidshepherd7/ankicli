from nose.tools import *
import ankicli.ankicli as ankicli


def test_parse_single_field():
    assert ankicli.parse("") == {}
    assert ankicli.parse("@First") == {'First': ''}
    assert ankicli.parse("@First\nFoo") == {'First': 'Foo'}
    assert ankicli.parse("@First\nFoo\n") == {'First': 'Foo\n'}
    assert ankicli.parse("@First\nFoo@@\n") == {'First': 'Foo@@\n'}
    assert ankicli.parse("@First\nFoo\nBar\nBaz") == {'First': 'Foo\nBar\nBaz'}


def test_parse_whitespace():
    assert ankicli.parse("@First    \nFoo\n") == {'First': 'Foo\n'}
    assert ankicli.parse("@   First    \nFoo\n") == {'First': 'Foo\n'}
    assert ankicli.parse("    @First") == {'First': ''}


def test_parse_multi_field():
    assert ankicli.parse("@First\nFoo\n@Second\nbar\n") == {'First': 'Foo\n', 'Second': 'bar\n'}
