Returned when a mandatory field is missing from the request

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "singular_label",
        "json_path": "$.modules[0].singular_label"
      },
      "message": "The required field 'singular_label' is missing from the request.",
      "status": "error"
    }
  ]
}
```
