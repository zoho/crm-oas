# Examples: updateServiceSById

**PUT /Services__s/{id}**

## Request examples

### `application/json` — SamplePutRequest

Service update with availability, status, and pricing fields.

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
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful single service record update.

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
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA on Availability_Type value not found in picklist.

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

DEPENDENT_MISMATCH when Available_Days not within configured business days.

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

To field violates business timing for the given Status.

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

INVALID_DATA error for Available_Dates due to date format mismatch.

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

Duration does not satisfy service timing for the given Status.

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

DEPENDENT_FIELD_MISSING when Unavailable_From required when Status is Temporarily Unavailable.

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

LIMIT_EXCEEDED error for Members exceeding the 100-user association cap.

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

LIMIT_EXCEEDED error for Status breaching the 500 active services limit.

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

DEPENDENT_MISMATCH on Job_Sheet_Section__s requiring Job_Sheet_Required as Yes.

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

DEPENDENT_MISMATCH on Available_Till where To value must exceed Available_From.

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

DEPENDENT_MISMATCH on Available_Dates falling on a holiday or non-business day.

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

INVALID_DATA error for Members record because member is not Confirmed.

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

INVALID_DATA error for Members record because member is not Active.

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

INVALID_DATA error for Job_Sheet_Required due to incorrect data type.

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

INVALID_DATA error for Job_Sheet_Required due to an invalid value.

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

### Status `400` — `application/json` — DependentMismatchResponse10

Status available but Unavailable_From is not a future date.

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

Unavailable_Till is not greater than the current time

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

Status available with invalid Unavailable_Till null/value combination.

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

Unavailable_Till is not lesser than Unavailable_From.

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

Unavailable_Till set on a scheduled service with Available_From.

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

Status Not In Use conflicts with a future Unavailable_From date.

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

Status Scheduled but Available_From is a past date

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

Status conflicts with an expired Available_Till date

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

INVALID_DATA error for Unavailable_From outside service availability window.

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

DEPENDENT_FIELD_MISSING when Available_Days required when Availability_Type is Specific Day(s).

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

INVALID_DATA error for the data field with a null or unprocessable value.

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

INVALID_DATA error for Status field due to incorrect data type.

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

INVALID_DATA on Status field containing an unacceptable value.

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

INVALID_DATA on Unavailable_Till field containing a malformed value.

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

INVALID_DATA on Duration outside the permitted range.

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

NOT_ALLOWED error for Job_Sheet_Required when Job Sheet is unconfigured.

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

NOT_ALLOWED error for Status when service availability configuration is invalid.

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

### Status `403` — `application/json` — NotAllowedResponse1

NOT_ALLOWED error when caller lacks permission to update the service.

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
