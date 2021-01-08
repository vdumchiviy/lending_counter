from collections import Counter

from django.shortcuts import render, HttpResponse

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    if request.GET.get("from-landing", "") == "original":
        counter_click["original"] = counter_click.get("original", 0) + 1
    elif request.GET.get("from-landing", "") == "test":
        counter_click["test"] = counter_click.get("test", 0) + 1

    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    landing = request.GET.get("ab-test-arg")
    print("landing", landing)

    if landing == "original":
        counter_show["original"] = counter_show.get("original", 0) + 1
        print(f"counter show original: {counter_show.get('original',0)}")
        return render(request, 'landing.html')
    elif landing == "test":
        counter_show["test"] = counter_show.get("test", 0) + 1
        print(f"counter show test: {counter_show.get('test',0)}")
        return render(request, 'landing_alternate.html')
    else:
        return HttpResponse("<H1>There is no such lending")


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    test_click = counter_click.get("test", 0)
    test_show = counter_show.get("test", 0)
    test_conversion = (0 if test_click == 0 else test_show / test_click)
    original_click = counter_click.get("original", 0)
    original_show = counter_show.get("original", 0)
    original_conversion = (0 if original_click ==
                           0 else original_show / original_click)

    original_conversion = (0 if counter_click.get(
        "original", 0) == 0 else counter_show.get("original", 0)/counter_click.get("original", 0))

    return render(request, 'stats.html', context={
        'test_conversion': str(test_conversion),
        'original_conversion': str(original_conversion),
        'test_click': str(test_click),
        'test_show': str(test_show),
        'original_click': str(original_click),
        'original_show': str(original_show)
    })
