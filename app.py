def calcular_salario(tipo_contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas):
    tarifas = {
        "docente_tc": {"diurna": 50000, "nocturna": 70000, "dominical": 90000, "festiva": 100000},
        "docente_mc": {"diurna": 30000, "nocturna": 50000, "dominical": 70000, "festiva": 80000},
    }

    if tipo_contrato not in tarifas:
        raise ValueError("Tipo de contrato no válido")

    for horas in [horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas]:
        if not isinstance(horas, (int, float)):
            raise TypeError("Las horas deben ser numéricas")
        if horas < 0:
            raise ValueError("Las horas no pueden ser negativas")

    total_horas = horas_diurnas + horas_nocturnas + horas_dominicales + horas_festivas
    if total_horas > 168:
        raise ValueError("No se pueden trabajar más de 168 horas al mes")

    t = tarifas[tipo_contrato]
    salario_bruto = (
        horas_diurnas * t["diurna"] +
        horas_nocturnas * t["nocturna"] +
        horas_dominicales * t["dominical"] +
        horas_festivas * t["festiva"]
    )

    parafiscales = salario_bruto * 0.09
    salario_neto = salario_bruto - parafiscales

    return {
        "Salario Bruto": salario_bruto,
        "Descuento Parafiscales": parafiscales,
        "Salario Neto": salario_neto
    }
