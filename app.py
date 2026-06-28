import streamlit as st

from src.search import search

st.set_page_config(
    page_title="AI Search Engine",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Search Engine")
st.caption("Powered by Exa AI")

query = st.text_input("Search")

col1, col2 = st.columns(2)

with col1:
    num_results = st.slider(
        "Number of Results",
        1,
        10,
        5
    )

with col2:
    domain = st.text_input(
        "Limit Domain (optional)",
        placeholder="github.com"
    )

if st.button("Search"):

    if query:

        with st.spinner("Searching..."):

            results = search(
                query,
                num_results,
                domain if domain else None
            )

        st.success(f"{len(results)} results found.")

        for i, result in enumerate(results, 1):

            st.divider()

            st.subheader(f"{i}. {result.title}")

            st.link_button(
                "Open Website",
                result.url
            )

            if result.text:
                st.write(result.text[:500] + "...")

    else:
        st.warning("Please enter a search query.")