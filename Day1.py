import requests


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "
    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)

    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(gh_api_search_url, params=parameters)

    status_code = response.status_code
    # Check if the rate limit was hit. Applies only for students running this code
    # in the in-person course.
    if status_code == 403:
        raise RuntimeError(
            "Rate limit reached. Please wait a minute and try again.")
    if status_code != 200:
        raise RuntimeError(
            f"An error occurred. HTTP Status Code was: {status_code}.")
    else:
        response_json = response.json()
        records = response_json["items"]
        return records


if __name__ == "__main__":
    # Have a main method
    languages = ["python", "javascript", "go", "c++"]
    data = repos_with_most_stars(languages)

    for repo in data:
        language = repo["language"]
        stars = repo["stargazers_count"]
        name = repo["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
