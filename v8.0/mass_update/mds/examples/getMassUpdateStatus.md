# Examples: getMassUpdateStatus

**GET /{module}/actions/mass_update**

## Response examples

### Status `200` — `application/json` — ScheduledJob

An example of mass update job in SCHEDULED state.

```json
{
  "data": [
    {
      "Status": "SCHEDULED",
      "Failed_Count": 0,
      "Updated_Count": 0,
      "Not_Updated_Count": 18,
      "Total_Count": 18
    }
  ]
}
```

### Status `400` — `application/json` — InvalidJobId

An example of invalid job_id being provided in the request.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "job_id"
  },
  "message": "The jobid given seems to be invalid",
  "status": "error"
}
```
