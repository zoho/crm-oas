Dependent mismatch when Job_Sheet_Section__s requires Job_Sheet_Required is Yes

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
