from jinja2utils import matcher, Stack


def test_single_value():
    m = matcher('foo', 'true', 'false')
    assert m('foo') == 'true'
    assert m('bar') == 'false'


def test_multiple_values():
    # Multiple values to match against
    m = matcher(('foo1', 'foo2'), 'true', 'false')
    assert m('foo2') == 'true'
    assert m('foo3') == 'false'

    # Multiple values trying to be matched
    m = matcher('foo', 'true', 'false')
    assert m('bar', 'foo') == 'true'
    assert m('bar', 'test') == 'false'


def test_stack():
    """Test with the stack object.
    """
    s = Stack()
    s('products')
    s('plasma')
    m = matcher(s, 'true', 'false')
    assert m('plasma') == 'true'
    assert m('lcd') == 'false'


def test_else_optional():
    m = matcher('foo', 'true')
    assert m('foo') == 'true'
    assert m('bar') == ''