# Examples: mergeRecords

**POST /{module}/{masterRecordId}/actions/merge**

## Request examples

### `application/json` — BasicMerge

Example of a basic merge operation with field selection. 

```json
{
  "merge": [
    {
      "data": [
        {
          "_fields": [
            {
              "api_name": "Last_Name"
            }
          ],
          "id": "111111000000116110"
        }
      ],
      "master_record_fields": [
        {
          "api_name": "Company"
        }
      ]
    }
  ]
}
```

### `application/json` — FileUploadMerge

Example of a merge with file upload field configuration. 

```json
{
  "merge": [
    {
      "data": [
        {
          "_fields": [
            {
              "api_name": "Image_Upload_1",
              "_data": [
                {
                  "id": "5364788765222"
                }
              ]
            }
          ],
          "id": "111111000000116110"
        }
      ],
      "master_record_fields": [
        {
          "api_name": "Image_Upload_1",
          "_data": [
            {
              "id": "5364788765222"
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — FileDeleteMerge

Example of merge operation with file deletion. 

```json
{
  "merge": [
    {
      "data": [
        {
          "_fields": [
            {
              "api_name": "Company"
            }
          ],
          "id": "111111000000116110"
        }
      ],
      "master_record_fields": [
        {
          "api_name": "Image_Upload_1",
          "_data": null
        }
      ]
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — MergeCompleted

Example of merge operation completed successfully.

```json
{
  "merge": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000116112"
      },
      "message": "The records has been merged successfully",
      "status": "success"
    }
  ]
}
```

### Status `201` — `application/json` — MergeScheduled

Example of merge operation scheduled for processing.

```json
{
  "merge": [
    {
      "code": "SCHEDULED",
      "details": {
        "job_id": "1234567890"
      },
      "message": "The records have been scheduled in a scheduler",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MasterRecordNotAvailable

Example of master record ID is not available.

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

Example of child record ID is empty or not available.

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

### Status `400` — `application/json` — InvalidModule

Example of invalid module name provided.

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

### Status `400` — `application/json` — RecordAlreadyBeingMerged

Example of record is already being merged.

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

Example of closing date is mentioned for deals module.

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

Example of stage being mentioned when child and master record have different pipelines.

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

Example of Expected Revenue and Probability fields are mentioned.

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

Example of closed deal is mentioned in the request body to merge.

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

Example of all mentioned record IDs are the same.

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

Example of one particular field is mentioned more than once.

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

Example of merge array size is larger than one.

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNameNotMentioned

Example of API name of a field that is not mentioned.

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

Example of the data size array more than 2.

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

Example of API name being not mentioned in master_record_fields array.

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

Example of data array being not mentioned or empty.

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

Example of File/Image upload field being mentioned in master record but _data array not given.

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

Example of File/Image upload field being mentioned in data array but _data array not given.

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

Example of records being associated with CPQ rules.

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

Example of total size of files/images in a field exceeding maximum upload size.

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

Example of providing only Reporting To for child record.

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

Example of configuring Reporting To for child and Account for master (or vice versa).

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
