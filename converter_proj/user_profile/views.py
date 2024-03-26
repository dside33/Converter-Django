from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from user_profile.models import UserProfile


class ProfileDataView(DetailView):
    model = UserProfile
    template_name = 'profile/user_profile.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        user_profile = UserProfile.objects.filter(id=2)
        context = super().get_context_data(**kwargs)
        context['profile'] = user_profile

        print(context)
        return context