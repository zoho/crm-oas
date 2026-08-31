Response of a partial success composite request.



```json
{
  "__composite_requests": [
    {
      "code": "SUCCESS",
      "message": "Request processed successfully",
      "status": "success",
      "details": {
        "response": {
          "headers": {
            "Content-Type": "application/json"
          },
          "body": {
            "data": "response data"
          },
          "status_code": 200
        }
      }
    },
    {
      "code": "INVALID_DATA",
      "message": "Invalid input data",
      "status": "error",
      "details": {
        "api_name": "sub_request_2",
        "json_path": "$.body.data[0].field",
        "expected_data_type": "string"
      }
    }
  ]
}
```
