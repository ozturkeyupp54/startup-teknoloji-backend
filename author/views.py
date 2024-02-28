from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.views.generic import DetailView
from post.models import Post
from category.models import Category
from advertisement.models import Advertisement
from author.models import Author
from alt_reklam_alani.models import FooterReklami

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail.html'
    context_object_name = 'author'

    def get(self, request, slug):
        author = get_object_or_404(Author, slug=slug)
        return render(request, self.template_name, {'author': author})
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        author = self.get_object()
        
        
        # Fetch the Post objects
        post_list = Post.objects.filter(author=author, yayimlanma_durumu='Yayinda')
        paginator = Paginator(post_list, 5)  

        page = self.request.GET.get('page')
        posts = paginator.get_page(page)
        context['posts'] = posts 
        # Get the related posts in the "GIRISIMCILIK" category
        girisimcilik_posts = Post.objects.filter(category__name="GIRISIMCILIK", yayimlanma_durumu='Yayinda', is_active=True, is_deleted=False)[:10]
        context['girisimcilik_posts'] = girisimcilik_posts      
        
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

        # Fetch the next advertisement to display
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
        
        context['advertisement_ust'] = Advertisement.objects.filter(is_active=True, is_deleted=False, reklam_gosterim_yeri='Üst').order_by('?').distinct().first()
        context['advertisement_alt'] = FooterReklami.objects.filter(is_active=True, is_deleted=False, reklam_gosterim_yeri='Alt').order_by('?').distinct().first()
    

        return context