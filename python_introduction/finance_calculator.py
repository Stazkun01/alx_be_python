# finance_calculator.py

# Demande les revenus et dépenses mensuels à l'utilisateur
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calcul des économies mensuelles
monthly_savings = monthly_income - monthly_expenses

# Taux d'intérêt annuel simple
interest_rate = 0.05

# Projection des économies annuelles avec intérêts
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

# Affichage des résultats
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
