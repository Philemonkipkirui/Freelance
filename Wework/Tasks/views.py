from django.shortcuts import render, redirect
from .task_form import task_data
from .models import Task
from django.utils.timezone import now

def index(request):
    form = task_data()
    tasks = Task.objects.filter(due_date__gte=now()).order_by('-created_at')
    return render(request, "index.html", {'form': form, 'tasks': tasks})


def task_info(request):
    form = task_data(request.POST or None)
    if request.method  == "POST" and form.is_valid():
        form.save()
        return redirect('index')

    return render(request , "task_form.html" , {'form':form})



from django.core.paginator import Paginator

from django.utils.timezone import now
from django.core.paginator import Paginator
from .models import Task

def ajax_filter_tasks(request):
    filter_type = request.GET.get('filter', 'all')
    page_number = request.GET.get('page', 1)

    # --- UPDATE TASK STATUSES BASED ON DUE DATE ---
    overdue_tasks = Task.objects.filter(
        due_date__lt= now(),
        status__in=['pending', 'in progress']
    )
    overdue_tasks.update(status='overdue')  # Bulk update for performance

    # --- FILTERING LOGIC ---
    if filter_type == 'priority':
        priority_order = {'high': 1, 'medium': 2, 'low': 3}
        tasks = Task.objects.filter(priority__isnull=False)
        tasks = [t for t in tasks if t.priority.lower() in priority_order]
        tasks = sorted(tasks, key=lambda t: priority_order.get(t.priority.lower(), 99))

    elif filter_type == 'due':
        tasks = Task.objects.filter(due_date__gte=now()).order_by('due_date')

    elif filter_type == 'status':
        status_order = {'in progress': 1, 'pending': 2, 'overdue': 3, 'completed': 4, 'cancelled': 5}
        tasks = Task.objects.filter(status__isnull=False)
        tasks = [t for t in tasks if t.status.lower() in status_order]
        tasks = sorted(tasks, key=lambda t: status_order.get(t.status.lower(), 99))

    else:
        tasks = Task.objects.filter(due_date__gte=now()).order_by('-created_at')

    paginator = Paginator(tasks, 5)
    page_obj = paginator.get_page(page_number)

    return render(request, 'task_cards.html', {
        'tasks': page_obj.object_list,
        'has_next': page_obj.has_next(),
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })

from django.shortcuts import get_object_or_404

def task_page(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_page.html', {
        'task': task
    })
