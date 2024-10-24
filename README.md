# ToS Wayback Machine Dataset

In this repository you can find two scipts used to automatically extract a dataset of snapshots for online webs, extracted from Internet Archive, better known as The Wayback Machine.

In the data/ folder you can find the snapshots downloaded for 10 SaaS providers.

## Dependencies

The only dependencies are:

* Selenium
* tqdm

Install them with:

```bash
pip install selenium
pip insatll tqdm
```

## Usage

Both script are executables. Run for help:

```bash
python extract-sass-snapshots.py --help
python extract-wayback-machine-snapshots.py --help
```

If you run `python extract-wayback-machine-snapshots.py -o data` it will stract downloading snapshots on the `data/` folder.

The list of SaaS is hardcoded into the script. This is the list:

| SaaS Provder | Website                                                                 |
|--------------|-------------------------------------------------------------------------|
| Salesforce   | https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/ |
| GitHub       | https://docs.github.com/en/github/site-policy/github-terms-of-service   |
| Postman      | https://www.postman.com/legal/terms/                                    |
| Databox      | https://databox.com/terms-of-service                                    |
| OpenPhone    | https://www.openphone.com/terms                                         |
| Wrike        | https://www.wrike.com/security/terms/                                   |
| Tableau      | https://www.tableau.com/tos                                             |
| Zapier       | https://zapier.com/legal/terms-of-service                               |
| Slack        | https://slack.com/terms-of-service/user                                 |
| MailChimp    | https://mailchimp.com/en/legal/terms/                                   |
| ClickUp      | https://clickup.com/terms                                               |
| Planable     | https://clickup.com/terms                                               |
| Clockify     | https://cake.com/terms                                                  |
| Microsoft    | https://www.microsoft.com/en-us/servicesagreement/                      |
| Trustmary    | https://trustmary.com/terms-of-service/                                 |
| Buffer       | https://buffer.com/legal#terms                                          |
| Jira         | https://www.atlassian.com/legal/cloud-terms-of-service                  |
| Notion       | https://www.atlassian.com/legal/atlassian-customer-agreement#intro      |
| Figma        | https://www.figma.com/legal/tos/                                        |
| Box          | https://www.box.com/legal/termsofservice                                |
| Canva        | https://www.canva.com/policies/terms-of-use/                            |
| Dropbox      | https://www.dropbox.com/terms                                           |
| Evernote     | https://evernote.com/legal/terms-of-service                             |
| Hypercontext | https://hypercontext.com/terms-of-service                               |
| Pumble       | https://cake.com/terms                                                  |
| UserGuiding  | https://userguiding.com/terms-of-service                                |
| Crowdcast    | https://www.crowdcast.io/terms-of-servics                               |
| Deskera      | https://www.deskera.com/terms-of-service                                |
| Overleaf     | https://www.overleaf.com/legal                                          |
| Quip         | https://quip.com/about/term                                             |

## Data

On the data folder you can find the dataset already generated.# tos-saas-dataset
