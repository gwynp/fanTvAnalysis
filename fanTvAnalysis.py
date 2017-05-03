from bs4 import BeautifulSoup
from xml.etree import ElementTree
import requests
import time
import datetime
from datetime import date, timedelta
import urllib2
import os
import pprint
import collections
import httplib
import urllib2
import json


# get the youtube from the environment
youtube_key = os.environ.get('YOUTUBE_KEY')

# Opens the statistics page for a youtube video
# reads in the json and extracts the views, comments and likes
# sample url: 
# https://www.googleapis.com/youtube/v3/videos?part=statistics&id=vGLJoJaMB6g&key=<youtube_api_key>
def getVideoStats(video_stub):
	stats_url_prefix='https://www.googleapis.com/youtube/v3/videos?part=statistics'
	stats_url = stats_url_prefix + '&id=' + video_stub + '&key=' + youtube_key
	opener = urllib2.build_opener()
	f = opener.open(stats_url)
	json_data = json.loads(f.read())
	for i in json_data["items"]:
		stats=i["statistics"]
		views=stats["viewCount"]
		likes=stats["likeCount"]
		comments=stats["commentCount"]
		return views, likes, comments

#curl https://www.googleapis.com/youtube/v3/videos?part=statistics\&id=vGLJoJaMB6g\&key=AIzaSyD0yfLmQjtus-EzjqXP4orxTLJVbllWihg

video_stub='vGLJoJaMB6g'
(views,likes,comments)=getVideoStats(video_stub)