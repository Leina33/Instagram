from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

#date function
def instagram_of_day(request):
    date = dt.date.today()
    return render(request, 'display/home.html',{'date': date})



def past_days_instagram(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(instagram_of_day)

    return render(request, 'display/index.html', {"date":date})
    


