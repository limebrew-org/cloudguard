# Cloud Guardian
A CLI built as a CSPM (Cloud Security Posture Management) tool to monitor major cloud providers like GCP, AWS and Azure written in Python

## Documentation

CLI commands:

1. cloudguardian config --provider gcp  (settings credentials for a provider)

2. cloudguardian run  (based on user prompt execute the commands)

3. cloudguardian run --provider gcp --all -export-json  (run all supported services for the provider)

4. cloudguardian run --provider gcp list   (list all supported provider services)

5. cloudguardian providers list   (list all available cloud providers)

6. cloudguardian --help (Default: help for more information)


## References:
1. Google Cloud APIs and SDK client libraries