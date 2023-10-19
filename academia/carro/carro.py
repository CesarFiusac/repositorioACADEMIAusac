class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}

        self.carro = carro

    def agregarcurso(self, Curso):
        if(str(Curso.id) not in self.carro.keys()):
            self.carro[Curso.id] = {
                "curso_id":Curso.catedratico_asignado_id,
                "nombrecurso": Curso.nombrecurso,
                "costo": str(Curso.costo),
                "cantidad":1    
            }
        else:
            for key, value in self.carro.items():
                if key == str(Curso.id):
                    value ["cantidad"] = value["cantidad"]+1
                    break
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, Curso):
        Curso.id = str(Curso.id)
        if Curso.id in self.carro:
            del self.carro[Curso.id]
            self.guardar_carro()

    def restar_curso(self, Curso):
        for key, value in self.carro.items():
                if key == str(Curso.id):
                    value ["cantidad"] = value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(Curso)
                    break
        self.guardar_carro()
    
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified = True