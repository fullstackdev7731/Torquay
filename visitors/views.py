from django.shortcuts import render
from .forms import (CommentForm, ReservationForm)
from .models import (Reservation, Room, Floor, Comment)
from datetime import date, datetime
from django.db.models import Q
from .utils import str_to_date
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def visitor_homepage(request):
    user = request.user
    context = {}
    if request.method == 'POST':
        reservations_id = request.POST.getlist('reservations')
        comments = request.POST.getlist('text')
        ratings = request.POST.getlist('rating')
        
        for reservations_id, comment, rating in zip(reservations_id, comments, ratings):
            reservation = Reservation.objects.get(id=int(reservations_id))
            Comment.objects.create(reservation=reservation, text = comment, rating = int(rating))

    if user.is_authenticated:
        reservations = user.visitor.reservations.all()
        context['past_reservations'] = reservations.filter(check_out__lt = date.today())
        context['future_reservations'] = reservations.filter(check_in__gt = date.today()).order_by('check_in')
        context['current_reservations'] = reservations.filter(Q(check_in__gte = date.today()) & Q(check_out__gt = date.today()))

        if context['past_reservations'].exists():
            comment_forms = []
            for reservation in context['past_reservations']:
                if not hasattr(reservation, 'comment'):
                    comment_forms.append(CommentForm(initial={'reservation': reservation}))
                else:
                    comment_forms.append(None)
                context['past_and_comments'] = zip(context['past_reservations'], comment_forms)


    return render(request, 'visitor_homepage.html', context)






@login_required
def create_reservation(request):
    context = {'form': ReservationForm(request.POST or None)}

    if 'room' in request.GET:

        room_numbers = request.GET.getlist('room')

        # request.GET.getlist('room')
        date_in = str_to_date(request, 'date_in')
        date_out = str_to_date(request, 'date_out')
        
        size = int(request.session.get('size'))
        

        reservation = Reservation(check_in=date_in, check_out=date_out, active=True)
        reservation.visitor = request.user.visitor
        reservation.save()

        for room_number in room_numbers:
            room = Room.objects.get(number = int(room_number))
            reservation.rooms.add(room)

        print(f"{reservation} WAS CREATED!")

    if request.method == 'POST':
        form_filled = ReservationForm(request.POST)
        if form_filled.is_valid():
            date_in = form_filled.cleaned_data['check_in']
            date_out = form_filled.cleaned_data['check_out']
            size = form_filled.cleaned_data['room_size']

            reservations = Reservation.objects.filter(Q(check_in__lt=date_out) & Q(check_out__gt=date_in))
            rooms_occupied = reservations.values_list('rooms__number', flat=True)
            available_rooms = Room.objects.exclude(number__in = rooms_occupied)

            if available_rooms.exists():
                request.session['date_in'] = date_in.strftime("%Y/%m/%d")
                request.session['date_out'] = date_out.strftime("%Y/%m/%d")
                request.session['size'] = str(size)

                return render(request, 'available_rooms.html', {'rooms': available_rooms})


    return render(request, 'create_reservation.html', context)


# ReservationList (ListView)
# show all reservations per user
# reservations.html

class ReservationList(LoginRequiredMixin, ListView):

    model = Reservation
    context_object_name = 'reservations'
    template_name = 'reservations.html'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):

        user = self.request.user
        all_reservations = super(ReservationList, self).get_queryset(*args, **kwargs)
        user_reservations = all_reservations.filter(visitor = user.visitor)

        return user_reservations.all()
        

class ReservationView(DetailView):
    model = Reservation
    template_name = 'reservation.html'

class RoomView(DetailView):
    model = Room
    template_name = 'room.html'