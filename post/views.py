from django.views.generic import DetailView
from meta.views import Meta
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
from post.models import Post
from comment.models import Comment
from advertisement.models import Advertisement
from alt_reklam_alani.models import FooterReklami


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'  # Eklediğimiz slug URL parametresini belirtiyoruz

    def get(self, request, *args, **kwargs):    
        try:
            post = self.get_object()

            # Check if the post is published
            if post.yayimlanma_durumu != 'Yayinda':
                raise Http404("Post not found")

            return super().get(request, *args, **kwargs)
        except Post.MultipleObjectsReturned:
            raise Http404("Post not found")

    def get_posts_by_creator(self, author):
        """
        Get all posts by a specific creator.
        """
        return Post.objects.filter(author=author, is_active=True, is_deleted=False)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        # Get the author associated with the post
        author = context['post'].author

        # Call the get_posts_by_creator function
        context['author_posts'] = self.get_posts_by_creator(author)
        
        
        # Get the post associated with the context
        post = context['post']
        
        # Get the latest 3 posts
        posts = Post.objects.filter(
            yayimlanma_durumu='Yayinda',
            is_active=True,
            is_deleted=False
        ).order_by('-post_date')[:3]

        context['posts'] = posts
        
        # Get related posts in the "GIRISIMCILIK" category
        related_posts = Post.objects.filter(
            category__name="GIRISIMCILIK",
            yayimlanma_durumu='Yayinda',
            is_active=True,
            is_deleted=False
        ).exclude(id=post.id)[:13]

        context['related_posts'] = related_posts
        
        # Get the previous and next posts
        previous_post = Post.objects.filter(
            post_date__lt=post.post_date, is_active=True, yayimlanma_durumu='Yayinda'
        ).order_by('-post_date').first()

        next_post = Post.objects.filter(
            post_date__gt=post.post_date, is_active=True, yayimlanma_durumu='Yayinda'
        ).order_by('post_date').first()

        context['previous_post'] = previous_post
        context['next_post'] = next_post

        # Get the comments related to the post
        comments = Comment.objects.filter(target_to_post=post, is_active=True, is_deleted=False)

        # You can further filter or order comments based on your requirements
        # For example, order comments by time_stamp in descending order:
        comments = comments.order_by('-time_stamp')

        context['comments'] = comments
        context['posts'] = posts

            # Get recent posts from the same category
        recent_posts = Post.objects.filter(
            category=post.category,  # Assuming category is a ForeignKey in your Post model
            yayimlanma_durumu='Yayinda',
            is_active=True,
            is_deleted=False
        ).exclude(id=post.id).order_by('-post_date')[:4]  # You can adjust the number of posts to show

        context['recent_posts'] = recent_posts
        
        # Get the advertisements that are not deleted, have not reached their view limit,
        # kampanya_baslangic_tarihi is after today, and kampanya_baslangic_tarihi is not in the past
        current_date = timezone.now().date()
        active_ads = Advertisement.objects.filter(
            is_active=True,
            is_deleted=False,
            max_views_per_image__gt=F('advertisement_ust_resmi_views'),
            kampanya_baslangic_tarihi__lte=current_date
        )

        # Exclude advertisements that have reached their view limit
        active_ads = active_ads.exclude(id__in=context.get('viewed_ad_ids', []))

        # Now, fetch the next advertisement to display
        try:
            advertisement = active_ads.order_by('?').distinct().first()

            if advertisement:
                # Increment the views for the selected advertisement
                advertisement.increment_views('advertisement_ust_resmi')

                # Add the advertisement ID to the viewed_ad_ids in the context
                context.setdefault('viewed_ad_ids', []).append(advertisement.id)
        except Advertisement.DoesNotExist:
            advertisement = None

        context['advertisement'] = advertisement

        context['meta'] = Meta(schema={
            '@type': 'Organization',
            'name': 'My Publisher',
            'logo': Meta(schema={
                '@type': 'ImageObject',
            })
        })
        
        # Check for success message in the query parameters
        success_message = self.request.GET.get('success_message')
        if success_message:
            context['success_message'] = success_message
        
        # context['advertisement_ust'] = Advertisement.objects.filter(is_active=True, is_deleted=False, reklam_gosterim_yeri='Üst').order_by('?').distinct().first()
        context['advertisement_alt'] = FooterReklami.objects.filter(is_active=True, is_deleted=False, reklam_gosterim_yeri='Alt').order_by('?').distinct().first()
        
        return context
    
    def get_image_full_url(self):
        # Provide the logic to get the full URL for the image.
        # Replace 'your_image_field_name' with the actual field name.
        if self.object.haber_baslik_resmi:
            return self.object.haber_baslik_resmi.url
        else:
            # Provide a default URL or handle the case where the image is not available.
            return 'default_image_url'

    
def get_reverse_url(post):
    """
    Generate the reverse URL for the 'post_detail' view.
    """
    return reverse('post:post_detail', kwargs={'slug': post.slug})