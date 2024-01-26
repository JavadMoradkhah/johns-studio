from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models import Count, F, ExpressionWrapper, IntegerField
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST, require_GET
from .models import Slide, User, Service, Category, Portfolio, InstagramPost, ContactInfo
from .forms import ContactForm


@require_GET
def home_page(request):
    slides = Slide.objects.select_related('portfolio').order_by('-created').all()[:12]

    context = {'slides': slides}
    return render(request, 'core/index.html', context)


@method_decorator(require_POST, name='dispatch')
class MessageCreateView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('home')


@require_GET
def about_page(request):
    admin = User.objects.select_related('profile').get(is_superuser=True)
    services = Service.objects.all()
    instagram_posts = InstagramPost.objects.select_related('portfolio').order_by(
        '-created'
    ).all()[:10]

    portfolio_count = Portfolio.objects.count()

    category_stats = Category.objects.annotate(
        portfolio_count=Count('portfolio')
    ).annotate(
        usage=ExpressionWrapper(F('portfolio_count') * 100 / portfolio_count, output_field=IntegerField())
    ).filter(portfolio_count__gte=1).order_by('-portfolio_count').all()[:4]

    context = {
        'admin': admin,
        'services': services,
        'category_stats': category_stats,
        'instagram_posts': instagram_posts
    }

    return render(request, 'core/about-me.html', context)


@require_GET
def portfolio_page(request, category='all'):
    categories = Category.objects.order_by('name').all()

    portfolio = Portfolio.objects.select_related('category')

    if category != 'all':
        portfolio = portfolio.filter(category__slug=category)

    portfolio = portfolio.order_by('-updated', '-created').all()[:12]

    context = {
        'categories': categories,
        'portfolio': portfolio,
        'active_category': category
    }

    return render(request, 'core/portfolio.html', context)


@require_GET
def contact_page(request):
    instagram_posts = InstagramPost.objects.select_related('portfolio').order_by(
        '-created'
    ).all()[:10]

    context = {
        'instagram_posts': instagram_posts
    }

    return render(request, 'core/contact.html', context)
