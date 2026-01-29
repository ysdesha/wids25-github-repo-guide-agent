import streamlit as st
import re
from week3 import get_repo, fetch_readme, fetch_repo_tree, filter_tree, extract_important_files, generate_guided_tour

# ----------------------
# Page config
# ----------------------
st.set_page_config(
    page_title="RepoGuide | Developer Tour",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------
# Clean Minimalist CSS
# ----------------------
st.markdown("""
    <style>
    /* Force dark background for the entire app */
    .stApp {
        background-color: #0d1117;
    }
    
    /* SIDEBAR: Force visibility for all text elements */
    section[data-testid="stSidebar"] .stMarkdown p, 
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] div[data-testid="stCaptionContainer"] {
        color: #e6edf3 !important;
    }

    section[data-testid="stSidebar"] h1 {
        color: #ffffff !important;
        font-weight: 700;
        margin-bottom: 0px;
    }

    /* INPUT FIELDS */
    .stTextInput input {
        background-color: #0d1117 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
    }

    /* BUTTONS */
    .stButton>button {
        width: 100%;
        border-radius: 6px;
        background-color: #238636; /* GitHub Green */
        color: white !important;
        border: 1px solid rgba(240,246,252,0.1);
    }
    
    .stButton>button:hover {
        background-color: #2ea043;
        color: white !important;
    }

    /* Reset Button (Gray) */
    div[data-testid="column"]:nth-of-type(2) .stButton>button {
        background-color: #21262d;
        color: #c9d1d9 !important;
        border: 1px solid #30363d;
    }

    /* MAIN CONTENT: Ensure all markdown text is white/light gray */
    .main .stMarkdown p, .main .stMarkdown h1, .main .stMarkdown h2, 
    .main .stMarkdown h3, .main .stMarkdown li, .main .stMarkdown code {
        color: #e6edf3 !important;
    }
    
    /* Divider line color */
    hr {
        border-color: #30363d !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------
# Helper: Render guide with optional code highlighting
# ----------------------
def render_guide(guide_text):
    # Split by triple backticks to separate code blocks
    parts = re.split(r"```(.*?)```", guide_text, flags=re.DOTALL)
    for i, part in enumerate(parts):
        if i % 2 == 1:  # odd indices are code blocks
            st.code(part.strip(), language="python")
        else:
            st.markdown(part.strip())

# ----------------------
# Sidebar Inputs
# ----------------------
with st.sidebar:
    st.title("RepoNavigator")
    st.markdown("Your AI assistant for exploring GitHub repositories")
    st.markdown("---")
    
    if "owner" not in st.session_state:
        st.session_state.owner = ""
    if "repo_name" not in st.session_state:
        st.session_state.repo_name = ""
    if "guide" not in st.session_state:
        st.session_state.guide = ""

    st.session_state.owner = st.text_input("Repository Owner", value=st.session_state.owner, placeholder="e.g. PyGithub")
    st.session_state.repo_name = st.text_input("Repository Name", value=st.session_state.repo_name, placeholder="e.g. PyGithub")

    st.markdown(" ") 
    col1, col2 = st.columns(2)
    with col1:
        generate_btn = st.button("Generate")
    with col2:
        reset_btn = st.button("Reset")
    
    st.markdown("---")
    st.caption("Enter the owner and name of a public GitHub repository.")

# ----------------------
# Main Page Header
# ----------------------
st.markdown("""
    <div style='background-color:#161b22; padding: 20px; border-radius:8px; margin-bottom:20px;'>
        <h1 style='color:#ffffff; margin:0;'>RepoNavigator</h1>
        <p style='color:#8b949e; margin:0;'>Your AI assistant for exploring GitHub repositories</p>
    </div>
""", unsafe_allow_html=True)

# ----------------------
# Logic
# ----------------------
if generate_btn:
    if not st.session_state.owner or not st.session_state.repo_name:
        st.sidebar.warning("Please enter both owner and repository name.")
    else:
        try:
            with st.spinner("Fetching repository data..."):
                repo = get_repo(st.session_state.owner, st.session_state.repo_name)
                readme_text = fetch_readme(repo)
                tree_items = fetch_repo_tree(repo)
                files = filter_tree(tree_items)
                important_files = extract_important_files(files)
                st.session_state.guide = generate_guided_tour(readme_text, important_files)
        except Exception as e:
            st.sidebar.error(f"Error: {e}")

# ----------------------
# Reset button fix (no st.experimental_rerun)
# ----------------------
if reset_btn:
    for key in ["owner", "repo_name", "guide"]:
        if key in st.session_state:
            st.session_state[key] = ""

# ----------------------
# Display Guide
# ----------------------
if st.session_state.guide:
    st.markdown(f"## Repository Guide: {st.session_state.owner} / {st.session_state.repo_name}")
    st.markdown("---")
    
    # Wrap guide in an expander for clean UI
    with st.expander("View Full Guide", expanded=True):
        render_guide(st.session_state.guide)
else:
    # Empty state placeholder
    st.markdown("""
        <div style='text-align: center; padding: 150px 20px; background-color: #161b22; border-radius: 12px; color: #8b949e;'>
            <h2 style='font-weight: 400;'>Welcome to RepoNavigator</h2>
            <p>Enter repository details in the sidebar to generate an AI-powered developer guide.</p>
        </div>
    """, unsafe_allow_html=True)
