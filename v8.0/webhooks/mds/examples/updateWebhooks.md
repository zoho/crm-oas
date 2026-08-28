# Examples: updateWebhooks

**PUT /settings/automation/webhooks**

## Request examples

### `application/json` — SamplePutRequest

Bulk update request for a webhook with all required fields

```json
{
  "webhooks": [
    {
      "headers": {
        "module_parameters": [
          {
            "name": "lead_email",
            "value": "${!Leads.Email}"
          },
          {
            "name": "lead_id",
            "value": "${!Leads.Id}"
          },
          {
            "name": "lead_owner",
            "value": "${!Leads.Owner}"
          }
        ],
        "custom_parameters": [
          {
            "name": "source",
            "value": "website"
          },
          {
            "name": "version",
            "value": "1.0"
          }
        ]
      },
      "module": {
        "api_name": "Leads",
        "id": "5725767000000002175"
      },
      "description": "Protected Data",
      "body": {
        "raw_data_content": "{\n  \"lead_id\": \"${!Leads.Id}\",\n  \"email\": \"${!Leads.Email}\",\n  \"owner\": \"${!Leads.Owner}\",\n  \"source\": \"website\",\n  \"version\": \"1.0\"\n}",
        "format": "JSON",
        "type": "raw"
      },
      "url": "https://webhook.site/3588de27-e3bd-4237-894b-f140143f3d99",
      "feature_type": "workflow",
      "http_method": "POST",
      "name": "Zoho's Data",
      "authentication": {
        "type": "general"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful webhook update response

```json
{
  "webhooks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "5725767000007098001"
      },
      "message": "webhook updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error for invalid module.ID value

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].module.id"
      },
      "message": "the module id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse1

Ambiguity error when module ID and api_name conflict

```json
{
  "webhooks": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.webhooks[0].module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.webhooks[0].module.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

INVALID_DATA error for special characters in webhook name

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name"
      },
      "message": "Special characters not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

INVALID_DATA name length exceeded error for webhook name

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 250,
        "api_name": "name",
        "json_path": "$.webhooks[0].name"
      },
      "message": "The lenght of name has exceeded the limit",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

INVALID_DATA error for unsupported http_method value

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "http_method",
        "json_path": "$.webhooks[0].http_method"
      },
      "message": "The method type given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

INVALID_DATA error for invalid webhook URL

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "url",
        "json_path": "$.webhooks[0].url"
      },
      "message": "please enter a valid URL",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

INVALID_DATA error for invalid date_format value

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "date_format",
        "json_path": "$.webhooks[0].date_time_format.date_format"
      },
      "message": "The Date given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

INVALID_DATA error for invalid time_zone value

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "time_zone",
        "json_path": "$.webhooks[0].date_time_format.time_zone"
      },
      "message": "The timezone given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

INVALID_DATA error for invalid datetime_format value

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "datetime_format",
        "json_path": "$.webhooks[0].date_time_format.datetime_format"
      },
      "message": "The date time format given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

INVALID_DATA error for invalid webhook ID in the request body

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].id"
      },
      "message": "The ID given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

INVALID_DATA error for unsupported merge field in headers

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "value",
        "json_path": "$.webhooks[0].headers.module_parameters[0].value"
      },
      "message": "Unsupported fields are present",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

Duplicate parameter name error in module_parameters

```json
{
  "webhooks": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[0].headers.module_parameters[1].name"
      },
      "message": "duplicate parameter name found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

Dependent mismatch error for incompatible authentication type

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "connection_name",
          "json_path": "$.webhooks[0].authentication.connetion_name"
        },
        "api_name": "type",
        "json_path": "$.webhooks[0].authentication.type"
      },
      "message": "provide appropriate authentication type",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

MANDATORY_NOT_FOUND error for missing required field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "value",
        "json_path": "$.webhooks[0].headers.custom_parameters[0].value"
      },
      "message": "the given parameter is invalid, specify both name and value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

MANDATORY_NOT_FOUND error for missing parameter name or value

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[0].headers.module_parameters[0].name"
      },
      "message": "the given parameter is invalid, specify both name and value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

MANDATORY_NOT_FOUND error for missing http_method field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "http_method",
        "json_path": "$.webhooks[0].http_method"
      },
      "message": "The method type is not given ",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

INVALID_DATA error for invalid authentication.connection_name

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "connection_name",
        "json_path": "$.webhooks[0].authentication.connetion_name"
      },
      "message": "Please provide valid connection name",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

Dependent mismatch error for incompatible HTTP method and headers

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "headers",
          "json_path": "$.webhooks[0].headers"
        },
        "api_name": "http_method",
        "json_path": "$.webhooks[0].http_method"
      },
      "message": "Invalid value provided for the given http method",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

NOT_ALLOWED error for editing a read-only webhook

```json
{
  "webhooks": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].id"
      },
      "message": "Insufficient privileges to edit Read only webhook",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse2

NOT_ALLOWED error for modifying a Marketplace-associated webhook

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "Webhook  is associated with MarketPlace",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse12

INVALID_DATA type error for headers field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "headers",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].headers"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

INVALID_DATA length error for headers field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "headers",
        "maximum_length": 2,
        "json_path": "$.webhooks[*].headers"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response1

MANDATORY_NOT_FOUND error for missing headers.module_parameters field

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "module_parameters",
      "json_path": "$.webhooks[*].headers.module_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response2

INVALID_DATA type error for headers.module_parameters field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "module_parameters",
      "expected_data_type": "jsonarray",
      "json_path": "$.webhooks[*].headers.module_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response3

INVALID_DATA length error for headers.module_parameters field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "module_parameters",
      "maximum_length": 3,
      "json_path": "$.webhooks[*].headers.module_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse14

INVALID_DATA type error for headers.module_parameters name field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.module_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

INVALID_DATA length error for headers.module_parameters name field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 10,
        "json_path": "$.webhooks[*].headers.module_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

INVALID_DATA type error for headers.module_parameters value field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.module_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

INVALID_DATA length error for headers.module_parameters value field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 15,
        "json_path": "$.webhooks[*].headers.module_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response4

INVALID_DATA type error for headers.custom_parameters field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "custom_parameters",
      "expected_data_type": "jsonarray",
      "json_path": "$.webhooks[*].headers.custom_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response5

INVALID_DATA length error for headers.custom_parameters field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "custom_parameters",
      "maximum_length": 2,
      "json_path": "$.webhooks[*].headers.custom_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse18

INVALID_DATA type error for headers.custom_parameters name field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.custom_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse19

INVALID_DATA length error for headers.custom_parameters name field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 6,
        "json_path": "$.webhooks[*].headers.custom_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse20

INVALID_DATA type error for headers.custom_parameters value field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.custom_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse21

INVALID_DATA length error for headers.custom_parameters value field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 7,
        "json_path": "$.webhooks[*].headers.custom_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

MANDATORY_NOT_FOUND error for missing module field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "module",
        "json_path": "$.webhooks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse22

INVALID_DATA type error for module field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse23

INVALID_DATA length error for module field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "module",
        "maximum_length": 2,
        "json_path": "$.webhooks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response6

INVALID_DATA type error for module.api_name field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "api_name",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].module.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response7

INVALID_DATA length error for module.api_name field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "api_name",
      "maximum_length": 5,
      "json_path": "$.webhooks[*].module.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response8

INVALID_DATA type error for module.ID field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.webhooks[*].module.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response9

INVALID_DATA length error for module.ID field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.webhooks[*].module.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse24

INVALID_DATA type error for description field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse25

INVALID_DATA length error for description field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 250,
        "json_path": "$.webhooks[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse26

INVALID_DATA type error for body field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "body",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].body"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse27

INVALID_DATA length error for body field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "body",
        "maximum_length": 3,
        "json_path": "$.webhooks[*].body"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response10

INVALID_DATA type error for body.raw_data_content field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "raw_data_content",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].body.raw_data_content"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response11

INVALID_DATA length error for body.raw_data_content field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "raw_data_content",
      "maximum_length": 500,
      "json_path": "$.webhooks[*].body.raw_data_content"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response12

MANDATORY_NOT_FOUND error for missing body.format field

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "format",
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response13

INVALID_DATA type error for body.format field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "format",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response14

INVALID_DATA length error for body.format field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "format",
      "maximum_length": 4,
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response15

INVALID_DATA unsupported value error for body.format field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "format",
      "supported_values": [
        "JSON",
        "XML",
        "Text",
        "HTML"
      ],
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response16

MANDATORY_NOT_FOUND error for missing body.type field

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "type",
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response17

INVALID_DATA type error for body.type field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "type",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response18

INVALID_DATA length error for body.type field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "maximum_length": 10,
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response19

INVALID_DATA unsupported value error for body.type field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "supported_values": [
        "form_data",
        "raw"
      ],
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse5

MANDATORY_NOT_FOUND error for missing url field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "url",
        "json_path": "$.webhooks[*].url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse28

INVALID_DATA type error for url field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "url",
        "expected_data_type": "website",
        "json_path": "$.webhooks[*].url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse29

INVALID_DATA length error for url field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "url",
        "maximum_length": 57,
        "json_path": "$.webhooks[*].url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse6

MANDATORY_NOT_FOUND error for missing feature_type field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "feature_type",
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse30

INVALID_DATA type error for feature_type field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "feature_type",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse31

INVALID_DATA length error for feature_type field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "feature_type",
        "maximum_length": 20,
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse7

MANDATORY_NOT_FOUND error for missing http_method field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "http_method",
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse32

INVALID_DATA type error for http_method field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "http_method",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse33

INVALID_DATA length error for http_method field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "http_method",
        "maximum_length": 4,
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse8

MANDATORY_NOT_FOUND error for missing name field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse34

INVALID_DATA type error for name field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse35

INVALID_DATA length error for name field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 11,
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse9

MANDATORY_NOT_FOUND error for missing authentication field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "authentication",
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse36

INVALID_DATA type error for authentication field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "authentication",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse37

INVALID_DATA length error for authentication field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "authentication",
        "maximum_length": 1,
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response20

MANDATORY_NOT_FOUND error for missing authentication.type field

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "type",
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response21

INVALID_DATA type error for authentication.type field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "type",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response22

INVALID_DATA length error for authentication.type field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "maximum_length": 7,
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response23

INVALID_DATA unsupported value error for authentication.type field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "supported_values": [
        "general"
      ],
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

### Status `403` — `application/json` — NoPermissionResponse1

NO_PERMISSION error for missing Manage Workflow profile permission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
