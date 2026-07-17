import streamlit as st
from PIL import Image
from ultralytics import YOLO
import ollama
from datetime import date

st.set_page_config(page_title="AI Steel QA Inspector", layout="wide")
st.title("🏭 AI-Powered Steel Surface Inspection")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

uploaded_file = st.file_uploader("Upload a steel surface image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with st.spinner("Detecting defects..."):
        results = model.predict(image, conf=0.15)
        r = results[0]
        annotated_image = r.plot()

        detections = []
        for box in r.boxes:
            cls_id = int(box.cls[0])
            detections.append({
                "label": model.names[cls_id],
                "confidence": float(box.conf[0])
            })

    with col2:
        st.subheader("Detected Defects")
        st.image(annotated_image, use_container_width=True)

    st.divider()

    if detections:
        st.subheader("Defects Found")
        for d in detections:
            st.write(f"• **{d['label']}** — {d['confidence']*100:.1f}% confidence")
    else:
        st.info("No defects detected.")

    st.divider()
    st.subheader("📋 AI-Generated Inspection Report")

    defect_text = "\n".join(f"- {d['label']} ({d['confidence']*100:.0f}%)" for d in detections) if detections else "No defects detected."

    prompt = f"""You are a quality assurance inspector for a steel manufacturing plant.

Based on the following detected surface defects, write a professional inspection report.

Detected Defects:
{defect_text}

Format your response EXACTLY like this:

Inspection Date: {date.today().strftime('%d %B %Y')}
Detected Defects:
{defect_text}
Summary:
<2-3 sentence summary>
Severity:
<Low, Medium, or High>
Recommended Action:
- <action 1>
- <action 2>
- <action 3>
"""

    with st.spinner("Generating report with Llama 3.2..."):
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
        report = response["message"]["content"]

    st.markdown(report)
    st.download_button("Download Report", report, file_name="inspection_report.txt")
    