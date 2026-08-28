# Examples: updateServicesS

**PUT /Services__s**

## Request examples

### `application/json` — SamplePutRequest

Update two services with mixed availability types and date range constraints.


```json
{
  "data": [
    {
      "Job_Sheet_Required": "No",
      "Owner": {
        "name": "Madeshwaran G",
        "id": "4671651000000635001",
        "email": "madeshwaran.g@zohocorp.com"
      },
      "Description": null,
      "Available_Days": [
        "Monday",
        "Tuesday",
        "Wednesday"
      ],
      "Tax": [],
      "Unavailable_From": "2026-01-13T15:40:03+05:30",
      "Record_Image": null,
      "id": "4671651000000862030",
      "Available_Dates": [],
      "Status": "Not in Use",
      "Available_Timings": null,
      "Service_Name": "service99",
      "Available_From": "2026-01-13",
      "Available_Till": "2026-01-13",
      "Duration": 30,
      "Job_Sheet_Section__s": null,
      "Price": 3993,
      "Tag": [],
      "Availability_Type": "Specific Day(s)",
      "Members": [
        {
          "id": "4671651000000862031",
          "Members": {
            "module": "Users",
            "name": "Madeshwaran G",
            "id": "4671651000000635001"
          }
        }
      ],
      "Location": "Business Address",
      "Unavailable_Till": null
    },
    {
      "Job_Sheet_Required": "No",
      "Owner": {
        "name": "Madeshwaran G",
        "id": "4671651000000635001",
        "email": "madeshwaran.g@zohocorp.com"
      },
      "Description": null,
      "Available_Days": [],
      "Tax": [],
      "Unavailable_From": "2026-01-14T12:20:35+05:30",
      "Record_Image": null,
      "id": "4671651000000867004",
      "Available_Dates": [],
      "Status": "Not in Use",
      "Available_Timings": null,
      "Service_Name": "dd",
      "Available_From": "2026-01-01",
      "Available_Till": "2026-01-29",
      "Duration": 120,
      "Job_Sheet_Section__s": null,
      "Price": 44,
      "Tag": [],
      "Availability_Type": "Specific Date Range",
      "Members": [
        {
          "id": "4671651000000867005",
          "Members": {
            "module": "Users",
            "name": "Madeshwaran G",
            "id": "4671651000000635001"
          }
        }
      ],
      "Location": "Business Address",
      "Unavailable_Till": null
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

All service records updated successfully with audit metadata and affected_data.


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-14T16:57:16+05:30",
        "Modified_By": {
          "name": "Madeshwaran G",
          "id": "4671651000000635001"
        },
        "Created_Time": "2025-12-16T17:04:11+05:30",
        "id": "4671651000000862030",
        "Created_By": {
          "name": "Madeshwaran G",
          "id": "4671651000000635001"
        },
        "affected_data": [
          {
            "$process_flow": false,
            "id": "4671651000000862030"
          }
        ]
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-14T16:57:16+05:30",
        "Modified_By": {
          "name": "Madeshwaran G",
          "id": "4671651000000635001"
        },
        "Created_Time": "2025-12-17T12:20:24+05:30",
        "id": "4671651000000867004",
        "Created_By": {
          "name": "Madeshwaran G",
          "id": "4671651000000635001"
        },
        "affected_data": [
          {
            "$process_flow": false,
            "id": "4671651000000867004"
          }
        ]
      },
      "message": "record updated",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Partial success with one record updated and one INVALID_DATA error on Duration.


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-14T17:25:57+05:30",
        "Modified_By": {
          "name": "Madeshwaran G",
          "id": "4671651000000635001"
        },
        "Created_Time": "2025-12-16T17:04:11+05:30",
        "id": "4671651000000862030",
        "Created_By": {
          "name": "Madeshwaran G",
          "id": "4671651000000635001"
        },
        "affected_data": [
          {
            "$process_flow": false,
            "id": "4671651000000862030"
          }
        ]
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Duration",
        "json_path": "$.data[1].Duration"
      },
      "message": "Duration value should not be greater than 24hrs or less than 5mins",
      "status": "error",
      "error_meta": "invalid_field"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid data error when Availability_Type is not a valid picklist value.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Availability_Type",
        "json_path": "$.data[0].Availability_Type"
      },
      "message": "The given Availability Type is not in picklist",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

An error when Available_Days values not within configured business days.


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Available_Days",
        "json_path": "$.data[0].Available_Days"
      },
      "message": "The given Available Days are not there in business days",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

Dependent mismatch when Available_Timings To value fails business timing

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "To",
        "json_path": "$.data[0].Available_Timings[0].To"
      },
      "message": "Service available time does not satisfy the business timing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Invalid data error when an Available_Dates value has an invalid format

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "date",
        "api_name": "Available_Dates",
        "json_path": "$.data[0].Available_Dates"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse3

Dependent mismatch when Duration does not satisfy service timing

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Duration",
        "json_path": "$.data[0].Duration"
      },
      "message": "Duration does not satisfy the service timing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

DEPENDENT_FIELD_MISSING error when Unavailable_From is absent and Status is its dependee.


```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_From",
        "json_path": "$.data[0].Unavailable_From"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse1

LIMIT_EXCEEDED error when more than five members are associated with a service

```json
{
  "data": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "Members",
        "limit": 100,
        "json_path": "$.data[0].Members"
      },
      "message": "More than 100 users cannot be associated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse2

LIMIT_EXCEEDED error when the 500-active-service limit for the organization is reached

```json
{
  "data": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "Status",
        "limit": 3,
        "json_path": "$.data[0].Status"
      },
      "message": "You cannot create more than 500 active services",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse7

Dependent mismatch when Job_Sheet_Section__s requires Job_Sheet_Required is Yes

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Job_Sheet_Required",
          "json_path": "$.data[0].Job_Sheet_Required"
        },
        "api_name": "Job_Sheet_Section__s",
        "json_path": "$.data[0].Job_Sheet_Section__s"
      },
      "message": "Job_Sheet_Section__s can have value only when value of Job_Sheet_Required is Yes",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse8

Dependent mismatch when Available_Timings To must be greater than From.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_From",
          "json_path": "$.data[0].Available_From"
        },
        "api_name": "Available_Till",
        "json_path": "$.data[0].Available_Till"
      },
      "message": "To value must be Greater than From value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse9

Dependent mismatch when Available_Dates falls on a holiday or non-business day.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Available_Dates",
        "json_path": "$.data[0].Available_Dates"
      },
      "message": "Available Dates value in holiday or Not in BusinessDays",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Invalid data error when a Members entry is an unconfirmed user

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "user_status": "unconfirmed",
        "api_name": "id",
        "json_path": "$.data[0].Members[0].Members.id"
      },
      "message": "Members is not Confirmed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Invalid data error when a Members entry is an inactive user

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "user_status": "inactive",
        "api_name": "id",
        "json_path": "$.data[0].Members[0].Members.id"
      },
      "message": "Members is not Active",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Invalid data type error for the Job_Sheet_Required field

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "Job_Sheet_Required",
        "expected_data_type": "text",
        "json_path": "$.data[*].Job_Sheet_Required"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Invalid data error for the Available_Timings request payload.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Job_Sheet_Required",
        "maximum_length": 3,
        "json_path": "$.data[*].Job_Sheet_Required"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

MANDATORY_NOT_FOUND error when a required service field is missing from the request

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.data[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse10

An error when Unavailable_From violates null rule when status is Available.


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_From",
          "json_path": "$.data[0].Unavailable_From"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "When the service status is available, Unavailable From must be greater than current date",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse11

An error when Unavailable_Till not greater than current time


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Unavailable Till must be greater than current Time.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse12

An error when invalid Unavailable_Till supplied when status is Available


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_Till",
          "json_path": "$.data[0].Unavailable_Till"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "When the service status is available,  either both Unavailable From and Unavailable Till must be null, or only Unavailable From can have a value.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse13

Dependent mismatch when Unavailable Till must be before Unavailable From


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_From",
          "json_path": "$.data[0].Unavailable_From"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Unavailable Till must be lesser than Unavailable From",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse14

Dependent mismatch when past Available_From blocks Available/Scheduled status


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_From",
          "json_path": "$.data[0].Available_From"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Service status cannot be marked as Not In Use or Temporarily Unavailable for scheduled services.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse15

Dependent mismatch when past Available_Till blocks Available/Scheduled status


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_From",
          "json_path": "$.data[0].Unavailable_From"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Services status cannot be marked as Not In Use when Unavailable From falls after the current Date",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse16

Dependent mismatch when past Available_From prevents Scheduled status


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_From",
          "json_path": "$.data[0].Available_From"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Starting date of service availability falls before the current Date, so service cannot be marked as Scheduled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse17

Dependent mismatch when past Available_Till blocks Available/Scheduled/Temp Unavailable


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_Till",
          "json_path": "$.data[0].Available_Till"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "End Date of service availability falls before the current Date, so service cannot be marked as Available or Scheduled or Temporarily Unavailable",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Invalid data error when Unavailable_From falls outside the service availability window.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Unavailable_From",
        "json_path": "$.data[0].Unavailable_From"
      },
      "message": "Unavailable From time does not fall within service availability",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse2

An error when Available_From missing when Availability_Type is Specific Date Range


```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Invalid data error when an Available_Dates value falls on a holiday or non-business day

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "data",
    "json_path": "$.data"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Invalid data type error for the Status field

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "Status",
        "expected_data_type": "text",
        "json_path": "$.data[*].Status"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Invalid data error when Available_From has an invalid date format.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Status",
        "maximum_length": 120,
        "json_path": "$.data[*].Status"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Invalid data error when Available_Till has an invalid date format.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Unavailable_Till",
        "supported_values": [
          "Temporarily Unavailable",
          "Available",
          "Not In Use",
          "Scheduled"
        ],
        "json_path": "$.data[*].Unavailable_Till"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Invalid data error when Duration is outside the permitted 5-min to 24-hr range.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Duration",
        "json_path": "$.data[0].Duration"
      },
      "message": "Duration value should not be greater than 24hrs or less than 5mins",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

NOT_ALLOWED error when Job Sheet is not configured in service preferences

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Job_Sheet_Required",
        "json_path": "$.data[0].Job_Sheet_Required"
      },
      "message": "Job Sheet is not configured in services preferences",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse2

NOT_ALLOWED error when past availability dates prevent an Active or Temporarily Unavailable status change

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "As service availability is not valid, status cannot be changed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

MANDATORY_NOT_FOUND error when another required field is absent from the request

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "Members",
        "json_path": "$.data[0].Members"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

MANDATORY_NOT_FOUND error when a third required field is absent from the request

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "Location",
        "json_path": "$.data[*].Location"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

Invalid data error when Available_Timings From or To is not in HH:MM format.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "To",
        "json_path": "$.data[0].Available_Timings"
      },
      "message": " The given custom time is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

Invalid data type error for the Owner field

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "Owner",
        "expected_data_type": "jsonobject",
        "json_path": "$.data[*].Owner"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

Invalid data error when Available_Till has an invalid value

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Owner",
        "maximum_length": 1,
        "json_path": "$.data[*].Owner"
      },
      "status": "error"
    }
  ]
}
```
