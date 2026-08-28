# Examples: updateAppointmentsS

**PUT /Appointments__s**

## Request examples

### `application/json` — SamplePutRequest

PUT request body with two appointment objects for update


```json
{
  "data": [
    {
      "Appointment_Name": "service06 - ll",
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "ll",
        "id": "111115000000120725"
      },
      "Service_Name": {
        "name": "service06",
        "id": "111115000000127506"
      },
      "Appointment_Start_Time": "2026-01-16T18:00:00+05:30",
      "Location": "Business Address",
      "Address": null,
      "Owner": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Additional_Information": null,
      "Remind_At": [
        {
          "unit": 1,
          "period": "hours"
        }
      ],
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Created_Time": "2026-01-16T16:50:29+05:30",
      "Modified_Time": "2026-01-19T16:12:24+05:30",
      "Tag": [],
      "Status": "Overdue",
      "Last_Activity_Time": "2026-01-19T16:12:24+05:30",
      "Rescheduled_From": null,
      "Reschedule_Reason": null,
      "Reschedule_Note": null,
      "Rescheduled_By": null,
      "Rescheduled_Time": null,
      "Cancelled_By": null,
      "Cancellation_Reason": null,
      "Cancellation_Note": null,
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": null,
      "Job_Sheet_Name__s": null,
      "Job_Sheet_Description__s": null,
      "Date_1": null,
      "Reschedule_Count": 0,
      "Appointment_End_Time": "2026-01-16T18:30:00+05:30",
      "Duration": 30
    },
    {
      "Appointment_Name": "service06 - ll",
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "ll",
        "id": "111115000000120725"
      },
      "Service_Name": {
        "name": "service06",
        "id": "111115000000127506"
      },
      "Appointment_Start_Time": "2026-01-16T18:00:00+05:30",
      "Location": "Business Address",
      "Address": null,
      "Owner": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Additional_Information": null,
      "Remind_At": [
        {
          "unit": 1,
          "period": "hours"
        }
      ],
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Created_Time": "2026-01-16T16:50:29+05:30",
      "Modified_Time": "2026-01-19T16:12:24+05:30",
      "Tag": [],
      "Status": "Overdue",
      "Last_Activity_Time": "2026-01-19T16:12:24+05:30",
      "Rescheduled_From": null,
      "Reschedule_Reason": null,
      "Reschedule_Note": null,
      "Rescheduled_By": null,
      "Rescheduled_Time": null,
      "Cancelled_By": null,
      "Cancellation_Reason": null,
      "Cancellation_Note": null,
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": null,
      "Job_Sheet_Name__s": null,
      "Job_Sheet_Description__s": null,
      "Date_1": null,
      "Reschedule_Count": 0,
      "Appointment_End_Time": "2026-01-16T18:30:00+05:30",
      "Duration": 30,
      "Rescheduled_To": null
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful update of two appointment records


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-19T17:42:07+05:30",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T16:50:29+05:30",
        "id": "111115000000147279",
        "Created_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-19T17:42:07+05:30",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T14:11:13+05:30",
        "id": "111115000000147238",
        "Created_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        }
      },
      "message": "record updated",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Multi-status response with one success and one invalid-ID error.


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-19T17:45:52+05:30",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T16:50:29+05:30",
        "id": "111115000000147279",
        "Created_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.data[1].id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error when required Appointment_For field is missing.


```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "Appointment_For",
        "json_path": "$.data[2].Appointment_For"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldUnchangedResponse1

Error when Rescheduled_From matches the existing appointment start time.


```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_UNCHANGED",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Reschedule_From and Appointment_Start_Time cannot be same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldUnchangedResponse2

Error when reschedule information fields change without a prior reschedule.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_UNCHANGED",
      "details": {
        "dependee": {
          "api_name": "Reschedule_Reason",
          "json_path": "$.data[0].Reschedule_Reason"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Reschedule the appointment atleast once to Update the fields of Reschedule Information Section",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

Error when Reschedule_Reason is set but Rescheduled_From is empty.


```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Reschedule_Reason",
          "json_path": "$.data[0].Reschedule_Reason"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Rescheduled_From cannot be empty",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse2

Error when cancellation fields are set but Status is not Cancelled.


```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Cancellation_Reason",
          "json_path": "$.data[0].Cancellation_Reason"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "To Update the fields of Cancellation Information Section, value of Status should be Cancelled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Error when Service_Name is unavailable at the appointment time.


```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Appointment_Start_Time",
        "json_path": "$.data[0].Appointment_Start_Time"
      },
      "message": "Service is not available on the given time",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse2

Error when Appointment_Start_Time is outside business hours.


```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Appointment_Start_Time",
        "json_path": "$.data[0].Appointment_Start_Time"
      },
      "message": "Appointment time does not falls under business hours",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

Error when appointment owner is not a member of the service


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Services.Members",
          "json_path": "$.data[0].Services.Members"
        },
        "api_name": "id",
        "json_path": "$.data[0].Owner.id"
      },
      "message": "Appointment Owner is not a part of Service Members",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid data error for Appointment_For module format.


```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonobject",
        "api_name": "module",
        "json_path": "$.data[0].Appointment_For.module"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Invalid data error for unknown module API name in Appointment_For.


```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.data[0].Appointment_For.module.api_name"
      },
      "message": "the given module name is not exist in multimodulelookup",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse3

Error when appointment is completed without a job sheet.


```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as completed without creating the jobsheet",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

Error when Status is set to Completed before appointment end time.


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as completed before the appointment ends",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse3

Error when a job sheet creation targets an incomplete appointment

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
        "api_name": "Job_Sheet_Name__s",
        "json_path": "$.data[0].Job_Sheet_Name__s"
      },
      "message": "Job Sheet can be created only for completed appointment",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse4

Error when Status is set to Overdue before appointment end time.


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as overdue before the appointment ends",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse5

Error when Appointment_Start_Time is set to a past date or time.


```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be scheduled for past dates",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error when required unit key is missing from Remind_At.


```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "unit",
        "json_path": "$.data[0].Remind_At[0].unit"
      },
      "message": "mandatory key missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Invalid data error when data array exceeds 100-record limit.


```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 4,
    "api_name": "data",
    "json_path": "$.data"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — RecordLockedResponse1

Error when appointment record is locked.


```json
{
  "data": [
    {
      "code": "RECORD_LOCKED",
      "details": {
        "api_name": "id",
        "action": "record_locking",
        "json_path": "$.data[0].id"
      },
      "message": "Sorry, you cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Invalid data error for Remind_At unit field.


```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "integer",
        "api_name": "unit",
        "json_path": "$.data[0].Remind_At[0].unit"
      },
      "message": "INVALID_DATA",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Invalid data error for an invalid appointment ID


```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.data[0].id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionCompleteResponse1

Permission denied to mark appointment as complete


```json
{
  "data": [
    {
      "code": "NO_PERMISSION",
      "details": {
        "permissions": [
          "Crm_Implied_Mark_As_Complete_Appointments"
        ]
      },
      "message": "permission denied",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionRescheduleResponse1

Permission denied to reschedule appointment.


```json
{
  "data": [
    {
      "code": "NO_PERMISSION",
      "details": {
        "permissions": [
          "Crm_Implied_Reschedule_Appointments"
        ]
      },
      "message": "permission denied",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionCancelResponse1

Permission denied to cancel appointment.


```json
{
  "data": [
    {
      "code": "NO_PERMISSION",
      "details": {
        "permissions": [
          "Crm_Implied_Cancel_Appointments"
        ]
      },
      "message": "permission denied",
      "status": "error"
    }
  ]
}
```
