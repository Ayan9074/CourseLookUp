from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from youtubesearchpython import PlaylistsSearch, Video
from youtubesearchpython import *
from .forms import NameForm
from django.db.models import Q
from . import search_courses
from pytube import Playlist
# Create your views here.
    
def createbasemodules():
    listtosearch = ['art tutorials','python tutorial', 'java tutorial','chemistry','physics','biology','crashcourse','guitar tutorial']
    for tosearch in listtosearch:
        search = PlaylistsSearch(tosearch, limit = 10, language = 'en', region = 'US')
        result = search.result(mode = ResultMode.dict)['result']
        
        for i in result:
            img = i['thumbnails']
            img = img[0]
            result1 = i['channel']
            try:
                desc = 'Channel Name: ' + result1['name'] + 'Channel Link: ' + result1['link'] + 'Playlist Link: ' + i['link']
            except:
                desc = 'Youtube Playlist'
            obj = Course(title=i['title'], description=desc, link=i['link'], img=img['url'], web='youtube', section=tosearch)
            obj.save()
    for tosearch in listtosearch:
        courses=search_courses.simple_search(search_phrase=tosearch,type='list')
        for i in courses:
            desc = 'Partner: ' + i['partner'] + 'Difficulty: '+i['course_difficulty']+'Type: '+i['type']
            obj = Course(title=i['course_title'], description=desc, link='https://www.coursera.org/search?query='+tosearch, img=i['imgurl'], web='coursera', section=tosearch, rating=i['rating_value'], rating_count=i['rating_count'], enrolnum = i['enrollment_numbers'], difficulty=i['course_difficulty'], Type=i['type'])
            obj.save()

def index(request):
    if request.method == 'POST':
        formres =  ' ' + request.POST['user']
        if request.POST['sortmethod'] == 'alph':
            data0 = Course.objects.filter(Q(title__contains=formres)).order_by('title')
            data1 = {
                "data": data0
            }
        else:
            data0 = Course.objects.filter(Q(title__contains=formres))
            data1 = {
                "data": data0
            }
        return render(request, 'maintemps/searchres.html', data1)
    else:
        data1 = {}
        listtosearch = ['art tutorials','python tutorial', 'java tutorial','chemistry','physics','biology','crashcourse','guitar tutorial']
        data1 = {
            "data": [{'title': 'art tutorials', 'desc':'If you love art and need some free tutorials this section is for you.', 'img':'art.jpg', 'link':'/art'},{'title': 'python tutorial', 'desc':'Do you like programming? Do you want to learn more. Check out some courses base on what you might like', 'img':'program.jpg', 'link':'/python'}, {'title': 'java tutorial', 'desc':'Do you like programming? Do you like coding in Java even more. How about you check out some courses on Java then', 'img':'java.jpg', 'link':'/java'},{'title': 'chemisty', 'desc':'Is chemisty your thing. Do you enjoy learning about atoms, how about you take a course on chemistry?', 'img':'chemistry.jpg', 'link':'/chemistry'},{'title': 'physics', 'desc':'Enjoy learning about newtons laws? Like chemical engineering, a course on physics might be fun?', 'img':'physics.jpg', 'link':'/physics'},{'title': 'biology', 'desc':'Do you like learning about anatomy? A biology course might be fun', 'img':'biology.jpg', 'link':'/biology'},{'title': 'crashcourse', 'desc':'Wanna take a crashcourse on a random topic? This is for you then', 'img':'crashcourse.jfif', 'link':'/crashcourse'},{'title': 'guitar tutorial', 'desc':'Like instruments? Favor guitar? Learn some more with a course here', 'img':'guitars.jpg', 'link':'/guitar'}]
        }
    return render(request, 'maintemps/homepage.html', data1)


def section(request, sector):
    if request.method == 'POST':
        formres = request.POST['user']
        if request.POST['sortmethod'] == 'alph':
            data0 = Course.objects.filter(Q(title__contains=formres)).order_by('title')
            data1 = {
                "data": data0
            }
        else:
            data0 = Course.objects.filter(Q(title__contains=formres))
            data1 = {
                "data": data0
            }
        return render(request, 'maintemps/searchres.html', data1)
    else:
        if Course.objects.all().count() == 0:
            createbasemodules()
        if sector == 'art':
            chosensector = 'art tutorials'
        elif sector == 'python':
            chosensector = 'python tutorial'
        elif sector == 'java':
            chosensector = 'java tutorial'
        elif sector == 'chemistry':
            chosensector = 'chemistry'
        elif sector == 'physics':
            chosensector = 'physics'
        elif sector == 'biology':
            chosensector = 'biology'
        elif sector == 'crashcourse':
            chosensector = 'crashcourse'
        elif sector == 'guitar':
            chosensector = 'guitar tutorial'
        data0 = Course.objects.all()
        data1 = {
            "data": data0,
            "sector": chosensector
        }
        return render(request, 'maintemps/index.html', data1)

def specific(request, title):
#   try:
    data = Course.objects.get(id=title)
    data1 = {'data':data}
    if data.web == 'youtube':
        p = Playlist(data.link)
        datam = {}
        i = 0
        datam['link'] = data.link
        for url in p.video_urls[:3]:
            video = Video.get(url, mode = ResultMode.dict)
            datam['title'+str(i)] = video['title']
            datam['rating'+str(i)] = video['averageRating']
            datam['desc'+str(i)] = video['description']
            img = video['thumbnails']
            img = img[0]
            datam['img'+str(i)] = img['url']
            viewcount = video['viewCount']
            datam['vc'+str(i)] = viewcount['text']
            i+=1
        return render(request, 'maintemps/coursedetailyoutube.html', datam)
    else:
        return render(request, 'maintemps/coursedetailcoursera.html', data1)
#    except:
        #return HttpResponse('error')