import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()

def converter(value, from_unit, to_unit):
    try:
        if from_unit in ["celsius", "fahrenheit", "kelvin"] and to_unit in ["celsius", "fahrenheit", "kelvin"]:
            result = ureg.Quantity(value, ureg[from_unit]).to(ureg[to_unit])
        else:
            result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude
    except Exception as e:
        return f"Error: {e}"

st.set_page_config(page_title="Unit Converter", layout="wide")

st.markdown(
    """
    <style>
        .stApp { background-color: #1ACFD6; }
    </style>
    """, 
    unsafe_allow_html=True
)

st.title('Unit Converter 🔄')
st.subheader("A Unit Converter to convert all the Units")

categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"],
    "Area": ["square meter", "square kilometer", "square foot", "square inch", "acre", "hectare"],
    "Volume": ["liter", "milliliter", "cubic_meter", "gallon", "pint"],
    "Speed": ["meter second", "kilometer hour", "mile hour", "knot"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour"],
    "Pressure": ["pascal", "bar", "atmosphere", "torr", "psi"],
    "Data Storage": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"]
}

category = st.selectbox("Select a Magnitude to Convert", list(categories.keys()))
from_unit = st.selectbox("From Unit", categories[category])
to_unit = st.selectbox("To Unit", categories[category])
value = st.number_input("Enter value", min_value=0.0, step=0.1)

if st.button("Convert"):
    result = converter(value, from_unit, to_unit)
    
    if "Error" in str(result):
        st.error(result)
    else:
        st.markdown(
            f'<p style="color: #ffffff; font-size: 40px; font-weight: bold;">'
            f'Answer : {value} {from_unit} = {result} {to_unit}</p>',
            unsafe_allow_html=True
        )