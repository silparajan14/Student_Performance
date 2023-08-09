
import pandas as pd
import pickle
import streamlit as st
from PIL import Image

#loading the saved model :
loaded_model = pickle.load(open("C:/Users/SILPA/Desktop/student_performance/Student_Performance_model.sav",'rb'))
loaded_file = pickle.load(open("C:/Users/SILPA/Desktop/student_performance/object.sav",'rb'))

#creating function for prediction :

def Performance_Index(data):
    pred = pd.DataFrame(data)
    pred['Hours Studied'] = loaded_file[1].transform(pred['Hours Studied'])
    pred['Previous Scores'] = loaded_file[1].transform(pred['Previous Scores'])
    pred['Extracurricular Activities'] = loaded_file[0].transform(pred['Extracurricular Activities'])
    pred['Extracurricular Activities'] = loaded_file[1].transform(pred['Extracurricular Activities'])
    pred['Sleep Hours'] = loaded_file[1].transform(pred['Sleep Hours'])
    pred['Sample Question Papers Practiced'] = loaded_file[1].transform(pred['Sample Question Papers Practiced'])
    new_pred = loaded_model.predict(loaded_file[1].transform(pred))
    return 'Performance_Index',new_pred

def main():
    st.header("Know Your Performance Index " )

    #Adding image
    image_path = Image.open("C:/Users/SILPA/Desktop/student_performance/WhatsApp Image 2023-07-31 at 10.54.10 AM.jpeg")
    st.image(image_path, use_column_width = True)
    st.write("Welcome to your Performance Index analysis !")
    st.subheader('\nEnter Details : ')

    #getting the input data
    hours_studied_options = [1,2,3,4,5,6,7,8,9]
    a = st.selectbox('Hours Studied',hours_studied_options)

    b = st.text_input('Previous Scores')

    sleep_hrs_options = [1,2,3,4,5,6,7,8,9,10]
    c = st.selectbox('Sleep Hours',sleep_hrs_options)

    extracurricular_activities_options = ['Yes','No']
    d = st.selectbox('Extracurricular Activities',extracurricular_activities_options)

    e = st.text_input('Sample Question Papers Practiced')

    data = {'Hours Studied' : [a],'Previous Scores':[b],'Extracurricular Activities':[c],
            'Sleep Hours':[d],'Sample Question Papers Practiced':[e] }

    output = ''

    if st.button('prediction'):
        output = Performance_Index(data)

    st.success(output)

if __name__=='__main__':
    main()


