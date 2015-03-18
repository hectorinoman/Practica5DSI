from django.shortcuts import render_to_response

def quick_test(request):
	return render_to_response("blog.html", {})