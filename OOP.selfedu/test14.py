import pandas as pd

df = pd.read_excel('book1.xlsx')

filtered_df = df[df['registration_date'] <= '2021-12-31']

total_loan_amount = filtered_df['amount'].sum()
print("Сумма всех займов для компаний, зарегистрированных не позднее 2021 года:", total_loan_amount)

rating_sum = filtered_df.groupby('rating')['amount'].sum().reset_index()
rating_sum.columns = ['Рейтинг', 'Сумма займов']
print("\nСумма займов для каждого из рейтингов:")
print(rating_sum)
