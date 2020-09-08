from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse,JsonResponse,QueryDict,Http404
from .models import Item,Bid

# Create your views here.
def home(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, 'epay/home.html', context)

def closedbids(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, 'epay/closedbids.html', context)


def searchView(request):
    return render(request, 'epay/search.html')

def turntoClosed(request):
    user = request.user
    theBool = request.POST.get('bool')
    item = request.POST.get('item')
    QueriedItem = Item.objects.get(id = item)
    QueriedItem.Isopen = theBool
    QueriedItem.save()
    return JsonResponse({
        'Items': "Success"
    })



def bidView(request):
    user = request.user
    bid = request.POST.get('bid')
    item = request.POST.get('item')
    # Add current bidder
    QueriedItem = Item.objects.get(id = item) # Get Object that we are working  on
    if QueriedItem.currentBid < float(bid) and float(bid)>QueriedItem.price:
        QueriedItem.currentBid = float(bid) #Set new field to bid field
        QueriedItem.winner = request.user # sets winner to current user
        QueriedItem.save() # Saves
        # After successfully updating the current bid, a new bid is created to store the details of past bids
        newBid=Bid(bidder = request.user,item =Item.objects.get(id = item),AmountBid = float(bid))
        newBid.save()
    else:
        raise Http404("Bid field is either empty or less than the current bid")
    return JsonResponse({
        'Items': "Success"
    })


def searchView1(request):
    return JsonResponse({
        'Items': list( Item.objects.values()),
    })

def itemDetailView(request,itemId):
    ItemDetail= Item.objects.get(pk=itemId)
    context ={
        'item':ItemDetail
    }
    return render(request,'epay/item_detail.html',context)

def signup(request):
    return render(request, 'epay/signup.html', {'title' : 'signup'})

class ItemListView(ListView):
    model = Item
    template_name = 'epay/home.html'
    context_object_name ='items'
    ordering = ['-date_listed']

class ItemDetailView(DetailView):
    model = Item

class ItemCreateView(LoginRequiredMixin,CreateView):
    model = Item
    fields = ['itemTitle','itemDescription','price','endTime', 'itemPicture']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Item
    fields = ['itemTitle','itemDescription','price','endTime']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            return True
        return False

class ItemDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Item
    success_url = '/'
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            return True
        return False
