"""
RefactoringSergio.py

Sistema de nóminas refactorizado con tipado, docstrings y mejores prácticas.

Este módulo implementa un pequeño sistema de gestión de empleados y cálculo


Module Contents
- Employee: dataclass que representa a un empleado
- calculate_net_salary: función pura para calcular sueldo neto
- add_employee_flow: flujo para solicitar datos de un empleado y guardarlo
- generate_report: muestra por consola un informe de empleados
- main: bucle principal de la aplicación (interactivo)

Notas de compatibilidad
- Se mantienen los departamentos y tasas/impuestos del script original:
  * Ventas: 15% impuesto + 50 de comedor
  * IT:    15% impuesto + 50 de comedor
  * RRHH:  16% impuesto + 50 de comedor
- El sueldo neto nunca baja de 0.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict


# Constantes de negocio
CAFETERIA_DISCOUNT: float = 50.0
TAX_RATES_BY_DEPARTMENT: Dict[str, float] = {
    "Ventas": 0.15,
    "IT": 0.15,
    "RRHH": 0.16,
}


@dataclass
class Employee:
    """Representa a un empleado del sistema de nóminas.

    Attributes:
        name: Nombre del empleado.
        department: Departamento al que pertenece ("Ventas", "IT" o "RRHH").
        gross_salary: Sueldo bruto ingresado.
        net_salary: Sueldo neto calculado (no negativo).
    """

    name: str
    department: str
    gross_salary: float
    net_salary: float


def calculate_net_salary(gross_salary: float, department: str) -> float:
    """Calcula el sueldo neto para un departamento dado.

    Reglas:
    - Impuesto por departamento (ver TAX_RATES_BY_DEPARTMENT).
    - Descuento fijo de comedor (CAFETERIA_DISCOUNT).
    - El sueldo neto no puede ser negativo.

    Args:
        gross_salary: Sueldo bruto ingresado.
        department: Nombre del departamento.

    Returns:
        El sueldo neto (>= 0).

    Raises:
        ValueError: Si el departamento no está configurado.
    """
    if department not in TAX_RATES_BY_DEPARTMENT:
        raise ValueError(f"Departamento desconocido: {department}")

    tax_rate = TAX_RATES_BY_DEPARTMENT[department]
    tax_amount = gross_salary * tax_rate
    net_salary = gross_salary - tax_amount - CAFETERIA_DISCOUNT

    return max(net_salary, 0.0)


def prompt_non_empty_string(prompt: str) -> str:
    """Solicita una cadena no vacía por consola.

    Repite hasta obtener un valor válido.

    Args:
        prompt: Mensaje a mostrar.

    Returns:
        La cadena ingresada, sin espacios de inicio/fin.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Entrada vacía. Inténtelo de nuevo.")


def prompt_float(prompt: str) -> float:
    """Solicita un número de tipo float por consola.

    Repite hasta obtener un valor numérico válido.

    Args:
        prompt: Mensaje a mostrar.

    Returns:
        El valor ingresado como float.
    """
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Valor inválido. Ingrese un número (use punto decimal si corresponde).")


def add_employee_flow(department: str, employees: List[Employee]) -> None:
    """Pide datos de un empleado, calcula el neto y lo agrega a la lista.

    Args:
        department: Departamento al que se agregará el empleado.
        employees: Lista mutable donde se almacenan los empleados.
    """
    name = prompt_non_empty_string("Nombre: ")
    gross = prompt_float("Sueldo Bruto: ")

    try:
        net = calculate_net_salary(gross, department)
    except ValueError as exc:
        print(str(exc))
        return

    employees.append(Employee(name=name, department=department, gross_salary=gross, net_salary=net))
    print(f"Guardado {department}.")


def generate_report(employees: List[Employee]) -> None:
    """Muestra un informe por consola con todos los empleados.

    Args:
        employees: Lista de empleados a reportar.
    """
    if not employees:
        print("No hay nadie")
        return

    for emp in employees:
        print(f"Emp: {emp.name}")
        print(f"Depto: {emp.department}")
        print(f"Pago Final: {emp.net_salary}")
        print("----------------")


def show_menu() -> str:
    """Muestra el menú y devuelve la opción elegida como cadena."""
    print("********************************")
    print("SISTEMA DE NOMINAS V2.3 FINAL_REAL_AHORA_SI")
    print("********************************")
    print("")
    print("1. Agregar empleado Ventas")
    print("2. Agregar empleado IT")
    print("3. Agregar empleado RRHH")
    print("4. Ver reporte")
    print("5. Salir")
    print("")
    return input("Seleccione opcion: ").strip()


def main() -> None:
    """Punto de entrada del programa interactivo."""
    employees: List[Employee] = []

    while True:
        option = show_menu()
        if option == "1":
            add_employee_flow("Ventas", employees)
        elif option == "2":
            add_employee_flow("IT", employees)
        elif option == "3":
            add_employee_flow("RRHH", employees)
        elif option == "4":
            generate_report(employees)
        elif option == "5":
            # Salimos del bucle principal
            break
        else:
            print("Error")


if __name__ == "__main__":
    main()
