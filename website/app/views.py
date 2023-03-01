from django.shortcuts import render
from .models import Brand, Bodywood, Neckwood, Pickups, Color, Order, GuitarPic
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def shop(request):
    brand = ['']+[val.name for val in Brand.objects.filter(enabled=True)]
    bodywood = ['']+[val.name for val in Bodywood.objects.filter(enabled=True)]
    neckwood = ['']+[val.name for val in Neckwood.objects.filter(enabled=True)]
    pickups = ['']+[val.name for val in Pickups.objects.filter(enabled=True)]
    color = ['']+[val.name for val in Color.objects.filter(enabled=True)]

    order_id = Order.objects.last()
    if not order_id:
        order_id = 1
    else:
        order_id = Order.objects.last().id + 1
    context = {
        'order_id': order_id,
        'brand': brand,
        'bodywood': bodywood,
        'neckwood': neckwood,
        'pickups': pickups,
        'color': color
    }
    return render(request, 'shop.html', context)


def about(request):
    return render(request, 'about.html')


def proc(request):
    order_id = request.POST['order_id']
    brand = request.POST['brand']
    bodywood = request.POST['bodywood']
    neckwood = request.POST['neckwood']
    pickups = request.POST['pickups']
    color = request.POST['color']

    name = request.POST['fullname']
    tel = request.POST['tel']
    notes = request.POST['notes']
    date = datetime.now()

    pic = GuitarPic.objects.filter(brand=brand, color=color)
    if pic:
        pic_id = pic.first().id
        pic = pic.first().pic
    else:
        pic_id = 0
        pic = ''

    record = Order.objects.filter(id=order_id)
    if record:
        record.update(brand=brand, bw=bodywood, nw=neckwood, pickups=pickups,
                      color=color, name=name, tel=tel, date=date, notes=notes, pic_id=pic_id)
    else:
        Order.objects.create(id=order_id, brand=brand, bw=bodywood, nw=neckwood, pickups=pickups,
                             color=color, name=name, tel=tel, date=date, notes=notes, pic_id=pic_id)
    # q = Order(brand=brand, bw=bodywood, nw=neckwood,
    #           pickups=pickups, color=color)
    # q.save()

    context = {
        'order_id': order_id,
        'brand': brand,
        'bodywood': bodywood,
        'neckwood': neckwood,
        'pickups': pickups,
        'color': color,
        'name': name,
        'tel': tel,
        'date': date,
        'pic': pic,
    }

    return render(request, 'order.html', context)
