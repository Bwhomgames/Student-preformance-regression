import streamlit as st 
import joblib 
import pandas as pd
regression = joblib.load("pipelines.pkl")
def predict_model(h_studied,P_scores,E_Activities,h_sleep,s_question):

    input_data = pd.DataFrame([{
        "Hours Studied": h_studied,
        "Previous Scores": P_scores,
        "Extracurricular Activities": E_Activities,
        "Sleep Hours": h_sleep,
        "Sample Question Papers Practiced": s_question

    }])

    prediction = regression.predict(input_data)
    print(prediction)
    return prediction[0] 
def main ():
     
    st.header("Student preformance")

    h_studied = st.number_input("Hours studied",min_value = 0, max_value = 24, step = 1) 
    P_scores = st.number_input("Previous Scores",min_value = 0, max_value = 100, step = 1) 
    E_Activities = st.selectbox("Extracurricular Activities",["Yes","No"]) 
    h_sleep = st.number_input("Sleep Hours",min_value = 0, max_value = 24, step = 1) 
    s_question = st.number_input("Sample Question Papers Practiced",min_value = 0, max_value = 9, step = 1)

    if E_Activities == "Yes":
        E_Activities = 1
    else :
        E_Activities = 0    

    pridict_btn = st.button("Predict")
    About_btn = st.button("About")
    if pridict_btn:
        result = predict_model(h_studied,P_scores,E_Activities,h_sleep,s_question)
        st.success(f"predicted preformance index: {result:.2f}")

    if About_btn:
        st.text("Created by (Bassel Galal ,Kreem Shady ,Ahmed Khaled)")
        st.text("Built with streamlit")
if __name__ == '__main__':
    main()
