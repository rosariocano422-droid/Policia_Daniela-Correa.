import streamlit as st
import random

st.set_page_config(page_title="Quiz Código de Policía - Ley 1801 de 2016", layout="centered")

preguntas = [
    {
        "pregunta": "Un hombre en la calle amenaza verbalmente a otro con causarle daño físico, pero no llega a agredirlo. ¿Qué numeral y medida correctiva del artículo 27 aplica?",
        "opciones": [
            "Artículo 27, numeral 1 - Multa General tipo 2",
            "Artículo 27, numeral 4 - Participación en programa comunitario; Multa General tipo 2",
            "Artículo 27, numeral 2 - Amonestación; Participación en programa comunitario",
            "Artículo 27, numeral 3 - Multa General tipo 3",
        ],
        "correcta": 1,
        "explicacion": "Art. 27, numeral 4: \"Amenazar con causar un daño físico a personas por cualquier medio\" -> Participación en programa comunitario o actividad pedagógica de convivencia; Multa General tipo 2.",
    },
    {
        "pregunta": "Una persona porta un arma neumática con el permiso ya vencido, sin estar bajo efectos de ninguna sustancia. ¿Qué numeral y medida correctiva le corresponde?",
        "opciones": [
            "Artículo 27, numeral 6 - Multa General tipo 2; Prohibición de ingreso a aglomeraciones; Destrucción de bien",
            "Artículo 27, numeral 10 - Multa General tipo 4; Destrucción de bien",
            "Artículo 27, numeral 2 - Amonestación; Participación en programa comunitario",
            "Artículo 27, numeral 1 - Multa General tipo 2",
        ],
        "correcta": 1,
        "explicacion": "Art. 27, numeral 10 (permiso vencido) comparte tabla con los numerales 8, 9 y 11: Multa General tipo 4; Destrucción de bien.",
    },
    {
        "pregunta": "Un ciudadano arroja escombros y lodo dentro del alcantarillado público, obstruyendo su funcionamiento. ¿Qué numeral y medida correctiva del artículo 28 aplica?",
        "opciones": [
            "Artículo 28, numeral 1 - Multa General tipo 3; Remoción de bienes; Destrucción de bien",
            "Artículo 28, numeral 3 - Multa General tipo 4",
            "Artículo 28, numeral 2 - Multa General tipo 3; Reparación de daños materiales",
            "Artículo 28, numeral 4 - Multa General tipo 3; Reparación de daños materiales",
        ],
        "correcta": 1,
        "explicacion": "Art. 28, numeral 3 -> únicamente Multa General tipo 4 (a diferencia de los numerales 1 y 2, que sí incluyen remoción/reparación).",
    },
    {
        "pregunta": "Alguien enciende fuego en un medio de transporte público. ¿Qué numeral del artículo 30 aplica y podría incluir suspensión definitiva de la actividad?",
        "opciones": [
            "Artículo 30, numeral 2 - Multa General tipo 4; Destrucción de bien; Suspensión temporal; Suspensión definitiva",
            "Artículo 30, numeral 3 - Multa General tipo 4; Destrucción de bien",
            "Artículo 30, numeral 6 - Multa General tipo 4; Suspensión temporal de actividad",
            "Artículo 30, numeral 5 - Multa General tipo 4",
        ],
        "correcta": 1,
        "explicacion": "Art. 30, numeral 3 (fuego en transporte público) -> solo Multa General tipo 4; Destrucción de bien. La suspensión definitiva solo aparece en los numerales 2 y 4.",
    },
    {
        "pregunta": "Un residente pone música fuerte en una fiesta dentro de su apartamento, afectando a los vecinos, y se niega a bajarle el volumen. ¿Qué numeral y medida correctiva del artículo 33 aplica?",
        "opciones": [
            "Artículo 33, numeral 1 - Multa General tipo 4; Disolución de reunión o actividad que involucra aglomeraciones de público no complejas",
            "Artículo 33, numeral 2 literal c - Multa General tipo 2; Disolución de reunión o actividad no compleja",
            "Artículo 33, numeral 2 literal a - Multa General tipo 3",
            "Artículo 33, numeral 2 literal e - Multa General tipo 1",
        ],
        "correcta": 0,
        "explicacion": "Art. 33, numeral 1 (perturbación en vecindario/lugar de habitación) -> Multa General tipo 4; Disolución de reunión o actividad que involucra aglomeraciones de público no complejas. Además, la autoridad puede desactivar temporalmente la fuente del ruido, pero el parágrafo 4 aclara que esto NO autoriza el ingreso a domicilio privado.",
    },
    {
        "pregunta": "¿Cuál de las siguientes combinaciones artículo-numeral-literal-sanción es la correcta, para el caso de fumar en un lugar prohibido?",
        "opciones": [
            "Artículo 33, numeral 2 literal d - Amonestación",
            "Artículo 33, numeral 2 literal b - Amonestación",
            "Artículo 33, numeral 2 literal d - Multa General tipo 3",
            "Artículo 33, numeral 2 literal a - Amonestación",
        ],
        "correcta": 0,
        "explicacion": "Art. 33, numeral 2, literal d (fumar en lugares prohibidos) -> Amonestación. El literal b (actos sexuales/exhibicionismo) tiene Multa tipo 3, y el literal a (irrespetar normas de sitios como salas de velación) también Multa tipo 3 - no Amonestación.",
    },
    {
        "pregunta": "Un estudiante mayor de edad consume alcohol DENTRO del colegio; otro, también mayor de edad, lo consume en la calle, dentro del perímetro que fijó el alcalde. ¿Qué numerales del artículo 34 aplican en cada caso?",
        "opciones": [
            "Dentro: numeral 1 (Multa tipo 3; Destrucción de bien) - Fuera: numeral 3 (Multa tipo 4; Destrucción de bien)",
            "Dentro: numeral 2 (Multa tipo 4; Destrucción de bien) - Fuera: numeral 4 (Multa tipo 4; Destrucción de bien; Suspensión temporal)",
            "Dentro: numeral 1 - Fuera: no aplica el artículo 34 en ningún caso",
            "Dentro y fuera: numeral 1 en ambos casos",
        ],
        "correcta": 0,
        "explicacion": "Art. 34, numeral 1 (consumir dentro de la institución) -> Multa tipo 3; Destrucción de bien. Numeral 3 (consumir en espacio público dentro del perímetro fijado por el alcalde, parágrafo 3) -> Multa tipo 4; Destrucción de bien.",
    },
    {
        "pregunta": "Una persona utiliza el número único de emergencias de forma indebida (llamadas falsas). ¿Qué numeral y medida correctiva exacta del artículo 35 le corresponde?",
        "opciones": [
            "Artículo 35, numeral 1 - Multa General tipo 2",
            "Artículo 35, numeral 7 - Multa General tipo 4; Participación en programa comunitario",
            "Artículo 35, numeral 4 - Multa General tipo 4",
            "Artículo 35, numeral 3 - Multa General tipo 4; Participación en programa comunitario",
        ],
        "correcta": 1,
        "explicacion": "Art. 35, numeral 7 (uso indebido del número único de emergencias) -> Multa General tipo 4; Participación en programa comunitario. El numeral 3 tiene la MISMA sanción pero corresponde a otro comportamiento (obstaculizar identificación), por eso el numeral exacto importa. Además, el parágrafo 3 aclara que la multa se carga a la factura telefónica de donde se originó la llamada.",
    },
    {
        "pregunta": "Un adulto permite que un adolescente de 17 años ingrese a un establecimiento de videojuegos con contenido apto solo para mayores de edad. ¿Qué regla exacta del artículo 38 aplica?",
        "opciones": [
            "Artículo 38, numeral 1 (regla general) - Multa tipo 4; Suspensión temporal; Destrucción de bien",
            "Artículo 38, numeral 1 literal b), parágrafo 1 (regla especial) - Solo Suspensión temporal de actividad",
            "Artículo 38, numeral 3 - Multa tipo 4; Destrucción de bien",
            "Artículo 38, numeral 2 - Multa tipo 4; Suspensión temporal de actividad",
        ],
        "correcta": 1,
        "explicacion": "Aunque la tabla general del numeral 1 dice Multa+Suspensión+Destrucción, el parágrafo 1 establece una regla ESPECIAL solo para el literal b) (videojuegos): se impone únicamente suspensión temporal de actividad, y se remite a la Ley 1554 de 2012.",
    },
    {
        "pregunta": "Una persona menor de 16 años porta y consume una sustancia psicoactiva restringida para menores. ¿Qué dice exactamente el parágrafo 1 del artículo 39 sobre la edad?",
        "opciones": [
            "Menor de 16: Amonestación - Mayor de 16: Participación en programa comunitario o actividad pedagógica",
            "Menor de 16: Participación en programa comunitario - Mayor de 16: Amonestación",
            "Ambos casos: Amonestación",
            "Ambos casos: Multa General tipo 1",
        ],
        "correcta": 0,
        "explicacion": "Art. 39, parágrafo 1: \"Para los menores de 16 años, amonestación; para los mayores de 16 años, participación en programa comunitario o actividad pedagógica de convivencia.\"",
    },
    {
        "pregunta": "Un adulto ejerce abuso sexual sobre un menor de edad. ¿Qué numeral y medida correctiva EXCLUSIVA del artículo 38 aplica (distinta a las multas de la mayoría de numerales)?",
        "opciones": [
            "Artículo 38, numeral 7 - Multa General tipo 2",
            "Artículo 38, numeral 8 - Suspensión definitiva de actividad (sin multa)",
            "Artículo 38, numeral 9 - Multa General tipo 4",
            "Artículo 38, numeral 10 - Suspensión temporal de actividad",
        ],
        "correcta": 1,
        "explicacion": "Art. 38, numeral 8 (ejercer, permitir, favorecer o propiciar abuso/explotación sexual de NNA) -> según la tabla del parágrafo 6, su única medida correctiva es Suspensión definitiva de actividad, sin multa asociada.",
    },
    {
        "pregunta": "Una persona reincide, dentro de un año, en un comportamiento del artículo 38 que inicialmente tuvo sanción de \"suspensión temporal de actividad\". ¿Qué parágrafo regula esto y qué establece?",
        "opciones": [
            "Parágrafo 6 del artículo 38 - Se le impone nuevamente la misma multa",
            "Parágrafo 8 del artículo 38 - Será objeto de suspensión definitiva de la actividad",
            "Parágrafo 7 del artículo 38 - Se aplican las medidas del Código de infancia y adolescencia",
            "Parágrafo 3 del artículo 39 - Se traslada a sitios adecuados determinados por la alcaldía",
        ],
        "correcta": 1,
        "explicacion": "Art. 38, parágrafo 8: quien reincida en un comportamiento que dio lugar a suspensión temporal, será objeto de suspensión definitiva de la actividad.",
    },
]

if "orden" not in st.session_state:
    st.session_state.orden = list(range(len(preguntas)))
    random.shuffle(st.session_state.orden)
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.respondida = False
    st.session_state.opcion_elegida = None

st.title("Quiz - Código Nacional de Seguridad y Convivencia Ciudadana")
st.caption("Ley 1801 de 2016 - Artículos 26 a 39 (Títulos III y IV)")

total = len(preguntas)
idx_actual = st.session_state.indice

if idx_actual >= total:
    st.header("Quiz terminado")
    correctas = st.session_state.puntaje
    incorrectas = total - correctas
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Respuestas correctas", correctas)
    with col2:
        st.metric("Respuestas incorrectas", incorrectas)
    st.write(f"**Puntaje final: {correctas} / {total}**")
    if st.button("Reiniciar quiz"):
        st.session_state.orden = list(range(len(preguntas)))
        random.shuffle(st.session_state.orden)
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.respondida = False
        st.session_state.opcion_elegida = None
        st.rerun()
else:
    pregunta_actual = preguntas[st.session_state.orden[idx_actual]]

    st.subheader(f"Pregunta {idx_actual + 1} de {total}")
    st.write(pregunta_actual["pregunta"])

    opcion = st.radio(
        "Elige una opción:",
        pregunta_actual["opciones"],
        index=None,
        disabled=st.session_state.respondida,
        key=f"radio_{idx_actual}",
    )

    if not st.session_state.respondida:
        if st.button("Responder", disabled=(opcion is None)):
            st.session_state.respondida = True
            st.session_state.opcion_elegida = opcion
            if pregunta_actual["opciones"].index(opcion) == pregunta_actual["correcta"]:
                st.session_state.puntaje += 1
            st.rerun()
    else:
        elegida_idx = pregunta_actual["opciones"].index(st.session_state.opcion_elegida)
        correcta_idx = pregunta_actual["correcta"]

        if elegida_idx == correcta_idx:
            st.success("Correcto")
        else:
            st.error("Incorrecto")
            st.write(f"**La respuesta correcta era:** {pregunta_actual['opciones'][correcta_idx]}")

        st.info(pregunta_actual["explicacion"])

        if st.button("Siguiente pregunta"):
            st.session_state.indice += 1
            st.session_state.respondida = False
            st.session_state.opcion_elegida = None
            st.rerun()

    st.write(f"Puntaje actual: {st.session_state.puntaje} / {idx_actual + (1 if st.session_state.respondida else 0)}")
