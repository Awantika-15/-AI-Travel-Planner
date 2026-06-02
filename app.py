import streamlit as st

from agent import travel_agent

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")

st.title("✈️ AI Travel Planner")
st.markdown("### Plan your trip smartly with AI 🚀")

source = st.text_input("🛫 Enter Source City").title()
destination = st.text_input("📍 Enter Destination City").title()

if st.button("Search Travel Details"):

    try:

        trip = travel_agent(source, destination)

        flight = trip["flight"]
        hotel = trip["hotel"]
        weather = trip["weather"]
        places = trip["places"]

        st.success("Travel Details Found Successfully ✅")

        st.header(f"Your Trip from {source} to {destination}")

        # Flight
        st.subheader("✈️ Flight Selected")

        if isinstance(flight, dict):
            st.write(
                f"**{flight['airline']}** (₹{flight['price']}) "
                f"- Departs {flight['from']} at {flight['departure_time']}"
            )
        else:
            st.write(flight)

        # Hotel
        st.subheader("🏨 Hotel Booked")

        if isinstance(hotel, dict):
            st.write(
                f"**{hotel['name']}** "
                f"(₹{hotel['price_per_night']}/night, {hotel['stars']}-star)"
            )
        else:
            st.write(hotel)

        # Weather
        st.subheader("🌦️ Weather")
        st.write(weather)

        # AI Summary
        st.subheader("🧠 AI Travel Summary")

        if isinstance(flight, dict) and isinstance(hotel, dict):
            st.write(
                f"""
                Your trip from **{source}** to **{destination}**
                includes a flight with **{flight['airline']}**,
                accommodation at **{hotel['name']}**,
                current weather of **{weather}**,
                and visits to top attractions in the city.
                """
            )

        # Itinerary
        st.subheader("📍 Itinerary")

        if isinstance(places, list) and len(places) > 0:

            for i, place in enumerate(places[:3], start=1):

                st.markdown(
                    f"""
### Day {i}

📍 **Place:** {place['name']}

🏷️ **Type:** {place['type']}

⭐ **Rating:** {place['rating']}
"""
                )

        else:
            st.write("No tourist places found")

    except Exception as e:
        st.error(f"Error: {e}")