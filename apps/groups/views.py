from django.shortcuts import render

# Create your views here.
def groups(request):
    return render(request, 'groups/groups.html')

def group_detail(request):
    pass

def group_members(request):
    pass