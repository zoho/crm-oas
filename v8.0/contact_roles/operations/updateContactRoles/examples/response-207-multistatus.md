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
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.contact_roles[0].id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```
