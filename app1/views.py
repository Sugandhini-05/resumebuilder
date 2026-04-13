from django.shortcuts import render
from .forms import ResumeForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def create_resume(request):
    form = ResumeForm()

    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            template = get_template('resume_template.html')
            html = template.render({'data': form.cleaned_data})

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

            pisa.CreatePDF(html, dest=response)
            return response

    return render(request, 'create_resume.html', {'form': form})