class SolucionDinamica():

    def __init__(self, listaPrediccion):
        self.prediccion = listaPrediccion
        self.tam = len(listaPrediccion)

    def getBestDays(self):
        """
        Idea para no olvidarme.
        Te quedas con el minimo hasta el momento que es dia venta aux.
        entonces vas comparando ganancia entre el dia i y el dia que mas barato
        te salio comprar hasta este momento. Cuando tu ganancia temporal es mas grande
        que la ganancia maxima hasta el momento actualizas esta ultima. En el caso de
        encontrar un dia donde te sale mas barato comprar acciones vos ya sabes
        que hasta el momento no pudiste obtener una ganancia maxima a la que ya tenes,
        entonces actualizas el minimo en dia compra aux y seguis comparando con las posiciones
        que te falten para adelante.
        """

        gananciaMax = 0
        gananciaTemporal = 0
        diaCompra = 0
        diaVenta = 0
        diaCompraAux = 0

        for x in xrange(1, self.tam):

            #Este chequeo lo hago antes porque si el valor actual es menor al valor de compra, da negativo
            if(self.prediccion[diaCompraAux] > self.prediccion[x]):
                diaCompraAux = x

            #Me quedo con la ganancia del dia que menor sale comprar con el dia actual
            gananciaTemporal = self.prediccion[x] - self.prediccion[diaCompraAux]
            print(gananciaTemporal)
            if(gananciaMax < gananciaTemporal):
                gananciaMax = gananciaTemporal
                diaCompra = diaCompraAux
                diaVenta = x

        return gananciaMax


def main():
    c = SolucionDinamica([2,9,1,70])
    print(c.getBestDays())
main()
