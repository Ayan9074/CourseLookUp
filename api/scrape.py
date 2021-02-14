#import search_courses
#courses=search_courses.simple_search(search_phrase='machine learning',type='list')
#courses = courses[0]
#print(courses)

from youtubesearchpython import Video, ResultMode

video = Video.get('https://www.youtube.com/watch?v=z0GKGpObgPY', mode = ResultMode.dict)
print(video['description'])