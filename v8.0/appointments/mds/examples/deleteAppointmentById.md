# Examples: deleteAppointmentById

**DELETE /Appointments__s/{appointmentId}**

## Response examples

### Status `200` — `application/json` — Success200

Successful deletion of a single appointment record.


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
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error where the appointment ID is invalid or record already deleted


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

INVALID_REQUEST_METHOD error where unsupported HTTP method used.


```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

INVALID_MODULE error where module API name is invalid


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

### Status `400` — `application/json` — InvalidDataFlatResponse1

INVALID_DATA error response when the appointment ID is invalid or already deleted.


```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "record not deleted",
  "status": "error"
}
```
