import streamlit as st

from countries import COUNTRIES as cts
from csv_creator import create_csv
from serp_ads import searcher


def get_items(dct):

    for value in dct.values():
        if isinstance(value, dict):
            for key1, value1 in value.items():
                st.success(f"{key1}: {value1}")
    return


def number_of_searches(dct):
    keys = dct.keys()
    return keys.keys()


def headers():
    st.header("AD SEARCH SYSTEM")
    st.subheader("Google ad search system in python")
    return


def sidebar():
    st.sidebar.title("Google Search Ad System")
    return


def get_total_results(country, domain, query):
    """
    The total results is also given as a json response in the search results.
    """
    searches = searcher(country=country, query=query, domain=domain)
    st.text(f"{number_of_searches(searches)} results")
    return


def create_body():
    st.info("GIVE THE COUNTRY YOU WANT ADS FROM")
    country = st.selectbox(
        "Select a country you wanna see ads from",
        list(cts.values())
    )

    st.info("GIVE THE SEARCH TERM FOR YOUR ADS")
    query = st.text_input("Please input the item you wanna search")

    st.info("GIVE THE SEARCH DOMAIN FOR YOUR ADS")
    domain = st.text_input("Please input the web domain you wanna search from")

    st.button("Reset")

    searches = searcher(country=country, query=query, domain=domain)

    if st.button('Search'):
        get_items(searches)

    return query, searches


def main():
    headers()
    sidebar()
    query, data = create_body()

    create_csv(data, query)


if __name__ == '__main__':
    main()
