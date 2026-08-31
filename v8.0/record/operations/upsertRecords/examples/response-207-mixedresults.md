Mixed results with success and failure items

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "duplicate_field": "Email",
      "action": "insert",
      "details": {
        "Modified_Time": "2023-05-10T01:10:47-07:00",
        "Modified_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "Created_Time": "2023-05-10T01:10:47-07:00",
        "id": "111112000000142001",
        "Created_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        }
      },
      "message": "record added",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "Company",
        "json_path": "$.data[1].Company"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
