# Cloud Guard
A CLI built as a CSPM (Cloud Security Posture Management) tool to monitor major cloud providers like GCP, AWS and Azure written in Python

## Documentation

1. Configure cloud provider credentials:

        cloudguard config --provider gcp  (settings credentials for a provider)
2. Run `cloudguard` with user prompt:

        cloudguard run
3. Run `cloudguard` with arguments:

        cloudguard run --provider gcp --all -export-json
4. Run `cloudguard` and list the supported resources for a cloud provider

        cloudguard run --provider gcp list
5. List all supported cloud providers:

        cloudguard providers list
6. Help:

        cloudguard --help 


## References:
1. Google Cloud APIs and SDK client libraries
