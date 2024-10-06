# azure-dokku-template

> Use this template to deploy your container of choice to Azure Cloud with [DokKu](https://dokku.com/docs/deployment/application-deployment/).

[![last commit](https://img.shields.io/github/last-commit/atrakic/azure-dokku-template)](https://github.com/atrakic/azure-dokku-template/commits/)
![License](https://img.shields.io/github/license/atrakic/azure-dokku-template)


## Getting started

### Prerequisites
- [Azure account](https://azure.microsoft.com/en-us/free/)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

### Local deployment

1. Use this repository as your GitOps template

Create a GitHub repository based on this starter template (see the green "Use this template" button).


2. Clone your repo
   ```sh
   git clone https://github.com/your-account/your-repo.git
   ```

3. Edit the `Dockerfile` and `Makefile` and `infra` to match your app


4. Create infrastructure on Azure Cloud
   ```make infra ```


5. Deploy the app to Dokku
   ```make ```

6. Access your app

### GitHub Actions deployment

1. Create a new secret in your new repo with the name `SSH_PRIVATE_KEY` and add the value of your private SSH key. This key will be used to authenticate with the Dokku server.
2. Create new branch with your changes and create PR to trigger the GitHub Actions workflows.


## Example deployment

- https://github.com/atrakic/dokku-clicks


## License Information
This project is licensed under the MIT License. View the [LICENSE](LICENSE) file for more details.
