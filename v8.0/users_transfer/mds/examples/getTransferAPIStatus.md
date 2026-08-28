# Examples: getTransferAPIStatus

**GET /users/actions/transfer**

## Response examples

### Status `200` — `application/json` — TransferStatusResponse

An example response of completed transfer status.

```json
{
  "transfer": [
    {
      "status": "completed"
    }
  ]
}
```

### Status `400` — `application/json` — MissingJobIdError

An example error response of missing job_id parameter.

```json
{
  "status": "error",
  "code": "REQUIRED_PARAM_MISSING",
  "message": "mandatory param missing",
  "details": {
    "param_name": "job_id"
  }
}
```
