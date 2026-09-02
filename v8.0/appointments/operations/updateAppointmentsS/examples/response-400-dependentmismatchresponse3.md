Error when a job sheet creation targets an incomplete appointment

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Job_Sheet_Name__s",
        "json_path": "$.data[0].Job_Sheet_Name__s"
      },
      "message": "Job Sheet can be created only for completed appointment",
      "status": "error"
    }
  ]
}
```
