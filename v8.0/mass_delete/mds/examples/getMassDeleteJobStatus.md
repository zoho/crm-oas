# Examples: getMassDeleteJobStatus

**GET /{module}/actions/mass_delete**

## Response examples

### Status `200` — `application/json` — CompletedJob

An example of completed mass delete job with all records deleted.

```json
{
  "data": [
    {
      "Status": "COMPLETED",
      "Failed_Count": 0,
      "Deleted_Count": 18,
      "Total_Count": 18
    }
  ]
}
```

### Status `200` — `application/json` — InProgressJob

An example of mass delete job currently in progress.

```json
{
  "data": [
    {
      "Status": "RUNNING",
      "Failed_Count": 0,
      "Deleted_Count": 12,
      "Total_Count": 18
    }
  ]
}
```

### Status `200` — `application/json` — PartialFailure

Example of mass delete job completed with some record failures.

```json
{
  "data": [
    {
      "Status": "COMPLETED",
      "Failed_Count": 3,
      "Deleted_Count": 15,
      "Total_Count": 18
    }
  ]
}
```

### Status `400` — `application/json` — MissingJobId

An example of missing required job_id parameter.

```json
{
  "status": "error",
  "code": "MANDATORY_NOT_FOUND",
  "message": "mandatory param missing",
  "details": {
    "param_name": "job_id"
  }
}
```

### Status `400` — `application/json` — InvalidJobIdFormat

An example of invalid job_id format (non-numeric).

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "The jobid given seems to be invalid",
  "details": {
    "param_name": "job_id"
  }
}
```

### Status `400` — `application/json` — InvalidModule

An example of invalid module name in path.

```json
{
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {
    "resource_path_index": 0
  }
}
```

### Status `400` — `application/json` — UnableToParseJobId

An example of non-numeric job_id causing parse failure.

```json
{
  "status": "error",
  "code": "UNABLE_TO_PARSE_DATA_TYPE",
  "message": "either the request body or parameters is in wrong format",
  "details": {}
}
```
