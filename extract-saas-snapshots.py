#!/usr/bin/env python3
# This script extracts the last five years of snapshots from The Wayback Machine of the terms of the given saas providers.
# Usage: python3 extract-saas.py -o <OUTPUT_FOLDER>

import os
import subprocess

SAAS_PROVIDERS = {
    "Salesforce":   "https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/",
    "GitHub":       "https://docs.github.com/en/github/site-policy/github-terms-of-service",
    "Postman":      "https://www.postman.com/legal/terms/",
    "Databox":      "https://databox.com/terms-of-service",
    "OpenPhone":    "https://www.openphone.com/terms",
    "Wrike":        "https://www.wrike.com/security/terms/",
    "Tableau":      "https://www.tableau.com/tos",
    "Zapier":       "https://zapier.com/legal/terms-of-service",
    "Slack":        "https://slack.com/terms-of-service/user",
    "MailChimp":    "https://mailchimp.com/en/legal/terms/",
    "ClickUp":      "https://clickup.com/terms",
    "Planable":     "https://clickup.com/terms",
    "Clockify":     "https://cake.com/terms",
    "Microsoft":    "https://www.microsoft.com/en-us/servicesagreement/",
    "Trustmary":    "https://trustmary.com/terms-of-service/",
    "Buffer":       "https://buffer.com/legal#terms",
    "Jira":         "https://www.atlassian.com/legal/cloud-terms-of-service",
    "Notion":       "https://www.atlassian.com/legal/atlassian-customer-agreement#intro",
    "Figma":        "https://www.figma.com/legal/tos/",
    "Box":          "https://www.box.com/legal/termsofservice",
    "Canva":        "https://www.canva.com/policies/terms-of-use/",
    "Dropbox":      "https://www.dropbox.com/terms",
    "Evernote":     "https://evernote.com/legal/terms-of-service",
    "Hypercontext": "https://hypercontext.com/terms-of-service",
    "Pumble":       "https://cake.com/terms",
    "UserGuiding":  "https://userguiding.com/terms-of-service",
    "Crowdcast":    "https://www.crowdcast.io/terms-of-servics",
    "Deskera":      "https://www.deskera.com/terms-of-service",
    "Overleaf":     "https://www.overleaf.com/legal",
    "Quip":         "https://quip.com/about/terms"
}


def parse_args():
    """Parse the arguments of the script"""
    import argparse
    parser = argparse.ArgumentParser(description="Extract the last five years of snapshots from The Wayback Machine of the terms of the given saas providers.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output folder to save the HTML snapthosts.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    output_folder = args.output
    
    # execute extract-wayback-machine-snapshots.py in parallel for each saas provider
    # at most 5 processes in parallel
    running_processes = []
    index = 0
    
    while True:
        if index >= len(SAAS_PROVIDERS):
            break
        
        if len(running_processes) < 5:
            saas_provider = list(SAAS_PROVIDERS.keys())[index]
            url = SAAS_PROVIDERS[saas_provider]
            output = os.path.join(output_folder, saas_provider)
            # create output folder
            os.makedirs(output, exist_ok=True)
            process = subprocess.Popen(["python3", "extract-wayback-machine-snapshots.py", "--one-per-month", "-y", "2020", "-u", url, "-o", output], stdout=open(f"{output}.log", "w"), stderr=subprocess.STDOUT)
            running_processes.append(process)
            index += 1
        
        for process in running_processes:
            if process.poll() is not None:
                running_processes.remove(process)
    