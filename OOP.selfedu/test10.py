closed_loan_borrowers_count = Borrower.objects.filter(loans__status=2).distinct().count()

borrowers_with_loans_in_2022_count = Borrower.objects.filter(
    loans__created_at__year=2022
).distinct().count()

total_amount_active_loans = Borrower.objects.filter(
    created_at__year=2021,
    loans__status=1
).aggregate(
    total_amount=Sum('loans__amount')
)['total_amount'] or 0