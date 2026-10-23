from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectMetricForm
from .models import ProjectMetric


def home_view(request):
  if request.method == 'POST':
    form = ProjectMetricForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = ProjectMetricForm()

  metrics = ProjectMetric.objects.all()

  context = {
      'username': "Brian Ong'ayo",
      'role': "Founder & CEO",
      'framework': "Django 6.1",
      'metrics': metrics,
      'form': form,
  }
  return render(request, 'index.html', context)


# New Delete View
def delete_metric(request, pk):
  metric = get_object_or_404(ProjectMetric, pk=pk)
  metric.delete()  # Deletes record from SQLite database
  return redirect('home')
