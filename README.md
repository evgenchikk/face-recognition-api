# API service for face recognition

## Launch
1) git clone https://github.com/evgenchikk/face-recognition-api

2) create or change .env file in the project directory with:<br>
PORT=\<port\><br>
FACE_PLUS_PLUS_API_KEY=\<your face++ api key\><br>
FACE_PLUS_PLUS_API_SECRET=\<your face++ api secret\>

3) run "docker compose up -d"

## HTTP methods:
#### POST /image
Requires a file upload<br>
___curl example:___
curl -X POST -F "file=@\<path to your file\>" "localhost:\<port\>/image"

#### GET /image/\<id\>?color=\<hex color in RGB format\>
Requires the image id and the color<br>
___curl exmaple:___
curl -X GET -O -J "localhost:\<port\>/image/1?color=f99"

#### PUT /image/\<id\>
Requires a file upload<br>
___curl example:___
curl -X PUT -F "file=@\<path to your file\>" "localhost:\<port\>/image/1"

#### DELETE /image/\<id\>
___curl example:___
curl -X DELETE "localhost:\<port\>/image/1"
