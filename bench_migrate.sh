#!/bin/bash

cd ../..
bench --site test.tailerp.com migrate
cp ~/apps/spiceco/spiceco/core_scripts/expense_claim.py ~/apps/erpnext/erpnext/hr/doctype/expense_claim/expense_claim.py
cp ~/apps/spiceco/spiceco/core_scripts/travel_request_dashboard.py ~/apps/erpnext/erpnext/hr/doctype/travel_request/travel_request_dashboard.py
cp ~/apps/spiceco/spiceco/public/js/travel_request_list.js ~/apps/erpnext/erpnext/hr/doctype/travel_request/travel_request_list.js

echo Done!


