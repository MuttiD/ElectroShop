from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse

from .models import Product, Category, SubCategory, Comment
from testimonials.models import Testimonial
from .forms import ProductForm, CommentForm
from testimonials.forms import TestimonialForm


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
    comments = product.comments.all()

    testimonials = product.testimonials.all()

    context = {
        'product': product,
        'comments': comments,
        'comment_form': CommentForm(),
        'testimonials': testimonials,
        'testimonial_form': TestimonialForm(),
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


class CustomSuccessMessageMixin(SuccessMessageMixin):
    """ A Class to handle success messages """

    success_message = ""


@login_required
def add_comment(request, product_id):
    """ Handles the creating of comments by users """
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            messages.success(request, 'Comment added successfully')
            return HttpResponseRedirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Comment creation failed. Please check the form.')

@login_required
def update_comment(request, comment_id):
    """ Handles comments updates """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully')
            return HttpResponseRedirect(reverse('product_detail', args=[comment.product.id]))
        else:
            messages.error(request, 'Comment update failed. Please check the form.')

    return redirect(reverse('product_detail', args=[comment.product.id]))

@login_required
def delete_comment(request, comment_id):
    """ Handles deletion of comments """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully')

    return redirect(reverse('product_detail', args=[comment.product.id]))

