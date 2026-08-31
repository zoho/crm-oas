Dependent mismatch where Job_Sheet_Section__s is set but Job_Sheet_Required is No.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Job_Sheet_Required",
          "json_path": "$.data[0].Job_Sheet_Required"
        },
        "api_name": "Job_Sheet_Section__s",
        "json_path": "$.data[0].Job_Sheet_Section__s"
      },
      "message": "Job_Sheet_Section__s can have value only when value of Job_Sheet_Required is Yes",
      "status": "error"
    }
  ]
}
```
