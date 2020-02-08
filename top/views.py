import json
import random

from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def index(request):
    return render(request, 'top/index.html', {'max_choices': 5})


def telling(request):
    if request.method == 'GET':
        return JsonResponse({})

    formList = json.loads(request.body)
    records = []
    for record in formList["formList"]:
        records.append(record["form"])
    random.shuffle(records)
    return JsonResponse({"result": records[0]})