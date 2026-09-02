Error when reschedule information fields change without a prior reschedule.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_UNCHANGED",
      "details": {
        "dependee": {
          "api_name": "Reschedule_Reason",
          "json_path": "$.data[0].Reschedule_Reason"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Reschedule the appointment atleast once to Update the fields of Reschedule Information Section",
      "status": "error"
    }
  ]
}
```
