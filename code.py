import numpy as np
from scipy.integrate import quad
def integrando_cp(T, a, b, c):
    """Ecuación polinómica para Cp: a + bT + cT^-2"""
    return a + b*T + c*(T**-2)

def calcular_kirchhoff(delta_H1, T1, T2, lista_reac, lista_prod):
    """Calcula Delta H a T2 usando Kirchhoff con polinomios."""
    delta_H2 = delta_H1
    
    for reac, prod in zip(lista_reac, lista_prod):
        # Calculamos el Delta Cp para esta sustancia
        cp_reac = reac['cp']
        cp_prod = prod['cp']
        
        delta_a = cp_prod['a'] - cp_reac['a']
        delta_b = cp_prod['b'] - cp_reac['b']
        delta_c = cp_prod['c'] - cp_reac['c']
        
        # integral Kirchhoff (multiplicada por el coeficiente estequiométrico del producto)
        # Nota: los coeficientes son los mismos para reactivos y productos en la iteración
        coef = prod['coef']
        
        integral, _ = quad(integrando_cp, T1, T2, args=(delta_a, delta_b, delta_c))
        
        delta_H2 += coef * (integral / 1000) # de J a kJ
        
    return delta_H2

def main():
    print("=========================================")
    print("   CALCULADORA TERMODINÁMICA (Hess y Kirchhoff)")
    print("=========================================")
    
    # --- 1. INGRESO DE REACTIVOS ---
    num_reactivos = int(input("\n¿Cuántos REACTIVOS hay en la reacción? "))
    lista_reactivos = []
    for i in range(num_reactivos):
        print(f"\nDatos del REACTIVO {i+1}:")
        nombre = input("Nombre: ")
        coef = float(input("Coeficiente estequiométrico: "))
        dHf = float(input("Entalpía de formación estándar (kJ/mol): "))
        estado = input("¿Es un GAS? (s/n): ").lower()
        
        # Pedimos coeficientes de Cp (si no los sabe, que ponga 0)
        print("Coeficientes de Cp (a, b, c) para a + bT + cT^-2:")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        
        lista_reactivos.append({
            'nombre': nombre, 'coef': coef, 'delta_H_f': dHf, 'es_gas': estado == 's',
            'cp': {'a': a, 'b': b, 'c': c}
        })

    # --- 2. INGRESO DE PRODUCTOS ---
    num_productos = int(input("\n¿Cuántos PRODUCTOS hay en la reacción? "))
    lista_productos = []
    for i in range(num_productos):
        print(f"\nDatos del PRODUCTO {i+1}:")
        nombre = input("Nombre: ")
        coef = float(input("Coeficiente estequiométrico: "))
        dHf = float(input("Entalpía de formación estándar (kJ/mol): "))
        estado = input("¿Es un GAS? (s/n): ").lower()
        
        print("Coeficientes de Cp (a, b, c):")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        
        lista_productos.append({
            'nombre': nombre, 'coef': coef, 'delta_H_f': dHf, 'es_gas': estado == 's',
            'cp': {'a': a, 'b': b, 'c': c}
        })

    # --- 3. CÁLCULO DE HESS (A T1) ---
    T1 = 298.15
    H_prod = sum([item['coef'] * item['delta_H_f'] for item in lista_productos])
    H_reac = sum([item['coef'] * item['delta_H_f'] for item in lista_reactivos])
    delta_H1 = H_prod - H_reac
    print(f"\n=> Entalpía a T1 (298.15 K): {delta_H1:.2f} kJ/mol")

    # --- 4. CÁLCULO DE KIRCHHOFF (SI APLICA) ---
    aplicar_kirchhoff = input("\n¿Calcular a otra temperatura? (s/n): ").lower()
    delta_H_final = delta_H1
    T_final = T1
    
    if aplicar_kirchhoff == 's':
        T_final = float(input("Ingresa la temperatura final (K): "))
        # Solo funciona si los coeficientes coinciden 1 a 1 (ej. 1 reactivo -> 1 producto)
        # Para simplificar, lo hacemos por separado:
        
        # Calculamos Delta Cp total de la reacción
        delta_a = sum([p['coef'] * p['cp']['a'] for p in lista_productos]) - sum([r['coef'] * r['cp']['a'] for r in lista_reactivos])
        delta_b = sum([p['coef'] * p['cp']['b'] for p in lista_productos]) - sum([r['coef'] * r['cp']['b'] for r in lista_reactivos])
        delta_c = sum([p['coef'] * p['cp']['c'] for p in lista_productos]) - sum([r['coef'] * r['cp']['c'] for r in lista_reactivos])
        
        integral, _ = quad(integrando_cp, T1, T_final, args=(delta_a, delta_b, delta_c))
        delta_H_final = delta_H1 + (integral / 1000) # Pasar a kJ
        print(f"\n=> Entalpía a T2 ({T_final} K): {delta_H_final:.2f} kJ/mol")

    # --- 5. CÁLCULO DE Q, W, DELTA U ---
    # (Convención: Trabajo Positivo = Sistema se expande)
    n_gas_prod = sum([item['coef'] for item in lista_productos if item['es_gas']])
    n_gas_reac = sum([item['coef'] for item in lista_reactivos if item['es_gas']])
    delta_n = n_gas_prod - n_gas_reac
    
    R = 0.008314 # kJ/(mol*K)
    Q = delta_H_final # A presión constante
    W = delta_n * R * T_final # Convención: positivo si se expande
    delta_U = Q - W # Primera Ley con esta convención

    print("\n" + "="*40)
    print(" ========RESULTADOS FINALES========")
    print("="*40)
    print(f"==Temperatura de cálculo: {T_final} K")
    print(f"==Variación de moles de gas (Delta n): {delta_n}")
    print(f"==Calor (Q): {Q:.4f} kJ/mol")
    print(f"==Trabajo (W): {W:.4f} kJ/mol")
    print(f"==Energía Interna (Delta U): {delta_U:.4f} kJ/mol")
    print("="*40)

if __name__ == "__main__":
    main()