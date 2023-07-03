
Если вам требуется сохранить две отдельные функции api_increase_a и api_increase_b, вы можете использовать аннотацию F() для обновления полей атомарно в пределах одной транзакции. Это позволит избежать возможных проблем с параллельным доступом и несогласованностью данных.

Вот исправленный код без объединения функций:

python
Copy code
from django.db.models import F

@api_view(['POST'])
@transaction.atomic
def api_increase_a(request, investor_id):
    investor = get_object_or_404(Investor, pk=investor_id)
    investor.a = F('a') + 100
    investor.save()
    return Response({"status": "OK"})


@api_view(['POST'])
@transaction.atomic
def api_increase_b(request, investor_id):
    investor = get_object_or_404(Investor, pk=investor_id)
    investor.b = F('b') + 100
    investor.save()
    return Response({"status": "OK"})
В обновленном коде мы использовали аннотацию F() для обновления полей a и b с использованием текущих значений полей в базе данных. Это позволяет обновлять поля атомарно в пределах одной транзакции без необходимости объединения функций.