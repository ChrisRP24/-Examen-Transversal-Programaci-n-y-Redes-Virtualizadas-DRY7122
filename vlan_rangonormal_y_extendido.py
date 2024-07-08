
RANGO_NORMAL = range(1, 1006)
RANGO_EXTENDIDO = range(1006, 4095)

numero_vlan = int(input("Ingrese el número de VLAN: "))

if numero_vlan in RANGO_NORMAL:
    print(f"La VLAN {numero_vlan} rango normal.")
elif numero_vlan in RANGO_EXTENDIDO:
    print(f"La VLAN {numero_vlan} rango extendido.")
else:
    print(f"La VLAN {numero_vlan} está fuera de los rangos normales y extendidos.")