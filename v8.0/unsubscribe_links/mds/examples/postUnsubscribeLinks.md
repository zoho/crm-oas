# Examples: postUnsubscribeLinks

**POST /settings/unsubscribe_links**

## Request examples

### `application/json` — SamplePostRequest

Sample request body for creating an unsubscribe link

```json
{
  "unsubscribe_links": [
    {
      "name": "Unsubscribe",
      "custom_location_url": "https://www.zoho.com/crm/developer/docs/api/v8/create-unsubscribe-link.html",
      "standard_page_message": "standard message",
      "submission_redirect_url": "https://www.zoho.com/crm/developer/docs/api/v8/create-unsubscribe-link.html",
      "submission_message": "display message",
      "page_type": "standard",
      "submission_action_type": "display_message"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success201

Success response for status 201

```json
{
  "unsubscribe_links": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000115581"
      },
      "message": "Unsubscribe Link created successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error: invalid body

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonobject"
  },
  "message": "body",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

MANDATORY_NOT_FOUND error: required field not found (unsubscribe_links)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "unsubscribe_links",
        "json_path": "$.unsubscribe_links"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

INVALID_DATA error: invalid data (unsubscribe_links)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "unsubscribe_links",
    "json_path": "$.unsubscribe_links"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

DUPLICATE_DATA error: Unsubscribe Link name already exists

```json
{
  "unsubscribe_links": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.unsubscribe_links[0].name"
      },
      "message": "Unsubscribe Link name already exists",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse1

LIMIT_EXCEEDED error: Unsubscribe Link limit exceeded

```json
{
  "unsubscribe_links": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 10,
        "limit_due_to": [
          {
            "api_name": "unsubscribe_links",
            "json_path": "$.unsubscribe_links"
          }
        ]
      },
      "message": "Unsubscribe Link limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

INVALID_DATA error: invalid data (custom_location_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "website",
        "api_name": "custom_location_url",
        "json_path": "$.unsubscribe_links[0].custom_location_url"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

INVALID_DATA error: invalid data (submission_redirect_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "website",
        "api_name": "submission_redirect_url",
        "json_path": "$.unsubscribe_links[0].submission_redirect_url"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

MANDATORY_NOT_FOUND error: required field not found (name)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.unsubscribe_links[0].name"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

MANDATORY_NOT_FOUND error: required field not found (page_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "page_type",
        "json_path": "$.unsubscribe_links[0].page_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

MANDATORY_NOT_FOUND error: required field not found (name) - empty string

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.unsubscribe_links[0].name"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse5

MANDATORY_NOT_FOUND error: required field not found (page_type) - empty string

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "page_type",
        "json_path": "$.unsubscribe_links[0].page_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse6

MANDATORY_NOT_FOUND error: required field not found (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

DEPENDENT_FIELD_MISSING error: required field not found (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "submission_redirect_url",
          "json_path": "$.unsubscribe_links[0].submission_redirect_url"
        },
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse2

DEPENDENT_FIELD_MISSING error: required field not found (page_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "standard_page_message",
          "json_path": "$.unsubscribe_links[0].standard_page_message"
        },
        "api_name": "page_type",
        "json_path": "$.unsubscribe_links[0].page_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse3

DEPENDENT_FIELD_MISSING error: required field not found (page_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "custom_location_url",
          "json_path": "$.unsubscribe_links[0].custom_location_url"
        },
        "api_name": "page_type",
        "json_path": "$.unsubscribe_links[0].page_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse4

DEPENDENT_FIELD_MISSING error: required field not found (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "submission_message",
          "json_path": "$.unsubscribe_links[0].submission_message"
        },
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse7

MANDATORY_NOT_FOUND error: Required field is missing (name)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "details": {
        "api_name": "name",
        "json_path": "$.unsubscribe_links[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

MANDATORY_NOT_FOUND error: required field not found (name)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

INVALID_DATA error: Invalid data type (name)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.unsubscribe_links[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

INVALID_DATA error: Invalid data (name)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "name",
        "minimum_length": 1,
        "json_path": "$.unsubscribe_links[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

MANDATORY_NOT_FOUND error: Required field is missing (page_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "custom_location_url",
        "expected_data_type": "website",
        "json_path": "$.unsubscribe_links[*].custom_location_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

INVALID_DATA error: Invalid data type (page_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "custom_location_url",
        "maximum_length": 250,
        "json_path": "$.unsubscribe_links[*].custom_location_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

INVALID_DATA error: Invalid data type (custom_location_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "standard_page_message",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].standard_page_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

INVALID_DATA error: Invalid data (custom_location_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "standard_page_message",
        "maximum_length": 2000,
        "json_path": "$.unsubscribe_links[*].standard_page_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

INVALID_DATA error: Invalid data type (standard_page_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_redirect_url",
        "expected_data_type": "website",
        "json_path": "$.unsubscribe_links[*].submission_redirect_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

INVALID_DATA error: Invalid data (standard_page_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_redirect_url",
        "maximum_length": 250,
        "json_path": "$.unsubscribe_links[*].submission_redirect_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

INVALID_DATA error: Invalid data type (submission_redirect_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_message",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].submission_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

INVALID_DATA error: Invalid data (submission_redirect_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_message",
        "maximum_length": 2000,
        "json_path": "$.unsubscribe_links[*].submission_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse8

MANDATORY_NOT_FOUND error: Required field is missing (page_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "details": {
        "api_name": "page_type",
        "json_path": "$.unsubscribe_links[*].page_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

INVALID_DATA error: Invalid data type (submission_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "page_type",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].page_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

INVALID_DATA error: Invalid data (submission_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "page_type",
        "maximum_length": 8,
        "json_path": "$.unsubscribe_links[*].page_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse18

INVALID_DATA error: Invalid data (page_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "page_type",
        "supported_values": [
          "standard",
          "custom"
        ],
        "json_path": "$.unsubscribe_links[*].page_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse5

DEPENDENT_FIELD_MISSING error: Dependent field is missing (custom_location_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "page_type",
          "json_path": "$.unsubscribe_links[*].page_type"
        },
        "api_name": "custom_location_url",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.custom_location_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse6

DEPENDENT_FIELD_MISSING error: Dependent field is missing (standard_page_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "page_type",
          "json_path": "$.unsubscribe_links[*].page_type"
        },
        "api_name": "standard_page_message",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.standard_page_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse9

MANDATORY_NOT_FOUND error: Required field is missing (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "details": {
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[*].submission_action_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse19

INVALID_DATA error: Invalid data type (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_action_type",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].submission_action_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse20

INVALID_DATA error: Invalid data (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_action_type",
        "maximum_length": 15,
        "json_path": "$.unsubscribe_links[*].submission_action_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse21

INVALID_DATA error: unsupported submission_action_type value

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_action_type",
        "supported_values": [
          "display_message",
          "redirect"
        ],
        "json_path": "$.unsubscribe_links[*].submission_action_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse7

DEPENDENT_FIELD_MISSING error: Dependent field is missing (submission_redirect_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "submission_action_type",
          "json_path": "$.unsubscribe_links[*].submission_action_type"
        },
        "api_name": "submission_redirect_url",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.submission_redirect_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse8

DEPENDENT_FIELD_MISSING error: Dependent field is missing (submission_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "submission_action_type",
          "json_path": "$.unsubscribe_links[*].submission_action_type"
        },
        "api_name": "submission_message",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.submission_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — MandatoryNotFoundResponse1

MANDATORY_NOT_FOUND error in 403 response: required field not found (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```
