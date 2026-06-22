from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

# 1. Show all movies in the table list
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'show.html', {'movies': movies})

# 2. Add a new movie (Simplified method capturing raw HTML inputs)
def add_movie(request):
    if request.method == 'POST':
        Movie.objects.create(
            title=request.POST.get('html_title'),
            director=request.POST.get('html_director'),
            movie_type=request.POST.get('html_type'),
            rating=request.POST.get('html_rating')
        )
        return redirect('movie_list')
    return render(request, 'add_movie_simple.html')

# 3. Edit an existing movie row
def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == 'POST':
        # Update the database fields manually with the edited values
        movie.title = request.POST.get('html_title')
        movie.director = request.POST.get('html_director')
        movie.movie_type = request.POST.get('html_type')
        movie.rating = request.POST.get('html_rating')
        movie.save()
        return redirect('movie_list')
        
    return render(request, 'add_movie_simple.html', {'movie': movie})

# 4. Delete a specific movie row
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
    return redirect('movie_list')