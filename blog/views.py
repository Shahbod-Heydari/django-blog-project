from datetime import date
from django.shortcuts import render

# Create your views here.


all_posts = [
    {
        'slug': 'learning-django',
        'title': 'Django course',
        'author': 'Shahbod',
        'image': 'django.jpg',
        'date':date(2026,9,18),
        'short_description': 'special python framework',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam at dignissimos dolores, 
        doloribus ducimus eaque, eius fugiat in ipsam libero magnam maiores neque perferendis 
        placeat quae recusandae repudiandae similique voluptate.
        ''',
    },
    {
        'slug': 'learning-git',
        'title': 'git course',
        'author': 'Mohammad',
        'image': 'git.jpg',
        'date':date(2024,9,18),
        'short_description': 'version control system',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam at dignissimos dolores, 
        doloribus ducimus eaque, eius fugiat in ipsam libero magnam maiores neque perferendis 
        placeat quae recusandae repudiandae similique voluptate.
        ''',
    },
    {
        'slug': 'learning-python',
        'title': 'Python course',
        'author': 'Shahbod',
        'image': 'python.jpg',
        'date':date(2020,9,18),
        'short_description': 'programming language',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam at dignissimos dolores, 
        doloribus ducimus eaque, eius fugiat in ipsam libero magnam maiores neque perferendis 
        placeat quae recusandae repudiandae similique voluptate.
        ''',
    },
    {
        'slug': 'learning-cpp',
        'title': 'c++ course',
        'author': 'Hossein',
        'image': 'c++.jpg',
        'date':date(2025,9,18),
        'short_description': 'programming language',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam at dignissimos dolores, 
        doloribus ducimus eaque, eius fugiat in ipsam libero magnam maiores neque perferendis 
        placeat quae recusandae repudiandae similique voluptate.
        ''',
    },
    {
        'slug': 'learning-potgreSQL',
        'title': 'postgreSQL course',
        'author': 'Shahbod',
        'image': 'postgresql.png',
        'date':date(2021,9,18),
        'short_description': 'relational database management system',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam at dignissimos dolores, 
        doloribus ducimus eaque, eius fugiat in ipsam libero magnam maiores neque perferendis 
        placeat quae recusandae repudiandae similique voluptate.
        ''',
    }
]

# Sort posts by publication date.
def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(all_posts,key = get_date)

    # Select the two most recent posts for the home page.
    latest_post = sorted_posts[-2:] # use for contex arg
    return render(request, 'blog/index.html',{'latest_post':latest_post})

def post(request):
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/all-posts.html',context)

def single_post(request,slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    context = {
        'post': post
    }
    return render(request, 'blog/post-details.html',context)