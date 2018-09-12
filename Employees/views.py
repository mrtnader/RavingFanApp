from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Person
from .forms import PersonForm


# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
    )

class employeeList(ListView):
  model = Person
  template_name = 'employeeApp/employeeList.html'
  queryset = Person.objects.all()

  def dispatch(self, *args, **kwargs):
    return super(employeeList, self).dispatch(*args, **kwargs)


class employeeSearch(FormView):
  model = Person
  form = PersonForm()

  def form_valid(self, form):
    return super(employeeSearch, self).form_valid(form)

  def form_invalid(self, form):
    return super(employeeSearch, self).form_invalid(form)

    
'''
Now in HTML we have the context object of form
{{form}}
'''