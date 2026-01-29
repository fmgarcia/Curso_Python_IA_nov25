import csv
import random

def generar_dataset_spam(nombre_archivo="dataset_spam_spanish.csv", total_mails=10000):
    """
    Genera un archivo CSV con 10,000 correos simulados en español.
    Incluye más de 100 templates por categoría para máxima diversidad.
    """

    # --- 100+ TEMPLATES PARA SPAM (1) ---
    spam_templates = [
        "¡URGENTE! Tu cuenta de {banco} ha sido bloqueada. Reactiva aquí: {url}",
        "Has ganado un premio de {monto} euros en la lotería de {pais}. Contacta a {email}.",
        "Gana dinero desde casa trabajando solo 2 horas al día. Detalles en {url}",
        "Oportunidad única: Invierte en {crypto} y multiplica tu capital hoy mismo.",
        "Tu paquete de {tienda} está retenido. Paga las tasas de aduana aquí: {url}",
        "¡Felicidades! Fuiste seleccionado para un sorteo de un iPhone 15 Pro Max.",
        "Descuentos del 90% en suplementos y salud. Visita nuestra farmacia en {url}",
        "Confirmación de transferencia de {monto} pendiente. Ver detalles: {url}",
        "Hola, soy una joven que busca amistad. Escríbeme a mi Telegram: @user_hot",
        "Recupera tu acceso a Instagram inmediatamente pulsando en este enlace seguro.",
        "Aviso de embargo: Tienes una deuda pendiente con {banco}. Paga ahora: {url}",
        "Gana {monto} extra al mes vendiendo productos de belleza desde tu móvil.",
        "Tu suscripción a {servicio} ha fallado. Actualiza tu método de pago: {url}",
        "Se ha detectado un inicio de sesión sospechoso en su cuenta de {banco}.",
        "¿Quieres perder peso rápido? Prueba nuestras pastillas milagrosas en {url}",
        "Oferta de empleo: Buscamos asistente remoto. Sueldo de {monto} semanales.",
        "Reclama tu tarjeta regalo de {tienda} de 500 euros antes de que caduque.",
        "Su préstamo de {monto} ha sido pre-aprobado. Solicítelo ya en {url}",
        "Invierta en el nuevo mercado de {crypto} antes de que suba de precio.",
        "Atención: Su cuenta de correo será eliminada si no confirma sus datos en {url}",
        "Última oportunidad para conseguir el curso de trading con un 80% de descuento.",
        "Te envié las fotos que me pediste aquí: {url} (Contenido solo para adultos)",
        "Tu factura de {servicio} está vencida. Evita el corte del servicio aquí: {url}",
        "¿Buscas pareja? Hay 5 personas cerca de ti queriendo conocerte en {url}",
        "Ayuda humanitaria: Donación de {monto} euros a su nombre. Responda a este mail.",
        "Descarga la nueva actualización crítica de seguridad para tu PC en {url}",
        "Hackers tienen tus videos privados. Paga en {crypto} para evitar que se publiquen.",
        "Gana una beca completa para estudiar en el extranjero. Pulsa aquí: {url}",
        "Tu pedido de {tienda} ha sido cancelado. Solicita el reembolso en {url}",
        "Su ID de Apple ha sido bloqueado por razones de seguridad. Desbloquee en {url}",
        "¡Bingo! Tienes un bono de bienvenida de {monto} para jugar en el casino online.",
        "Invierta en oro y plata de forma segura con nuestra plataforma en {url}",
        "Aumenta tus seguidores en redes sociales de forma orgánica y rápida con {url}",
        "Felicidades {nombre}, has sido preseleccionado para el reality show de moda.",
        "Obtenga su diploma universitario sin estudiar. Información por privado.",
        "Su cuenta de PayPal ha sido restringida. Verifique su identidad aquí: {url}",
        "Reciba muestras gratuitas de productos {tienda} en su domicilio hoy mismo.",
        "Acceda a la preventa exclusiva de la nueva moneda {crypto} solo por invitación.",
        "Tu coche tiene una multa de tráfico pendiente de pago. Ver imagen: {url}",
        "¿Problemas de rendimiento masculino? Tenemos la solución definitiva en {url}",
        "¡Bomba! La noticia que {banco} no quiere que sepas sobre cómo ahorrar.",
        "Gana dinero probando videojuegos desde casa. Regístrate en {url}",
        "Te han dejado un mensaje de voz importante. Escúchalo aquí: {url}",
        "Solicitud de amistad pendiente de una persona que conoces en {url}",
        "Su reembolso de impuestos de {monto} está listo. Confirme su cuenta: {url}",
        "Gana un viaje todo incluido a {pais} respondiendo esta encuesta de 1 minuto.",
        "Atención cliente: Su clave de acceso caduca en 24 horas. Cámbiela en {url}",
        "Consiga la sonrisa perfecta con nuestros implantes dentales a mitad de precio.",
        "Urgente: Alerta de virus detectada en su navegador. Limpie su sistema en {url}",
        "Vea quién está espiando su perfil de Facebook entrando en {url}",
        "Tu cuenta de Netflix será suspendida. Por favor actualiza tus datos de pago.",
        "Reclama tus tokens gratuitos de {crypto} conectando tu wallet en {url}",
        "Trabajo de medio tiempo para Amazon. Gana hasta {monto} al día.",
        "Has sido mencionado en una publicación. Haz clic para ver el comentario.",
        "Consigue el nuevo Samsung Galaxy S24 Ultra por solo 1 euro participando aquí.",
        "Oferta de préstamo personal sin intereses para nuevos clientes en {url}",
        "Tu paquete de Correos está listo para entrega pero faltan datos. Pulsa {url}",
        "Invierta en acciones de Tesla y gane dividendos mensuales garantizados.",
        "Usted tiene una herencia sin reclamar de un pariente en {pais}.",
        "Mejora tu historial crediticio con nuestro método legal y rápido.",
        "Tu suscripción premium ha caducado. Haz clic para renovar con descuento.",
        "Recibe una tarjeta de combustible de 100€ por ser cliente de {banco}.",
        "Gana dinero enviando correos electrónicos desde casa. Método probado.",
        "Nuevo mensaje de tu banco: Tienes un aviso importante en tu buzón virtual.",
        "Se ha realizado una compra de {monto} en {tienda} con su tarjeta. ¿No fue usted?",
        "Consigue licencias de Windows y Office por menos de 5 euros en {url}",
        "Aprende a ganar en la ruleta con este truco matemático infalible.",
        "Tu cuenta de Amazon Prime ha sido bloqueada temporalmente. Verifica en {url}",
        "Participa en el sorteo de un crucero por el Mediterráneo para dos personas.",
        "Haz que tu web aparezca en el número 1 de Google con nuestros servicios.",
        "Compra seguidores reales para TikTok e Instagram al mejor precio en {url}",
        "Últimos días para aprovechar las rebajas de verano en relojes de lujo.",
        "Su acceso a la banca online de {banco} ha sido deshabilitado. Entre en {url}",
        "Gana una cena para dos en un restaurante estrella Michelin de tu ciudad.",
        "Te han enviado un archivo confidencial por WeTransfer. Descarga en {url}",
        "Invierta en propiedades inmobiliarias desde solo 100 euros con crowdfunding.",
        "Tu mascota puede ser la imagen de nuestra nueva campaña de {tienda}.",
        "Ahorra hasta un 70% en tu factura de la luz con estos nuevos paneles solares.",
        "Su dirección IP está siendo utilizada para actividades ilegales. Protéjase.",
        "Consigue el carnet de conducir sin examen práctico. Escríbenos ya.",
        "¡Alerta! Alguien ha intentado cambiar la contraseña de su cuenta de {servicio}.",
        "Recibe {monto} euros por abrir una cuenta en nuestro nuevo banco digital.",
        "Tu seguro de coche está a punto de vencer. Compara y ahorra con nosotros.",
        "Gana una tarjeta regalo de IKEA de 200 euros completando este test.",
        "Su cuenta ha sido seleccionada para una auditoría de seguridad. Pulse aquí.",
        "Descubra el secreto para ganar la lotería nacional cada semana.",
        "Trabaje como probador de productos electrónicos para grandes marcas.",
        "Consiga una suscripción de por vida a {servicio} por un pago único de 10€.",
        "Tu crédito de Google Ads está listo para ser usado. Actívalo en {url}",
        "Únete a nuestra red de inversores VIP y recibe señales de trading diarias.",
        "Su paquete ha sido entregado en un punto de recogida. Ver dirección: {url}",
        "Gana dinero compartiendo enlaces en tus redes sociales. Es gratis.",
        "Felicidades, eres el visitante número un millón. Reclama tu premio aquí.",
        "Tu cuenta de Disney+ se renovará automáticamente al precio completo. Cancela.",
        "Consiga el nuevo perfume de Dior totalmente gratis participando en {url}",
        "Su préstamo ha sido aprobado. Reciba el dinero en menos de 10 minutos.",
        "Invierta en la industria del cannabis legal y obtenga grandes rentabilidades.",
        "Su acceso a la plataforma de inversión ha sido bloqueado por seguridad.",
        "Obtenga un cupón de 50€ para gastar en {tienda} por su fidelidad.",
        "Atención: Se ha detectado un virus en su dispositivo móvil. Instale {url}"
    ]

    # --- 100+ TEMPLATES PARA NO SPAM (0) ---
    ham_templates = [
        "Hola {nombre}, ¿confirmamos la reunión para el próximo {dia} a las {hora}?",
        "Adjunto envío el reporte de ventas correspondiente al mes de {mes}.",
        "Recordatorio: Tienes una cita médica el {dia} a las {hora}. Por favor llega puntual.",
        "Gracias por tu compra en {tienda}. Tu pedido #{numero} ya está de camino.",
        "¿Qué tal todo? Hace mucho que no hablamos, a ver si quedamos pronto para comer.",
        "La presentación del proyecto {proyecto} ha sido pospuesta para la semana que viene.",
        "Tu suscripción a {servicio} se ha renovado correctamente. Gracias por tu confianza.",
        "Hola equipo, les comparto el acta de la reunión de hoy. Saludos.",
        "¿Me podrías pasar el contacto de Laura? Necesito consultarle una duda técnica.",
        "Confirmación de tu reserva en el restaurante para el {dia} a las {hora}.",
        "Hola {nombre}, te envío los apuntes que me pediste de la clase de ayer.",
        "Tu factura de {servicio} de este mes ya está disponible para descargar.",
        "El profesor ha subido una nueva nota al portal de la universidad.",
        "¿Vienes a la cena de cumpleaños de Carmen este viernes? Confírmame por favor.",
        "Te mando el presupuesto para la reforma del baño. Avísame si tienes dudas.",
        "Confirmación de envío: Su paquete de {tienda} llegará mañana entre las 9 y las 14h.",
        "Hola jefe, ya he terminado las tareas que me encargó esta mañana.",
        "¿Podrías revisar el texto que te envié por correo antes de mandarlo al cliente?",
        "Gracias por contactar con nuestro servicio de atención al cliente. Su ticket es #{numero}.",
        "He reservado las entradas para el cine del domingo. Nos vemos allí.",
        "Recordatorio de pago: Tu recibo de autónomos se cargará el próximo {dia}.",
        "Hola mamá, ya hemos llegado al hotel. Todo está perfecto. Besos.",
        "¿Me confirmas si recibiste el paquete que te envié la semana pasada?",
        "Te adjunto el contrato firmado para que podamos proceder con el alta.",
        "El equipo de IT estará haciendo mantenimiento del servidor este {dia} de madrugada.",
        "Hola {nombre}, te comparto las fotos del viaje. ¡Lo pasamos genial!",
        "La reunión de padres de alumnos será en el aula magna el {dia} a las {hora}.",
        "Tu pedido de {tienda} ya está disponible para recoger en la tienda física.",
        "¿Tienes un momento para una llamada rápida? Es sobre el tema de {proyecto}.",
        "El dentista me ha pedido que te recuerde tu limpieza de boca anual.",
        "Hola, te escribo para agradecerte la ayuda con la mudanza del otro día.",
        "Adjunto el itinerario de nuestro viaje a {pais}. ¡Qué ganas de ir!",
        "Tu coche ya está reparado. Puedes pasar a recogerlo por el taller esta tarde.",
        "Hola {nombre}, ¿sabes a qué hora abre la biblioteca hoy?",
        "Te envío el enlace de Zoom para la clase de yoga de mañana.",
        "Confirmación de cancelación: Tu suscripción a {servicio} ha finalizado.",
        "Hola grupo, ¿alguien se ha dejado un paraguas azul en la oficina?",
        "La entrega de premios será en el auditorio el {dia} por la tarde.",
        "Te adjunto mi CV actualizado por si te enteras de alguna vacante.",
        "¿Te apetece ir a correr un rato por el parque esta tarde?",
        "Tu cita para renovar el DNI es el {dia} a las {hora} en la comisaría.",
        "Hola, te mando la lista de la compra para que no se nos olvide nada.",
        "El pedido de papelería para la oficina ya ha llegado. Está en recepción.",
        "¿Me puedes pasar la receta de la tarta que hiciste el domingo? Estaba riquísima.",
        "Hola {nombre}, espero que estés mejor de tu resfriado. Recupérate pronto.",
        "Te adjunto el manual de usuario del nuevo software que vamos a implementar.",
        "La clase de inglés se ha cancelado por enfermedad del profesor.",
        "¿Quedamos en la puerta del metro a las {hora} para ir al concierto?",
        "Tu recibo del alquiler de este mes ya ha sido procesado por el banco.",
        "Hola equipo, recordad que el lunes es festivo y la oficina estará cerrada.",
        "He visto un piso que te podría gustar. Te paso el enlace por aquí.",
        "Confirmación de vuelo: Tu check-in para el viaje a {pais} ya está abierto.",
        "Hola, ¿me podrías decir qué deberes tienen los niños para mañana?",
        "Te envío la captura de pantalla con el error que me sale en la web.",
        "¿Podemos mover la reunión de las {hora} a una hora más tarde?",
        "Gracias por participar en nuestro evento. Aquí tienes el certificado de asistencia.",
        "Hola {nombre}, ¿te llegó el correo con los detalles del proyecto {proyecto}?",
        "Te adjunto la factura de la comida de empresa para que la pases a contabilidad.",
        "El gimnasio me ha avisado de que mañana abren en horario especial.",
        "Hola, te escribo para confirmarte que ya he recibido el pago. Gracias.",
        "¿Me podrías prestar el libro que me comentaste el otro día?",
        "Recordatorio: Mañana es el último día para entregar el informe trimestral.",
        "Tu reserva de hotel en {pais} ha sido confirmada con éxito.",
        "Hola, ¿sabes dónde puedo encontrar el archivo de los clientes antiguos?",
        "Te envío el menú para la boda de mi hermana. Elige un plato principal.",
        "La conferencia de tecnología empieza a las 10:00 en el pabellón 4.",
        "Hola {nombre}, te llamé pero no me lo cogiste. Llámame cuando puedas.",
        "Adjunto el documento con los cambios que sugeriste en la última reunión.",
        "¿Me confirmas tu dirección actual para enviarte la invitación por correo?",
        "Tu pedido de comida a domicilio llegará en unos 15 minutos. ¡Que aproveche!",
        "Hola, te escribo desde el soporte técnico para resolver tu incidencia.",
        "He encontrado las llaves que habías perdido. Las tengo yo en casa.",
        "Te envío la presentación para que le eches un vistazo antes de mañana.",
        "¿Quieres que compremos algo para cenar o prefieres salir fuera?",
        "Recordatorio de cita: Peluquería el {dia} a las {hora}.",
        "Hola {nombre}, ¿has visto el mensaje que han puesto en el grupo de WhatsApp?",
        "Te adjunto el plano de la nueva oficina. Mi mesa es la del rincón.",
        "¿Me podrías ayudar a configurar el nuevo router este fin de semana?",
        "Confirmación de suscripción: Bienvenido al boletín de noticias de {tienda}.",
        "Hola, te mando el contacto del fontanero que vino a mi casa, es muy bueno.",
        "¿A qué hora quedamos mañana para ir a la universidad?",
        "Te envío la lista de reproducción para la fiesta del sábado. ¿Te gusta?",
        "La reunión con los inversores ha ido muy bien. Luego te cuento los detalles.",
        "Hola {nombre}, ¿puedes traer el cargador del portátil mañana a la oficina?",
        "Adjunto el informe de gastos del viaje a {pais} para su revisión.",
        "¿Me confirmas si el restaurante tiene opciones vegetarianas para la cena?",
        "Tu cita para la revisión del gas es el próximo {dia} por la mañana.",
        "Hola, te escribo para decirte que al final no podré ir al cine, lo siento.",
        "Te envío el código de acceso para entrar en el edificio esta tarde.",
        "¿Has recibido el enlace para la encuesta de satisfacción del curso?",
        "Hola {nombre}, te adjunto la propuesta de colaboración que hablamos.",
        "Recordatorio: Tienes una clase particular de música el {dia} a las {hora}.",
        "Tu cuenta de usuario ha sido creada correctamente. Pulsa aquí para activar.",
        "¿Me puedes decir qué tal te fue en la entrevista de trabajo de ayer?",
        "Hola equipo, el café de la cocina se ha terminado. ¿Alguien puede comprar?",
        "Te envío el documento de Word con mis comentarios en control de cambios.",
        "¿A qué hora pasa el autobús para ir al centro comercial?",
        "Confirmación de cita: Masaje relajante el {dia} a las {hora}.",
        "Hola {nombre}, ¿has podido revisar el presupuesto que te mandé?",
        "Te adjunto el ticket de compra por si tienes que cambiar algo en la tienda."
    ]

    # --- VARIABLES PARA RELLENAR ---
    bancos = ["Santander", "BBVA", "CaixaBank", "Banco Sabadell", "Bankinter", "Abanca", "Unicaja", "ING"]
    montos = ["100", "500", "1.200", "2.500", "5.000", "15.000", "45.000"]
    urls = ["bit.ly/secure-auth", "verificar-cuenta.net", "premios-ya.org/click", "t.co/promo", "shrt.url/xyz", "seguridad-banca.com"]
    paises = ["España", "México", "Argentina", "Colombia", "Chile", "Perú"]
    nombres = ["Juan", "María", "Carlos", "Lucía", "Pedro", "Elena", "Roberto", "Ana", "Javier", "Sofía"]
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "próximo lunes"]
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    tiendas = ["Amazon", "Mercado Libre", "Zara", "El Corte Inglés", "IKEA", "Decathlon", "AliExpress"]
    servicios = ["Netflix", "Spotify", "Disney+", "iCloud", "Prime Video", "HBO Max", "Movistar+"]
    
    dataset = []

    for _ in range(total_mails):
        es_spam = random.choice([0, 1])
        
        if es_spam == 1:
            texto = random.choice(spam_templates).format(
                nombre=random.choice(nombres),
                banco=random.choice(bancos),
                monto=random.choice(montos),
                url=random.choice(urls),
                pais=random.choice(paises),
                email="admin@verificar-datos.com",
                crypto="Bitcoin",
                tienda=random.choice(tiendas),
                servicio=random.choice(servicios)
            )
        else:
            texto = random.choice(ham_templates).format(
                nombre=random.choice(nombres),
                dia=random.choice(dias),
                hora=f"{random.randint(9, 20)}:{random.choice(['00', '15', '30', '45'])}",
                mes=random.choice(meses),
                tienda=random.choice(tiendas),
                numero=random.randint(1000, 99999),
                proyecto=random.choice(["Alpha", "Beta", "Sigma", "Ventas 2024", "Marketing"]),
                servicio=random.choice(servicios),
                pais=random.choice(paises)
            )
        
        # Escapar comas para evitar errores en el CSV
        texto = texto.replace(",", ";")
        dataset.append([texto, es_spam])

    # Mezclar el dataset para que no estén ordenados
    random.shuffle(dataset)

    # Guardar en CSV
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["mail", "Spam"])
        writer.writerows(dataset)

    print(f"Dataset generado con éxito: {nombre_archivo}")
    print(f"Total de registros: {len(dataset)}")

if __name__ == "__main__":
    generar_dataset_spam()