from django.shortcuts import render, redirect
from review.models import Product, Review
from django.http import HttpResponse

# Create your views here.
def index_page(request):
    return render(request, "review/index_page.html")


def product_list(request):
    products = Product.objects.all()

    context = {
        "product_list": products
    }

    return render(request, "review/product_list.html", context=context)


def product_page(request, product_id):

    if request.method == "POST":
        author = request.POST.get('review-author')
        text = request.POST.get('review-text')
        rating = request.POST.get('review-rating')

        if author.strip() != "" and text.strip() != "":
            Review.objects.create(
                product_id=product_id,
                author=author,
                text=text,
                rating=rating
            )

        return redirect(f"/products/{product_id}")

    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product_id=product_id)
    
    context = {
        "reviews": reviews,
        "product": product
    }

    return render(request, "review/product_page.html", context=context)