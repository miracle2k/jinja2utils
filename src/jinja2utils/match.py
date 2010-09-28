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

    def __init__(self, cmp_value, insert_text):
        self.cmp_value, self.insert_text = cmp_value, insert_text

    def __call__(self, *items):
        if self.cmp_value in items:
            return self.insert_text
        return ''
