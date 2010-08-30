__all__ = ('Stack',)


class Stack(object):
    """Provides a global object to store and retrieve a stack of values.

    There is strictly speaking nothing about this that's specific to
    Jinja2, though it's written with a template engine in mind, and
    requires one that can do full function calls.

    Define a stack object, and make it available as a global::

        jinja2_env.globals['breadcrumbs'] = Stack()

    Then, in your ``page.html`` template:

        {% do breadcrumbs('Page', '/page') %}
        {% extends 'base.html' %}

    You ``base.html`` would include something like this:

        Index
        {% for name, url in breadcrumbs %}
            | {{ name }}
        {% endfor %}
    """

    def __init__(self, reverse=True):
        self.data = []
        self._reverse = reverse

    def __call__(self, *items):
        if self._reverse:
            self.data.insert(0, items)
        else:
            self.data.append(items)
        # Not returning anything means the user doesn't has to use
        # the do-extensions.
        return ''

    def __iter__(self):
        for item in self.data:
            yield item

    def __len__(self):
        return len(self.data)

    def top(self):
        try:
            return self.data[-1]
        except IndexError:
            return None

    def bottom(self):
        try:
            return self.data[0]
        except IndexError:
            return None
