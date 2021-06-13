from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("BQCNxA2krVlpOwwpzOQGujW45yKZqifS7jkpCZ0D0NU2YGvKflRUpW13-pzLe4aD-S4a6ynQXr6bvYphbTGxiBn2-aLqTN4bRqHkpcvSYoqM1FMpm0WwYqHeBuWEAaA5HnATu7q3RrglNctVwhFOjv4i85ZjFYONFqkB0tStnRLlt3ayfnIWrur6Ww9yS_g0u3TqBgd4CPNeU4XPMVlqcdaaCxbSp_msPh5p9fVxIj7k-elzCkClByHGR9tPjAbkEhKoi9qGR7CeuWSI4InbsBn-WAs5sGmCvS7JELGE1alnxKPwfmxpbbxpD69ozOArBPgFQ55Xn11oYLfN3_TPQlAFPpWp3QA", "session")
BOT_TOKEN = getenv("1783812858:AAHRM4OHST08YWY4p2Suwk0LVU9C2gM8XW0")
BOT_NAME = getenv("MUSIC_BOT")
admins = {"991509668"}
API_ID = int(getenv("5586962"))
API_HASH = getenv("516bddd96363744455f44778452e55f6")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("991509668").split()))
