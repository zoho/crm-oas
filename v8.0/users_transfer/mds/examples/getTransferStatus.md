# Examples: getTransferStatus

**GET /users/actions/transfer_and_delete**

## Response examples

### Status `200` — `application/json` — TransferStatusResponse

An example of success response of a completed transfer and delete status.

```json
{
  "transfer_and_delete": [
    {
      "status": "completed"
    }
  ]
}
```

### Status `400` — `application/json` — MissingJobIdError

An example response of a missing job_id parameter.

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
