# 우리 동네 붕세권 Back-end Server


## API
| route           | required data                                                                                                                                                                                     | response data                                                                                                                                                                                                          | description |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| /               | None                                                                                                                                                                                              | - html                                                                                                                                                                                                                 | for test    |
| /get_store_info | json("id": String)                                                                                                                                                                                | - json("ok": Boolean, "error": String(if "ok" is false), "name": String, "store_name": String, "category": String, "store_description": String, "store_open_info": String, "store_photo": json(), "menu_info": json()) |             |
| /get_location   | None                                                                                                                                                                                              | - json("ok": Boolean, "error": String(if "ok" is false), "store_id": Int, locations": [json("latitude": Double, "longitude": Double), ...])                                                                            |             |
| /set_store_info | json("id": String, "token": String, "name": String, "store_name": String, "category": String, "store_description": String, "store_open_info": json(), "store_photo": json(), "menu_info": json()) | - json("ok": Boolean, "error": String(if "ok" is false))                                                                                                                                                               |             |
| /set_location   | json("id": String, "token": String, "latitude": Double, "longitude": Double, "is_open": Boolean)                                                                                                  | - json("ok": Boolean, "error": String(if "ok" is false))                                                                                                                                                               |             |
| /login          | json("id": String, "password": String)                                                                                                                                                            | - json("ok": Boolean, "error": String(if "ok" is false), "token": String)                                                                                                                                              |             |
| /logout         | json("id": String)                                                                                                                                                                                | - json("ok": Boolean, "error": String(if "ok" is false))                                                                                                                                                               |             |


## API Examples

## /get_store_info: json

### request
> { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"id": "String", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"token": "valid_token", <br>
> }

### response
> { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"ok": true, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"error": None, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"name": "purple pig", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"store_name": "my_store", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"category": "Default", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"store_description": "It is purple pig's store", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"store_open_info": { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"information": [<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"월, 화 -> 대전광역시 유성구 ~ 16시 ~ 20시", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"월, 화 -> 대전광역시 유성구 ~ 16시 ~ 20시", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] <br>
> &nbsp;&nbsp;&nbsp;&nbsp;}, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"store_photo": { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"photo_urls": [<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "photo_url", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "photo_url", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] <br>
> &nbsp;&nbsp;&nbsp;&nbsp;}, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"menu_info": { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"menu": [ <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { "name": "음식", "price": 10000, "photo": "photo_url", }, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { "name": "음식", "price": 20000, "photo": "photo_url", }, <br> 
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] <br>
> &nbsp;&nbsp;&nbsp;&nbsp;}, <br>
> }


## /get_location: json

### request
> None

### response
> { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"ok": true, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"error": None, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"locations": [ <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ "store_id": 2, "latitude": 63.342435, "longitude": 123.523425 }, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ "store_id": 3, "latitude": 142.342435, "longitude": 23.523425 }, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;], <br>
> }


## /set_store_info: json

### request
> { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"id": "purplepig", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"name": "changed name", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"store_name": "my_store", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"category": "Default", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"store_description": "It is purple pig's store. ok?", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"store_open_info": { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"information": [<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"월, 화 -> 대전광역시 유성구 ~ 16시 ~ 20시", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"월, 화 -> 대전광역시 유성구 ~ 12시 ~ 20시", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] <br>
> &nbsp;&nbsp;&nbsp;&nbsp;}, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"store_photo": { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"photo_urls": [<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "photo_url", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "raw data base64 encoded", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "raw data base64 encoded", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] <br>
> &nbsp;&nbsp;&nbsp;&nbsp;}, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"menu_info": { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"menu": [ <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { "name": "음식", "price": 10000, "photo": "photo_url", }, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { "name": "치킨", "price": 30000, "photo": "raw data base64 encoded", }, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] <br>
> &nbsp;&nbsp;&nbsp;&nbsp;}, <br>
> }

### response
> { <br>
> &nbsp;&nbsp;&nbsp;&nbsp; "ok": true, <br>
> &nbsp;&nbsp;&nbsp;&nbsp; "error": None, <br>
> }

## /set_location: json

### request
> { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"id": "purplepig", <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"latitude": 63.342435, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"longitude": 123.523425, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;"is_open": true, <br>
> }

### response
> { <br>
> &nbsp;&nbsp;&nbsp;&nbsp; "ok": true, <br>
> &nbsp;&nbsp;&nbsp;&nbsp; "error": None, <br>
> }
