# #!/bin/bash

# # This script acts as an SSH wrapper for gcloud compute ssh
# service_account=$(curl -v -w "\n" -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/email)
# zone_extract=$(curl -v -w "\n" -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/zone)
# project_id=$(curl -v -w "\n" -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/project/project-id)
# zone=$(basename "$zone_extract")
# # Extract the target host from the arguments
# arg="$@"
# TARGET_HOST=$(echo "$arg" | sed -n "s/.* \([^ ]\+\) '\/bin\/sh.*/\1/p")

# host="${@: -2: 1}"
# cmd="${@: -1: 1}"
# # Unfortunately ansible has hardcoded ssh options, so we need to filter these out
# # It's an ugly hack, but for now we'll only accept the options starting with '--'
# declare -a opts
# for ssh_arg in "${@: 1: $# -3}" ; do
#         if [[ "${ssh_arg}" == --* ]] ; then
#                 opts+="${ssh_arg} "
#         fi
# done

# # Execute gcloud compute ssh with the necessary arguments
# # You might need to adjust project and zone based on your setup
# exec gcloud compute ssh $opts "sa_457587479195-compute${host}" --impersonate-service-account=$service_account --project=$project_id --zone=$zone --tunnel-through-iap --ssh-flag="-A"  -- -C "${cmd}"


#!/bin/bash
# This is a wrapper script allowing to use GCP's IAP SSH option to connect
# to our servers.

# Ansible passes a large number of SSH parameters along with the hostname as the
# second to last argument and the command as the last. We will pop the last two
# arguments off of the list and then pass all of the other SSH flags through
# without modification:
host="${@: -2: 1}"
cmd="${@: -1: 1}"

# Unfortunately ansible has hardcoded ssh options, so we need to filter these out
# It's an ugly hack, but for now we'll only accept the options starting with '--'
declare -a opts
for ssh_arg in "${@: 1: $# -3}" ; do
        if [[ "${ssh_arg}" == --* ]] ; then
                opts+="${ssh_arg} "
        fi
done

exec gcloud compute ssh $opts "sa_573056899267-compute@${host}" -- -C "${cmd}"
