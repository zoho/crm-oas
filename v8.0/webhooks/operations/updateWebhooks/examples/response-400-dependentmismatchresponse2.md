Dependent mismatch error for incompatible HTTP method and headers

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "headers",
          "json_path": "$.webhooks[0].headers"
        },
        "api_name": "http_method",
        "json_path": "$.webhooks[0].http_method"
      },
      "message": "Invalid value provided for the given http method",
      "status": "error"
    }
  ]
}
```
