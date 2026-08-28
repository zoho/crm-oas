# Examples: deleteAppointmentsS

**DELETE /Appointments__s**

## Response examples

### Status `200` — `application/json` — Success200

All three appointment records deleted successfully.


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111115000000147279"
      },
      "message": "record deleted",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111115000000147229"
      },
      "message": "record deleted",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111115000000147224"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Partial deletion where one record deleted, one failed with INVALID_DATA.


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111115000000147279"
      },
      "message": "record deleted",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "23132423"
      },
      "message": "record not deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error where appointment ID is invalid or already deleted


```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "23132423"
      },
      "message": "record not deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRequestMethodResponse1

Invalid HTTP request method type used in the request.


```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Invalid module API name provided in the request.


```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```
