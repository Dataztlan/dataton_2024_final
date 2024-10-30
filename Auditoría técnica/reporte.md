# Reporte de Evaluación de Plataformas de E-commerce

## Introducción

Este informe presenta una evaluación detallada de las plataformas de E-Commerce de las tiendas departamentales afiliadas a la ANTAD. Realizar esta auditoría es crucial para identificar vulnerabilidades, mejorar la experiencia del cliente y asegurar que los sitios cumplan con los más altos estándares de seguridad. La presencia y confiabilidad de estas plataformas son esenciales para proteger la información de los usuarios, garantizar transacciones seguras y fomentar la confianza en el comercio electrónico.

Para llevar a cabo esta auditoría, se han utilizado herramientas avanzadas de hacking ético y técnicas de evaluación de seguridad. El proceso incluyó pruebas de penetración (pentesting) que simulan ataques cibernéticos para identificar posibles brechas de seguridad. Los códigos y protocolos fueron revisados exhaustivamente, y se llevaron a cabo pruebas de estrés en los servidores para evaluar su capacidad de manejar grandes volúmenes de tráfico. Además, se realizó una evaluación de riesgos utilizando herramientas profesionales de seguridad informática, asegurando que cada plataforma fuera analizada bajo diversos métodos y condiciones.

Las categorías evaluadas incluyen:

- **Servicio al Cliente**
- **Cumplimiento/Fiabilidad**
- **Facilidad de Uso**
- **Portafolio de Productos/Servicios**
- **Seguridad y Privacidad**

Cada categoría se evaluó teniendo en cuenta las mejores prácticas de la industria en E-commerce, y los resultados permiten identificar tanto puntos fuertes como áreas de mejora para cada plataforma. Las categorías evaluadas se basan en la investigación presentada en el artículo *"Key Drivers of Customer Satisfaction on the E-Commerce Business"* de Muhammad Masyhuri, publicado en el **East Asian Journal of Multidisciplinary Research** (EAJMR), Vol.1, No.3, 2022, pp. 657-670. Este estudio analiza los factores clave que contribuyen a la satisfacción del cliente en el comercio electrónico, destacando la importancia de la seguridad y confianza en plataformas en línea (DOI: 10.55927).

La evaluación de seguridad informática de las plataformas se llevó a cabo empleando herramientas avanzadas de hacking ético. Se realizaron pruebas de penetración (pentest), evaluaciones de código y servidores, análisis de riesgo, y revisiones exhaustivas de certificados y protocolos de seguridad HTTPS. Estas pruebas se ejecutaron en distintos sistemas operativos y navegadores ampliamente utilizados, garantizando que los entornos evaluados fueran representativos de los usuarios comunes y que la seguridad fuera consistente en diversos contextos técnicos.

## Criterios de Evaluación

- **Servicio al Cliente**: Evalúa la calidad y eficiencia del soporte al cliente, la disponibilidad de canales de atención (chat en vivo, teléfono, correo electrónico) y la resolución efectiva de problemas.
- **Cumplimiento/Fiabilidad**: Este aspecto considera la rapidez y puntualidad de los envíos o recolecciones, así como la consistencia en la experiencia de compra.
- **Facilidad de Uso**: Evalúa la calidad de la interfaz y experiencia de usuario (UI/UX). Una calificación de 5 en esta categoría indica que la plataforma sigue las mejores prácticas de la industria en términos de diseño intuitivo, facilidad de navegación y un carrito de compras accesible, fácil de modificar y de actualizar en cualquier momento.
- **Portafolio de Productos/Servicios**: Se refiere a la variedad y disponibilidad de productos o servicios en la plataforma.
- **Seguridad y Privacidad**: Evalúa el uso de HTTPS, la presencia de certificados SSL/TLS y prácticas de seguridad adicionales que garanticen la protección de los datos personales y financieros de los usuarios.

## Evaluación Detallada por Plataforma

### 1. **Almacenes García**
   - **Servicio al Cliente**: 5 - Almacenes García destaca en la atención al cliente, con personal capacitado y múltiples canales de contacto que facilitan la resolución de dudas o problemas de los usuarios.
   - **Cumplimiento/Fiabilidad**: 5 - La plataforma es altamente confiable en términos de entrega, ofreciendo incluso la opción de entrega el mismo día en algunas ubicaciones, lo cual es una ventaja competitiva importante en el sector.
   - **Facilidad de Uso**: 5 - La plataforma sigue las mejores prácticas de UI/UX en E-commerce, ofreciendo una navegación clara, diseño intuitivo y un carrito de compras que permite modificaciones de manera sencilla, lo cual mejora la experiencia de compra.
   - **Portafolio de Productos/Servicios**: 5 - Almacenes García ofrece una amplia gama de productos que cubren diversas necesidades de los consumidores, asegurando buena disponibilidad y variedad.
   - **Seguridad y Privacidad**: 5 - Cumple con altos estándares de seguridad, utilizando HTTPS y un certificado SSL válido para garantizar la protección de la información del cliente.

   #### Análisis de Seguridad Informática

Almacenes García ha recibido una calificación **A+** en el análisis de su certificado SSL. Este puntaje refleja una excelente implementación de seguridad en su plataforma de e-commerce, cumpliendo con los estándares más altos de la industria para la protección de datos y la privacidad de sus usuarios. A continuación, se detallan los aspectos relevantes evaluados:

1. **Certificado SSL**
   - El sitio de Almacenes García utiliza un certificado **RSA de 2048 bits** con un algoritmo de firma **SHA256withRSA**. Este tipo de cifrado es actualmente robusto y ampliamente aceptado en la industria para proteger la transmisión de datos entre el cliente y el servidor.
   - El certificado es emitido por **Go Daddy Secure Certificate Authority - G2** y es válido hasta el **13 de septiembre de 2025**, asegurando un periodo de validez largo antes de requerir renovación.

2. **Soporte de Protocolo**
   - El servidor de Almacenes García soporta **TLS 1.3**, que es la versión más reciente y segura del protocolo TLS. Este protocolo mejora la eficiencia y seguridad en la conexión en comparación con versiones anteriores como TLS 1.2, al reducir la latencia y evitar ciertas vulnerabilidades.
   - Además, el sitio utiliza **HSTS (HTTP Strict Transport Security)** con una duración extendida, lo que asegura que los navegadores siempre accedan al sitio mediante HTTPS, reduciendo el riesgo de ataques de tipo "downgrade" o ataques de intermediario (MITM).

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del intercambio de claves y la fortaleza del cifrado recibió una puntuación alta, indicando que el sitio utiliza algoritmos fuertes para proteger la integridad y confidencialidad de las comunicaciones.
   - Al soportar los mecanismos de intercambio de claves y cifrado actualizados, se mitiga el riesgo de compromisos en la sesión, protegiendo así los datos del usuario durante su transferencia.

4. **Validación de Certificado y Transparencia**
   - Almacenes García ha implementado **Certificate Transparency**, lo que añade una capa adicional de seguridad al hacer pública la emisión de certificados. Esto permite detectar y evitar certificados falsificados o maliciosos que pudieran intentar suplantar al sitio oficial.
   - El sitio también respalda el **OCSP (Online Certificate Status Protocol)**, permitiendo verificar en tiempo real el estado del certificado, lo cual refuerza la seguridad al garantizar que el certificado no haya sido revocado.

5. **Consideraciones Generales**
   - Aunque la configuración actual es sólida, se recomienda a Almacenes García mantener actualizadas sus prácticas de seguridad y renovar su certificado antes de su fecha de caducidad en septiembre de 2025.
   - La adopción de TLS 1.3 y HSTS refuerza el compromiso de Almacenes García con la protección de la información de sus clientes, disminuyendo la vulnerabilidad a interceptaciones y manipulaciones de datos.

##### Conclusión
La infraestructura de seguridad de Almacenes García en términos de **Certificado SSL, Soporte de Protocolo, Intercambio de Claves y Transparencia del Certificado** es óptima, ubicándose en el nivel de excelencia en estándares de seguridad para sitios e-commerce. Esto contribuye a una experiencia de compra segura y confiable para los usuarios.

### 2. **Cimaco**

Cimaco se destaca por ofrecer una atención al cliente de alta calidad, aunque presenta algunas limitaciones en sus canales de comunicación. A continuación, se analizan los aspectos clave relacionados con su experiencia general:

**Servicio al Cliente**: **5** - El servicio al cliente de Cimaco es sobresaliente, caracterizado por respuestas rápidas y eficaces a las inquietudes de los usuarios. Sin embargo, una desventaja significativa es la falta de opciones de contacto a través de WhatsApp, un canal que muchos consumidores hoy en día consideran conveniente y accesible. A pesar de esto, Cimaco compensa esta limitación con la atención al cliente disponible por medio de llamadas telefónicas. Este enfoque permite a los clientes obtener asistencia directa, pero la ausencia de opciones más modernas puede hacer que algunos clientes se sientan menos satisfechos en comparación con otras plataformas que ofrecen múltiples vías de comunicación. 

**Cumplimiento/Fiabilidad**: **4** - Cimaco generalmente cumple con los tiempos de entrega que promete, manteniendo una reputación sólida en este aspecto. Sin embargo, su servicio de entrega podría no ser tan rápido como el de competidores locales como Almacenes García, lo que podría influir en la satisfacción general de los clientes que buscan rapidez en sus compras. Mejorar los tiempos de entrega sería beneficioso para incrementar su competitividad en el mercado.

**Facilidad de Uso**: **4** - La plataforma de Cimaco es relativamente fácil de navegar, ofreciendo una experiencia funcional para los usuarios. No obstante, hay algunos aspectos de la interfaz que podrían ser refinados para alinearse más estrechamente con las mejores prácticas de UI/UX. Por ejemplo, aunque la experiencia en el carrito de compras es adecuada, podría mejorarse para que sea más intuitiva y fluida. La simplificación de ciertos procesos podría facilitar aún más las compras para los usuarios, mejorando la experiencia general.

**Portafolio de Productos/Servicios**: **4** - La variedad de productos ofrecidos por Cimaco es buena, abarcando varios sectores. Sin embargo, hay espacio para ampliar la gama en algunas categorías específicas, lo cual podría enriquecer la oferta al cliente y atraer a un público más amplio. Ampliar el portafolio sería una estrategia efectiva para aumentar las opciones disponibles y satisfacer mejor las diversas necesidades del consumidor.

**Seguridad y Privacidad**: **4** - Cimaco utiliza HTTPS y un certificado SSL, lo que garantiza un nivel adecuado de seguridad en las transacciones y la protección de los datos de los clientes. Sin embargo, se han detectado vulnerabilidades menores en el código fuente, como la visibilidad de ciertos scripts, que deben ser abordadas para asegurar que la plataforma se mantenga segura y confiable. Es fundamental que Cimaco realice un seguimiento continuo de sus prácticas de seguridad para proteger la información sensible de los usuarios y mantener la confianza del cliente.

   #### Análisis de Seguridad Informática

El análisis de seguridad SSL para **Cimaco** muestra una excelente implementación de protocolos de seguridad, obteniendo una calificación **A+**, lo que indica que Cimaco ha adoptado medidas avanzadas para proteger la información y garantizar una navegación segura para sus usuarios. A continuación se detallan los aspectos clave de su seguridad informática:

1. **Certificado SSL**
   - Cimaco utiliza un certificado de **RSA 2048 bits** firmado con el algoritmo **SHA256withRSA**, el cual proporciona un nivel de cifrado adecuado y seguro para la transferencia de datos. Este tipo de certificado es ampliamente confiable y comúnmente aceptado por navegadores y sistemas modernos.
   - Este nivel de cifrado asegura que las comunicaciones entre el servidor y el cliente estén encriptadas, impidiendo el acceso de terceros a la información transmitida, como datos de pago y personales.

2. **Soporte de Protocolo**
   - El servidor de Cimaco soporta **TLS 1.3**, la versión más actual y segura del protocolo TLS. Este protocolo mejora tanto la seguridad como la velocidad de la conexión en comparación con versiones anteriores, eliminando ciertos pasos en el proceso de establecimiento de la conexión y mejorando la resistencia a ataques de seguridad como el “downgrade” de protocolo y el ataque de intermediario (MITM).
   - Además, la implementación de **HTTP Strict Transport Security (HSTS)** con una duración prolongada asegura que todos los usuarios accedan siempre a la versión segura del sitio, previniendo que se acceda al sitio a través de conexiones HTTP inseguras.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - El puntaje en la categoría de intercambio de claves y fortaleza del cifrado es alto, lo que sugiere que el sitio utiliza configuraciones de intercambio de claves robustas, que minimizan las posibilidades de comprometer la integridad de las sesiones.
   - Esta configuración protege contra ataques comunes de desvío o intercepción, fortaleciendo la privacidad de las transacciones y la navegación de los usuarios.

4. **Buenas Prácticas en Seguridad de Certificados**
   - Cimaco implementa prácticas de transparencia en sus certificados, lo que permite verificar que estos certificados están públicamente disponibles y registrados, evitando el riesgo de certificados maliciosos o suplantaciones del sitio.
   - El servidor respalda el uso del **Online Certificate Status Protocol (OCSP)**, un mecanismo que permite verificar la validez del certificado en tiempo real, brindando una capa adicional de seguridad al asegurar que el certificado no ha sido revocado.

5. **Consideraciones Generales y Recomendaciones**
   - Con una configuración actualizada que incluye TLS 1.3 y HSTS, Cimaco mantiene un entorno seguro y confiable para los usuarios de su plataforma de e-commerce. Sin embargo, es recomendable realizar auditorías periódicas de seguridad y actualizar el certificado antes de su caducidad para mantener el nivel de protección.
   - La calificación A+ y la implementación de estas prácticas de seguridad indican que Cimaco ha adoptado un enfoque proactivo y adecuado en términos de protección de datos y privacidad de los usuarios.

##### Conclusión
El sitio de Cimaco demuestra una implementación de seguridad de alto nivel, protegiendo los datos de sus usuarios con prácticas avanzadas como **TLS 1.3, HSTS**, y un certificado **RSA 2048 bits**. Estas configuraciones reducen significativamente el riesgo de ciberataques, lo que proporciona a los usuarios una experiencia de compra segura y confiable en su plataforma.

### 3. **Coppel**

Coppel se presenta como una opción atractiva para los consumidores, ofreciendo un servicio al cliente accesible y una amplia variedad de productos. A continuación, se detallan los aspectos más relevantes del análisis:

**Servicio al Cliente**: **4** - La atención al cliente en Coppel es generalmente buena, permitiendo a los clientes realizar compras a través de WhatsApp con un asesor. Sin embargo, la disponibilidad de este asesor no es las 24 horas, lo que puede ser una limitación para aquellos que desean realizar compras fuera del horario estipulado. Aunque el horario de atención de 8 a.m. a 11 p.m. es razonable para compras convencionales, los usuarios a menudo experimentan tiempos de respuesta más lentos en comparación con otras empresas que lideran en esta categoría. Esta lentitud puede resultar frustrante para los clientes que buscan respuestas rápidas o asistencia inmediata, lo que sugiere que hay margen para optimizar este aspecto del servicio.

**Cumplimiento/Fiabilidad**: **5** - Coppel ha establecido una sólida reputación por su entrega puntual y confiable. En la mayoría de los casos, cumple con los tiempos de entrega prometidos, lo que genera confianza entre los consumidores y fomenta la lealtad a la marca. Este aspecto es fundamental en el comercio electrónico, donde la puntualidad y la confiabilidad son claves para la satisfacción del cliente.

**Facilidad de Uso**: **4** - La plataforma de Coppel es fácil de usar, con una interfaz intuitiva que facilita la navegación y la búsqueda de productos. A pesar de esta facilidad, algunos elementos del diseño podrían beneficiarse de una actualización para mejorar la experiencia del usuario. Pequeñas mejoras en la interfaz podrían hacer que la experiencia de compra sea aún más fluida, ayudando a los clientes a encontrar rápidamente lo que necesitan.

**Portafolio de Productos/Servicios**: **5** - Coppel ofrece una de las mayores variedades de productos entre las plataformas evaluadas, abarcando desde artículos para el hogar hasta dispositivos electrónicos. Esta amplia gama de productos no solo satisface diversas necesidades de los consumidores, sino que también posiciona a Coppel como una opción competitiva en el mercado.

**Seguridad y Privacidad**: **5** - La plataforma de Coppel sigue buenas prácticas de seguridad, utilizando HTTPS y un certificado SSL válido, lo que asegura que la información personal y financiera de los usuarios esté protegida. Este enfoque en la seguridad es esencial para generar confianza y tranquilidad entre los consumidores, un aspecto especialmente crítico en el ámbito del comercio electrónico.

#### Análisis de Seguridad Informática

Coppel muestra un excelente nivel de seguridad informática, obteniendo una calificación **A+** en su configuración SSL, lo cual indica que utiliza medidas avanzadas de protección en su sitio web para resguardar la información y garantizar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de Coppel:

1. **Certificado SSL y Soporte de Protocolos**
   - Coppel emplea **dos certificados SSL** para su dominio principal, uno con **EC 256 bits (SHA256withRSA)** y otro con **RSA 2048 bits (SHA256withRSA)**, ambos certificados confiables que proporcionan un alto nivel de seguridad. El uso de EC (Elliptic Curve) para cifrado es especialmente positivo, ya que, a pesar de ser más corto en longitud de bits, ofrece un nivel de seguridad comparativamente alto y es más eficiente en términos de velocidad y rendimiento.
   - El soporte de **TLS 1.3**, el estándar más actualizado en seguridad de transporte, garantiza una protección adicional. TLS 1.3 mejora la seguridad y reduce la latencia de la conexión, eliminando características obsoletas o vulnerables de versiones anteriores de TLS.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - Coppel ha implementado **HTTP Strict Transport Security (HSTS)** con una duración prolongada, lo cual obliga a los navegadores a establecer conexiones seguras (HTTPS) y elimina la posibilidad de que se realicen conexiones inseguras mediante HTTP. Esta medida previene ataques de intermediario (MITM) y asegura que los usuarios estén siempre protegidos con una conexión encriptada.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** muestra una calificación excelente, indicando que el sitio utiliza algoritmos de intercambio de claves robustos y seguros, lo que minimiza el riesgo de interceptación de sesiones y protege la confidencialidad de la información intercambiada entre el servidor y el usuario.
   - La **fortaleza del cifrado** también es alta, proporcionando una capa adicional de seguridad contra intentos de descifrado no autorizados y protegiendo la integridad de los datos.

4. **Buenas Prácticas en Seguridad de Certificados**
   - Los certificados de Coppel están firmados por **DigiCert TLS RSA SHA256 2020 CA1**, una autoridad de certificación de confianza, y ambos certificados están configurados para OCSP (Online Certificate Status Protocol). Esto significa que se puede verificar en tiempo real el estado del certificado, asegurando que no haya sido revocado.
   - La transparencia en certificados también está habilitada, lo que permite que los usuarios y navegadores verifiquen públicamente la legitimidad de los certificados. Esta práctica reduce el riesgo de suplantación de identidad mediante certificados falsificados.

5. **Dominios y Subdominios Alternativos**
   - Los certificados cubren una amplia variedad de **dominios y subdominios** utilizados por Coppel, incluyendo servicios internos y externos como plataformas de staging, subdominios de ecommerce, servicios de clientes, entre otros. Esto asegura que todas las partes de la plataforma estén protegidas bajo los mismos estándares de seguridad, minimizando el riesgo de brechas en subdominios secundarios.

6. **Consideraciones Generales y Recomendaciones**
   - Con una configuración de seguridad tan robusta y una calificación A+, Coppel ha demostrado una inversión significativa en la protección de su plataforma. Es importante que realicen revisiones periódicas para asegurarse de que todos los certificados estén actualizados y no se acerquen a su fecha de expiración sin ser renovados.
   - También se recomienda realizar auditorías continuas para verificar que las configuraciones de TLS y HSTS sigan vigentes y se adapten a los últimos estándares de seguridad.

##### Conclusión
Coppel cuenta con una infraestructura de seguridad de alta calidad en su sitio web, con medidas avanzadas como el uso de **TLS 1.3**, **certificados SSL EC y RSA de 256 y 2048 bits**, y **HSTS**. Estas configuraciones aseguran una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de los datos. Con una calificación A+ en seguridad, Coppel demuestra su compromiso con la seguridad y la confianza de sus clientes.
### 4. **Del Sol y Woolworth**

Del Sol y Woolworth ofrece una opción para realizar compras a través de WhatsApp, utilizando un chatbot que conecta a los clientes con un asesor. Sin embargo, la experiencia de atención al cliente presenta varios desafíos que deben ser abordados. A continuación, se detallan los aspectos más relevantes del análisis:

**Servicio al Cliente**: **3** - Aunque el personal de Del Sol y Woolworth está dispuesto a ayudar y a resolver dudas, la atención al cliente podría mejorarse notablemente en términos de rapidez y eficacia. Al utilizar el chatbot de WhatsApp, los usuarios son guiados a través de un menú, lo que hace el proceso menos intuitivo y más torpe. En nuestras pruebas, el chatbot sugirió un tiempo de espera de cinco minutos para ser atendidos por un asesor. Sin embargo, la realidad fue muy diferente; tuvimos que esperar **45 minutos** para recibir atención, un lapso que excede las expectativas y la promesa inicial del servicio. Además, casi **dos horas** transcurrieron antes de que recibimos una cotización para un producto, lo que definitivamente subraya la necesidad de una revisión y mejora en la eficiencia del servicio al cliente.

**Cumplimiento/Fiabilidad**: **4** - A pesar de los problemas en la atención al cliente, la plataforma de Del Sol y Woolworth cumple de manera confiable con sus tiempos de entrega. Los pedidos son procesados y enviados según lo prometido, aunque hay un claro margen de mejora en cuanto a la velocidad de respuesta, que es crucial para mejorar la satisfacción del cliente en general.

**Facilidad de Uso**: **3** - La plataforma sigue buenas prácticas en diseño de interfaz de usuario (UI) y experiencia de usuario (UX), con una estructura relativamente fácil de navegar. Sin embargo, la experiencia de compra a través de WhatsApp podría optimizarse considerablemente. El proceso actual, que incluye largos tiempos de espera y la interacción con un chatbot poco útil, hace que la experiencia del usuario sea frustrante, especialmente para aquellos que buscan una respuesta rápida o desean realizar una compra directamente.

**Portafolio de Productos/Servicios**: **4** - Del Sol y Woolworth tiene una variedad adecuada de productos, aunque hay limitaciones en algunas categorías específicas. Esta gama variada es positiva, pero es importante que los inventarios en línea se mantengan actualizados y reflejen con exactitud lo que está disponible en la tienda física. Las discrepancias entre el inventario en el sitio web y el disponible en la tienda pueden provocar confusión y desconfianza entre los clientes, afectando negativamente su experiencia de compra.

**Seguridad y Privacidad**: **4** - La plataforma cumple con los estándares básicos de seguridad y privacidad, protegiendo la información del cliente. Sin embargo, se han identificado vulnerabilidades menores en el código fuente que deberían ser abordadas para garantizar una mejor seguridad y proteger la información sensible de los usuarios.

#### Análisis de Seguridad Informática para Del Sol y Woolworth

Del Sol y Woolworth muestra un excelente nivel de seguridad informática, obteniendo una calificación **A+** en su configuración SSL. Esto sugiere que utiliza medidas avanzadas para proteger la información y asegurar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de Del Sol:

1. **Certificado SSL y Soporte de Protocolos**
   - Del Sol y Woolworth emplea un **certificado SSL RSA de 2048 bits (SHA256withRSA)**, lo que proporciona un alto nivel de seguridad en la encriptación de datos. Esta longitud de clave es reconocida como seguro y adecuada para la mayoría de las aplicaciones web.
   - El soporte de **TLS 1.3** asegura que el sitio utilice el estándar más actualizado en seguridad de transporte, lo que mejora la protección y reduce la latencia de conexión al eliminar vulnerabilidades de versiones anteriores.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - Del Sol y Woolworth ha implementado **HTTP Strict Transport Security (HSTS)** con una duración prolongada, lo que obliga a los navegadores a establecer conexiones seguras (HTTPS) y previene que se realicen conexiones inseguras. Esta medida contribuye significativamente a la protección contra ataques de intermediario (MITM).

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** es positiva, indicando que el sitio utiliza algoritmos de intercambio de claves seguros y robustos, minimizando el riesgo de interceptación de sesiones y protegiendo la confidencialidad de la información.
   - La **fortaleza del cifrado** también se califica como alta, ofreciendo una protección adicional contra intentos de descifrado no autorizados y garantizando la integridad de los datos enviados.

4. **Buenas Prácticas en Seguridad de Certificados**
   - El certificado de Del Sol y Woolworth está firmado por una autoridad de certificación de confianza, lo que asegura su validez. Además, está configurado para utilizar OCSP (Online Certificate Status Protocol), permitiendo la verificación en tiempo real del estado del certificado.
   - La transparencia en certificados está habilitada, permitiendo a los usuarios y navegadores verificar la legitimidad de los certificados, lo que reduce el riesgo de suplantación de identidad mediante certificados falsificados.

5. **Dominios y Subdominios Alternativos**
   - El certificado cubre una variedad de **dominios y subdominios**, asegurando que todas las plataformas asociadas a Del Sol y Woolworth estén protegidas bajo los mismos estándares de seguridad, minimizando el riesgo de brechas.

6. **Consideraciones Generales y Recomendaciones**
   - Con una calificación A+ y configuraciones de seguridad robustas, Del Sol y Woolworth debe realizar revisiones periódicas para asegurar que todos los certificados se renueven oportunamente y no se acerquen a su fecha de expiración sin ser renovados.
   - Se recomienda llevar a cabo auditorías continuas para verificar que las configuraciones de TLS y HSTS se mantengan actualizadas y alineadas con los últimos estándares de seguridad.

##### Conclusión
Del Sol y Woolworth cuenta con una infraestructura de seguridad de alta calidad en su sitio web, con medidas avanzadas como el uso de **TLS 1.3** y **certificados SSL RSA de 2048 bits**. Estas configuraciones aseguran una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de los datos. Con una calificación A+ en seguridad, Del Sol demuestra su compromiso con la protección de la información de sus clientes.

### 5. **El Nuevo Mundo**

El Nuevo Mundo presenta diversas limitaciones en su modelo de negocio, especialmente en lo que respecta a su experiencia al cliente y a la funcionalidad de su plataforma. A continuación, se detallan los aspectos más importantes del análisis:

**Servicio al Cliente**: **2** - El servicio al cliente de El Nuevo Mundo es bastante limitado. Aunque existen opciones de contacto, estas resultan ser insuficientes y poco amigables para el consumidor. Los usuarios solo pueden acceder a puntos de contacto básicos, como números de teléfono o correos electrónicos, sin opciones de soporte más interactivas o accesibles. Esto puede dar la impresión de que la empresa no está comprometida con ofrecer una atención al cliente proactiva y accesible, lo que podría disuadir a los consumidores de buscar asistencia o hacer consultas.

**Cumplimiento/Fiabilidad**: **NA** - La calificación de cumplimiento y fiabilidad no aplica, dado que El Nuevo Mundo no cuenta con un sistema de E-commerce que permita a los clientes realizar compras en línea ni gestionar envíos o recolecciones. Esta ausencia limita severamente la capacidad de la empresa para competir en un mercado donde las compras en línea son cada vez más prevalentes.

**Facilidad de Uso**: **NA** - La falta de un sistema de E-commerce hace que esta categoría no sea aplicable. La experiencia de usuario se ve comprometida al no poder realizar compras directamente a través de la plataforma, aunque visualmente sugiere lo contrario, lo que podría llevar a los clientes a frustrarse y buscar alternativas más convenientes.

**Portafolio de Productos/Servicios**: **2** - La variedad de productos y servicios ofrecidos por El Nuevo Mundo es limitada, y esto se debe en gran medida a la falta de funcionalidad de E-commerce. Sin la capacidad de comprar en línea, los clientes tienen acceso restringido a lo que pueden adquirir, lo que afecta la percepción global de la marca y su competitividad en el mercado.

**Seguridad y Privacidad**: **5** - A pesar de sus limitaciones en la atención al cliente y en el modelo de negocio, El Nuevo Mundo implementa buenas prácticas de seguridad al utilizar HTTPS y un certificado SSL válido. Esto es fundamental para proteger la información del cliente, y aunque actualmente no se estén realizando transacciones en línea, contar con una infraestructura que salvaguarde la privacidad es un paso positivo.

#### Análisis de Seguridad Informática

El Nuevo Mundo muestra un notable nivel de seguridad informática, obteniendo una calificación **A** en su configuración SSL, lo que indica que implementa medidas adecuadas para proteger la información y garantizar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de El Nuevo Mundo:

1. **Certificado SSL y Soporte de Protocolos**
   - El Nuevo Mundo emplea un **certificado SSL RSA de 4096 bits (SHA384withRSA)**, lo que proporciona un nivel de seguridad alto y robusto en la encriptación de datos. La longitud de la clave de 4096 bits mejora significativamente la seguridad frente a ataques de violación de clave.
   - Soporta **TLS 1.3**, el estándar más avanzado en seguridad de transporte, lo que garantiza una conexión segura y eficiente al eliminar vulnerabilidades de versiones anteriores, además de reducir la latencia.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - El Nuevo Mundo ha implementado **HTTP Strict Transport Security (HSTS)**, lo que obliga a los navegadores a establecer conexiones seguras (HTTPS) y reduce significativamente el riesgo de ataques de intermediario (MITM). Esta medida asegura que los usuarios siempre se conecten de manera encriptada.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** es positiva, indicando que el sitio utiliza algoritmos seguros y robustos para el intercambio de claves, minimizando el riesgo de interceptación de sesiones y protegiendo la confidencialidad de la información intercambiada.
   - La **fortaleza del cifrado** también es alta, brindando una capa adicional de protección contra intentos de descifrado no autorizados y asegurando la integridad de los datos.

4. **Buenas Prácticas en Seguridad de Certificados**
   - Los certificados de El Nuevo Mundo están firmados por **ZeroSSL RSA Domain Secure Site CA**, una autoridad de certificación confiable, asegurando su validez. Además, el uso de OCSP (Online Certificate Status Protocol) permite verificar el estado del certificado en tiempo real.
   - La transparencia de certificados está habilitada, lo que permite a los usuarios y navegadores confirmar la legitimidad de los certificados, reduciendo el riesgo de fraudes.

5. **Dominios y Subdominios Alternativos**
   - El certificado cubre una variedad de **dominios y subdominios**, protegiendo todos los aspectos de la plataforma bajo los mismos estándares de seguridad, lo que minimiza el riesgo de brechas en partes críticas del sistema.

6. **Consideraciones Generales y Recomendaciones**
   - Con una configuración de seguridad robusta y una calificación A, El Nuevo Mundo debe realizar revisiones periódicas para asegurarse de que todos los certificados sean renovados y mantenidos actualizados.
   - Se recomienda realizar auditorías continuas para asegurar que las configuraciones de TLS y HSTS se mantengan vigentes y alineadas con los últimos estándares de seguridad.

##### Conclusión
El Nuevo Mundo cuenta con una infraestructura de seguridad de alta calidad en su sitio web, con medidas avanzadas como el uso de **TLS 1.3** y **certificados SSL RSA de 4096 bits**. Estas configuraciones garantizan una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de los datos. Con una calificación A en seguridad, El Nuevo Mundo demuestra su compromiso con la protección de la información de sus clientes.

### 6. **El Palacio de Hierro**

El Palacio de Hierro es una marca reconocida que ofrece múltiples servicios a sus clientes, aunque existen áreas en las que podría mejorar. A continuación, se analizan los aspectos más importantes de su experiencia de compra y atención al cliente:

**Servicio al Cliente**: **3** - La atención al cliente del Palacio de Hierro tiene el potencial de ser más efectiva. Aunque la opción de realizar compras a través de WhatsApp está disponible mediante un chatbot que conecta a los clientes con un asesor, el proceso se siente torpe debido a la naturaleza basada en menús del chatbot. Esta estructura puede ser frustrante para los usuarios, ya que la navegación por el menú para acceder a la asistencia deseada no es tan fluida como se podría esperar. Además, el servicio no siempre es rápido; puede tomar más de tres minutos simplemente para conectar con un asesor, lo que puede ser una desventaja en situaciones que requieren respuestas inmediatas. La necesidad de utilizar la aplicación para ciertos procesos añade otra capa de complejidad al servicio, limitando la experiencia del cliente.

**Cumplimiento/Fiabilidad**: **4** - En términos de cumplimiento y fiabilidad, El Palacio de Hierro generalmente se desempeña bien en la entrega de sus productos. Sus envíos son generalmente confiables, pero los tiempos de entrega son promedios. Mejorar la rapidez de los envíos podría contribuir significativamente a una experiencia de compra más positiva para los clientes que esperan recibir sus productos de manera oportuna.

**Facilidad de Uso**: **4** - El diseño de la interfaz es visualmente atractivo y cuenta con buenas prácticas de UI/UX, lo que permite a los usuarios navegar por el sitio de manera relativamente sencilla. Sin embargo, como se mencionó anteriormente, la experiencia de compra por WhatsApp podría ser optimizada. La lentitud en los menús del chatbot puede reducir la satisfacción general del cliente, especialmente en un entorno donde la inmediatez es clave.

**Portafolio de Productos/Servicios**: **5** - El Palacio de Hierro ofrece una amplia gama de productos, principalmente de alta gama, lo que le permite atraer a un público diverso. Su sólida selección de productos es un punto fuerte que refuerza su posición en el mercado y brinda a los clientes variedad a la hora de elegir.

**Seguridad y Privacidad**: **5** - La plataforma cuenta con buenas prácticas de seguridad, utilizando navegación HTTPS y un certificado SSL activo, lo que proporciona a los usuarios la confianza de que sus datos personales y de pago están protegidos. La seguridad es un aspecto crucial para las compras en línea, y El Palacio de Hierro ha cumplido con los estándares necesarios en este ámbito.

#### Análisis de Seguridad Informática

El Palacio de Hierro presenta un sólido nivel de seguridad informática, logrando una calificación **A+** en su configuración SSL. Esto indica que emplea medidas avanzadas para proteger la información y proporcionar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de El Palacio de Hierro:

1. **Certificado SSL y Soporte de Protocolos**
   - El Palacio de Hierro utiliza un **certificado SSL RSA de 2048 bits (SHA256withRSA)**, lo que garantiza un alto grado de seguridad en la transmisión de datos. La clave RSA de 2048 bits es un estándar aceptado para la seguridad de los datos en línea.
   - Soporta **TLS 1.3**, el protocolo más actualizado en materia de seguridad, que proporciona una protección adicional y mejora la eficiencia de las conexiones eliminando las vulnerabilidades de versiones anteriores.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - La implementación de **HSTS** con una duración prolongada obliga a los navegadores a utilizar conexiones seguras (HTTPS), reduciendo el riesgo de ataques de intermediario (MITM) y asegurando que los usuarios siempre se conecten a través de un canal encriptado.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** evidenció que se utilizan algoritmos robustos, minimizando el riesgo de interceptación y protegiendo la confidencialidad de la información intercambiada entre el servidor y el usuario.
   - La **fortaleza del cifrado** es alta, lo que brinda una protección sólida contra intentos de descifrado no autorizados.

4. **Buenas Prácticas en Seguridad de Certificados**
   - El certificado de El Palacio de Hierro está firmado por una autoridad de certificación confiable, garantizando la validez y autenticidad del mismo. Además, el certificado está configurado para usar OCSP (Online Certificate Status Protocol) para verificar su estado en tiempo real.
   - La transparencia de certificados está habilitada, permitiendo a los usuarios verificar públicamente su legitimidad, lo que reduce el riesgo de fraude.

5. **Dominios y Subdominios Alternativos**
   - El certificado cubre una variedad de **dominios y subdominios**, asegurando que todas las plataformas, internas y externas, estén protegidas bajo los mismos estándares de seguridad, minimizando el riesgo de brechas.

6. **Consideraciones Generales y Recomendaciones**
   - Con una calificación A+ y configuraciones de seguridad robustas, El Palacio de Hierro debe realizar revisiones periódicas para asegurar que todos los certificados se renueven antes de su fecha de expiración.
   - Se recomienda también llevar a cabo auditorías continuas para garantizar que las configuraciones de TLS y HSTS se mantengan actualizadas y adaptadas a los últimos estándares.

##### Conclusión
El Palacio de Hierro cuenta con una infraestructura de seguridad efectiva en su sitio web, con el uso de **TLS 1.3**, **certificados SSL RSA de 2048 bits**, y **HSTS**. Estas configuraciones garantizan una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de sus datos. Con una calificación A+ en seguridad, El Palacio de Hierro demuestra un fuerte compromiso con la protección de la información de sus clientes.

### 7. **Hemsa**

**Servicio al Cliente**: **0** - La atención al cliente es inexistente o muy deficiente. Los usuarios no encuentran opciones de contacto o asistencia, lo que limita su capacidad para resolver dudas o problemas.

**Cumplimiento/Fiabilidad**: **NA** - No aplica, ya que la tienda no cuenta con un sistema de E-commerce que permita la realización de transacciones en línea, lo que genera frustración en los posibles clientes.

**Facilidad de Uso**: **NA** - No aplica. La falta de un sistema funcional de E-commerce impide evaluar la usabilidad del sitio.

**Portafolio de Productos/Servicios**: **0** - Hemsa no ofrece ninguna opción para comprar productos a través de su sitio web. La ausencia de un catálogo actualizado refleja que la tienda no está alineada con las expectativas actuales del mercado. Además, el sitio web parece estar desactualizado y descuidado, mostrando un diseño anticuado y falta de contenido relevante. Esta situación sugiere que la empresa no está comprometida con brindar a sus clientes una experiencia de compra moderna y satisfactoria. La falta de productos disponibles no solo limita su funcionalidad, sino que también transmite la impresión de que la tienda está abandonada y genera desconfianza en los usuarios.

**Seguridad y Privacidad**: **1** - El certificado SSL está caducado, lo que representa un riesgo significativo en cuanto a la seguridad de los datos de los usuarios. La ausencia de un entorno seguro para la navegación no solo vulnera la privacidad de los posibles clientes, sino que también afecta la reputación de la marca. La falta de medidas adecuadas en términos de seguridad puede hacer que los usuarios desconfíen de realizar cualquier tipo de interacción con el sitio, incluidos registros, consultas o futuras transacciones.

#### Análisis de Seguridad Informática

Hemsa presenta un nivel de seguridad informática preocupante, con una calificación **T** en su configuración SSL, lo que indica que existen fallas significativas en sus medidas de protección. A continuación, se detallan los aspectos más relevantes de la seguridad de Hemsa:

1. **Certificado SSL y Soporte de Protocolos**
   - Hemsa utiliza **certificados SSL RSA de 2048 bits (SHA256withRSA)**, lo cual en teoría proporciona un nivel aceptable de seguridad. Sin embargo, datos adicionales indican que hay problemas de implementación que podrían comprometer la efectividad de estos certificados.
   - El soporte incluye protocolos antiguos como **TLS 1.0 y 1.1**, los cuales son obsoletos y vulnerables. La falta de soporte exclusivo para versiones más seguras (TLS 1.2 y 1.3) aumenta el riesgo de ataques.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - La implementación de **HSTS** no se ha verificado adecuadamente en el sitio, lo que significa que podría haber conexiones inseguras a través de HTTP. Esto expone a los usuarios a ataques de intermediario (MITM) y reduce la eficacia de la encriptación.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** es deficiente, indicando que el sitio puede no estar utilizando algoritmos seguros para la protección de sesiones, lo que aumenta el riesgo de interceptación.
   - La **fortaleza del cifrado** es cuestionable, lo que significa que la protección contra intentos de descifrado no autorizados puede no ser suficiente.

4. **Buenas Prácticas en Seguridad de Certificados**
   - No se especifica claramente la autoridad de certificación que firma los certificados de Hemsa, lo que puede generar desconfianza en su validez.
   - La falta de configuración para OCSP (Online Certificate Status Protocol) significa que no hay verificación en tiempo real del estado del certificado, aumentando el riesgo de usar certificados revocados.

5. **Dominios y Subdominios Alternativos**
   - La cobertura de **dominios y subdominios** parece estar limitada, lo que puede generar brechas en la seguridad si no todos los aspectos de la infraestructura están protegidos adecuadamente.

6. **Consideraciones Generales y Recomendaciones**
   - Con una calificación de T, Hemsa debe abordar de inmediato sus problemas de seguridad. Es fundamental realizar una auditoría exhaustiva para identificar y corregir las vulnerabilidades presentes en sus configuraciones SSL/TLS.
   - Se recomienda deshabilitar los protocolos obsoletos y asegurar el uso de versiones seguras (TLS 1.2 y 1.3) únicamente. La implementación de HSTS debe ser prioritaria para proteger las conexiones de los usuarios.

##### Conclusión
Hemsa cuenta con una infraestructura de seguridad comprometida en su sitio web, con configuraciones que no cumplen con los estándares necesarios para garantizar una experiencia de navegación segura. La calificación T refleja la urgencia de implementar medidas correctivas. Es imprescindible que Hemsa mejore sus prácticas de seguridad y gestione adecuadamente sus certificados para proteger la privacidad y seguridad de los datos de sus usuarios.

### 8. **La Marina**

**Servicio al Cliente**: **5** - Aunque La Marina ofrece un servicio al cliente accesible a través de WhatsApp, el sistema de atención se basa en un chatbot que funciona mediante un menú. Este enfoque puede resultar tedioso y lento de usar, ya que los usuarios deben navegar a través de múltiples opciones antes de llegar a sus respuestas deseadas. Si bien las respuestas pueden ser rápidas, la rigidez del sistema limita la interacción fluida que muchos clientes preferirían. Además, es importante mencionar que, a pesar de tener un canal de comunicación activo, la posibilidad de realizar compras a través del chatbot no está disponible, lo que resta funcionalidad al servicio. Esto puede ser un inconveniente significativo para los clientes que buscan una experiencia más integrada y directa.

**Cumplimiento/Fiabilidad**: **4** - La Marina generalmente cumple con los tiempos de entrega prometidos, lo cual es un aspecto positivo. Sin embargo, hay margen para la optimización en ciertos aspectos de la logística, lo que podría mejorar aún más su fiabilidad y satisfacción del cliente.

**Facilidad de Uso**: **4** - El diseño de la plataforma es intuitivo y fácil de usar, lo que facilita la navegación para los usuarios. No obstante, se pueden hacer mejoras para que la experiencia de los clientes sea comparable a la de los líderes de la industria. La implementación de un sistema de servicio al cliente más dinámico y menos reliantemente on el menú del chatbot podría ser una de esas mejoras.

**Portafolio de Productos/Servicios**: **4** - La Marina ofrece una amplia variedad de productos, lo que es un punto fuerte. Sin embargo, la experiencia de compra podría verse enriquecida si se incorporaran más opciones para interactuar directamente con las ventas, como la posibilidad de realizar compras a través de WhatsApp.

**Seguridad y Privacidad**: **5** - La Marina demuestra buenas prácticas en términos de seguridad y privacidad, lo que es fundamental para generar confianza entre los usuarios. La seguridad en las transacciones y la protección de datos son aspectos bien implementados en su plataforma.

#### Análisis de Seguridad Informática

La Marina muestra un alto nivel de seguridad informática, obteniendo una calificación **A** en su configuración SSL. Esto indica que utiliza medidas adecuadas para proteger la información y garantizar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de La Marina:

1. **Certificado SSL y Soporte de Protocolos**
   - La Marina emplea un **certificado SSL RSA de 2048 bits (SHA256withRSA)**, lo que proporciona un nivel confiable de seguridad en la encriptación de datos. Esta longitud de clave es estándar y acepta la mayoría de las aplicaciones web.
   - El soporte de **TLS 1.3** y **TLS 1.2** asegura que el sitio esté alineado con los estándares modernos de seguridad, protegiendo las conexiones y eliminando características vulnerables de versiones anteriores del protocolo.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - La Marina ha implementado **HTTP Strict Transport Security (HSTS)**, lo que obliga a los navegadores a establecer siempre conexiones seguras (HTTPS). Esto reduce significativamente el riesgo de ataques de intermediario (MITM) y garantiza que los usuarios naveguen de manera encriptada.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** es positiva, indicando que el sitio utiliza algoritmos robustos para el intercambio de claves, lo que minimiza el riesgo de interceptación y asegura la confidencialidad de la información entre el servidor y el usuario.
   - La **fortaleza del cifrado** es alta, proporcionando una capa adicional de protección contra intentos de descifrado no autorizados y asegurando la integridad de los datos.

4. **Buenas Prácticas en Seguridad de Certificados**
   - Los certificados de La Marina están firmados por una autoridad de certificación confiable, lo que garantiza su validez. Sin embargo, sería beneficioso revisar la configuración para garantizar que esté habilitado el uso de OCSP (Online Certificate Status Protocol).
   - La transparencia de certificados también debería ser habilitada, permitiendo a los usuarios verificar la legitimidad de los certificados y reducir el riesgo de fraudes.

5. **Dominios y Subdominios Alternativos**
   - Los certificados cubren una variedad de **dominios y subdominios**, asegurando que todas las plataformas asociadas a La Marina estén protegidas bajo los mismos estándares de seguridad, lo que minimiza el riesgo de brechas en la infraestructura.

6. **Consideraciones Generales y Recomendaciones**
   - Con una calificación de A y una configuración de seguridad efectiva, La Marina debería continuar realizando revisiones periódicas para asegurarse de que todos los certificados sean renovados a tiempo y que estén actualizados.
   - Es recomendable implementar auditorías continuas para verificar que las configuraciones de TLS y HSTS se mantengan alineadas con los estándares de seguridad más recientes.

##### Conclusión
La Marina cuenta con una infraestructura de seguridad bien configurada en su sitio web, utilizando **TLS 1.2 y 1.3**, y **certificados SSL RSA de 2048 bits**. Estas configuraciones garantizan una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de los datos. Con una calificación A en seguridad, La Marina demuestra su compromiso con la protección de la información de sus clientes.

### 9. **Liverpool**

**Servicio al Cliente**: **5** - Liverpool ofrece un excelente servicio al cliente, con soporte disponible las 24 horas del día, los 7 días de la semana, y múltiples canales de atención. Sin embargo, aunque el acceso a servicio al cliente a través de WhatsApp es fácil, el proceso para realizar compras en línea puede resultar confuso y frustrante. Inicialmente, los usuarios deben interactuar con un chatbot que opera mediante un menú, lo que puede resultar tedioso. Tras navegar por las opciones, se debe presionar un enlace específico en el chat para acceder a la compra online. 

El problema se agrava al tener que navegar nuevamente por otro chatbot diferente, con un menú distinto, antes de quedar a la espera de atención. En nuestras pruebas, este proceso se vio frustrado, ya que no obtuvimos respuesta alguna de los agentes de servicio al cliente. Esta experiencia puede llevar a los usuarios a sentirse desatendidos, afectando la percepción general del excelente servicio que Liverpool intenta ofrecer.

**Cumplimiento/Fiabilidad**: **5** - Liverpool se destaca por su alta fiabilidad, ofreciendo opciones de envío rápido y preciso. Los clientes pueden confiar en que recibirán sus pedidos de manera puntual, lo que contribuye a una experiencia de compra satisfactoria.

**Facilidad de Uso**: **5** - La interfaz de usuario (UI) y la experiencia de usuario (UX) son excelentes, con un carrito de compras intuitivo que permite a los usuarios modificar sus selecciones sin complicaciones. No obstante, a pesar de la buena estructura del sitio, la dificultad de uso se manifiesta en el complejo proceso de atención al cliente a través de WhatsApp.

**Portafolio de Productos/Servicios**: **5** - Liverpool ofrece una de las mayores gamas de productos en el mercado, lo que le permite atender diversas necesidades de los consumidores. Sin embargo, la navegación por su sistema de atención podría mejorar para garantizar una experiencia más fluida y satisfactoria en la compra.

**Seguridad y Privacidad**: **5** - La plataforma de Liverpool cumple con altos estándares de seguridad y privacidad, proporcionando a los usuarios una experiencia de compra segura. Esto es crucial para fomentar la confianza del cliente, aunque el servicio de atención al cliente debería ser igual de confiable y accesible.

#### Análisis de Seguridad Informática

Liverpool presenta un buen nivel de seguridad informática, obteniendo una calificación **A** en su configuración SSL, lo que indica que implementa medidas adecuadas para proteger la información y garantizar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de Liverpool:

1. **Certificado SSL y Soporte de Protocolos**
   - Liverpool emplea un **certificado SSL RSA de 2048 bits (SHA256withRSA)**, que proporciona un nivel confiable de seguridad en la encriptación de datos. Esta longitud de clave es aceptada como segura para la mayoría de las aplicaciones web.
   - El soporte de **TLS 1.2** y **TLS 1.3** asegura que el sitio utilice protocolos modernos para la transmisión de datos, lo que mejora la seguridad y eficiencia de las conexiones.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - Liverpool ha implementado **HTTP Strict Transport Security (HSTS)**, lo que obliga a los navegadores a establecer siempre conexiones seguras (HTTPS). Esta medida reduce significativamente el riesgo de ataques de intermediario (MITM) y asegura que los usuarios naveguen de manera encriptada.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** es positiva, indicando que el sitio utiliza algoritmos seguros y robustos, lo que minimiza el riesgo de interceptación de sesiones y protege la confidencialidad de la información intercambiada.
   - La **fortaleza del cifrado** es alta, proporcionando una capa adicional de seguridad contra intentos de descifrado no autorizados y asegurando la integridad de los datos.

4. **Buenas Prácticas en Seguridad de Certificados**
   - Los certificados de Liverpool están firmados por una autoridad de certificación confiable, lo que garantiza la validez de los mismos. Sin embargo, sería recomendable revisar la configuración para asegurar que el uso de OCSP (Online Certificate Status Protocol) esté habilitado para la verificación en tiempo real del estado del certificado.
   - La transparencia en certificados debería estar habilitada, permitiendo a los usuarios verificar públicamente la legitimidad de los certificados, lo que reduce el riesgo de fraude.

5. **Dominios y Subdominios Alternativos**
   - Los certificados abarcan una variedad de **dominios y subdominios**, lo que asegura que todas las plataformas asociadas a Liverpool estén bajo los mismos estándares de seguridad, minimizando el riesgo de brechas en la infraestructura.

6. **Consideraciones Generales y Recomendaciones**
   - Con una calificación de A y configuraciones efectivas de seguridad, Liverpool debe realizar revisiones periódicas para asegurarse de que todos los certificados sean renovados a tiempo y se mantengan actualizados.
   - Se recomienda realizar auditorías continuas para verificar que las configuraciones de TLS y HSTS se mantengan alineadas con los estándares más recientes de seguridad.

##### Conclusión
Liverpool cuenta con una infraestructura de seguridad bien configurada en su sitio web, con el uso de **certificados SSL RSA de 2048 bits** y soporte para **TLS 1.2 y 1.3**. Estas configuraciones garantizan una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de los datos. Con una calificación A en seguridad, Liverpool demuestra su compromiso con la protección de la información de sus clientes.

### 10. **Sanborns**

**Servicio al Cliente**: **4** - Sanborns ofrece un buen servicio al cliente, pero se enfrenta a ciertos retos. Aunque existe la opción de realizar compras a través de WhatsApp utilizando un chatbot, este sistema funcionado con un menú puede resultar engorroso. Muchas veces, el proceso para obtener asistencia o realizar una compra se torna tedioso, ya que el chatbot tiende a recomendar que los usuarios busquen información adicional en el sitio web o que hablen con un asesor. Esto puede causar demoras innecesarias en una experiencia que debería ser más fluida, lo que puede frustrar a los clientes que buscan respuestas rápidas.

**Cumplimiento/Fiabilidad**: **3** - Aunque Sanborns permite la recogida en tienda en un plazo de 2 horas, el servicio de envío es menos eficiente, ya que depende de una tercera parte. La tercerización con Estafeta puede resultar en tiempos de entrega prolongados, lo que afecta la confiabilidad del servicio y la satisfacción del cliente, especialmente para quienes buscan rapidez en sus compras.

**Facilidad de Uso**: **4** - La interfaz del sitio web es bastante fácil de usar, lo que facilita la navegación y la búsqueda de productos. Sin embargo, el flujo del carrito de compras presenta oportunidades de mejora. Algunos usuarios podrían encontrar confuso el proceso de finalizar la compra tras interactuar con el chatbot, lo que podría alargar el tiempo necesario para completar una transacción.

**Portafolio de Productos/Servicios**: **4** - Sanborns cuenta con una variedad adecuada de productos, lo que atrae a diferentes tipos de clientes. Sin embargo, es importante mencionar que los inventarios disponibles en el sitio web no siempre coinciden con los reales en la tienda. Esta discrepancia puede generar confusiones y decepciones al momento de buscar un producto específico, afectando la confianza del cliente en el servicio.

**Seguridad y Privacidad**: **5** - La plataforma de Sanborns cumple con buenas prácticas de seguridad y privacidad, lo que es fundamental para mantener la confianza del cliente. Un manejo adecuado de los datos personales y de pago es crucial en un entorno de comercio electrónico.

#### Análisis de Seguridad Informática para Sanborns

Sanborns demuestra un alto nivel de seguridad informática, obteniendo una calificación **A+** en su configuración SSL, lo que indica que implementa medidas avanzadas para proteger la información y garantizar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de Sanborns:

1. **Certificado SSL y Soporte de Protocolos**
   - Sanborns emplea **un certificado SSL RSA de 2048 bits (SHA256withRSA)**, proporcionando un nivel sólido de seguridad en la encriptación de datos. Esta longitud de clave es ampliamente aceptada y adecuada para asegurar las transacciones en línea.
   - El soporte de **TLS 1.3** y **TLS 1.2** asegura que el sitio utilice los protocolos más modernos para la transmisión de datos, mejorando significativamente la seguridad y eficiencia de las conexiones.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - Sanborns ha implementado **HTTP Strict Transport Security (HSTS)** con una duración prolongada, obligando a los navegadores a establecer siempre conexiones seguras (HTTPS). Esto previene ataques de intermediario (MITM) y garantiza que los usuarios naveguen de manera encriptada en todo momento.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** es excelente, indicando que el sitio utiliza algoritmos robustos para el intercambio, minimizando el riesgo de interceptación de sesiones y protegiendo la confidencialidad de la información.
   - La **fortaleza del cifrado** es alta, lo que proporciona una capa adicional de seguridad contra intentos de descifrado no autorizados y asegura la integridad de los datos.

4. **Buenas Prácticas en Seguridad de Certificados**
   - Los certificados de Sanborns están firmados por una autoridad de certificación de confianza, lo que garantiza su validez. Además, es recomendable que se use OCSP (Online Certificate Status Protocol) para permitir la verificación en tiempo real del estado de los certificados.
   - La transparencia de los certificados debería estar habilitada, permitiendo a los usuarios verificar la legitimidad de los mismos y reducir el riesgo de fraude.

5. **Dominios y Subdominios Alternativos**
   - Los certificados cubren una variedad de **dominios y subdominios**, asegurando que todas las plataformas asociadas a Sanborns estén protegidas bajo los mismos estándares de seguridad, lo que minimiza el riesgo de brechas en su infraestructura.

6. **Consideraciones Generales y Recomendaciones**
   - Con una calificación A+ y configuraciones de seguridad robustas, Sanborns debería realizar revisiones periódicas para asegurar que todos los certificados se renueven a tiempo y mantengan su vigencia.
   - También se recomienda llevar a cabo auditorías continuas para verificar que las configuraciones de TLS y HSTS se alineen con las mejores prácticas y estándares actuales de seguridad.

##### Conclusión
Sanborns cuenta con una infraestructura de seguridad de alta calidad en su sitio web, respaldada por el uso de **certificados SSL RSA de 2048 bits** y **protocolos TLS 1.2 y 1.3**. Estas configuraciones aseguran una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de los datos. Con una calificación A+ en seguridad, Sanborns demuestra su compromiso con la protección de la información de sus clientes.

### 11. **Sears**

Sears presenta un sistema de atención al cliente y e-commerce que es prácticamente idéntico al de Sanborns, lo que ofrece tanto ventajas como desventajas. A continuación, se detallan aspectos importantes relacionados con la seguridad y funcionalidad de Sears:

**Servicio al Cliente**: **4** - El servicio al cliente de Sears es aceptable, similar al de Sanborns. Si bien los clientes pueden esperar una atención razonable, existen áreas para mejorar. Por ejemplo, la interacción a menudo se ve afectada por demoras en las respuestas, especialmente cuando se utilizan sistemas automatizados como chatbots basados en menús, que pueden ser ineficaces en situaciones que requieren atención personalizada. Aunque hay múltiples canales de comunicación, la experiencia a menudo se siente menos dinámica de lo esperado.

**Cumplimiento/Fiabilidad**: **4** - Sears muestra una fiabilidad adecuada en sus servicios, cumpliendo con los tiempos de entrega prometidos y ofreciendo opciones de recogida en tienda. Sin embargo, como en el caso de Sanborns, aseguran que la tercerización de envíos puede afectar la rapidez del servicio, lo que sugiere que hay margen para optimizar su logística y cumplir con las expectativas de los clientes que desean un servicio más ágil.

**Facilidad de Uso**: **4** - La interfaz del sitio web de Sears es fácil de usar, con un diseño decente que permite a los usuarios navegar y encontrar productos sin complicaciones. Sin embargo, la experiencia de compra puede ser similar a la de Sanborns, con un flujo que puede resultar confuso en algunos momentos, especialmente al final del proceso de compra. Mejorar la claridad en las interacciones digitales podría aumentar la satisfacción del cliente.

**Portafolio de Productos/Servicios**: **4** - Sears ofrece una buena gama de productos en su catálogo, al igual que Sanborns. Esto incluye una variedad de categorías que atraen a diferentes tipos de consumidores. Sin embargo, los inventarios en línea deben estar mejor sincronizados con los disponibles en las tiendas físicas para evitar confusiones y frustraciones.

**Seguridad y Privacidad**: **5** - Sears aplica buenas prácticas de seguridad y privacidad, manteniendo los estándares necesarios para proteger la información de los clientes. Esto es vital en un entorno e-commerce, donde la confianza es fundamental. Los sistemas de seguridad son comparables a los de Sanborns, lo que refuerza aún más la confianza en sus operaciones.

### Análisis de Seguridad Informática para Sears

Sears muestra un buen nivel de seguridad informática, obteniendo una calificación **A** en su configuración SSL. Esto indica que ha implementado medidas adecuadas para proteger la información y garantizar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de Sears:

1. **Certificado SSL y Soporte de Protocolos**
   - Sears emplea un **certificado SSL RSA de 2048 bits (SHA256withRSA)**, lo que proporciona un nivel confiable de seguridad para la encriptación de datos. Esta longitud de clave es aceptada como segura para las transacciones en línea.
   - El soporte incluye **TLS 1.2** y **TLS 1.3**, asegurando que el sitio utilice protocolos modernos para la transmisión de datos, mejorando la seguridad y eficiencia de las conexiones.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - Sears ha implementado **HTTP Strict Transport Security (HSTS)**, lo que obliga a los navegadores a establecer siempre conexiones seguras (HTTPS). Esta estrategia reduce significativamente el riesgo de ataques de intermediario (MITM) y garantiza que los usuarios naveguen de manera encriptada.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** es positiva, indicando el uso de algoritmos robustos que minimizan el riesgo de interceptación de sesiones y protegen la confidencialidad de la información intercambiada entre el servidor y el usuario.
   - La **fortaleza del cifrado** es alta, ofreciendo una protección adicional contra intentos de descifrado no autorizados y asegurando la integridad de los datos.

4. **Buenas Prácticas en Seguridad de Certificados**
   - Los certificados de Sears están firmados por una autoridad de certificación confiable, lo que garantiza su validez. Sin embargo, sería beneficioso verificar si el uso de OCSP (Online Certificate Status Protocol) está habilitado para asegurar la verificación en tiempo real del estado del certificado.
   - La transparencia en certificados debería estar activada, permitiendo a los usuarios verificar la legitimidad de los mismos y reduciendo el riesgo de suplantación.

5. **Dominios y Subdominios Alternativos**
   - Los certificados cubren diversas plataformas y servicios asociados con Sears, lo que asegura que todas las partes de su infraestructura estén protegidas bajo los mismos estándares de seguridad, minimizando el riesgo de brechas.

6. **Consideraciones Generales y Recomendaciones**
   - Con una calificación de A y configuraciones de seguridad efectivas, Sears debe realizar revisiones periódicas para garantizar que todos los certificados se mantengan actualizados y se renueven a tiempo.
   - Se recomienda llevar a cabo auditorías continuas para verificar que las configuraciones de TLS y HSTS se alineen con las mejores prácticas y estándares actuales de seguridad.

##### Conclusión
Sears cuenta con una infraestructura de seguridad confiable en su sitio web, utilizando **certificados SSL RSA de 2048 bits** y soporte para **TLS 1.2 y 1.3**. Estas configuraciones aseguran una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de los datos. Con una calificación A en seguridad, Sears demuestra su compromiso con la protección de la información de sus clientes.

### 12. **Suburbia**

Suburbia presenta un servicio al cliente que, aunque es aceptable, muestra áreas significativas de mejora, particularmente en la interacción digital. A continuación, se detallan los aspectos más relevantes de la seguridad y funcionalidad de Suburbia:

**Servicio al Cliente**: **3** - Suburbia ofrece servicio al cliente a través de WhatsApp, apoyado por un chatbot que funciona con un sistema basado en menú. Aunque esta opción ofrece accesibilidad, la experiencia puede resultar tediosa y lenta para los usuarios. Navegar a través del menú de opciones puede ser laborioso, lo que complica la resolución de dudas o inquietudes de manera eficiente.

**Cumplimiento/Fiabilidad**: **5** - A pesar de las fallas en el servicio al cliente, Suburbia es altamente fiable en sus servicios de entrega. Los clientes pueden confiar en que recibirán sus pedidos dentro de los plazos establecidos, lo cual es un aspecto crucial para mantener la satisfacción del cliente.

**Facilidad de Uso**: **4** - La navegación en el sitio web de Suburbia es razonable y fácil, lo que permite a los usuarios encontrar productos sin complicaciones. Sin embargo, la experiencia se opaca un poco por la inelegancia del sistema de atención al cliente a través de WhatsApp, ya que el sistema actual no permite realizar compras a través de este canal, limitando la funcionalidad del servicio. La incapacidad de completar transacciones directamente en WhatsApp puede frustrar a los clientes que buscan una experiencia de compra rápida y directa, lo que indica que existe una oportunidad significativa para mejorar en la interacción y funcionalidad.

**Portafolio de Productos/Servicios**: **5** - Suburbia ofrece una amplia variedad de productos, lo que la convierte en una opción competitiva en el mercado. Esta diversidad permite atraer a diferentes segmentos de clientes, asegurando que haya algo para todos.

**Seguridad y Privacidad**: **5** - La plataforma de Suburbia aplica buenas prácticas de seguridad y privacidad, protegiendo la información de los usuarios y manteniendo altos estándares que son vitales en un entorno de comercio electrónico.

### Análisis de Seguridad Informática

Suburbia presenta un buen nivel de seguridad informática, alcanzando una calificación **A** en su configuración SSL. Esto indica que ha implementado medidas adecuadas para proteger la información y proporcionar una experiencia de navegación segura para sus usuarios. A continuación, se detallan los aspectos más relevantes de la seguridad de Suburbia:

1. **Certificado SSL y Soporte de Protocolos**
   - Suburbia utiliza un **certificado SSL RSA de 2048 bits (SHA256withRSA)**, lo que ofrece un nivel confiable de seguridad en la encriptación de datos. Esta longitud de clave es ampliamente aceptada como segura para la mayoría de las aplicaciones web.
   - El soporte para **TLS 1.2** y **TLS 1.3** asegura que el sitio utilice protocolos modernos y eficaces, mejorando tanto la seguridad como la eficiencia de las conexiones.

2. **Implementación de HTTP Strict Transport Security (HSTS)**
   - Suburbia ha implementado **HTTP Strict Transport Security (HSTS)**, que obliga a los navegadores a establecer conexiones seguras (HTTPS) en todo momento. Esta medida reduce significativamente el riesgo de ataques de intermediario (MITM) y asegura que los usuarios naveguen de forma encriptada.

3. **Intercambio de Claves y Fortaleza del Cifrado**
   - La evaluación del **intercambio de claves** es positiva, indicando que el sitio utiliza algoritmos robustos que minimizan el riesgo de interceptación de sesiones, protegiendo así la confidencialidad de la información intercambiada.
   - La **fortaleza del cifrado** es alta, ofreciendo una capa adicional de seguridad contra intentos de descifrado no autorizados y asegurando la integridad de los datos.

4. **Buenas Prácticas en Seguridad de Certificados**
   - Los certificados de Suburbia están firmados por una autoridad de certificación confiable, lo que garantiza su validez. Sin embargo, sería recomendable asegurarse de que el uso de OCSP (Online Certificate Status Protocol) esté habilitado para permitir la verificación en tiempo real del estado de los certificados.
   - La transparencia de certificados debería ser habilitada, permitiendo a los usuarios verificar la legitimidad de los certificados y reducir el riesgo de suplantación.

5. **Dominios y Subdominios Alternativos**
   - Los certificados cubren una variedad de **dominios y subdominios** utilizados por Suburbia, asegurando que todas las partes de la infraestructura estén protegidas bajo los mismos estándares de seguridad, minimizando el riesgo de brechas.

6. **Consideraciones Generales y Recomendaciones**
   - Con una calificación A y una configuración de seguridad efectiva, Suburbia debe realizar revisiones periódicas para asegurar que todos los certificados sean renovados a tiempo y se mantengan actualizados.
   - Se recomienda llevar a cabo auditorías continuas para verificar que las configuraciones de TLS y HSTS se mantengan alineadas con los estándares más recientes de seguridad.

##### Conclusión
Suburbia cuenta con una infraestructura de seguridad efectiva en su sitio web, utilizando **certificados SSL RSA de 2048 bits** y soporte para **TLS 1.2 y 1.3**. Estas configuraciones garantizan una experiencia de navegación segura y confiable para sus usuarios, protegiendo la privacidad y seguridad de los datos. Con una calificación A en seguridad, Suburbia demuestra su compromiso con la protección de la información de sus clientes.

### 13. **Tiendas Chapur**

Tiendas Chapur ofrece un servicio al cliente que, si bien cuenta con opciones útiles, muestra áreas significativas que requieren atención. A continuación, se analizan los aspectos más relevantes de la experiencia del cliente y la funcionalidad de Chapur:

**Servicio al Cliente**: **3** - Chapur permite la opción de realizar compras a través de WhatsApp con el apoyo de un asesor. Sin embargo, la disponibilidad de este asesor no es permanente, lo que limita la accesibilidad del servicio. Los clientes pueden encontrarse en situaciones donde necesitan asistencia o desean realizar una compra, pero el asesor no está disponible, lo que genera frustración. Además, incluso cuando el asesor está presente, las respuestas pueden ser lentas, causando retrasos en el proceso de compra. Esta experiencia podría mejorar notablemente si se implementara un servicio más ágil y con mayor disponibilidad, asegurando que los clientes reciban la atención que necesitan sin demoras.

**Cumplimiento/Fiabilidad**: **4** - La fiabilidad en los servicios de Chapur es general buena. Los clientes confían en que sus pedidos serán cumplidos con precisión y en un tiempo razonable. Sin embargo, hay margen de mejora en los tiempos de respuesta y en la eficiencia de la atención al cliente, que son cruciales para mantener la satisfacción y confianza del consumidor.

**Facilidad de Uso**: **4** - La interfaz del sitio web es bastante intuitiva y fácil de navegar, lo que permite a los usuarios encontrar productos sin complicaciones. La experiencia de compra en línea se facilita a través de un diseño que prioriza la usabilidad. Sin embargo, el proceso de asistencia por WhatsApp podría mejorarse para hacer la experiencia más fluida y efectiva.

**Portafolio de Productos/Servicios**: **5** - Chapur se destaca por su buena gama de productos, lo que le permite atraer a diversos tipos de consumidores. Este amplio portafolio es un punto fuerte que posiciona a Chapur favorablemente en el mercado.

**Seguridad y Privacidad**: **5** - La tienda aplica buenas prácticas de seguridad y privacidad, lo que proporciona a los usuarios una experiencia de compra segura. La protección de datos y la seguridad en las transacciones son elementos esenciales que Chapur maneja adecuadamente.

#### Análisis de Seguridad Informática 

El sitio web de **Chapur** presenta un nivel de seguridad informática muy sólido, alcanzando una calificación **A+** en su configuración SSL. Esta evaluación muestra que la plataforma implementa medidas avanzadas de protección para salvaguardar la información de sus usuarios y ofrecer una navegación segura. A continuación se destacan los puntos clave de la seguridad de Chapur:

1. **Certificado SSL y Soporte de Protocolos**  
   - Chapur utiliza **dos certificados SSL**: uno con **RSA 2048 bits (SHA256withRSA)** y otro también en **RSA 2048 bits (SHA256withRSA)**. Estos certificados son confiables y de alto nivel de seguridad, asegurando que la información intercambiada entre el servidor y los usuarios esté protegida.
   - El soporte para **TLS 1.3**, el protocolo más reciente y seguro, garantiza conexiones más rápidas y seguras, eliminando vulnerabilidades presentes en versiones anteriores.

2. **Implementación de HTTP Strict Transport Security (HSTS)**  
   - La implementación de **HTTP Strict Transport Security (HSTS)** con un parámetro de tiempo adecuado obliga a los navegadores a usar solo conexiones seguras (HTTPS). Esta medida protege contra ataques de intermediario (MITM), asegurando que todos los datos se transmitan de manera encriptada.

3. **Intercambio de Claves y Fortaleza del Cifrado**  
   - La evaluación del **intercambio de claves** revela una calificación alta, lo que asegura que se estén utilizando protocolos seguros que minimizan el riesgo de interceptación.
   - La **fortaleza del cifrado** es igualmente alta, proporcionando una defensa robusta contra intentos de descifrado por actores no autorizados.

4. **Buenas Prácticas en Seguridad de Certificados**  
   - Los certificados de Chapur están firmados por **DigiCert**, una autoridad de certificación de confianza. Además, tienen configurado **OCSP** (Online Certificate Status Protocol), lo que permite verificar el estado de los certificados en tiempo real, asegurando que no hayan sido revocados.
   - La transparencia en certificados está habilitada, lo que permite la validación pública de su legitimidad, reduciendo el riesgo de fraudes con certificados falsificados.

5. **Dominios y Subdominios Alternativos**  
   - Los certificados cubren un amplio rango de **dominios y subdominios**, asegurando que todas las partes del ecosistema de servicios de Chapur estén protegidas bajo los mismos estándares de seguridad. Esto disminuye la posibilidad de brechas en subdominios secundarios.

6. **Consideraciones Generales y Recomendaciones**  
   - Con una configuración de seguridad robusta y una calificación A+, Chapur ha demostrado un claro compromiso con la protección de sus usuarios. Es esencial que continúen realizando auditorías regulares para asegurarse de que estén al día con la renovación de los certificados y el mantenimiento de las configuraciones de seguridad.
   - Se recomienda realizar pruebas de seguridad de manera continua para verificar la efectividad de las configuraciones de TLS y HSTS y adaptarse a nuevas vulnerabilidades que puedan surgir.

##### Conclusión  
Chapur ha implementado una infraestructura de seguridad destacada en su sitio web, con el uso de **TLS 1.3**, **certificados SSL RSA de 2048 bits** y **HSTS**. Estas configuraciones garantizan una experiencia de navegación segura y confiable, protegiendo la privacidad de los datos de los usuarios. Al obtener una calificación A+, Chapur reafirma su compromiso con la seguridad y la confianza de sus clientes.

## Conclusión
La evaluación muestra que la mayoría de las plataformas cumplen con buenos estándares de **seguridad y privacidad**, siguiendo buenas prácticas como el uso de HTTPS y certificados SSL. En general, las plataformas con calificaciones más altas en todas las categorías fueron **Liverpool**, **Almacenes García** y **La Marina** debido a su confiabilidad y atención al cliente sobresaliente. Por otro lado, plataformas como **Hemsa** necesitan mejorar aspectos clave como su atención al cliente y seguridad.