Multi-Status Response for Blueprint State Deletion

```json
{
  "states": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1234567890"
      },
      "message": "State deleted successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "1234567890"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```
