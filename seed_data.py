from ejemplo.models import Familiar
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")


from ejemplo.models import Obreros
Obreros(nombre="Pedro López", categoria="Capataz", edad=35).save()
Obreros(nombre="Nelson Burgos", categoria="Oficial", edad=30).save()
Obreros(nombre="Luis Carlos Rodríguez", categoria="Medio oficial", edad=22).save()
Obreros(nombre="Mario Bergara", categoria="Carpintero", edad=49).save()
Obreros(nombre="Alejandro Piriz", categoria="Albañil", edad=20).save()
print("Se cargaron con éxito los obreros")


from ejemplo.models import Obras
Obras(nombre="Luna de Mar", direccion=" Calle Patagonia y Av. Italia, PUnta del Este", niveles=9).save()
Obras(nombre="Cardinal", direccion="Calle Monte Caseros 2700, MOntevideo", niveles=4).save()
Obras(nombre="Otto", direccion="Calle Bolivia 5699, Montevideo", niveles=15).save()
print("Se cargaron con éxito las obras")
