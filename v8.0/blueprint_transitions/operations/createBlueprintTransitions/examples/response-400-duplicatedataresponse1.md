DUPLICATE_DATA error for duplicate during field **type** in the transition

```json
{
  "transitions": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.transitions[0].during_inputs[1].type"
      },
      "message": "Only one type of this during field is allowed to be in the transition",
      "status": "error"
    }
  ]
}
```
