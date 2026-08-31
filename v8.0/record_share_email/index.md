# Record Email Sharing

- [OpenAPI specification](record_share_email.yaml)
- [Share Record Emails](operations/shareEmails/operation.md)
  - To share email threads linked to a specific CRM record with colleagues in the same organization. Requires custom email sharing to be enabled in the organization and a valid email configuration for the user.
  - [Examples](operations/shareEmails/examples/)
- [Unshare Record Emails](operations/unshareEmails/operation.md)
  - To revoke email sharing for a specific CRM record, making the linked email threads no longer visible to colleagues. Requires custom email sharing to be enabled in the organization and a valid email configuration for the user.
  - [Examples](operations/unshareEmails/examples/)
- [Share Record Emails](operations/shareBulkEmails/operation.md)
  - To share email threads linked to multiple CRM records with colleagues in the same organization. Accepts up to 100 record IDs per request. Supports partial success - each record in the response is processed independently, and individual results indicate success or failure.
  - [Examples](operations/shareBulkEmails/examples/)
- [Unshare emails in bulk](operations/unshareBulkEmails/operation.md)
  - To revoke email sharing for multiple CRM records in a single request. Accepts up to 100 record IDs per request. The `data` array in the 207 response contains an item for each record, indicating success or failure.
  - [Examples](operations/unshareBulkEmails/examples/)
