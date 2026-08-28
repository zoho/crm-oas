# Examples: getMassConvertJobStatus

**GET /Leads/actions/mass_convert**

## Response examples

### Status `200` — `application/json` — Success

Example of completed mass convert job with all leads converted.

```json
{
  "data": [
    {
      "Status": "Completed",
      "Total_Count": 50,
      "Converted_Count": 50,
      "Not_Converted_Count": 0,
      "Failed_Count": 0
    }
  ]
}
```

### Status `200` — `application/json` — CompletedStatus

Example of completed mass convert job with partial conversion failures.

```json
{
  "data": [
    {
      "Total_Count": 40,
      "Converted_Count": 45,
      "Not_Converted_Count": 0,
      "Failed_Count": 5,
      "Status": "completed"
    }
  ]
}
```

### Status `200` — `application/json` — FailedStatus

Example of failed mass convert job with no leads converted.

```json
{
  "data": [
    {
      "Total_Count": 50,
      "Converted_Count": 0,
      "Not_Converted_Count": 0,
      "Failed_Count": 50,
      "Status": "failed"
    }
  ]
}
```

### Status `200` — `application/json` — InProgressStatus

Example of mass convert job currently in progress with partial conversions.

```json
{
  "data": [
    {
      "Total_Count": 50,
      "Converted_Count": 25,
      "Not_Converted_Count": 20,
      "Failed_Count": 5,
      "Status": "in progress"
    }
  ]
}
```

### Status `200` — `application/json` — ScheduledStatus

Example of scheduled mass convert job awaiting execution.

```json
{
  "data": [
    {
      "Status": "scheduled",
      "Failed_Count": 0,
      "Converted_Count": 0,
      "Not_Converted_Count": 50,
      "Total_Count": 50
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissing

Example of missing job_id query parameter in the request.

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "message": "job_id is required.",
  "status": "error",
  "details": {
    "param": "job_id",
    "json_path": "$.job_id"
  }
}
```

### Status `400` — `application/json` — InvalidJobId

Example of invalid job_id value provided in the request.

```json
{
  "code": "INVALID_DATA",
  "message": "The jobid given seems to be invalid",
  "status": "error",
  "details": {
    "param_name": "job_id"
  }
}
```

### Status `403` — `application/json` — Success

Example of forbidden response when the user lacks mass convert permission.

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Mass_Convert_Leads"
    ]
  },
  "status": "error"
}
```
