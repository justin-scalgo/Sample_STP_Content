from django.shortcuts import render,redirect,get_object_or_404
from .models import Content
from .forms import ContentForm
from django.http import JsonResponse
from datetime import datetime 

import json


def add_content(request):
        # return JsonResponse({'list_content': "yyyyy"})
    if request.method == 'POST':
        #json_data = json.loads(request.body.decode('utf-8'))
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            title = json_data['title']
            description = json_data['description']
            #form = ContentForm(json_data)
            if not title or not description:
                return JsonResponse({'status': False, 'message': 'Title and description are required.'})

            content = Content(title=title, description=description)
            content.save()

            data = {
            'id' : content.id,
            'title' : content.title,
            'description' : content.description,
            'createdDate' : content.createdDate.strftime('%B %d, %Y, %H:%M %P')
    
            }
            return JsonResponse({'status': True, 'message': 'Content added successfully.','content': data})
            
        except json.JSONDecodeError as e:
            return JsonResponse({'status': False, 'message': 'Invalid JSON data.', 'error': str(e)})
        except KeyError as e:
            return JsonResponse({'status': False, 'message': 'Missing key in JSON data.', 'error': str(e)})
    else:
        return JsonResponse({'status': False, 'message': 'Invalid method.'})

def edit_content(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        cms_content = get_object_or_404(Content, pk=id)
    
        # form = ContentForm(request.PUT,instance=content)
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Update the CMS content fields
        # cms_content.pk = 'id',
        cms_content.title = title
        cms_content.description = description
        cms_content.createdDate = datetime.now()
        cms_content.save()

        data = {
            'id': cms_content.id,
            'title': cms_content.title,
            'description': cms_content.description,
            'createdDate': cms_content.createdDate.strftime('%B %d, %Y, %H:%M %P'),
            # Other fields if needed
        }
        # Return success response
        return JsonResponse(data)
    # Return error response if the request method is not PUT
    return JsonResponse({'error': 'Invalid request method'})


def delete_content(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        cms_content = get_object_or_404(Content, pk=id)

        # Delete the CMS content only if it exists
        if cms_content:
            deleted_content_id = cms_content.pk
            cms_content.delete()
            return JsonResponse({'status': True, 'message': 'CMS content deleted successfully', 'id': deleted_content_id})
        else:
            return JsonResponse({'status': False, 'message': 'CMS content not found'})

    # Return error response if the request method is not POST
    return JsonResponse({'error': 'Invalid request method'})


def content_list(request):
    contents = Content.objects.all()
    return render(request, 'content_list.html', {'contents': contents})

def fetch_cms_content(request,pk):
    cms_content = get_object_or_404(Content, pk=pk)  # Assuming you have only one CMS content instance

    # Retrieve the CMS content data
    data = {
         'id': cms_content.pk,
        'title': cms_content.title,
        'description': cms_content.description,
    }

    # Return the CMS content data as JSON response
    return JsonResponse(data)


