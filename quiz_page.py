import streamlit as st

quiz_questions = st.session_state.get("quiz_questions", None)

st.title("Landed on Quiz Page")

def on_form_submit(user_answers, correct_answers):
    total_question = 0
    true_ans = 0
    for key in user_answers.keys():
        if user_answers[key] == correct_answers[key]: true_ans += 1

        total_question += 1
    
    if true_ans == total_question:
        st.balloons()
    st.markdown(f'## You score {true_ans}/{total_question}')

if quiz_questions is not None and len(quiz_questions) > 0:

    with st.form("my_form"):

        user_answers = {}
        correct_answers = {}
        for indx, question in enumerate(quiz_questions):
            st.write(question.question)
            user_answers[indx] = st.radio("", options=question.options)
            # st.write("Correct Answer:", question.answer)
            correct_answers[indx] = question.options[question.answer]
            st.divider()
        
        
        submitted = st.form_submit_button("Submit", on_click=on_form_submit, args=(user_answers, correct_answers))
else:
    st.markdown('### No quiz formed yet.')