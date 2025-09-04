from django.shortcuts import get_list_or_404, render
from .models import StructureInventory

def default(request):
    # des = get_list_or_404(StructureInventory, DEExtID=DEExtID)
    # print(des)
    des = StructureInventory.objects.all()[:5]
    return render(request, template_name='db_example/base.html', context={'des': des})
