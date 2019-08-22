import requests
import requests_with_caching
import json
import operator
def get_movie_data(movie_name):
    baseurl="http://www.omdbapi.com/"
    dictionry={"t": movie_name,"r": "json"}
    output_recom=requests.get(baseurl,params=dictionry)   
    prin=json.loads(output_recom.text)
    #print(prin)
    return prin
def get_movie_rating(movie_detail_dict):
    for diff_raters in movie_detail_dict["Ratings"]:
        for rater in diff_raters:
            #print(rater)
            #print(diff_raters)
            if diff_raters[rater]=="Rotten Tomatoes":
                return int(diff_raters["Value"][:-1])
    return 0
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

def get_movies_from_tastedive(movie_name):
    baseurl="https://tastedive.com/api/similar"
    dictionry={"q": movie_name,"type": "movies", "limit" : 5}
    output_recom=requests.get(baseurl,params=dictionry)   
    prin=json.loads(output_recom.text)
    #print(prin)
    return prin
def extract_movie_titles(prin):
    recommendations=[]
    for i in range(0,5):
        recommendations.append(prin['Similar']['Results'][i]['Name'])
    return recommendations
def remove(mov_lst): 
    fin_lst=[] 
    for mov_name in mov_lst: 
        if mov_name not in fin_lst: 
             fin_lst.append(mov_name) 
    return fin_lst
def get_related_titles(list_of_movies):
    rel_list=[]
    for movie in list_of_movies:
        rel_list=rel_list+extract_movie_titles(get_movies_from_tastedive(movie))
    fin_list=remove(rel_list)
    #print(fin_list)
    return fin_list
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

def get_sorted_recommendations(list_of_movies):
    ratings=[]
    outputlist=get_related_titles(list_of_movies)
    
    for movie in outputlist:
        ratings.append(get_movie_rating(get_movie_data(movie)))
    print(ratings)
    tup=zip(outputlist,ratings)
    print(tup)
    #sorted_movie_list=zip(outputlist,ratings)
    rat=sorted(tup,key=lambda x:x[1],reverse=True)
    print(rat)
    return rat
