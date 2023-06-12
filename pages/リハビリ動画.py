import streamlit as st
import pydeck as pdk
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

def get_location_by_address(address):
    location = geolocator.geocode(address)
    if location is None:
        return None
    return (location.latitude, location.longitude)

st.title('住所から緯度・経度への変換')

address = st.text_input('住所を入力してください:')

if st.button('変換'):
    location = get_location_by_address(address)
    if location is None:
        st.write('指定された住所の位置を見つけることができませんでした。')
    else:
        st.write('緯度: ', location[0])
        st.write('経度: ', location[1])
        # Create a map centered at the location
        view_state = pdk.ViewState(
            latitude=location[0],
            longitude=location[1],
            zoom=10
        )
        layer = pdk.Layer(
            'ScatterplotLayer',
            data={'coordinates': [location]},
            get_position='coordinates',
            get_radius=1000,
            get_fill_color=[255, 0, 0]
        )
        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state
        )
        st.pydeck_chart(deck)


