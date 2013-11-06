from django.forms.widgets import FileInput
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode


class InlineFileInput(FileInput):
    def __init__(self, attrs={}):
        super(InlineFileInput, self).__init__(attrs)

    def _get_filename(self, value):
        return value.split('/')[-1:][0]

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output = ['<a href="%s">%s</a>' % (value.url, self._get_filename(force_unicode(value)))]
        else:
            output.append(super(InlineFileInput, self).render(name, value, attrs))
        return mark_safe(u''.join(output))