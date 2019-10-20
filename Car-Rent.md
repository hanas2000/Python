# Car-Rent
. Створити серсів для прокату авто. Користувачі сервісу можуть бути двох рівнів – адміністратори та пасажири. Адміністратори можуть додавати та видаляти авто із системи, редагувти інформацію про авто. Пасажири можуть переглядати каталог та бронювати авто на певний час.

## Version: 1.0

**Contact information:**  
Khanas Yura  
hanasura79@gmail.com  

### /users

#### GET
##### Summary:

Отримання даних про користувачів

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт користувача | [User](#user) |

#### POST
##### Summary:

Створення нового користувача

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| body | body | Об'єкт користувача | Yes | [User](#user) |
| api_key | header | індивідуальний ключ користувача | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт користувача | [User](#user) |
| 400 | Bad data |  |
| 401 | Unauthorized |  |
| 406 | Not Acceptable |  |

### /users/{id}

#### GET
##### Summary:

Отримання даних про користувача

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | унікальний ідентифікатор | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт користувача | [User](#user) |
| 404 | Not Found |  |

#### PUT
##### Summary:

Оновлення даних

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | унікальний ідентифікатор | Yes | integer |
| body | body | Об'єкт користувача | Yes | [User](#user) |
| api_key | header | індивідуальний ключ користувача | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт користувача | [User](#user) |
| 400 | Bad data |  |
| 401 | Unauthorized |  |
| 404 | Not Found |  |
| 406 | Not Acceptable |  |

#### DELETE
##### Summary:

Видалення користувача

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | унікальний ідентифікатор | Yes | integer |
| api_key | header | індивідуальний ключ користувача | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Успішне видалення |
| 401 | Unauthorized |
| 404 | Not Found |
| 406 | Not Acceptable |

### /car

#### GET
##### Summary:

Отримання даних про машину

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт машини | [Car](#car) |

#### POST
##### Summary:

Створення нової машини

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| body | body | Об'єкт машини | Yes | [Car](#car) |
| api_key | header | індивідуальний ключ машини | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт машини | [Car](#car) |
| 400 | Bad data |  |
| 401 | Unauthorized |  |
| 406 | Not Acceptable |  |

### /car/{id}

#### GET
##### Summary:

Отримання даних про машини

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | унікальний ідентифікатор | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт машини | [Car](#car) |
| 404 | Not Found |  |

#### PUT
##### Summary:

Оновлення даних

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | унікальний ідентифікатор | Yes | integer |
| body | body | Об'єкт машини | Yes | [Car](#car) |
| api_key | header | індивідуальний ключ машини | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт машини | [Car](#car) |
| 400 | Bad data |  |
| 401 | Unauthorized |  |
| 404 | Not Found |  |
| 406 | Not Acceptable |  |

#### DELETE
##### Summary:

Видалення машини

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | унікальний ідентифікатор | Yes | integer |
| api_key | header | індивідуальний ключ машини | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Успішне видалення |
| 401 | Unauthorized |
| 404 | Not Found |
| 406 | Not Acceptable |

### /car/rent/{id}

#### GET
##### Summary:

Отримання даних про орендовану машину

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | унікальний ідентифікатор | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Об'єкт машини | [Car](#car) |
| 404 | Not Found |  |

### Models


#### User

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | long |  | No |
| user_name | string |  | No |
| id_car | long |  | No |
| status | long |  | No |

#### Car

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | long |  | No |
| car_name | string |  | No |
| id_user | long |  | No |
| date_from | dateTime |  | No |
| date_to | dateTime |  | No |
| text | string |  | No |