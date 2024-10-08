import sqlite3
import streamlit as st
import pandas as pd
# import numpy as np
import requests

DB_FILE = "/var/db/github_repos.db"


def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None


def flatten_repo_data(repo):
    return {
        "id": repo["id"],
        "name": repo["name"],
        "full_name": repo["full_name"],
        "html_url": repo["html_url"],
        "description": repo["description"],
        "fork": repo["fork"],
        "created_at": repo["created_at"],
        "updated_at": repo["updated_at"],
        "pushed_at": repo["pushed_at"],
        "stargazers_count": repo["stargazers_count"],
        "watchers_count": repo["watchers_count"],
        "forks_count": repo["forks_count"],
        "language": repo["language"],
    }


def save_to_sqlite(data, db_name=DB_FILE):
    conn = sqlite3.connect(db_name)
    flattened_data = [flatten_repo_data(repo) for repo in data]
    df = pd.DataFrame(flattened_data)
    df.to_sql("repos", conn, if_exists="replace", index=False)
    conn.close()


def load_from_sqlite(db_name=DB_FILE):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql("SELECT * FROM repos", conn)
    conn.close()
    return df


def main():
    st.title("GitHub Repositories Status")
    username = st.text_input("Enter GitHub username")

    if st.button("Fetch and Load Repositories"):
        repos = fetch_github_repos(username)
        if repos:
            save_to_sqlite(repos)
            st.success("Repositories fetched and saved to database")

        df = load_from_sqlite()
        st.write(df)
        st.write(df.describe())
        st.subheader("Repository Name Counts")
        st.write(df["name"].value_counts())

        st.subheader("Stargazers Count Bar Chart")
        st.bar_chart(df["stargazers_count"])

        st.subheader("Forks Count Line Chart")
        st.line_chart(df["forks_count"])

        st.subheader("Watchers Count Area Chart")
        st.area_chart(df["watchers_count"])


if __name__ == "__main__":
    main()
