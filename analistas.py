import requests


url = "https://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    lista_empleados = data.get('data', [])
    if lista_empleados:
        numero_de_empleados = len(lista_empleados)
        promedio_salario = sum(float(empleados.get('employee_salary', 0))
            for empleados in lista_empleados) / numero_de_empleados
        edad_empleados = sum(int(empleados.get('employee_age', 0))
            for empleados in lista_empleados) / numero_de_empleados
        salario = [float(empleados.get('employee_salary', 0))
            for empleados in lista_empleados]
        max_salario = max(salario)
        min_salario = min(salario)
        edad = [int(empleados.get('employee_age', 0))
            for empleados in lista_empleados]
        max_edad = max(edad)
        min_edad = min(edad)


        print(f"Número de empleados: {numero_de_empleados}")
        print(f"Promedio de salario: {promedio_salario}")
        print(f"Promedio de edad: {edad_empleados}")
        print(f"Salario máximo: {max_salario}")
        print(f"Salario mínimo: {min_salario}")
        print(f"Edad máxima: {max_edad}")
        print(f"Edad mínima: {min_edad}")

    else:
        print("No hay datos de empleados en la respuesta del API.")
else:
    print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")
