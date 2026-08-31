Multi-status response with one success and one invalid-ID error.


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-19T17:45:52+05:30",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T16:50:29+05:30",
        "id": "111115000000147279",
        "Created_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.data[1].id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```
