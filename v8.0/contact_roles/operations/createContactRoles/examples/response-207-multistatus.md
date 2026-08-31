Mixed success and error results

```json
{
  "contact_roles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "123456789"
      },
      "message": "Contact role created successfully.",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.contact_roles[1].name",
        "expected_data_type": "text"
      },
      "message": "invalid data provided",
      "status": "error"
    }
  ]
}
```
