from django.shortcuts import render, redirect
from .forms import InputFormStas
from .models import StasInputFile
import json


def index(request):
    if request.method == 'POST':
        form = InputFormStas(request.POST)
        if form.is_valid():
            # Take data from the initial form
            name_input = form.cleaned_data['name0']
            # Convert to json type
            data = json.dumps(name_input, ensure_ascii=False)
            # Create object
            StasInputFile.objects.create(data=data, field='name0')

            # Loop take data from other form
            for count in range(1, len(request.POST) - 1):
                query = 'name' + str(count)
                input_value = request.POST[query]
                # Check for empty field
                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    StasInputFile.objects.create(data=data, field=field)
                count += 1
        return redirect('base')
    else:
        form = InputFormStas()
    return render(request, 'app_stasik/index.html', {'form': form})


def base(request):
    # Take data from the db
    query = StasInputFile.objects.all().values('id', 'field', 'data')
    json_list = list(query)
    return render(request, 'app_stasik/base.html', {'json_list': json_list})
