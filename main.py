import streamlit as st
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import hmac

# Warningの非表示
st.set_option('deprecation.showPyplotGlobalUse', False)

# データの取得と表示
def get_data(start, end, id):
    df = web.DataReader(id, 'fred', start, end)
    return df

def plot_graph(start):
    end = dt.date.today()
    jpn = get_data(start, end, 'IRLTLT01JPM156N')
    usa = get_data(start, end, 'DGS10')
    
    ax_jpn = plt.subplot(211)
    ax_jpn.set_xlim(start,end)
    ax_jpn.plot(jpn.index, jpn, label='JPN')
    ax_jpn.legend()

    ax_usa = plt.subplot(212)
    ax_usa.set_xlim(start,end)
    ax_usa.plot(usa.index, usa, label='USA')
    ax_usa.legend()
    
    st.pyplot()

# グローバルパスワード用のコード

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# ここまでがパスワードチェック用

min_date = dt.date(2012,1,1)
max_date = dt.date.today()

start = st.date_input('start date', min_date, min_value=min_date, max_value=max_date)

if st.button('plot'):
    plot_graph(start)

    
