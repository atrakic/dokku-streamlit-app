# Dokku Streamlit App

This repository contains a Streamlit application deployed using Dokku.

## Prerequisites

- Dokku installed on your server
- A domain name pointed to your server
- Streamlit installed in your project

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/atrakic/dokku-streamlit-app.git
    cd dokku-streamlit-app
    ```

2. Create a new Dokku app:

    ```sh
    dokku apps:create streamlit-app
    ```

3. Set up the domain for your app:

    ```sh
    dokku domains:add streamlit-app yourdomain.com
    ```

4. Deploy the app:

    ```sh
    git remote add dokku dokku@yourserver.com:streamlit-app
    git push dokku main
    ```

## Usage

After deployment, your Streamlit app will be accessible at `http://yourdomain.com`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
