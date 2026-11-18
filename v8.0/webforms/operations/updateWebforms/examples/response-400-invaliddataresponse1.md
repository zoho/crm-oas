INVALID_DATA error when the Company field is set as both hidden and required

```json
{
  "webforms": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Company",
        "json_path": "$.webforms[0].$.form_fields[0].hidden"
      },
      "message": "Company cannot be hidden and required it can be either hidden or required",
      "status": "error"
    }
  ]
}
```
