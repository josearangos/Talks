# General Docs

http://localhost:8000/docs

# Meals chain

http://localhost:8000/meals_chain/playground/

## Invoke
curl --location --request POST 'http://localhost:8000/meals_chain/invoke/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "input": {
            "country": "Colombia"
        }
    }'

## Batch
curl --location --request POST 'http://localhost:8000/meals_chain/batch/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "inputs": [
            {"country": "Colombia"},
            {"country": "Argentina"},
            {"country": "Venezula"},
            {"country": "Chile"},
            {"country": "Ecuador"}
        ]
    }'

## Stream
curl --location --request POST 'http://localhost:8000/meals_chain/stream/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "input": {
            "country": "Colombia"
        }
    }'


# Translation chain
http://localhost:8000/translation_chain/playground/ 

## Invoke
curl --location --request POST 'http://localhost:8000/translation_chain/invoke/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "input": {
            "input_language": "Spanish",
            "output_language": "English",
            "text": "Que viva LangChain carajo!!!!"
        }
    }'

## Invoke text.
curl --location --request POST 'http://localhost:8000/translation_chain/invoke/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "input": {
            "input_language": "Spanish",
            "output_language": "English",
            "text": "LZString es una biblioteca de JavaScript que proporciona funciones para comprimir y descomprimir cadenas de texto utilizando el algoritmo de compresión Lempel-Ziv. Este algoritmo es comúnmente utilizado para la compresión de datos y se ha implementado en varias formas a lo largo de los años. LZString en particular se utiliza en entornos web y proporciona una forma de comprimir y descomprimir cadenas de texto en el lado del cliente (navegador web) utilizando JavaScript. Esto puede ser útil en situaciones donde se necesita transmitir datos entre el cliente y el servidor de manera eficiente, como en aplicaciones web que manejan grandes cantidades de información."
        }
    }'

## Stream
curl --location --request POST 'http://localhost:8000/translation_chain/stream/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "input": {
            "input_language": "Spanish",
            "output_language": "English",
            "text": "LZString es una biblioteca de JavaScript que proporciona funciones para comprimir y descomprimir cadenas de texto utilizando el algoritmo de compresión Lempel-Ziv. Este algoritmo es comúnmente utilizado para la compresión de datos y se ha implementado en varias formas a lo largo de los años. LZString en particular se utiliza en entornos web y proporciona una forma de comprimir y descomprimir cadenas de texto en el lado del cliente (navegador web) utilizando JavaScript. Esto puede ser útil en situaciones donde se necesita transmitir datos entre el cliente y el servidor de manera eficiente, como en aplicaciones web que manejan grandes cantidades de información."
        }
    }'


# Coupo 
http://localhost:8000/agent_coupon_code/playground/ 


"Busca los 2 usuarios que más han comprado y envía el siguiente correo: Asunto: Código de descuento por compras Contenido: "Hola, gracias por tus compras. Tienes un bono de descuento en tu siguiente compra. Utiliza el código: #LLMConEsteroides y obtén un 50% de descuento."