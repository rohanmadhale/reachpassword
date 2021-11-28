# Import libraries
import streamlit as st
import random
import pandas as pd
from streamlit import legacy_caching
# ------------------------------------------------------------------------------
# Set page configuration (to be set only once)
st.set_page_config(page_title='Password Generator', page_icon=None,
                   layout='centered', initial_sidebar_state='auto')
# Set page title
st.title('Simple Password Generator')
# Set slider to change number of words
num_of_words = st.slider("Select number of words (default is 3 words) : ",
                         min_value=1, max_value=10, value=3)
# ------------------------------------------------------------------------------
# Read word dictonary from GitHub
# url = 'https://github.com/rohanmadhale/pass_phrase_generator/blob/main/pass_phrase_words.txt?raw=true'
url = 'https://github.com/rohanmadhale/data/blob/main/pass_phrase_words.txt?raw=true'
# url = pd.read_csv('pass_phrase_words.txt')
# word_dict = pd.read_csv(url)
# words = word_dict['a'].tolist()
# ------------------------------------------------------------------------------


def rerun():
    raise st.script_runner.RerunException(
        st.script_request_queue.RerunData(None))
# ------------------------------------------------------------------------------
# Function to generate password
# stramlit.cache is used to change separator of the password without refreshing the page


@st.cache(suppress_st_warning=True, show_spinner=False)
def generate_password():
    word_dict = pd.read_csv(url)
    words = word_dict[word_dict.columns[0]].to_list() # word_dict['a'].tolist()
    words = [str(i) for i in words]
    password = [i.capitalize() for i in random.sample(
        [i for i in words if len(i) == random.randint(3, 9)], k=num_of_words)]
    password.append(str(random.randint(1, 9)))
    return password


password = generate_password()
# ------------------------------------------------------------------------------
# Get password length
pass_len = 3
for char in password:
    pass_len = pass_len + len(char)
# ------------------------------------------------------------------------------
# Change separator
x = st.selectbox('Select separator below : ',
                 options=['#', '@', '!', '-', '%'])
# x = st.sidebar.selectbox('Change Separator', options=['!', '@','#','-','%'])
if x == '#':
    string = '#'.join(password)
elif x == '@':
    string = '@'.join(password)
elif x == '!':
    string = '!'.join(password)
elif x == '-':
    string = '-'.join(password)
elif x == '%':
    string = '%'.join(password)
else:
    string = '#'.join(password)
# ------------------------------------------------------------------------------
st.subheader('Your password is : ' + string)
st.write(f'\nThis password has **_{pass_len}_** characters')
# if st.button("Click here to copy the password"):
    # pc.copy(string)
    # df = pd.DataFrame([string])
    # df.to_clipboard(index=False, header=False)
    # r = Tk()
    # r.withdraw()
    # r.clipboard_clear()
    # r.clipboard_append(string)
    # r.update() # now it stays on the clipboard after the window is closed
    # r.destroy()
    # st.success('Copied to Clipboard!')
if st.button("Click here to generate new password"):
    legacy_caching.clear_cache()
    rerun()
st.write('\nYou can check the strength of your password on below websites : ')
st.write('https://howsecureismypassword.net/')
st.write('https://www.my1login.com/resources/password-strength-test/')
st.write('https://password.kaspersky.com/')


st.markdown("<h5 style='text-align: center; color: white;'>🌟 Developed by  <a href='https://www.rohan.contact' target='_blank'>Rohan Madhale</a> 🌟 </h5>", unsafe_allow_html=True)

