# carts/context_processors.py

from .models import CartItem

def cart_summary(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)  # Общее количество товаров
        total = sum(item.product.price * item.quantity for item in cart_items)  # Общая сумма
    else:
        total_quantity = 0
        total = 0.0

    return {
        'total_quantity': total_quantity,
        'total': total,
    }
