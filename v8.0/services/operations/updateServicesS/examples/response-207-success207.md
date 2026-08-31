Partial success with one record updated and one INVALID_DATA error on Duration.


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-14T17:25:57+05:30",
        "Modified_By": {
          "name": "Madeshwaran G",
          "id": "4671651000000635001"
        },
        "Created_Time": "2025-12-16T17:04:11+05:30",
        "id": "4671651000000862030",
        "Created_By": {
          "name": "Madeshwaran G",
          "id": "4671651000000635001"
        },
        "affected_data": [
          {
            "$process_flow": false,
            "id": "4671651000000862030"
          }
        ]
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Duration",
        "json_path": "$.data[1].Duration"
      },
      "message": "Duration value should not be greater than 24hrs or less than 5mins",
      "status": "error",
      "error_meta": "invalid_field"
    }
  ]
}
```
