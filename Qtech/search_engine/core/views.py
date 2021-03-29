from django.shortcuts import render
from .models import Keyword,User,Result
from datetime import date, timedelta
from django.db.models import Count
# Create your views here.
def index(request):
    k=Result.objects.values('keyword__name').annotate(count=Count('keyword__name'))
    counts_by_keyword = {d['keyword__name']: d['count'] for d in k}
    u=Result.objects.values('user__name').annotate(count=Count('user__name'))
    counts_by_user = {f['user__name']: f['count'] for f in u}
    d=['Yesterday','Last Week','Last Month']
    context_data={
        'keywords':counts_by_keyword ,
        'users':counts_by_user ,
        'dates':d,
    }
    if request.method=="POST":
        context_data['searched']=True
        query_search=request.POST.get('query')
        print('q: ',query_search)
        result=[]
        if query_search!="":
            print('search')
            q=Result.objects.filter(title__icontains=query_search)|Result.objects.filter(description__icontains=query_search)|Result.objects.filter(keyword__name__icontains=query_search)
            result.append(q)
        key_q=request.POST.getlist('keys')
        if key_q:
            for k in key_q:
                print('keyword')
                q=Result.objects.filter(keyword__name=k)
                result.append(q)
        user_q=request.POST.getlist('creator')
        if user_q:
            for k in user_q:
                print('user')
                q=Result.objects.filter(user__name=k)
                result.append(q)
        date_q=request.POST.getlist('date')
        if date_q:
            print('date')
            print(date_q)
            if "Yesterday" in date_q:
                y=date.today()-timedelta(days=1)
                dy=Result.objects.filter(date__gte=y)
                result.append(dy)
            if "Last Week" in date_q:
                w=date.today()-timedelta(days=7)
                dm=Result.objects.filter(date__gte=w)
                result.append(dm)
            if "Last Month" in date_q:
                m=date.today()-timedelta(days=30)
                dm=Result.objects.filter(date__gte=m)
                result.append(dm)
        start=request.POST.get('start')
        end=request.POST.get('end')
        if start and end:
            print('time')
            dt=Result.objects.filter(date__range=[start,end])
            result.append(dt)
        final_result=result[0].union(*result[1:])
        context_data['results']=final_result

    return render(request,'core/index.html',context=context_data)
