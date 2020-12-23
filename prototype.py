class Budget:
    def __init__(self):
        self.annual_salary = 0
        self.weekly_pay = 0
        self.NIC_contributions = 0
        self.tax = 0
        self.net_pay = 0
        self.net_pay_weekly = 0
        self.pension_contributions = 0

    def set_income(
        self,
        annual_salary: float = 0,
        hourly_rate: float = 0,
        hours_per_week: float = 0,
    ):
        if annual_salary:
            self.annual_salary = annual_salary
            self.weekly_pay = annual_salary / 52
        elif hourly_rate and hours_per_week:
            self.weekly_pay = hourly_rate * hours_per_week
            self.annual_salary = self.weekly_pay * 52
        else:
            return None
        return None

    def _calculate_NICs(self):
        self.NIC_contributions = 0
        zero_rated = 8632
        to_contribute = self.annual_salary - self.pension_contributions
        first_rate = to_contribute - zero_rated
        second_rate = to_contribute - 50000
        if first_rate > 0 and first_rate <= 50000 - zero_rated:
            self.NIC_contributions += first_rate * 0.12
        elif first_rate > 0 and first_rate > 50000 - 8632:
            self.NIC_contributions += 50000 * 0.12

        if second_rate > 0:
            self.NIC_contributions += second_rate * 0.02

    def _calculate_tax(self):
        self.tax = 0
        allowance = 12500 + self.pension_contributions
        taxable_income = self.annual_salary - allowance
        normal_rate = taxable_income * 0.2
        higher_rate = (taxable_income - 37500) * 0.4
        additional_rate = (taxable_income - 150000) * 0.45
        if normal_rate > 0:
            self.tax += normal_rate
        if higher_rate > 0:
            self.tax += higher_rate
        if additional_rate > 0:
            self.tax += additional_rate

    def add_pension(self, amount: float = 0, kind: str = 'weekly'):
        if kind == 'weekly':
            self.pension_contributions = amount*52
        elif kind == 'monthly':
            self.pension_contributions = amount*12
        elif kind == 'annual':
            self.pension_contributions = amount
        else:
            print('kind must be one of: weekly, monthly, annual')
    
    def calculate_net_pay(self):
        self._calculate_NICs()
        self._calculate_tax()
        self.net_pay = self.annual_salary - self.tax - self.NIC_contributions - self.pension_contributions
        self.net_pay_weekly = self.net_pay/52

    def display_calculations(self):
        for i in [
            self.annual_salary,
            self.weekly_pay,
            self.pension_contributions,
            self.NIC_contributions,
            self.tax,
            self.net_pay,
            self.net_pay_weekly
        ]:
            print(i)


b = Budget()
b.set_income(hourly_rate=14.75, hours_per_week=40)
b.add_pension(amount=26.55, kind='weekly')
b.calculate_net_pay()
b.display_calculations()
