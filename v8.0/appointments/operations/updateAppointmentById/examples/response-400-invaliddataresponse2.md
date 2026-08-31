**INVALID_DATA** error is thrown when  **api_name** in **Appointment_For.module** not found in multi-module lookup.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.data[0].Appointment_For.module.api_name"
      },
      "message": "the given module name is not exist in multimodulelookup",
      "status": "error"
    }
  ]
}
```
