#!/bin/bash

# This script acts as an SSH wrapper for gcloud compute ssh
service_account=$(curl -v -w "\n" -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/email)
zone_extract=$(curl -v -w "\n" -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/zone)
project_id=$(curl -v -w "\n" -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/project/project-id)
zone=$(basename "$zone_extract")
# Extract the target host from the arguments
arg="$@"
TARGET_HOST=$(echo "$arg" | sed -n "s/.* \([^ ]\+\) '\/bin\/sh.*/\1/p")

# for arg in "$@"; do
# if [[ "$arg" =~ ^[a-zA-Z0-9._-]+$ ]]; then
#         TARGET_HOST="$arg"
#         break
# fi
# done

# if [ -z "$TARGET_HOST" ]; then
# echo "Error: Could not determine target host from arguments."
# exit 1
# fi

# Execute gcloud compute ssh with the necessary arguments
# You might need to adjust project and zone based on your setup
exec gcloud compute ssh "$TARGET_HOST" --project=$poject_id --zone=$zone --tunnel-through-iap --ssh-flag="-A" "$@"
