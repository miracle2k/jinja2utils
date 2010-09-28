__all__ = ('matcher',)


class matcher(object):
    """A global object similar to the joiner() and cycler() builtins.

    Usage:

        {% set cur_pag_mark = matcher(PAGE, ' class="active"'|safe) %}
        <a href=""{{ cur_pag_mark('index') }}></a>
        <a href=""{{ cur_pag_mark('contact') }}></a>

    The example shows how to use the matcher to easily flag the current
    page link within a navigation.
    """

    def __init__(self, cmp_value, match_insert, no_match=''):
        self.cmp_value = cmp_value
        self.match_insert = match_insert
        self.no_match = no_match

    def __call__(self, *items):
        if self.cmp_value in items:
            return self.match_insert
        return self.no_match
