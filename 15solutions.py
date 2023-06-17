class Phone:

    def _init_(self, manufact, model, price):
        self._manufact = manufact
        self._model = model
        self._retail_price = price

    def set_manufact(self, manufact):
        self._manufact = manufact

    def set_model(self, model):
        self._model = model

    def set_retail_price(self, price):
        self._retail_price = price

    def get_manufact(self):
        return self._manufact

    def get_model(self):
        return self._model

    def get_retail_price(self):
        return self._retail_price

def write(manufact, model, price):
    print("Производитель: " + manufact)
    print("Модель: " + model)
    print("Цена: " + str(price))

phone1 = Phone()
phone1._init_("Производитель", "Модель", 50000)
write(phone1.get_manufact(), phone1.get_model(), phone1.get_retail_price())
phone1.set_manufact("Новый производитель")
phone1.set_model("Новый модель")
phone1.set_retail_price(12000)
write(phone1.get_manufact(), phone1.get_model(), phone1.get_retail_price())
