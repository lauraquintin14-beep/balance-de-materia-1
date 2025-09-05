import streamlit as st

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Calculadora de Balance de Masa",
    page_icon="🍇",
    layout="wide"
)

# --- Título y Descripción de la Aplicación ---
st.title("🍇 Calculadora de Balance de Masa para Pulpa de Fruta")
st.markdown(
    "Esta aplicación web calcula la cantidad de azúcar (sacarosa) necesaria para "
    "aumentar la concentración de sólidos solubles (medidos en grados °Brix) en una pulpa de fruta."
)

st.markdown("---")

# --- Columnas para el Problema y la Calculadora ---
col1, col2 = st.columns(2, gap="large")

with col1:
    # --- Planteamiento del Problema ---
    st.header("Planteamiento del Problema")
    st.info(
        """
        **Contexto:** Luego de procesar una fruta para obtener **50 kg de pulpa**, se midieron 
        los grados °Brix, obteniendo una concentración de sólidos disueltos (azúcar) de **7%**. 
        
        Sin embargo, para mantener la calidad del producto, la empresa debe ajustar la pulpa 
        hasta **10 °Brix**. Para ello, se necesita agregar una cantidad de azúcar adecuada.
        
        **Pregunta:** ¿Cuál es la cantidad de azúcar que se debe agregar?
        """
    )
    st.image("https://i.imgur.com/2YQ8gE1.png", caption="Diagrama del proceso de balance de masa.")


with col2:
    st.header("Calculadora Interactiva")
    st.write("Usa los siguientes campos para calcular la cantidad de azúcar necesaria para tus propios datos.")

    # --- Campos de Entrada ---
    masa_inicial = st.number_input(
        "Masa Inicial de Pulpa (kg)", 
        min_value=0.1, 
        value=50.0, 
        step=0.1,
        help="Ingresa la cantidad inicial de pulpa que tienes."
    )

    brix_inicial = st.number_input(
        "°Brix Iniciales (%)", 
        min_value=0.0, 
        max_value=100.0, 
        value=7.0, 
        step=0.1,
        help="Ingresa la concentración inicial de azúcar en la pulpa."
    )

    brix_final = st.number_input(
        "°Brix Finales Deseados (%)", 
        min_value=0.0, 
        max_value=100.0, 
        value=10.0, 
        step=0.1,
        help="Ingresa la concentración de azúcar que deseas alcanzar."
    )

    # --- Lógica de Cálculo y Botón ---
    if st.button("Calcular Cantidad de Azúcar", type="primary", use_container_width=True):
        if brix_final <= brix_inicial:
            st.error("Error: La concentración final deseada debe ser mayor que la concentración inicial.", icon="🚨")
        else:
            # Convertir porcentajes a decimales para el cálculo
            c1 = brix_inicial / 100
            c2 = brix_final / 100
            m1 = masa_inicial

            # Fórmula derivada del balance de masa: A = M1 * (C2 - C1) / (1 - C2)
            azucar_a_agregar = m1 * (c2 - c1) / (1 - c2)
            
            masa_final = masa_inicial + azucar_a_agregar

            # --- Mostrar Resultados ---
            st.success(f"Resultado: Se deben agregar **{azucar_a_agregar:.2f} kg** de azúcar.", icon="✅")
            st.info(f"La masa final de la pulpa será de **{masa_final:.2f} kg**.", icon="⚖️")

            with st.expander("Ver detalles del cálculo y la fórmula"):
                st.write("El cálculo se basa en la siguiente ecuación de balance de masa para los sólidos (azúcar):")
                st.latex(r'''
                \text{Sólidos}_{iniciales} + \text{Sólidos}_{agregados} = \text{Sólidos}_{finales}
                ''')
                st.latex(r'''
                (M_1 \times C_1) + A = (M_1 + A) \times C_2
                ''')
                st.markdown(f"""
                Donde:
                - **$M_1$**: Masa inicial de pulpa = **{m1} kg**
                - **$C_1$**: Concentración inicial (°Brix) = **{brix_inicial}%**
                - **$C_2$**: Concentración final (°Brix) = **{brix_final}%**
                - **$A$**: Masa de azúcar a agregar (la incógnita)
                
                Despejando **A**, obtenemos la fórmula:
                """)
                st.latex(r'''
                A = \frac{M_1 \times (C_2 - C_1)}{1 - C_2}
                ''')
                st.write("Sustituyendo los valores del problema:")
                st.latex(f'''
                A = \\frac{{{m1} \\times ({c2} - {c1})}}{{1 - {c2}}} = {azucar_a_agregar:.2f} \\text{{ kg}}
                ''')

# --- Pie de Página ---
st.markdown("---")
st.write("Aplicación desarrollada con Python y Streamlit para resolver problemas de balance de masa en la industria de alimentos.")
