
from django.http import HttpResponse
from .models import StockCode
# from django.template import loader
# there is a short cut to the above line as follows
from django.shortcuts import render
# this below import is needed for handling resource errors.
from django.http import Http404
#Below library is for reading Website Data
#import the library used to query a website
import urllib2

def index(request):
    all_StockCodes = StockCode.objects.all()
    #These below 4 lines is how you would display data by having html inside the python program file.
    #But now we will comment it out and see how we can move this in to templates..
    # first add the line from django.templates import loader
    # html = ''
    # for Stock in all_StockCodes :
    #    url = '/TopPositivEarning2day/' + str(Stock.id) + '/'
    #    html += '<a href="' + url + '">' + Stock.StockCode + '</a><br>'
    # return HttpResponse(html)
    # Below is the way to do the same thing template way
    # this below line "template =" can be replaced with one statement which is using the render function.
    # template = loader.get_template('TopPositivEarning2day/index.html')
    # Here below is the dictionary. First the template is imported. Then the dictionary. This can be named anything. But Context is the standard.
    context = {
        'all_StockCodes' : all_StockCodes,
    }
    # so the above template line and the below return of a httpresponse can be replaced with a render function. because render has httpresponse built in to it.
    # return HttpResponse(template.render(context, request))
    return render(request,'TopPositivEarning2day/index.html',context)

def detail(request,StockCode_id):
    # replace this standard response with an 404 error if the id does not exist in the database.
    # return HttpResponse("<h2>Details for StockCode Id :" + str(StockCode_id) + "</h2>" );
    try:
        stockcode = StockCode.objects.get(pk=StockCode_id)
    except StockCode.DoesNotExist:
        raise Http404("Stock code does not exist")
    return render(request,'TopPositivEarning2day/detail.html',{'stockcode':stockcode})


def fetchStockCodes():
    #Write the function here to take today's date as input and spit out the positive earnings one.
    #http://www.nasdaq.com/earnings/earnings-calendar.aspx?date=2017-Dec-01
    # take today date and convert it in to "2017-Dec-01" format and then form the url and read through content
    
