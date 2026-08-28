# Examples: getMergeJobStatus

**GET /{module}/{masterRecordId}/actions/merge**

## Response examples

### Status `200` — `application/json` — ScheduledJob

Example of merge job in scheduled state. 

```json
{
  "merge": [
    {
      "job_id": "1041770000009251159",
      "status": "SCHEDULED"
    }
  ]
}
```

### Status `200` — `application/json` — FailedJob

Example of merge job with a failed status. 

```json
{
  "merge": [
    {
      "job_id": "1234567890",
      "status": "failed"
    }
  ]
}
```

### Status `200` — `application/json` — RunningJob

Example of merge job currently in progress. 

```json
{
  "merge": [
    {
      "job_id": "1234567890",
      "status": "running"
    }
  ]
}
```

### Status `200` — `application/json` — CompletedJob

Example of a merge job completed successfully. 

```json
{
  "merge": [
    {
      "job_id": "1234567890",
      "status": "completed"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Example of an invalid module name in request URL. 

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — MasterRecordNotFound

Example of master record not found in the module. 

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "Master record is not found",
  "status": "error"
}
```

### Status `400` — `application/json` — MasterRecordNotAvailable

Example of master record ID not available. 

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "Master record id is not available",
  "status": "error"
}
```

### Status `400` — `application/json` — ChildRecordIdMissing

Example of child record ID missing from data array. 

```json
{
  "merge": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.merge[0].data[0].id"
      },
      "message": "required id not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RecordAlreadyBeingMerged

Example of the error saying that the record is already being merged. 

```json
{
  "merge": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.merge[0].data[0].id"
      },
      "message": "This record id is not allowed to be merged",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ClosingDateNotAllowed

Example of Closing Date field specified in merge request. 

```json
{
  "merge": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "Closing date will be automatically populated based on master record",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — StageFieldNotAllowed

Example of Stage being mentioned when child and master record have different pipelines. 

```json
{
  "merge": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "Stage field will be automatically populated based on chosen Pipeline",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ProbabilityRevenueNotAllowed

Example of errors related to Expected Revenue and Probability fields. 

```json
{
  "merge": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "Probability and Expected Revenue fields will be automatically populated based on chosen Stage",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ClosedDealNotAllowed

Example for an attempt to merge a closed deal. 

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "api_name": "record",
    "resource_path_index": 1
  },
  "message": "Only Open Deals can be merged",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateRecordIds

Example of duplicate record IDs in merge request. 

```json
{
  "merge": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.merge[0].data[0].id"
      },
      "message": "Valid record ids need to be given for merging",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateFieldMention

Example of duplicate field API name in merge request. 

```json
{
  "merge": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "When one field is mentioned more than once",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MergeArraySizeExceeded

Example of merge array containing more than one object. 

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNameNotMentioned

Example of API name missing from configuration. 

```json
{
  "merge": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "API name of the field is not mentioned",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DataArraySizeExceeded

Example of data array exceeding maximum of two child records. 

```json
{
  "merge": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "data",
        "json_path": "$.merge[0].data",
        "maximum_length": 2
      },
      "message": " More than 2 child record ids cannot be merged.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MasterRecordApiNameMissing

Example of API name missing from master_record_fields entry. 

```json
{
  "merge": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].master_record_fields[0].api_name"
      },
      "message": "API name not mentioned for the master record",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DataArrayEmpty

Example of data array empty or missing from request. 

```json
{
  "merge": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "data",
        "json_path": "$.merge[0].data",
        "minimum_length": 1
      },
      "message": " Atleast one child record id is required to be merged.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FileUploadDataMissingMaster

Example of _data array missing for master record file upload field. 

```json
{
  "merge": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "id",
        "json_path": "$.merge[0].master_record_fields[0]._data",
        "dependee": {
          "api_name": "api_name",
          "json_path": "$.merge[0].master_record_fields[0].api_name"
        }
      },
      "message": "_data array is not mentioned for the master record",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FileUploadDataMissingChild

Example of _data array missing for child record file upload field. 

```json
{
  "merge": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "id",
        "json_path": "$.merge[0].data[0]._fields[0]._data",
        "dependee": {
          "api_name": "api_name",
          "json_path": "$.merge[0].data[0]._fields[0].api_name"
        }
      },
      "message": "_data array is not mentioned for the child record",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CpqAssociationError

Example of child record has CPQ rule associations. 

```json
{
  "merge": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "data": [
          {
            "_associated_places": [
              {
                "resources": [
                  {
                    "name": "asdfsdf",
                    "id": "111111000000071837"
                  }
                ],
                "type": "product_configurators"
              },
              {
                "resources": [
                  {
                    "name": "PR -sample",
                    "id": "111111000000072007"
                  }
                ],
                "type": "pricing_rules"
              }
            ],
            "id": "111111000000071814"
          }
        ],
        "api_name": "data",
        "json_path": "$.merge[0].data"
      },
      "message": "unable to merge records since there are association in child records",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FileSizeLimitExceeded

Example of total file size across merge participants exceeds limit. 

```json
{
  "merge": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "MAXIMUM_SIZE": "30 MB",
        "limit_due_to": [
          {
            "api_name": "File_Upload_30MB",
            "json_path": "$.merge[0].data[0]._fields[0].api_name"
          },
          {
            "api_name": "File_Upload_30MB",
            "json_path": "$.merge[0].data[1]._fields[1].api_name"
          },
          {
            "api_name": "File_Upload_30MB",
            "json_path": "$.merge[0].master_record_fields[1].api_name"
          }
        ]
      },
      "message": "Attachment size limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReportingToChildOnly

Example of only Reporting To is given for child record. 

```json
{
  "merge": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "Reporting to and account should belong to the same record",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReportingToWithAccountMismatch

Example of Reporting To configured for child and Account for master (or vice versa). 

```json
{
  "merge": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.merge[0].data[0]._fields[0].api_name"
      },
      "message": "Reporting to and account should belong to the same record",
      "status": "error"
    }
  ]
}
```
