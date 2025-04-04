import streamlit as st
import pandas as pd
from database import create_table, add_book, view_books

create_table()

st.title("📚 Library Manager")

menu = ["Add Book", "View Books"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1800, max_value=2025, step=1)
    
    if st.button("Add Book"):
        add_book(title, author, year)
        st.success(f"Book '{title}' added successfully!")

elif choice == "View Books":
    st.subheader("Library Books")
    books = view_books()
    df = pd.DataFrame(books, columns=["ID", "Title", "Author", "Year"])
    st.dataframe(df)
