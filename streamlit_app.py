
import streamlit as st

def main():
    # Set the title text
    st.title("Streamlit App")

    # Input text
    input_text = st.text_input("Enter Text:")

    # Dropdown with options 'submitted' and 'deleted'
    status_options = ['submitted', 'deleted']
    selected_status = st.selectbox("Select Status:", status_options)

    # Button to trigger an action
    if st.button("Submit"):
        # Action to perform when the button is clicked
        st.success(f"Text: {input_text}, Status: {selected_status} Submitted!")

if __name__ == "__main__":
    main()
