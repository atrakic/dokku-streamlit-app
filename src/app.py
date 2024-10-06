import streamlit as st
import pandas as pd

# import numpy as np
import sqlite3
import requests

db_file = "/var/db/github_repos.db"


def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch repositories")
        return []


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


def save_to_sqlite(data, db_name=db_file):
    conn = sqlite3.connect(db_name)
    flattened_data = [flatten_repo_data(repo) for repo in data]
    df = pd.DataFrame(flattened_data)
    df.to_sql("repos", conn, if_exists="replace", index=False)
    conn.close()


def load_from_sqlite(db_name=db_file):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql("SELECT * FROM repos", conn)
    conn.close()
    return df


# Streamlit app
st.title("GitHub Repositories Status")

username = st.text_input("Enter GitHub username")

if st.button("Fetch Repositories"):
    repos = fetch_github_repos(username)
    if repos:
        save_to_sqlite(repos)
        st.success("Repositories fetched and saved to database")

if st.button("Load Repositories from Database"):
    df = load_from_sqlite()
    st.write(df)
    st.write(df.describe())
    st.write(df["name"].value_counts())
    st.bar_chart(df["stargazers_count"])
    st.line_chart(df["forks_count"])
    st.area_chart(df["watchers_count"])
