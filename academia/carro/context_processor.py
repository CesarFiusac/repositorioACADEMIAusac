def importe_total_carro(request):
    if "carro" not in request.session:
        request.session["carro"] = {}
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + (float(value["costo"])*value["cantidad"])
    return {"importe_total_carro": total}