import numpy as np
import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas

model = load_model('model')
# st.markdown('<style>body{color: White; background-color: DarkSlateGrey}</style>', unsafe_allow_html=True)

st.title('My Digit Recognizer')
st.markdown('''
Try to write a digit!
''')

# data = np.random.rand(28,28)
# img = cv2.resize(data, (256, 256), interpolation=cv2.INTER_NEAREST)

SIZE = 192
mode = st.checkbox("Draw (or Delete)?", True)
data = st_canvas(20, '#FFFFFF', '#000000', width=SIZE, height=SIZE, drawing_mode=mode, key='canvas')
img = cv2.resize(data.astype('uint8'), (28, 28))
rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
st.write('Model Input')
st.image(rescaled)

if st.button('Predict'):
    test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    val = model.predict(test_x.reshape(1, 28, 28))
    st.write(f'result: {np.argmax(val[0])}')
    st.bar_chart(val[0])