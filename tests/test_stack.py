from jinja2utils import Stack


def test_default_reverse_order():
    s = Stack()  # This is the default
    s('first')
    s('second')
    s('third')
    assert len(s) == 3
    assert s.top() == ('first',)
    assert s.bottom() == ('third',)
    assert list(s) == [('third',), ('second',), ('first',)]


def test_straight_order():
    s = Stack(reverse=False)
    s('first')
    s('second')
    s('third')
    assert s.top() == ('third',)
    assert s.bottom() == ('first',)
    assert list(s) == [('first',), ('second',), ('third',)]


def test_contains():
    s = Stack(reverse=False)
    s('foo')
    s('bar', '2')
    # Test the special case that __contains__ allows us to search
    # for a 1-tuple with the value itself. It doesn't work for n-tuples
    # with n > 1 though.
    assert 'foo' in s
    assert ('foo',) in s
    assert not 'bar' in s