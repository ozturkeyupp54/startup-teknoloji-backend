from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.validators import ValidationError
from django.shortcuts import redirect
from django.urls import reverse
from comment.models import Comment
from post.models import Post
from comment.forms import CommentForm


@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.target_to_post = post
        comment.save()

        # Build the URL with the success_message parameter
        url = reverse('post:post_detail', kwargs={'slug': post.slug})
        url += '?success_message=Comment+successfully+created.'

        # Redirect back to the post_detail page with a success message
        return redirect(url)
    else:
        errors = dict((field, [error for error in errors]) for field, errors in form.errors.items())
        return JsonResponse({'status': 'error', 'errors': errors}, status=400)
