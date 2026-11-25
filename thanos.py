import streamlit as st
import time

# Configuración de la página (se ve genial en celulares en modo oscuro)
st.set_page_config(
    page_title="Protocolo Final - Thanos",
    page_icon="🫰",
    layout="centered"
)

# Estilos personalizados para darle estética de terminal/guantelete
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    .titulo-thanos {
        text-align: center;
        color: #a855f7;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }
    .subtitulo {
        text-align: center;
        color: #94a3b8;
        font-family: 'Courier New', monospace;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .carta-box {
        background-color: #1e1b4b;
        border-left: 5px solid #a855f7;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Segoe UI', sans-serif;
        line-height: 1.6;
        margin-top: 20px;
    }
    .destello {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: white;
        z-index: 9999;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown('<div class="titulo-thanos">PROTOCOLO DE CIERRE: SEMESTRE 2026-2</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Sistema de Evaluación y Equilibrio Universal</div>', unsafe_allow_html=True)

# Botón principal para iniciar el espectáculo en el celular
if st.button("🫰 Ejecutar Chasquido Final", use_container_width=True, type="primary"):
    
    gemas = [
        ("🧠 Gema de la Mente (Lógica y Algoritmos)", "#06b6d4"),
        ("💜 Gema del Poder (Trasnochos de Estudio)", "#a855f7"),
        ("❤️ Gema de la Realidad (Parciales Imposibles)", "#ef4444"),
        ("🧡 Gema del Alma (Tinto y Lágrimas)", "#f97316"),
        ("💚 Gema del Tiempo (Entregas al Límite)", "#22c55e"),
        ("💙 Gema del Espacio (Conocimiento Real y ojeras)", "#3b82f6")
    ]

    contenedor_gemas = st.container()
    
    with contenedor_gemas:
        st.write("### Recolectando las Gemas del Semestre...")
        for nombre, color in gemas:
            st.markdown(f"<span style='color:{color}; font-weight:bold;'>{nombre}</span>", unsafe_allow_html=True)
            barra = st.progress(0)
            for porcentaje in range(0, 101, 10):
                barra.progress(porcentaje)
                time.sleep(0.03)
        
        st.success("✅ ¡Todas las gemas están en el Guantelete!")
        time.sleep(0.8)

    # Efecto de destello blanco en pantalla (El Chasquido)
    flash = st.empty()
    flash.markdown('<div class="destello"></div>', unsafe_allow_html=True)
    time.sleep(0.25)
    flash.empty()

    # Limpiamos las barras para dar paso al mensaje final
    contenedor_gemas.empty()
    st.balloons() # Efecto visual extra de cierre

    # Mensaje final con efecto de aparición progresiva
    st.markdown("""
    <div class="carta-box">
        <h3 style="color: #c084fc; margin-top: 0;">📜 REPORTE FINAL DE LA BATALLA</h3>
        <p>Estimados futuros profesionales,</p>
        <p>El semestre ha llegado a su fin. Sé que el camino fue duro, que a veces sentían que el universo estaba en su contra y que mi reputación como <b>'Thanos'</b> estuvo a la altura de los parciales.</p>
        <p style="color: #38bdf8; font-style: italic;">"Las decisiones más difíciles requieren las voluntades más fuertes."</p>
        <p>El sufrimiento académico fue temporal, pero el criterio, la lógica y lo que aprendieron les servirá para toda la vida profesional.</p>
        <p>Gracias por su esfuerzo, su paciencia, las buenas preguntas en clase y por no rendirse cuando el código no compilaba o la ecuación no cerraba. Ha sido un honor guiarlos en esta etapa.</p>
        <p>Ahora, el semestre ha quedado <b style="color: #4ade80;">perfectamente equilibrado</b>, como todo debe estar.</p>
        <h4 style="color: #a855f7;">¡Buen viento y buena mar en lo que viene de sus carreras! 🚀⚓</h4>
        <p style="margin-bottom: 0;">Atentamente,<br><b>Su profesor (alias Thanos)</b></p>
    </div>
    """, unsafe_allow_html=True)
