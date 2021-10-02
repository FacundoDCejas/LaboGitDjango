from django.shortcuts import render

def index(request,template_name="tienda/index.html"):
    return (request,template_name)