Error response when module_parameters exceeds the maximum allowed count in headers.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "module_parameters",
      "maximum_length": 3,
      "json_path": "$.webhooks[*].headers.module_parameters"
    },
    "status": "error"
  }
}
```
