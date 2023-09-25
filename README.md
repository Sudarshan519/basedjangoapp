# basedjangoapp
alias migrate="python manage.py makemigrations;python manage.py migrate"
alias serve="python manage.py runserver"


from django.db.models import Sum, F

# Query to calculate the total price for each product
product_list = Product.objects.annotate(
    total_price=Sum(F('order__quantity') * F('price'), distinct=True)
)

# Print the result
for product in product_list:
    print(f"Product: {product.name}, Total Price: {product.total_price}")