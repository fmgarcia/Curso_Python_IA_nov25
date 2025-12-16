/**
 * Sistema de traducciones multiidioma
 * Idiomas soportados: Español, Inglés, Francés, Alemán
 */

const translations = {
    es: {
        // Header
        title: '🧮 Calculadora Gráfica',
        subtitle: 'Ingresa una función matemática y visualiza su gráfica en tiempo real',
        
        // Pestañas
        tab_graphs: '📈 Funciones Trigonométricas',
        tab_calculator: '🔢 Operaciones Básicas',
        
        // Entrada de función
        input_placeholder: 'Ej: sin(x) + x^2, cos(2*x), exp(-x^2)',
        range_min: 'x mín:',
        range_max: 'x máx:',
        range_points: 'Puntos:',
        btn_graph: '📈 Graficar',
        
        // Ejemplos
        examples_title: 'Ejemplos de funciones:',
        
        // Ayuda
        help_title: '📖 Funciones disponibles',
        help_trig: 'Trigonométricas:',
        help_exp: 'Exponencial:',
        help_log: 'Logaritmo:',
        help_sqrt: 'Raíz cuadrada:',
        help_abs: 'Valor absoluto:',
        help_pow: 'Potencias:',
        help_const: 'Constantes:',
        help_ops: 'Operadores:',
        
        // Calculadora
        calc_title: '🔢 Calculadora Básica',
        calc_num1: 'Número 1',
        calc_num2: 'Número 2',
        calc_add: '+ Sumar',
        calc_sub: '− Restar',
        calc_mult: '× Multiplicar',
        calc_div: '÷ Dividir',
        calc_pow: '^ Potencia',
        calc_sqrt: '√ Raíz',
        calc_result: 'Resultado:',
        
        // Errores
        error_empty_function: 'Por favor, ingresa una función matemática.',
        error_invalid_range: 'El valor de x mín debe ser menor que x máx.',
        error_connection: 'No se pudo conectar con el servidor. Asegúrate de que el backend está corriendo en http://localhost:5000',
        error_first_number: 'Error: Ingresa el primer número',
        error_second_number: 'Error: Ingresa el segundo número',
        error_exponent: 'Error: Ingresa el exponente',
        error_division_zero: 'Error: División por cero',
        error_sqrt_negative: 'Error: Raíz de número negativo',
        
        // Footer
        footer: 'Desarrollado con Flask + Plotly.js | EOI 2025'
    },
    
    en: {
        // Header
        title: '🧮 Graphing Calculator',
        subtitle: 'Enter a mathematical function and visualize its graph in real time',
        
        // Tabs
        tab_graphs: '📈 Trigonometric Functions',
        tab_calculator: '🔢 Basic Operations',
        
        // Function input
        input_placeholder: 'Ex: sin(x) + x^2, cos(2*x), exp(-x^2)',
        range_min: 'x min:',
        range_max: 'x max:',
        range_points: 'Points:',
        btn_graph: '📈 Graph',
        
        // Examples
        examples_title: 'Function examples:',
        
        // Help
        help_title: '📖 Available functions',
        help_trig: 'Trigonometric:',
        help_exp: 'Exponential:',
        help_log: 'Logarithm:',
        help_sqrt: 'Square root:',
        help_abs: 'Absolute value:',
        help_pow: 'Powers:',
        help_const: 'Constants:',
        help_ops: 'Operators:',
        
        // Calculator
        calc_title: '🔢 Basic Calculator',
        calc_num1: 'Number 1',
        calc_num2: 'Number 2',
        calc_add: '+ Add',
        calc_sub: '− Subtract',
        calc_mult: '× Multiply',
        calc_div: '÷ Divide',
        calc_pow: '^ Power',
        calc_sqrt: '√ Root',
        calc_result: 'Result:',
        
        // Errors
        error_empty_function: 'Please enter a mathematical function.',
        error_invalid_range: 'x min value must be less than x max.',
        error_connection: 'Could not connect to the server. Make sure the backend is running on http://localhost:5000',
        error_first_number: 'Error: Enter the first number',
        error_second_number: 'Error: Enter the second number',
        error_exponent: 'Error: Enter the exponent',
        error_division_zero: 'Error: Division by zero',
        error_sqrt_negative: 'Error: Square root of negative number',
        
        // Footer
        footer: 'Developed with Flask + Plotly.js | EOI 2025'
    },
    
    fr: {
        // Header
        title: '🧮 Calculatrice Graphique',
        subtitle: 'Entrez une fonction mathématique et visualisez son graphique en temps réel',
        
        // Tabs
        tab_graphs: '📈 Fonctions Trigonométriques',
        tab_calculator: '🔢 Opérations Basiques',
        
        // Function input
        input_placeholder: 'Ex: sin(x) + x^2, cos(2*x), exp(-x^2)',
        range_min: 'x min:',
        range_max: 'x max:',
        range_points: 'Points:',
        btn_graph: '📈 Tracer',
        
        // Examples
        examples_title: 'Exemples de fonctions:',
        
        // Help
        help_title: '📖 Fonctions disponibles',
        help_trig: 'Trigonométriques:',
        help_exp: 'Exponentielle:',
        help_log: 'Logarithme:',
        help_sqrt: 'Racine carrée:',
        help_abs: 'Valeur absolue:',
        help_pow: 'Puissances:',
        help_const: 'Constantes:',
        help_ops: 'Opérateurs:',
        
        // Calculator
        calc_title: '🔢 Calculatrice Basique',
        calc_num1: 'Nombre 1',
        calc_num2: 'Nombre 2',
        calc_add: '+ Additionner',
        calc_sub: '− Soustraire',
        calc_mult: '× Multiplier',
        calc_div: '÷ Diviser',
        calc_pow: '^ Puissance',
        calc_sqrt: '√ Racine',
        calc_result: 'Résultat:',
        
        // Errors
        error_empty_function: 'Veuillez entrer une fonction mathématique.',
        error_invalid_range: 'La valeur x min doit être inférieure à x max.',
        error_connection: 'Impossible de se connecter au serveur. Assurez-vous que le backend fonctionne sur http://localhost:5000',
        error_first_number: 'Erreur: Entrez le premier nombre',
        error_second_number: 'Erreur: Entrez le deuxième nombre',
        error_exponent: 'Erreur: Entrez l\'exposant',
        error_division_zero: 'Erreur: Division par zéro',
        error_sqrt_negative: 'Erreur: Racine d\'un nombre négatif',
        
        // Footer
        footer: 'Développé avec Flask + Plotly.js | EOI 2025'
    },
    
    de: {
        // Header
        title: '🧮 Grafischer Rechner',
        subtitle: 'Geben Sie eine mathematische Funktion ein und visualisieren Sie ihren Graphen in Echtzeit',
        
        // Tabs
        tab_graphs: '📈 Trigonometrische Funktionen',
        tab_calculator: '🔢 Grundrechenarten',
        
        // Function input
        input_placeholder: 'Bsp: sin(x) + x^2, cos(2*x), exp(-x^2)',
        range_min: 'x min:',
        range_max: 'x max:',
        range_points: 'Punkte:',
        btn_graph: '📈 Grafik',
        
        // Examples
        examples_title: 'Funktionsbeispiele:',
        
        // Help
        help_title: '📖 Verfügbare Funktionen',
        help_trig: 'Trigonometrische:',
        help_exp: 'Exponential:',
        help_log: 'Logarithmus:',
        help_sqrt: 'Quadratwurzel:',
        help_abs: 'Absolutwert:',
        help_pow: 'Potenzen:',
        help_const: 'Konstanten:',
        help_ops: 'Operatoren:',
        
        // Calculator
        calc_title: '🔢 Grundrechner',
        calc_num1: 'Zahl 1',
        calc_num2: 'Zahl 2',
        calc_add: '+ Addieren',
        calc_sub: '− Subtrahieren',
        calc_mult: '× Multiplizieren',
        calc_div: '÷ Dividieren',
        calc_pow: '^ Potenz',
        calc_sqrt: '√ Wurzel',
        calc_result: 'Ergebnis:',
        
        // Errors
        error_empty_function: 'Bitte geben Sie eine mathematische Funktion ein.',
        error_invalid_range: 'Der Wert von x min muss kleiner als x max sein.',
        error_connection: 'Verbindung zum Server konnte nicht hergestellt werden. Stellen Sie sicher, dass das Backend auf http://localhost:5000 läuft',
        error_first_number: 'Fehler: Geben Sie die erste Zahl ein',
        error_second_number: 'Fehler: Geben Sie die zweite Zahl ein',
        error_exponent: 'Fehler: Geben Sie den Exponenten ein',
        error_division_zero: 'Fehler: Division durch Null',
        error_sqrt_negative: 'Fehler: Quadratwurzel einer negativen Zahl',
        
        // Footer
        footer: 'Entwickelt mit Flask + Plotly.js | EOI 2025'
    }
};
