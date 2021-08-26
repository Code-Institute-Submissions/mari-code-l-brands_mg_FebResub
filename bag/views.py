from django.shortcuts import render


def view_bag(request):
    """ A view that renders a bag contents page """
    return render(request, 'bag/bag.html')
