Error response when custom_parameters exceeds the maximum allowed count.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "custom_parameters",
      "maximum_length": 2,
      "json_path": "$.webhooks[*].headers.custom_parameters"
    },
    "status": "error"
  }
}
```
