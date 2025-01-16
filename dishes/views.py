from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from dishes.models import Dish, Cook, DishType
from dishes.forms import CookCreationForm, CookUpdateForm
from django.contrib.auth.models import User


@login_required
def index(request):
    latest_dishes = Dish.objects.all().order_by('-id')[:3]
    dish_types = DishType.objects.all()
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits

    context = {
        "num_dishes": Dish.objects.count(),
        "num_cooks": Cook.objects.count(),
        "num_dish_types": dish_types.count(),
        "latest_dishes": latest_dishes,
        "num_visits": num_visits,
    }
    return render(request, "dishes/index.html", context)

if not User.objects.filter(username='testuser').exists():
    User.objects.create_user(
        username='testuser',
        email='testuser@test.com',
        password='test123'
    )
    print("Test user created: testuser")
else:
    print("Test user already exists.")



class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "dishes/dish_type_list.html"
    paginate_by = 5


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "dishes/dish_type_detail.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("dishes:dish-type-list")
    template_name = "dishes/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("dishes:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("dishes:dish-type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = "dishes/dish_list.html"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "dishes/dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("dishes:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("dishes:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("dishes:dish-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    template_name = "dishes/cook_list.html"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "dishes/cook_detail.html"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("dishes:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("dishes:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("dishes:cook-list")


def about(request):
    return render(request, 'dishes/about.html')


def contact(request):
    return render(request, 'dishes/contact.html')


def toggle_assign_to_dish(request, pk):
    cook = Cook.objects.get(user=request.user)
    dish = get_object_or_404(Dish, id=pk)

    if dish in cook.dishes.all():
        cook.dishes.remove(dish)
    else:
        cook.dishes.add(dish)

    return HttpResponseRedirect(reverse_lazy("chef:menu-detail", args=[pk]))
