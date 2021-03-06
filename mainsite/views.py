# -*- coding: utf-8 -*-
from django.template.loader import get_template
from datetime import datetime

from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.

def homepage(request):
	
	template = get_template('index.html')
	now=datetime.now()

	posts = Post.objects.all()
	html=template.render(locals())
	
	return HttpResponse(html)
	
def showpost(request, slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug=slug)
		if post != None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')
