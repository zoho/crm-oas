# Examples: getMassChangeOwnerStatus

**GET /{module}/actions/mass_change_owner**

## Response examples

### Status `200` — `application/json` — JobStatusResponse

An example of a completed mass change owner job with all records updated.

```json
{
  "data": [
    {
      "Status": "COMPLETED",
      "Failed_Count": 0,
      "Not_Updated_Count": 0,
      "Updated_Count": 10,
      "Total_Count": 10
    }
  ]
}
```

### Status `204` — `application/json` — NoDataFound

Example of no job data found for the specified job ID.

```json
{
  "code": "NO_DATA",
  "message": "there is no data to show"
}
```

### Status `400` — `application/json` — RequiredParamMissing

An example of the missing job_id query parameter in request.

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "message": "Required parameter is missing",
  "status": "error",
  "details": {
    "param_name": "job_id"
  }
}
```

### Status `404` — `application/json` — JobBelongsToAnotherModule

Example of a job ID belonging to a different module.

```json
{
  "code": "NOT_FOUND",
  "message": "The specified job does not belong to this module",
  "status": "error",
  "details": {}
}
```
