Partial Delete where One Function Deleted, One Invalid ID Returns an Error

```json
{
  "functions": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "678446000051490025"
      },
      "message": "Function is deleted",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "678446030057490025"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```
