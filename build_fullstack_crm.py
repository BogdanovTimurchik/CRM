import re
import json
import os

print("Building Maryam Academy Mission (MAM) Full-Stack CRM/ERP...")

# 1. Read existing crm.html to extract dataset and base structure
with open('crm.html', 'r', encoding='utf-8') as f:
    crm_source = f.read()

# Extract SERVICE_ACCOUNTS
acc_match = re.search(r"const SERVICE_ACCOUNTS = (\{.*?\n    \});", crm_source, re.DOTALL)
accounts_code = acc_match.group(1) if acc_match else ""

# Extract rawNames
raw_match = re.search(r"const rawNames = (\[.*?\n      \]);", crm_source, re.DOTALL)
raw_names_code = raw_match.group(1) if raw_match else ""

# Extract groups
grp_match = re.search(r"const groups = (\[.*?\n      \]);", crm_source, re.DOTALL)
groups_code = grp_match.group(1) if grp_match else ""

# Extract equipment
eq_match = re.search(r"const equipment = (\[.*?\n      \]);", crm_source, re.DOTALL)
equipment_code = eq_match.group(1) if eq_match else ""

# Extract expenses
exp_match = re.search(r"const expenses = (\[.*?\n      \]);", crm_source, re.DOTALL)
expenses_code = exp_match.group(1) if exp_match else ""

# Extract auditLogs
audit_match = re.search(r"const auditLogs = (\[.*?\n      \]);", crm_source, re.DOTALL)
audit_code = audit_match.group(1) if audit_match else ""

# Extract kanbanLeads
kanban_match = re.search(r"const kanbanLeads = (\[.*?\n      \]);", crm_source, re.DOTALL)
kanban_code = kanban_match.group(1) if kanban_match else ""

# Extract timesheetRecords
timesheet_match = re.search(r"const timesheetRecords = (\[.*?\n      \]);", crm_source, re.DOTALL)
timesheet_code = timesheet_match.group(1) if timesheet_match else ""

# Extract receipts
rec_match = re.search(r"const receipts = (\[.*?\n      \]);", crm_source, re.DOTALL)
receipts_code = rec_match.group(1) if rec_match else ""

print(f"Extracted components: accounts={bool(accounts_code)}, rawNames={bool(raw_names_code)}, groups={bool(groups_code)}")
