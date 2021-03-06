import random
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django_user_agents.utils import get_user_agent
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from english_words import english_words_lower_alpha_set

from keyboard.models import DataCollectionSwipe, DeviceType
from keyboard.serializers import DataCollectionSwipeSerializer
from keyboard.validators import trace_matches_target_text

@login_required()
def game(request):
    context = {'is_mobile': request.user_agent.is_mobile}
    return render(request=request, template_name='keyboard/game.html', context=context)


@require_http_methods(['GET'])
def random_word(request):
    word_list = list(english_words_lower_alpha_set)
    word = random.choice(word_list)
    return JsonResponse({'word': word})


class DataCollectionSwipeViewSet(viewsets.ModelViewSet):
    queryset = DataCollectionSwipe.objects.all()
    serializer_class = DataCollectionSwipeSerializer
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Add additional fields to serializer before saving."""
        trace_matches_text = trace_matches_target_text(
            trace=serializer.validated_data['trace'],
            target_text=serializer.validated_data['target_text']
        )
        serializer.save(
            user=self.request.user,
            trace_matches_text=trace_matches_text,
            device_type=self._get_device_type()
        )

    def _get_device_type(self) -> DeviceType:
        user_agent = get_user_agent(self.request)
        if user_agent.is_mobile:
            device_type = DeviceType.MOBILE
        elif user_agent.is_tablet:
            device_type = DeviceType.TABLET
        elif user_agent.is_pc:
            device_type = DeviceType.PC
        else:
            device_type = DeviceType.OTHER
        return device_type
