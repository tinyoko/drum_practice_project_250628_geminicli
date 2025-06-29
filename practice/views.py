from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Score
from django.http import JsonResponse
import json

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'practice/song_list.html', {'songs': songs})

def upload_song(request):
    if request.method == 'POST':
        title = request.POST['title']
        audio_file = request.FILES['audio_file']
        pdf_file = request.FILES['pdf_file']
        
        song = Song.objects.create(title=title, audio_file=audio_file)
        Score.objects.create(song=song, pdf_file=pdf_file)
        
        return redirect('song_list')
    return render(request, 'practice/upload_song.html')

def practice_view(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    score = get_object_or_404(Score, song=song)
    page_timings_json = json.dumps(score.page_timings)
    return render(request, 'practice/practice_view.html', {
        'song': song, 
        'score': score,
        'page_timings_json': page_timings_json
    })

def save_timings(request, score_id):
    if request.method == 'POST':
        score = get_object_or_404(Score, pk=score_id)
        timings = json.loads(request.body).get('timings', [])
        score.page_timings = timings
        score.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)