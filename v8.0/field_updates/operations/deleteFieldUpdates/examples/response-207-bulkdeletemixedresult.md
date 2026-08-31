Mixed response  - one invalid ID, one success, one associated field update

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000090003"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000081106"
      },
      "message": "field update deleted successfully",
      "status": "success"
    },
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000064003"
      },
      "message": "This field update is associated with at least one of Approval Process/Workflow Rules/Blueprint",
      "status": "error"
    }
  ]
}
```
