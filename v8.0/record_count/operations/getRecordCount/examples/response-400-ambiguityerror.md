Ambiguous parameters - cvid with criteria

```json
{
  "status": "error",
  "code": "AMBIGUITY_DURING_PROCESSING",
  "message": "Please use either Cvid or Search Params. Combination of both the params is not allowed",
  "details": {
    "ambiguity_due_to": [
      {
        "param_name": "cvid"
      },
      {
        "param_name": "criteria"
      }
    ]
  }
}
```
