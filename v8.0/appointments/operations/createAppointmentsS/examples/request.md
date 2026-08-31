### `application/json` — SamplePostRequest

Request body with four appointment objects covering varied statuses.

```json
{
  "data": [
    {
      "Status": "Scheduled",
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Service_Name": {
        "name": "service04",
        "id": "111115000000127440"
      },
      "Appointment_Start_Time": "2026-01-29T12:00:00+04:00",
      "Appointment_End_Time": "2026-01-29T12:30:00+04:00",
      "Duration": 30,
      "Appointment_Name": "service04 - bb",
      "Location": "Business Address",
      "Address": null,
      "Owner": {
        "id": "111115000000122075",
        "email": "madeshwaran.g+csez02@zohotest.com",
        "name": "madesh"
      },
      "Additional_Information": null,
      "Remind_At": [
        {
          "unit": 15,
          "period": "minutes"
        }
      ],
      "$currency_symbol": "£",
      "$sharing_permission": "full_access",
      "$state": "save",
      "$editable": true,
      "Tag": [],
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Created_Time": "2026-01-16T09:39:43+04:00",
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Modified_Time": "2026-01-16T09:39:43+04:00",
      "Rescheduled_From": null,
      "Rescheduled_To": null,
      "Reschedule_Reason": null,
      "Rescheduled_Time": null,
      "Reschedule_Count": 0,
      "Rescheduled_By": null,
      "Reschedule_Note": null,
      "Cancellation_Reason": null,
      "Cancellation_Note": null,
      "Cancelled_By": null,
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": null,
      "Record_Status__s": "Available"
    },
    {
      "Owner": {
        "id": "111115000000122075",
        "email": "madeshwaran.g+csez02@zohotest.com",
        "name": "madesh"
      },
      "$currency_symbol": "£",
      "Address": null,
      "Appointment_Start_Time": "2026-01-22T13:00:00+04:00",
      "Cancellation_Reason": null,
      "$field_states": null,
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Rescheduled_To": "2026-01-22T13:00:00+04:00",
      "$sharing_permission": "full_access",
      "Reschedule_Reason": "By Customer",
      "Additional_Information": null,
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": null,
      "Cancellation_Note": null,
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Reschedule_Count": 2,
      "Rescheduled_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Date_1": "2026-01-14",
      "Rescheduled_Time": "2026-01-16T10:29:58+04:00",
      "Remind_At": [
        {
          "unit": 15,
          "period": "minutes"
        }
      ],
      "Appointment_End_Time": "2026-01-22T13:30:00+04:00",
      "Status": "Scheduled",
      "Modified_Time": "2026-01-16T10:29:58+04:00",
      "Service_Name": {
        "name": "service04",
        "id": "111115000000127440"
      },
      "Created_Time": "2026-01-16T09:39:43+04:00",
      "Rescheduled_From": "2026-01-21T14:30:00+04:00",
      "Cancelled_By": null,
      "$editable": true,
      "Appointment_Name": "service-reschedule",
      "Duration": 30,
      "Record_Status__s": "Available",
      "$status": "cmv_1-1",
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Location": "Business Address",
      "Reschedule_Note": "for customer need"
    },
    {
      "Owner": {
        "id": "111115000000122075",
        "email": "madeshwaran.g+csez02@zohotest.com",
        "name": "madesh"
      },
      "$currency_symbol": "£",
      "Address": null,
      "Appointment_Start_Time": "2026-01-22T13:00:00+04:00",
      "Cancellation_Reason": "By Customer",
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Rescheduled_To": "2026-01-22T13:00:00+04:00",
      "$sharing_permission": "full_access",
      "Reschedule_Reason": "By Customer",
      "Additional_Information": null,
      "Last_Activity_Time": "2026-01-16T10:34:44+04:00",
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": "2026-01-16T10:34:44+04:00",
      "Cancellation_Note": "request from customer",
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Reschedule_Count": 2,
      "Rescheduled_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Date_1": "2026-01-14",
      "Rescheduled_Time": "2026-01-16T10:29:58+04:00",
      "Remind_At": [
        {
          "unit": 15,
          "period": "minutes"
        }
      ],
      "Appointment_End_Time": "2026-01-22T13:30:00+04:00",
      "Status": "Cancelled",
      "Modified_Time": "2026-01-16T10:34:44+04:00",
      "Service_Name": {
        "name": "service04",
        "id": "111115000000127440"
      },
      "Created_Time": "2026-01-16T09:39:43+04:00",
      "Rescheduled_From": "2026-01-21T14:30:00+04:00",
      "Cancelled_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "$editable": true,
      "Appointment_Name": "service04 - bb",
      "Duration": 30,
      "Record_Status__s": "Available",
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Location": "Business Address",
      "Reschedule_Note": "for customer need"
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com",
        "name": "madesh04"
      },
      "$currency_symbol": "£",
      "Address": null,
      "Appointment_Start_Time": "2026-01-07T13:00:00+04:00",
      "Cancellation_Reason": null,
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Rescheduled_To": null,
      "$sharing_permission": "full_access",
      "Reschedule_Reason": null,
      "Job_Sheet_Name__s": "ss",
      "Additional_Information": null,
      "Last_Activity_Time": null,
      "Job_Sheet_Created__s": true,
      "Cancelled_Time": null,
      "Cancellation_Note": null,
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Reschedule_Count": 0,
      "Rescheduled_By": null,
      "Date_1": null,
      "Rescheduled_Time": null,
      "Remind_At": null,
      "Appointment_End_Time": "2026-01-07T15:00:00+04:00",
      "Status": "Completed",
      "Modified_Time": "2026-01-16T10:40:45+04:00",
      "Service_Name": {
        "name": "service03",
        "id": "111115000000127405"
      },
      "Created_Time": "2026-01-16T10:40:45+04:00",
      "Rescheduled_From": null,
      "Cancelled_By": null,
      "$editable": true,
      "Appointment_Name": "service-jobsheet",
      "Duration": 120,
      "Job_Sheet_Section__s": "Job Sheet Information",
      "Record_Status__s": "Available",
      "Job_Sheet_Description__s": "done and dusted",
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Location": "Business Address",
      "Reschedule_Note": null
    }
  ]
}
```
