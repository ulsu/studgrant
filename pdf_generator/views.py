# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from cStringIO import StringIO
from django.template.loader import render_to_string

# Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % \
            (sUrl, mUrl))
    return path

def generate_pdf(request, context):
    result = StringIO()
    html = render_to_string('main/report.html', context)

    pdf = pisa.CreatePDF(StringIO(html.encode('utf-8')), result, show_error_as_pdf=True, encoding='utf-8')
    if not pdf.err:
        from django.http import HttpResponse
        response = HttpResponse(mimetype='application/pdf')
        response['Content-Desposition'] = 'attachment; filename=super_file.pdf'
        response.write(result.getvalue())
        result.close()
        return response