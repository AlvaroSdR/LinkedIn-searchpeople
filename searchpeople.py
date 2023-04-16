# Import the necessary modules
from linkedin_api import Linkedin
import streamlit as st

# Get user input for job position and search position
job_position = st.text_input("Search for people in this Position")
search_position = st.text_input("Search for this open positions")

# Add a "Search" button
search_button = st.button("Search")

# Check if the "Search" button is clicked
if search_button:
    # Authenticate to LinkedIn
    try:
        linkedin = Linkedin('username', 'password')
    except Exception as e:
        st.error(f"Failed to authenticate: {e}")
        st.stop()

    # Search for companies with open positions for search position
    try:
        companies = linkedin.search_companies(job_position=search_position)
    except Exception as e:
        st.error(f"Failed to search companies: {e}")
        st.stop()

    # Display the list of companies
    st.write(f"Companies with open positions for {search_position}:")
    for company in companies:
        st.write(company)

    # Get the profiles of people with job matching the job position
    profiles = []
    for company in companies:
        try:
            employees = linkedin.get_company_employees(company_id=company["id"])
            for employee in employees:
                if job_position in employee["title"]:
                    profiles.append(employee)
        except Exception as e:
            st.warning(f"Failed to get employees for company {company['name']}: {e}")

    # Display the list of profiles
    st.write(f"Profiles with job title '{job_position}' in the companies above:")
    for profile in profiles:
        st.write(profile)
