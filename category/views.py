from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.utils import timezone
from django.views.generic import DetailView
from category.models import Category
from post.models import Post
from advertisement.models import Advertisement  
from alt_reklam_alani.models import FooterReklami

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'categories'

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            category = self.get_object()
            
            # Seçilen ana kategoriye ait yayınlanan haberler
            category_posts = category.posts.filter(yayimlanma_durumu='Yayinda')
            context['posts'] = category_posts
            
            # Alt kategoriye ait haberler (örneğin, APPLE)
            # girisimcilik_posts = category.posts.filter(category__name="GIRISIMCILIK")
            # context['girisimcilik_posts'] = girisimcilik_posts
         
            girisimcilik_posts = Post.objects.filter(category__name="GIRISIMCILIK", yayimlanma_durumu='Yayinda')
            context['girisimcilik_posts'] = girisimcilik_posts


            # Custom pagination logic:
            page_size = 20  # Define your desired page size
            page = self.request.GET.get('page', 1)  # Get current page from request

            posts = category.posts.filter(yayimlanma_durumu='Yayinda')
            paginator = Paginator(posts, page_size)

            try:
                paginated_posts = paginator.page(page)
            except PageNotAnInteger:
                paginated_posts = paginator.page(1)
            except EmptyPage:
                paginated_posts = paginator.page(paginator.num_pages)

            # Update context with pagination data:
            context['posts'] = paginated_posts
            context['page_range'] = paginator.page_range  # For pagination links
            context['current_page'] = paginated_posts.number

            # Additional context data for pagination UI (optional):
            context['is_paginated'] = paginated_posts.has_other_pages()

            # You can calculate previous and next page URLs using the standard methods
            if paginated_posts.has_previous():
                context['previous_page_url'] = self.request.path + '?page=' + str(paginated_posts.previous_page_number())
            else:
                context['previous_page_url'] = None

            if paginated_posts.has_next():
                context['next_page_url'] = self.request.path + '?page=' + str(paginated_posts.next_page_number())
            else:
                context['next_page_url'] = None
                
                
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
            # context['advertisement_ust'] = Advertisement.objects.filter(is_active=True, is_deleted=False, reklam_gosterim_yeri='Üst').order_by('?').distinct().first()
            context['advertisement_alt'] = FooterReklami.objects.filter(is_active=True, is_deleted=False, reklam_gosterim_yeri='Alt').order_by('?').distinct().first()

            return context



