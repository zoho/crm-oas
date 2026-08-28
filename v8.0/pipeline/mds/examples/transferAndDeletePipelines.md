# Examples: transferAndDeletePipelines

**POST /settings/pipeline/actions/transfer**

## Request examples

### `application/json` — PipelineTransferRequest

```json
{
  "transfer_pipeline": [
    {
      "pipeline": {
        "from": "2766660000056473266",
        "to": "2766660000056473305"
      },
      "stages": [
        {
          "from": "2766660000000007104",
          "to": "2766660000000007104"
        },
        {
          "from": "2766660000000007106",
          "to": "2766660000000007106"
        },
        {
          "from": "2766660000000007110",
          "to": "2766660000000007104"
        },
        {
          "from": "2766660000000007112",
          "to": "2766660000000007106"
        },
        {
          "from": "2766660000000007114",
          "to": "2766660000000007104"
        },
        {
          "from": "2766660000030928184",
          "to": "2766660000000007104"
        },
        {
          "from": "2766660000030928185",
          "to": "2766660000000007106"
        },
        {
          "from": "2766660000030928272",
          "to": "2766660000000007104"
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — PipelineTransferResponseSuccess

```json
{
  "transfer_pipeline": [
    {
      "code": "SUCCESS",
      "details": {
        "job_id": "2766660000056808404"
      },
      "message": "transfer pipeline scheduled successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyUsedStagedError

```json
{
  "transfer_pipeline": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "from",
        "exists_in": {
          "json_path": "$.transfer_pipeline[0].stages[0].from"
        },
        "json_path": "$.transfer_pipeline[0].stages[1].from"
      },
      "message": "from id is mapped more than once",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadySchedulerError

```json
{
  "transfer_pipeline": [
    {
      "code": "ALREADY_SCHEDULED",
      "details": {
        "api_name": "cvid",
        "value": "2766660000054211054"
      },
      "message": "Scheduler already running for this pipeline",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidPipelineFromID

```json
{
  "transfer_pipeline": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "from",
        "json_path": "$.transfer_pipeline[0].pipeline[0].from"
      },
      "message": "Invalid from id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidPipelineToID

```json
{
  "transfer_pipeline": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "to",
        "json_path": "$.transfer_pipeline[0].pipeline[0].to"
      },
      "message": "Invalid to id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — PipelineFromAndToIDAreSame

```json
{
  "transfer_pipeline": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "to",
        "json_path": "$.transfer_pipeline[0].pipeline[0].to"
      },
      "message": "Both from_id and to_id cannot be same ",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidStageFromID

```json
{
  "transfer_pipeline": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "from",
        "json_path": "$.transfer_pipeline[0].stages[0].from"
      },
      "message": "Invalid from id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidStageToID

```json
{
  "transfer_pipeline": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "to",
        "json_path": "$.transfer_pipeline[0].stages[0].to"
      },
      "message": "Invalid to id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — StageNotFound

```json
{
  "transfer_pipeline": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "stages",
        "json_path": "$.transfer_pipeline[0].stages"
      },
      "message": "Required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidLayoutID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "layout_id"
  },
  "message": "Invalid layoutid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionErrorResponse

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": "Crm_Implied_Customize_Zoho_CRM"
  },
  "message": "permission denied to customize Zoho CRM",
  "status": "error"
}
```
