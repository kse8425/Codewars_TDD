class BuyCar:
    def __init__(self, start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
        self.old_car = start_price_old
        self.new_car = start_price_new
        self.saving_per_month = saving_per_month
        self.loss = percent_loss_by_month
        self.month = 0

    def _next_month(self):
        self.month += 1
        self.loss = self.loss + 0.5 if self.month % 2 == 0 else self.loss
        self.old_car = self.old_car * (100 - self.loss) / 100
        self.new_car = self.new_car * (100 - self.loss) / 100

    def _get_need_money(self):
        return self.old_car - self.new_car + (self.saving_per_month * self.month)

    def end_month(self):
        while self._get_need_money() < 0:
            self._next_month()
        return [self.month, round(self._get_need_money())]


def nbMonths(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    buy_car = BuyCar(start_price_old, start_price_new, saving_per_month, percent_loss_by_month)
    return buy_car.end_month()
