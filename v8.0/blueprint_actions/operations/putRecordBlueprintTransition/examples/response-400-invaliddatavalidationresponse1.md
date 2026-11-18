Error response for validation errors in the transition data

```json
{
  "blueprint": [
    {
      "code": "INVALID_DATA",
      "details": {
        "validation_error": [
          {
            "api_name": "Notes",
            "message": "mandatory param missing",
            "info_message": "Notes cannot be empty."
          }
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
