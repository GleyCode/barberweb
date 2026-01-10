from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    """View genérica para a página inicial do painel administrativo."""
    template_name = "barberback_app/index.html"
