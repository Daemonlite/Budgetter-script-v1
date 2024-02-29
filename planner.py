import calendar
import datetime
from test import send_notification


class Budgetter:
    def calculate_transport(self, transport_fare):
        now = datetime.datetime.now()
        days = sum(
            1
            for day in range(1, calendar.monthrange(now.year, now.month)[1] + 1)
            if datetime.date(now.year, now.month, day).weekday() < 5
        )
        transport = days * transport_fare
        print(days)
        return transport

    def calculate_budget(self, salary, transport):
        main_savings = salary * 0.25
        rent_savings = salary * 0.10
        pocket_money = salary * 0.25
        clothing = salary * 0.10

        budget = salary - main_savings - rent_savings - pocket_money - clothing
        fare = self.calculate_transport(transport)
        remainder = budget - fare

        return {
            "lorry_fare": fare,
            "main_savings": main_savings,
            "rent_savings": rent_savings,
            "pocket_money": pocket_money,
            "clothing": clothing,
            "remaining": remainder,
        }


save = Budgetter()


def main():
    # Assuming user inputs monthly earnings
    earnings_monthly = float(input("Enter your monthly earnings: "))

    # Assuming user inputs daily transport cost
    transport_cost_daily = float(input("Enter your daily transport cost: "))

    budget = save.calculate_budget(earnings_monthly, transport_cost_daily)

    print("\nBudget Breakdown:")
    print(f"Transport Fare: {budget['lorry_fare']}")
    print(f"Main Savings: {budget['main_savings']} cedis")
    print(f"Savings towards Rent: {budget['rent_savings']} cedis")
    print(f"Pocket money for the month: {budget['pocket_money']} cedis")
    print(f"Clothing: {budget['clothing']} cedis")
    print(f"Remaining amount: {budget['remaining']}")

    message = f"Dear Eugene,\nThis is your budget breakdown for the month:\n1. Transport Fare: {budget['lorry_fare']} cedis\n2. Main Savings: {budget['main_savings']} cedis\n3. Savings towards Rent: {budget['rent_savings']} cedis\n4. Pocket money for the month: {budget['pocket_money']} cedis\n5. Clothing: {budget['clothing']} cedis\nRemaining amount: {budget['remaining']}"


    send_notification(recipient="0209414099", message=message)


if __name__ == "__main__":
    main()
