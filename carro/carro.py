from decimal import Decimal


class Carro:
    def __init__(self,request):
        self.request =request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        
        self.carro=carro
            
    def agregar(self, articulo):
        if (str(articulo.id)not in self.carro.keys()):
            self.carro[articulo.id]={
                "articulo_id":articulo.id,
                "nombre":articulo.name,
                "precio":str(articulo.price),
                "cantidad":1,
                "iamgen":articulo.imagen.url,
            }
        else:
            for key,value in self.carro.items():
                if key==str(articulo.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"]) + int(articulo.price)
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
                
    def eliminar(self, articulo):
        articulo.id=str(articulo.id)
        if articulo.id in self.carro:
            del self.carro[articulo.id]
            self.guardar_carro()
            
    def restar_articulo(self, articulo):
        for key,value in self.carro.items():
            if key==str(articulo.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"]) - int(articulo.price)
                if value["cantidad"]<1:
                    self.eliminar(articulo)                
                break
        self.guardar_carro()

    def limpiar_carro(self, ):
        self.session["carro"]={}
        self.session.modified=True