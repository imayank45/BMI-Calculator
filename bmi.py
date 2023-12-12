import streamlit as st

st.title('BMI Calculator')

with st.form('BMI Calculator'):
    col1, col2, col3 = st.columns([3,3,2])

with col1:
    weight = st.number_input('Enter your weight in KGs', )

with col2:
    height = st.number_input('Enter your height in Centi-Metres', )*0.01

with col3:
    submit = st.form_submit_button('Calculate')

if submit:
    BMI = round((weight / (height**2)),2)

    if BMI < 18.5:
        st.error('Underweight')
        st.write(BMI)
    elif BMI >= 18.8 and BMI <= 24.9:
        st.success('Healthy / Normal')
        st.write(BMI)
    elif BMI > 24.9 and BMI <= 29.9:
        st.warning('Overweight')
        st.write(BMI)
    elif BMI >= 30.0:
        st.error('Obese')
        st.write(BMI)
