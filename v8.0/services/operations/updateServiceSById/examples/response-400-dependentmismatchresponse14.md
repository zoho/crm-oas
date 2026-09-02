Unavailable_Till set on a scheduled service with Available_From.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_From",
          "json_path": "$.data[0].Available_From"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Service status cannot be marked as Not In Use or Temporarily Unavailable for scheduled services.",
      "status": "error"
    }
  ]
}
```
