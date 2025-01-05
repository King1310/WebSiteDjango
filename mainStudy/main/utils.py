from django.db.models import Q

from main.models import Product
from main.views import product
from numba.scripts.generate_lower_listing import description
from pygments.lexers.srcinfo import keywords
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    vector = SearchVector("name")
    query = SearchQuery(query)

    return Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

#    keywords = [word for word in query.split() if len(word) > 2]
#
#    q_objects = Q()
#
#    for token in keywords:
#        q_objects |= Q(name__icontains=token)
#
#    return Product.objects.filter(q_objects)