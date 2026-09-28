import streamlit as st

from scoring import calculate_score

st.set_page_config(page_title="Student Performance Prediction")

st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", ["Scoring Demo", "Project Information"])

if selected_page == "Project Information":
    st.title("Student Performance Prediction Using a Simple Average Scoring Method")
    st.write(
        "This application demonstrates student data input, validation, and "
        "simple average score calculation."
    )
else:
    st.title("Student Performance Prediction Using a Simple Average Scoring Method")
    st.header("Student Data Input and Scoring")
    st.write(
        "Enter the three academic indicators to demonstrate the simple average "
        "scoring method."
    )

    with st.form("student_data_form"):
        student_name = st.text_input("Student Name")
        previous_grade = st.number_input(
            "Previous Grade",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
        )
        attendance = st.number_input(
            "Attendance Percentage",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
        )
        assignment_completion = st.number_input(
            "Assignment Completion Percentage",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
        )
        submitted = st.form_submit_button("Calculate Score")

    if submitted:
        validation_errors = []

        if not student_name.strip():
            validation_errors.append("Student Name must not be empty.")
        if not 0 <= previous_grade <= 100:
            validation_errors.append("Previous Grade must be between 0 and 100.")
        if not 0 <= attendance <= 100:
            validation_errors.append("Attendance must be between 0 and 100.")
        if not 0 <= assignment_completion <= 100:
            validation_errors.append(
                "Assignment Completion must be between 0 and 100."
            )

        if validation_errors:
            for validation_error in validation_errors:
                st.error(validation_error)
        else:
            score = calculate_score(
                previous_grade,
                attendance,
                assignment_completion,
            )

            st.success("Student information recorded and score calculated successfully.")
            st.header("Student Information")
            st.write(f"**Student Name:** {student_name.strip()}")
            st.write(f"**Previous Grade:** {previous_grade:g}%")
            st.write(f"**Attendance:** {attendance:g}%")
            st.write(f"**Assignment Completion:** {assignment_completion:g}%")

            st.header("Scoring Calculation")
            st.write(
                "Score = "
                f"({previous_grade:g} + {attendance:g} + "
                f"{assignment_completion:g}) / 3"
            )
            st.write(f"Score = {score:.2f}")

            st.header("Calculated Score")
            st.metric("Score", f"{score:.2f} / 100")
