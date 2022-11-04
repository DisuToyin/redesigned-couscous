from django.shortcuts import render, redirect
from .models import Project
# Create your views here.
from .forms import ProjectForm

def projects(request):
    project_list = Project.objects.all()
    result = {"projects": project_list}
    return render(request, "projects/projects.html", result)

def single_project(request, pk):
    project = Project.objects.get(id=pk)
    # project_tags = project.objects.all() 
    result={"project":project }
    return render(request, "projects/single.html", result)

def create_project(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/")

    context={"form": form}
    return render(request, "projects/project_form.html", context)

def update_project(request, pk):
    projectInstance = Project.objects.get(id=pk)
    form = ProjectForm(instance=projectInstance)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=projectInstance)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/")

    context={"form": form}
    return render(request, "projects/project_form.html", context)


def delete_project(request, pk):
    projectInstance = Project.objects.get(id=pk)

    if request.method=="POST":
        projectInstance.delete()
        return redirect("http://127.0.0.1:8000/")

    context={"object": projectInstance}
    return render(request, "projects/delete_template.html", context)