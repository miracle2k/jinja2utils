__all__ = ('matcher',)


class matcher(object):
    """A global object similar to the joiner() and cycler() builtins.

    Usage:

        {% set cur_pag_mark = matcher(PAGE, 'class="active"'|safe) %}
        <a {{ cur_pag_mark('index') }}></a>
        <a {{ cur_pag_mark('contact') }}></a>

    The example shows how to use the matcher to easily flag the current
    page link within a navigation.

    For more complex cases, say a nested navigation, the first argument
    to matcher() may be an iterable, in which case any one of the giving
    values can cause a match:

        {% set cur_pag_mark = matcher(('projects', 'plasma'), 'class="active"'|safe) %}
        <li>
           <a {{ cur_pag_mark('products') }}></a>
           <ul>
               <a {{ cur_pag_mark('plasma') }}></a>
               <a {{ cur_pag_mark('lcd') }}></a>
           </ul>
        </li>

    Note: the ``jinja2utils.Stack`` object is something that fits well here.
    """

    def __init__(self, cmp_value, match_insert, no_match=''):
        try:
            iter(cmp_value)
        except TypeError:
            self.cmp_values = [cmp_value]
        else:
            self.cmp_values = cmp_value
        self.match_insert = match_insert
        self.no_match = no_match

    def __call__(self, *items):
        for item in items:
            if item in self.cmp_values:
                return self.match_insert
        return self.no_match
