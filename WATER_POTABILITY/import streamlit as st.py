import streamlit as st
import pickle
from PIL import Image
import pandas as pd
import base64
from io import BytesIO

#load dataset in pycharam

df=pd.read_csv(r'C:\Users\user\PycharmProjects\Mechine_Learning\ML_model\water_potability\water_potability.csv')

#handle missing values

df['ph']=df['ph'].fillna(df['ph'].mean())
df['Sulfate']=df['Sulfate'].fillna(df['Sulfate'].mean())
df['Trihalomethanes']=df['Trihalomethanes'].fillna(df['Trihalomethanes'].mean())


#load the scaler and the model
model=pickle.load(open('water1','rb'))
scaler=pickle.load((open('scaler1','rb')))

def navigate_to(page):
    st.session_state.current_page = page
if 'current_page' not in st.session_state:
    st.session_state.current_page ='Home'

with st.sidebar:
    st.title('Navigation')

    if st.button("Home"):
        navigate_to("Home")

    if st.button("Water Pollution & Prevention"):
        navigate_to("Water Pollution & Prevention")

    if st.button("Dataset Overview"):
        navigate_to("Dataset Overview")

    if st.button('Check Potability'):
        navigate_to('Potability Checker')





if st.session_state.current_page == "Home":

    st.title(':blue[WATER POTABILITY PREDICTION]:droplet:')

    image = Image.open('water image.jpeg')

    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Embed with HTML and center it
    st.markdown(
     f"""
        <div style='text-align: center;'>
            <img src='data:image/jpeg;base64,{img_str}' style='width:500px; height:300px;'/>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write('Monitoring the quality of water and testing it regularly is very important to maintain reliable '
             'and safe water sources and eliminate the potential health risks related to water contamination.')  # shrt note about the project

elif st.session_state.current_page == "Dataset Overview":
    st.title('Dataset Overview')

    # Turbidity
    st.markdown(":point_right::blue[Turbidity]:- It is the measure of relative clarity of a liquid.")

    # Hardness
    st.markdown(
        ":point_right::blue[Hardness]:- Water hardness is the amount of dissolved calcium and magnesium in the water.")

    # Solids
    st.markdown(
        ":point_right::blue[Solids]:- Total solids are dissolved solids plus suspended and settleable solids in water."
        " In stream water, dissolved solids consist of calcium, chlorides, nitrate, phosphorus, iron, sulfur, "
        "and other ions and particles that will pass through a filter with pores of around 2 microns.")
     # pH
    st.markdown(
        ":point_right::blue[pH]:- Water has a neutral pH of 7, which indicates that it is neither acidic nor basic."
        " The scale ranges from 0 (very acidic) to 14 (very basic). It is normal for water to have a pH range of between 6.5 and 8.5.")

    # Chloramines
    st.markdown(
        ":point_right::blue[Chloramines]:- Chloramines are a group of chemical compounds that contain chlorine and ammonia."
        " The particular type of chloramine used in drinking water disinfection is called monochloramine, which is mixed into water at levels"
        " that kill germs but are still safe to drink.")

    # Sulfate
    st.markdown(
        ":point_right::blue[Sulfate]:- At high levels, sulfate can give water a bitter or medicinal taste and can have laxative effects.")

    # Conductivity
    st.markdown(
        ":point_right::blue[Conductivity]:- Conductivity is a measure of the ability of water to pass an electrical current."
        " Because dissolved salts and other inorganic chemicals conduct electrical current, conductivity increases as salinity increases.")

    # Organic Carbon
    st.markdown(
        ":point_right::blue[Organic Carbon]:- Total organic carbon is a measure of the amount of organic compounds contained in a water sample."
        " A high organic content means an increase in the growth of microorganisms, which contributes to the depletion of oxygen supplies.")

    # Trihalomethanes
st.markdown(
        ":point_right::blue[Trihalomethanes]:- Trihalomethanes (THMs) are widespread disinfection by-products (DBPs) in drinking water,"
        " and long-term exposure has been consistently associated with increased bladder cancer risk.")
    on = st.toggle('Dataset', )
    if on:
        st.write(':green[water potability dataset]')
        st.write(df)

elif st.session_state.current_page == "Potability Checker":
    st.title('Check Potability')

    a = st.number_input('ph', min_value=0.0000, max_value=14.0000, step=0.0001, format="%.4f")
    b = st.text_input('hardness', 'text here')
    c = st.text_input('solids', 'text here')
    d = st.text_input('chloramines', 'text here')
    e = st.text_input('sulfate', 'text here')
    f = st.text_input('conductivity', 'text here')
    g = st.text_input('organic_carbon', 'text here')
    h = st.text_input('trihalomethanes', 'text here')
    i = st.text_input('turbidity', 'text here')

    # store features ina a variable
    fe = [a, b, c, d, e, f, g, h, i]

    # predict button
    pred = st.button(':rainbow[PREDICT]:point_left:')

    # prediction
 if pred:
        prediction = model.predict(scaler.transform([fe]))
        if prediction == 0:
            st.write(':red[non potable 	:heavy_multiplication_x:]')
            # short note about non potability
            with st.expander("See explanation"):
                st.write(
                    'Non-potable water can contain chemicals from industry and agriculture, human or animal waste, water treatment and distribution, or natural contaminants (when water travels through soil).'
                    ' Soil can contain arsenic, heavy metals and pesticide residues.')
        else:
            st.write(':green[potable :heavy_check_mark:]')
            # short note about potability
            with st.expander("See explanation"):
                st.write(
                    'Potable water is the water which is filtered and treated properly and is finally free from all contaminants and harmful bacteria. This purified water is fit to drink, or it can be called '
                    'drinking water after the purification processes and is safe for both cooking and drinking.')


if st.session_state.current_page == "Water Pollution & Prevention":
    st.title('🌊 Water Pollution & Prevention')
    st.write()
    st.write('### 🔍 *What is Water Pollution?*')
    st.markdown('Water pollution occurs when harmful substances contaminate water bodies (rivers, lakes, oceans, groundwater), degrading water quality and harming ecosystems and human health.')

    st.write()

    # Selectbox for choosing a topic
    topic = st.selectbox(
        'Select a Topic:',
        ['Select','Real-World Causes of Water Pollution', 'Water Pollution Prevention 
         Techniques']
    )

    # Display information based on the selected topic
    if topic == 'Real-World Causes of Water Pollution':
        st.write('### 🏭 *Real-World Causes of Water Pollution*')
        st.write(':one: *Industrial Waste*')
        st.markdown('- Factories release toxic chemicals and heavy metals into water bodies.')

        st.write(':two: *Agricultural Runoff*')
        st.markdown('- Pesticides and fertilizers wash into rivers and lakes.')

        st.write(':three: *Sewage and Wastewater*')
        st.markdown('- Untreated sewage enters water systems, spreading disease.')

        st.write(':four: *Plastic & Marine Litter*')
        st.markdown('- Plastic waste pollutes oceans and harms marine life.')

        st.write(':five: *Oil Spills*')
        st.markdown('- Accidental spills affect marine ecosystems and coastal areas.')

        st.write(':six: *Mining Activities*')
        st.markdown('- Runoff from mines carries toxic elements like mercury and arsenic.')

    elif topic == 'Water Pollution Prevention Techniques':
        st.write('### ✅ *Water Pollution Prevention Techniques*')

        st.write(':one: *Wastewater Treatment*')
        st.markdown('- Use treatment plants before releasing wastewater.')
        st.markdown('- Recycle industrial and domestic wastewater.')

        st.write(':two: *Sustainable Agriculture*')
st.markdown('- Use organic fertilizers, drip irrigation, crop rotation.')
        st.markdown('- Reduce pesticide and chemical runoff.')

        st.write(':three: *Plastic Ban & Cleanup*')
        st.markdown('- Avoid single-use plastics.')
        st.markdown('- Support beach and river cleanup efforts.')

        st.write(':four: *Eco-Friendly Products*')
        st.markdown('- Use biodegradable detergents and household cleaners.')

        st.write(':five: *Public Participation*')
        st.markdown('- Report illegal dumping.')
        st.markdown('- Join local water conservation programs.')

        st.write(':six: *Government Regulations*')
        st.markdown('- Enforce environmental laws.')
        st.markdown('- Penalize polluters and promote eco-friendly policies.')





