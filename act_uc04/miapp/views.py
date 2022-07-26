from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
<h1> Proyecto Web (LP3) | roxana  </h1>
<hr>
<ul>
        <li>
        <a href="/intregrantes"> Integrantes</a>
        </li>
        <li>
        <a href="/saludo"> Mensaje de saludo</a>
        </li>
        <li>
       
</ul>
</hr>
"""
def index(request):
    integrantes=['Roxana Condori Condori',                
                'Ricardo Pablo Trigo Suarez',
                'Fernando Acuña Saavedra',                
                ]
   

    return render(request,'index.html', {
        'titulo':'Integrantes',
        'integrantes':integrantes
    })
def saludo(request):
    
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        
    })

