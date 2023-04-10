from django.urls import path
from .views import HomePortfolioListView, PortfolioDetailView, PortfolioCreateView

urlpatterns = [
    path('', HomePortfolioListView.as_view(), name='index'),
    path('portfolio_detailed/<int:pk>', PortfolioDetailView.as_view(), name='portfolio_details'),
    path('add_portfolio', PortfolioCreateView.as_view(), name='add_portfolio'),
]

# этот name пишется в html странице в поле для перехода в другую html, а вьюшка которая тут прописана как раз таки указывает в какую именно html мы попадаем
# 'portfolio_detailed название обязательно должен совпадать с шаблоном html
