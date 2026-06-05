import streamlit as st
import tempfile
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found. Check your .env file.")
    st.stop()

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:
    st.title("🏢 UnderwriteAI")

    st.markdown("""
    ### Features

    ✅ Policy Summary

    ✅ Risk Assessment

    ✅ Approval Recommendation

    ✅ Missing Information Detection

    ✅ Underwriting Report

    ✅ RAG Question Answering
    """)

# ----------------------------
# Main UI
# ----------------------------

st.title("📄 UnderwriteAI")
st.subheader(
    "RAG-Based Insurance Underwriting Assistant"
)

uploaded_file = st.file_uploader(
    "Upload Insurance Policy PDF",
    type="pdf"
)

if uploaded_file:

    st.metric(
        "Document Status",
        "Processed"
    )

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.split_documents(pages)
    
    embeddings = OpenAIEmbeddings()

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    text = ""

    for page in pages:
        text += page.page_content

    st.success("PDF Loaded Successfully!")

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    # Summary

    if st.button("📋 Generate Summary"):

        prompt = f"""
        Analyze this insurance policy.

        Provide:
        1. Policy Type
        2. Coverage
        3. Exclusions
        4. Premium Details
        5. Important Clauses

        Policy:

        {text[:12000]}
        """

        with st.spinner("Analyzing policy..."):
            response = llm.invoke(prompt)

        st.subheader("📋 Policy Summary")
        st.write(response.content)

    # Risk Assessment

    if st.button("⚠️ Risk Assessment"):

        risk_prompt = f"""
        You are a senior insurance underwriter.

        Analyze this insurance policy.

        Provide:

        1. Overall Risk Score (1-10)
        2. Major Risks
        3. Red Flags
        4. Missing Information
        5. Underwriting Recommendation

        Policy:

        {text[:12000]}
        """

        with st.spinner("Analyzing risk..."):
            risk_response = llm.invoke(risk_prompt)

        st.subheader("⚠️ Risk Assessment")
        st.write(risk_response.content)

    # Missing Information

    if st.button("📋 Missing Information"):

        missing_prompt = f"""
        Act as a commercial underwriter.

        Identify:

        1. Missing Information
        2. Why it matters
        3. Risk Impact
        4. Information Required

        Policy:

        {text[:12000]}
        """

        with st.spinner("Analyzing missing information..."):
            missing_response = llm.invoke(
                missing_prompt
            )

        st.subheader(
            "📋 Missing Information Analysis"
        )

        st.write(
            missing_response.content
        )

    # Approval Recommendation

    if st.button("✅ Approval Recommendation"):

        approval_prompt = f"""
        Act as a senior insurance underwriter.

        Based on the policy provide:

        1. Decision (Approve / Reject / Review)
        2. Confidence Score (%)
        3. Reasoning
        4. Suggested Actions

        Policy:

        {text[:12000]}
        """

        approval_response = llm.invoke(
            approval_prompt
        )

        st.subheader(
            "✅ Approval Recommendation"
        )

        st.write(
            approval_response.content
        )

    # Underwriting Report

    if st.button("📄 Generate Report"):

        report_prompt = f"""
        Create a professional underwriting report.

        Include:

        1. Executive Summary
        2. Coverage Analysis
        3. Risk Assessment
        4. Missing Information
        5. Recommendation

        Policy:

        {text[:12000]}
        """

        report_response = llm.invoke(
            report_prompt
        )

        st.metric(
            "Risk Score",
            "7/10"
        )

        st.progress(70)

        st.subheader(
            "📄 Underwriting Report"
        )

        st.write(
            report_response.content
        )
        st.download_button(
            "⬇️ Download Report",
            report_response.content,
            file_name="underwriting_report.md"
        )

    # RAG Q&A

    st.divider()

    question = st.text_input(
        "Ask a question about the policy"
    )

    if question:

        retrieved_docs = retriever.invoke(
            question
        )

        if not retrieved_docs:
            st.write("No relevant documents found for this question.")
        else:
            context = "\n\n".join(
                [doc.page_content for doc in retrieved_docs]
            )
            with st.expander("Retrieved Context"):
                st.write(context[:2000])

            qa_prompt = f"""
            You are an insurance expert.

            Use ONLY the context below.

            Context:

            {context}

            Question:

            {question}
            """

            answer = llm.invoke(
                qa_prompt
            )

            st.subheader("💬 Answer")
            st.write(answer.content)

