# Generar un email

Nombre = " Freddy Uriostegui Cruz "
Empresa = " Global Mentoring "
Dominio = ".com.mx"

Nombre_usuario = Nombre.lower()
Nombre_usuario = Nombre_usuario.strip()
Nombre_usuario = Nombre_usuario.replace(' ', '.')

print(f'Nombre usuario normalizado: {Nombre_usuario}')
print(f'Nombre empresa: {Empresa}')
print(f'Dominio: {Dominio}')

Correcion_empresa = Empresa.lower()
Correcion_empresa = Correcion_empresa.strip()
Correcion_empresa = Correcion_empresa.replace(' ','')


Correcion_dominio = Dominio.replace(' ', '.')

Concatenar1 = Correcion_empresa+Correcion_dominio
print(f' Dominio corregido: {Concatenar1}')

Concatenar = Nombre_usuario + '@'+Correcion_empresa + Correcion_dominio
print(f'Dominio generado: {Concatenar}')