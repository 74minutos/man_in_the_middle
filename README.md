Tenemos que instalar mitmproxy con brew

abrir la configuración de proxies y cambiarla a la por defecto de mitm (127.0.0.1 y 8080)

para lanzar el script que va a empezar a captar las trazas con las que trabajamos, tendremos que utilizar la feature de mitmdump de la siguiente manera:

```bash
mitmdump -s mitm_ae.py
```

para el móvil tendremos que configurar nuestro proxy para que cuadre con la dirección de nuestro wifi y cambiaremos el puerto a 8080. Abriremos mitmproxy desde terminal y en el móvil iremos a la dirección mitm.it

Cuando estemos en esa web nos descargaremos e instalaremos el certificado adecuado a nuestro sistema operativo.

Más información en https://visiondefunnel.com/man-in-the-middle-como-generar-tu-propio-proxy
