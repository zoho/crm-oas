Partial success - label length exceeded error for one module

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000263276"
      },
      "message": "module updated successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 50,
        "api_name": "plural_label",
        "json_path": "$.modules[1].plural_label"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
