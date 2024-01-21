from django.urls import path
from . import views

# A fuking important point:
# prefix of this routes are `app`
# (It taked one day of my time.)
urlpatterns = [
    path('', views.login, name='login'),
    # If this pattern is targeted in an include(),
    # ensure the include() pattern has a trailing '/'.
    path('/master', views.get_master, name='master'),
    path('/plan', views.get_plan, name='get_plan'),
    path('/terms', views.get_terms, name='get_terms'),
    path('/groups', views.get_groups, name='get_groups'),
    path('/items', views.get_items, name='get_items'),
    path('/save', views.save_items, name='save_items'),

]