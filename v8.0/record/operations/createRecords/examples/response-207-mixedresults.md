Mixed create results with one success and one validation error

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2023-05-10T01:10:47-07:00",
        "Modified_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "Created_Time": "2023-05-10T01:10:47-07:00",
        "id": "5725767000000524157",
        "Created_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "$approval_state": "approved"
      },
      "message": "record added",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Last_Name",
        "json_path": "$.data[1].Last_Name"
      },
      "message": "the field api name given seems to be invalid",
      "status": "error"
    }
  ]
}
```
