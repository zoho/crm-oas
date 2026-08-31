# Shared Records API

- [OpenAPI specification](share_records.yaml)
- [Share Records](operations/getShareRecords/operation.md)
  - To retrieve the share details of a specific record in a module of your Zoho CRM organization. The response lists each entry with the recipient, the access level, and the sharing metadata.
  - [Examples](operations/getShareRecords/examples/)
- [Share a record](operations/createShareRecords/operation.md)
  - To share a specific record in a module with one or more users, roles, or groups. A record can be shared with up to 10 users, 5 roles, and 5 groups. > **Note**: > - The records can be shared to other users in the organization only if certain conditions are met. For simplicity, let us assume that User A shares a record with User B. Now, User A can share the record successfully only if: > - User B is a **confirmed** and **active** user. > - User B **does not already have access** to that particular record. > - User B has access to that particular module. For instance, to share a contact, User B must have access to the Contacts module. > - You cannot share the records in Calls, Meetings, Tasks, and Linking modules directly. They can be shared as related lists. > - The users who have profiles with **share** permission can share any records that they have access to, except the records that are shared to them. To check the same, go to Setup > Users and Control > Security Control > Choose the profile > Tool Permissions. Check if **share** is enabled. It is enabled by default for Standard and Administrator Profiles. > - The details of the records that form many-to-many relationships (with multi-select lookup) cannot be shared. > - A record can be shared only with **10 users**, **5 groups**, and **5 roles**. > - Once the record gets shared successfully, the user who initiated the share operation can be notified via email.
  - [Examples](operations/createShareRecords/examples/)
- [Update share permissions](operations/updateShareRecords/operation.md)
  - To update the sharing permissions of a specific record in a module of your Zoho CRM organization. The update can change the access level, change the visibility between private and public, or alter whether related records are shared along with the record.
  - [Examples](operations/updateShareRecords/examples/)
- [Revoke sharing on a record](operations/deleteShareRecords/operation.md)
  - To revoke all sharing on a specific record in a module of your Zoho CRM organization. Use this operation to remove access that was previously granted to users, roles, or groups through record-level sharing.
  - [Examples](operations/deleteShareRecords/examples/)
