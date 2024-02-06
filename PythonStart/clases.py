
class Casa(object):
    propietario = ''
    def __init__(self, prop, num, street):
        self.numero = num
        self.calle = street
        self.propietario = prop

    def info(self):
        print('**************')
        print(f'prop:{self.propietario}')
        print(f'en la calle:{self.calle}')
        print(f'en el numero:{self.numero}')
        print('**************')


class Departamento(Casa):
    def __init__(self, prop, num, habitantes):
        super().__init__(prop, num, None)
        self.habitantes = habitantes

    def info(self):
        print('**************')
        print(f'prop:{self.propietario}')
        print(f'en el numero:{self.numero}')


class Edificio(Casa):
    departamentos = {}

    def __init__(self, num, street):
        super().__init__('multiples propietarios', num, street)

    def add_dept_data(self, prop, num, habitantes=None):
        self.departamentos[num] = Departamento(prop, num, habitantes)

    def info(self):
        super().info()
        for each_key in self.departamentos:
            self.departamentos[each_key].info()


mi_casa = Casa('Daniel', 234, 'peel st')
mi_casa_a = Casa('Randi', 56, 'councillors st')
mi_edificio = Edificio(78, 'Av des canadiens')
mi_casa.info()
mi_casa_a.info()

mi_edificio.add_dept_data('alma', 98, habitantes=4)
mi_edificio.add_dept_data('michael', 3, habitantes=2)
mi_edificio.add_dept_data('juan', 2, habitantes=2)
mi_edificio.add_dept_data('pedro', 5, habitantes=3)


mi_edificio.info()
from pprint import pprint as pp
pp(mi_edificio.departamentos)



