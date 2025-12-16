/**
 * Calculadora Gráfica - Frontend JavaScript
 * Maneja la comunicación con el backend Flask y renderiza gráficos con Plotly.js
 */

// Importar traducciones (se carga desde translations.js)
let currentLang = 'es';

// ========================================
// Elementos del DOM
// ========================================
const functionInput = document.getElementById('functionInput');
const graphButton = document.getElementById('graphButton');
const errorMessage = document.getElementById('errorMessage');
const graphContainer = document.getElementById('graphContainer');
const xMinInput = document.getElementById('xMin');
const xMaxInput = document.getElementById('xMax');
const numPuntosInput = document.getElementById('numPuntos');
const exampleButtons = document.querySelectorAll('.example-btn');

// Elementos de la calculadora básica
const calcA = document.getElementById('calcA');
const calcB = document.getElementById('calcB');
const calcOperator = document.getElementById('calcOperator');
const calcResult = document.getElementById('calcResult');
const calcButtons = document.querySelectorAll('.calc-btn');

// Elementos de pestañas
const tabButtons = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

// Elementos de idioma
const langButtons = document.querySelectorAll('.lang-btn');

// URL del backend
const API_URL = '/api/graficar';

// ========================================
// Sistema de Pestañas
// ========================================

/**
 * Cambia entre pestañas
 * @param {string} tabId - ID de la pestaña a mostrar
 */
function switchTab(tabId) {
    // Ocultar todos los contenidos
    tabContents.forEach(content => {
        content.classList.remove('active');
    });
    
    // Desactivar todos los botones
    tabButtons.forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Mostrar el contenido seleccionado
    const selectedContent = document.getElementById(`${tabId}-tab`);
    if (selectedContent) {
        selectedContent.classList.add('active');
    }
    
    // Activar el botón correspondiente
    const selectedButton = document.querySelector(`[data-tab="${tabId}"]`);
    if (selectedButton) {
        selectedButton.classList.add('active');
    }
}

// ========================================
// Sistema Multiidioma
// ========================================

/**
 * Traduce toda la interfaz al idioma seleccionado
 * @param {string} lang - Código del idioma (es, en, fr, de)
 */
function translatePage(lang) {
    if (!translations[lang]) {
        console.error(`Idioma ${lang} no soportado`);
        return;
    }
    
    currentLang = lang;
    const t = translations[lang];
    
    // Traducir elementos con data-i18n
    document.querySelectorAll('[data-i18n]').forEach(elem => {
        const key = elem.getAttribute('data-i18n');
        if (t[key]) {
            elem.textContent = t[key];
        }
    });
    
    // Traducir placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(elem => {
        const key = elem.getAttribute('data-i18n-placeholder');
        if (t[key]) {
            elem.placeholder = t[key];
        }
    });
    
    // Actualizar idioma del HTML
    document.documentElement.lang = lang;
}

/**
 * Cambia el idioma activo
 * @param {string} lang - Código del idioma
 */
function changeLanguage(lang) {
    // Actualizar botones de idioma
    langButtons.forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.lang === lang) {
            btn.classList.add('active');
        }
    });
    
    // Traducir página
    translatePage(lang);
}

// ========================================
// Funciones principales
// ========================================

/**
 * Muestra un mensaje de error en la interfaz
 * @param {string} message - Mensaje de error a mostrar
 */
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

/**
 * Oculta el mensaje de error
 */
function hideError() {
    errorMessage.style.display = 'none';
}

/**
 * Activa/desactiva el estado de carga del botón
 * @param {boolean} loading - true para activar, false para desactivar
 */
function setLoading(loading) {
    if (loading) {
        graphButton.disabled = true;
        graphButton.classList.add('loading');
        graphButton.textContent = 'Calculando...';
    } else {
        graphButton.disabled = false;
        graphButton.classList.remove('loading');
        graphButton.textContent = '📈 Graficar';
    }
}

/**
 * Renderiza el gráfico usando Plotly.js
 * @param {number[]} xCoords - Coordenadas X
 * @param {number[]} yCoords - Coordenadas Y
 * @param {string} funcionStr - Expresión de la función para el título
 */
function renderGraph(xCoords, yCoords, funcionStr) {
    const trace = {
        x: xCoords,
        y: yCoords,
        type: 'scatter',
        mode: 'lines',
        name: `f(x) = ${funcionStr}`,
        line: {
            color: '#4f46e5',
            width: 2.5
        },
        hovertemplate: 'x: %{x:.3f}<br>y: %{y:.3f}<extra></extra>'
    };

    const layout = {
        title: {
            text: `f(x) = ${funcionStr}`,
            font: {
                size: 18,
                color: '#1e293b'
            }
        },
        xaxis: {
            title: 'x',
            zeroline: true,
            zerolinecolor: '#94a3b8',
            zerolinewidth: 1,
            gridcolor: '#e2e8f0',
            tickfont: { size: 12 }
        },
        yaxis: {
            title: 'f(x)',
            zeroline: true,
            zerolinecolor: '#94a3b8',
            zerolinewidth: 1,
            gridcolor: '#e2e8f0',
            tickfont: { size: 12 }
        },
        plot_bgcolor: '#fafafa',
        paper_bgcolor: '#ffffff',
        margin: { l: 60, r: 30, t: 60, b: 50 },
        hovermode: 'closest',
        showlegend: false,
        autosize: true,
        height: 450
    };

    const config = {
        responsive: true,
        displayModeBar: true,
        modeBarButtonsToRemove: ['lasso2d', 'select2d'],
        displaylogo: false
    };

    Plotly.newPlot(graphContainer, [trace], layout, config);
}

/**
 * Maneja el click en el botón de graficar
 * Envía la función al backend y renderiza el resultado
 */
async function handleGraphButtonClick() {
    const funcion = functionInput.value.trim();
    const t = translations[currentLang];
    
    // Validación básica
    if (!funcion) {
        showError(t.error_empty_function);
        functionInput.focus();
        return;
    }

    // Obtener parámetros de rango
    const xMin = parseFloat(xMinInput.value) || -10;
    const xMax = parseFloat(xMaxInput.value) || 10;
    const numPuntos = parseInt(numPuntosInput.value) || 200;

    // Validar rango
    if (xMin >= xMax) {
        showError(t.error_invalid_range);
        return;
    }

    hideError();
    setLoading(true);

    try {
        // Enviar petición al backend
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                funcion: funcion,
                x_min: xMin,
                x_max: xMax,
                num_puntos: numPuntos
            })
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(data.error || 'Error desconocido del servidor');
        }

        // Renderizar el gráfico
        renderGraph(data.x_coords, data.y_coords, data.funcion_parseada);

    } catch (error) {
        console.error('Error:', error);
        
        if (error.message.includes('Failed to fetch')) {
            showError(t.error_connection);
        } else {
            showError(error.message);
        }
    } finally {
        setLoading(false);
    }
}

/**
 * Maneja el click en los botones de ejemplo
 * @param {Event} event - Evento del click
 */
function handleExampleClick(event) {
    const func = event.target.dataset.func;
    if (func) {
        functionInput.value = func;
        handleGraphButtonClick();
    }
}

/**
 * Realiza operaciones de calculadora básica
 * @param {string} operation - Operación a realizar (+, -, *, /, **, sqrt)
 */
function calcular_basico(operation) {
    const a = parseFloat(calcA.value);
    const b = parseFloat(calcB.value);
    const t = translations[currentLang];
    
    if (isNaN(a)) {
        calcResult.textContent = t.error_first_number;
        calcResult.style.color = 'var(--color-error)';
        return;
    }
    
    let resultado;
    let operacionTexto = '';
    
    try {
        switch (operation) {
            case '+':
                if (isNaN(b)) {
                    calcResult.textContent = t.error_second_number;
                    calcResult.style.color = 'var(--color-error)';
                    return;
                }
                resultado = a + b;
                operacionTexto = `${a} + ${b} = ${resultado}`;
                break;
            case '-':
                if (isNaN(b)) {
                    calcResult.textContent = t.error_second_number;
                    calcResult.style.color = 'var(--color-error)';
                    return;
                }
                resultado = a - b;
                operacionTexto = `${a} − ${b} = ${resultado}`;
                break;
            case '*':
                if (isNaN(b)) {
                    calcResult.textContent = t.error_second_number;
                    calcResult.style.color = 'var(--color-error)';
                    return;
                }
                resultado = a * b;
                operacionTexto = `${a} × ${b} = ${resultado}`;
                break;
            case '/':
                if (isNaN(b)) {
                    calcResult.textContent = t.error_second_number;
                    calcResult.style.color = 'var(--color-error)';
                    return;
                }
                if (b === 0) {
                    calcResult.textContent = t.error_division_zero;
                    calcResult.style.color = 'var(--color-error)';
                    return;
                }
                resultado = a / b;
                operacionTexto = `${a} ÷ ${b} = ${resultado}`;
                break;
            case '**':
                if (isNaN(b)) {
                    calcResult.textContent = t.error_exponent;
                    calcResult.style.color = 'var(--color-error)';
                    return;
                }
                resultado = Math.pow(a, b);
                operacionTexto = `${a}^${b} = ${resultado}`;
                break;
            case 'sqrt':
                if (a < 0) {
                    calcResult.textContent = t.error_sqrt_negative;
                    calcResult.style.color = 'var(--color-error)';
                    return;
                }
                resultado = Math.sqrt(a);
                operacionTexto = `√${a} = ${resultado}`;
                break;
            default:
                calcResult.textContent = 'Operación no válida';
                calcResult.style.color = 'var(--color-error)';
                return;
        }
        
        calcResult.textContent = operacionTexto;
        calcResult.style.color = 'var(--color-primary)';
        
    } catch (error) {
        calcResult.textContent = `Error: ${error.message}`;
        calcResult.style.color = 'var(--color-error)';
    }
}

/**
 * Actualiza el símbolo de operación mostrado
 * @param {string} op - Operador a mostrar
 */
function actualizarOperador(op) {
    const simbolos = {
        '+': '+',
        '-': '−',
        '*': '×',
        '/': '÷',
        '**': '^',
        'sqrt': '√'
    };
    calcOperator.textContent = simbolos[op] || op;
}

// ========================================
// Event Listeners
// ========================================

// Botón de graficar
graphButton.addEventListener('click', handleGraphButtonClick);

// Enter en el input de función
functionInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        handleGraphButtonClick();
    }
});

// Botones de ejemplo
exampleButtons.forEach(btn => {
    btn.addEventListener('click', handleExampleClick);
});

// Botones de calculadora básica
calcButtons.forEach(btn => {
    btn.addEventListener('click', (event) => {
        const operation = event.target.dataset.op;
        if (operation) {
            actualizarOperador(operation);
            calcular_basico(operation);
        }
    });
});

// Enter en los inputs de calculadora
calcA.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        calcB.focus();
    }
});

calcB.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        // Usar el último operador seleccionado (por defecto suma)
        const lastOp = calcOperator.textContent === '×' ? '*' : 
                       calcOperator.textContent === '÷' ? '/' : 
                       calcOperator.textContent === '−' ? '-' : 
                       calcOperator.textContent === '^' ? '**' : 
                       calcOperator.textContent === '√' ? 'sqrt' : '+';
        calcular_basico(lastOp);
    }
});

// Pestañas
tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const tabId = btn.dataset.tab;
        switchTab(tabId);
    });
});

// Selector de idioma
langButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const lang = btn.dataset.lang;
        changeLanguage(lang);
    });
});

// ========================================
// Inicialización
// ========================================

// Mostrar mensaje inicial en el contenedor del gráfico
const initialMessage = {
    es: 'Ingresa una función y presiona "Graficar" para visualizarla',
    en: 'Enter a function and press "Graph" to visualize it',
    fr: 'Entrez une fonction et appuyez sur "Tracer" pour la visualiser',
    de: 'Geben Sie eine Funktion ein und drücken Sie "Grafik" zum Visualisieren'
};

function setInitialMessage() {
    graphContainer.innerHTML = `<p style="text-align: center; color: #64748b;">${initialMessage[currentLang]}</p>`;
}

setInitialMessage();

// Graficar sin(x) como ejemplo inicial al cargar la página
window.addEventListener('load', () => {
    functionInput.value = 'sin(x)';
    // Pequeño delay para asegurar que Plotly esté cargado
    setTimeout(() => {
        handleGraphButtonClick();
    }, 500);
});

// ========================================
// Diagrama de Flujo (comentario documentación)
// ========================================
/*
┌─────────────────────────────────────────────────────────────────────┐
│                    DIAGRAMA DE FLUJO                                │
│              Comunicación Frontend - Backend                        │
└─────────────────────────────────────────────────────────────────────┘

    ┌─────────────────┐
    │  Usuario ingresa │
    │  función: sin(x) │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Click en botón  │
    │   "Graficar"    │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │   JavaScript    │
    │ handleGraphBtn  │
    │ Click()         │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐         POST /api/graficar
    │   Fetch API     │─────────────────────────────────┐
    │  (Async Request)│                                 │
    └─────────────────┘                                 │
                                                        ▼
                                               ┌─────────────────┐
                                               │   Flask Server  │
                                               │    (Backend)    │
                                               └────────┬────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │  SymPy Parser   │
                                               │ (Seguro, no     │
                                               │  usa eval)      │
                                               └────────┬────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │     NumPy       │
                                               │ np.linspace()   │
                                               │ Calcula puntos  │
                                               └────────┬────────┘
                                                        │
    ┌─────────────────┐         JSON Response           │
    │   JavaScript    │◄────────────────────────────────┘
    │ Recibe x_coords │        {x_coords, y_coords}
    │    y_coords     │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │   Plotly.js     │
    │  renderGraph()  │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  Gráfico        │
    │  renderizado    │
    │  en <div>       │
    └─────────────────┘

*/
