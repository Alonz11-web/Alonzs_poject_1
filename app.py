import streamlit as st

st.set_page_config(page_title="חיזוי משקל פינגווין", page_icon="🐧")

# כותרת והסבר קצר
st.title("🐧 מודל חיזוי משקל פינגווין")
st.write("הזינו את אורך הסנפיר (במ\"מ) כדי לקבל את המשקל החזוי של הפינגווין (בגרמים).")

# פרמטרי המודל הליניארי
W = 40.27238311213039
B = -3925.6906470178465

# קלט מהמשתמש
flipper_length = st.number_input(
    label="אורך סנפיר (מ\"מ):",
    min_value=100.0,
    max_value=300.0,
    value=200.0,
    step=1.0
)

# כפתור חישוב
if st.button("חשב משקל"):
    # חישוב הנוסחה הליניארית: y = w * x + b
    predicted_weight = W * flipper_length + B
    
    if predicted_weight > 0:
        st.success(f"⚖️ המשקל החזוי: **{predicted_weight:.2f} גרם** ({predicted_weight / 1000:.2f} ק\"ג)")
    else:
        st.warning("אורך הסנפיר שהוזן קטן מדי והתוצאה אינה הגיונית פיזיקלית.")

st.divider()
st.caption(f"משוואת המודל: $y = {W:.2f} \\cdot x + ({B:.2f})$")
