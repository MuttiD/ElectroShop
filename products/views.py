from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# 'Q' an object to generate search queries. either product name or description.
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, SubCategory

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    query = None
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    sort = None
    direction = None

    if request.GET:

        # sorting element by name and direction (ascendent or descendent)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # filter the category & name IN the categories list
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=[str(categories) for category in categories])

        if 'subcategory' in request.GET:
            subcategories = request.GET.getlist('subcategory')

            categories = Category.objects.filter(subcategory__name__in=subcategories).distinct()
            subcategories = SubCategory.objects.filter(name__in=subcategories)

            products = products.filter(subcategory__name__in=subcategories.values('name'))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria.")
                return redirect(reverse('products'))

            # a query containing name OR description. 'i' means insentitive on typing
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show details of products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
