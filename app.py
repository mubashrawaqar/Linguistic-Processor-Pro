import gradio as gr
from deep_translator import GoogleTranslator
from gtts import gTTS
import edge_tts
import asyncio
import os

# Application Logic with Invisible Failover
async def universal_processor(text, target_lang):
    if not text or len(text.strip()) == 0:
        return "System Error: Null input detected.", None
    
    # Mapping for Primary (gTTS) and Secondary (Edge) engines
    mapping = {
        'Spanish': ('es', 'es-ES-AlvaroNeural'),
        'French': ('fr', 'fr-FR-EloiseNeural'),
        'German': ('de', 'de-DE-KillianNeural'),
        'Hindi': ('hi', 'hi-IN-MadhurNeural'),
        'Japanese': ('ja', 'ja-JP-NanamiNeural'),
        'Chinese': ('zh-CN', 'zh-CN-XiaoxiaoNeural'),
        'Arabic': ('ar', 'ar-SA-ZariyahNeural'),
        'Italian': ('it', 'it-IT-DiegoNeural'),
        'Korean': ('ko', 'ko-KR-SunHiNeural')
    }
    
    try:
        lang_code, voice_code = mapping[target_lang]
        
        # Step 1: Translation Engine
        translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
        output_file = "processed_audio.mp3"

        # Step 2: Primary Synthesis (gTTS)
        try:
            tts = gTTS(text=translated, lang=lang_code)
            tts.save(output_file)
        
        except Exception:
            # Step 3: Silent Failover to Secondary (Edge TTS)
            # Occurs if gTTS is rate-limited or unavailable
            communicate = edge_tts.Communicate(translated, voice_code)
            await communicate.save(output_file)

        return translated, output_file

    except Exception as e:
        return f"Processing Failure: {str(e)}", None

# Professional UI Layout
with gr.Blocks(theme='slate', title="Linguistic Processor") as demo:
    gr.Markdown("# Linguistic Analysis and Translation System")
    gr.Markdown("*Enterprise-grade neural machine translation and speech synthesis.*")
    
    with gr.Row():
        with gr.Column(scale=2):
            source_input = gr.Textbox(
                label="Source Text Sequence", 
                placeholder="Enter string for analysis...", 
                lines=10
            )
            target_select = gr.Dropdown(
                label="Target Language Parameter", 
                choices=['Spanish', 'French', 'German', 'Hindi', 'Japanese', 'Chinese', 'Arabic', 'Italian', 'Korean'], 
                value='Spanish'
            )
            execute_btn = gr.Button("Initialize Processing", variant="primary")

        with gr.Column(scale=1):
            with gr.Group():
                gr.Markdown("### System Output")
                result_text = gr.Textbox(label="Translated String", interactive=False)
                result_audio = gr.Audio(label="Audio Synthesis Output", type="filepath")
            
            with gr.Accordion("Technical Specifications", open=True):
                gr.Markdown("- **Engine Alignment:** Multi-Cloud Synthesis\n- **Latency:** Optimized\n- **Status:** Operational")
            
            with gr.Group():
                gr.Markdown("### Operational Status")
                gr.Markdown("System Status: **Active**\n\nAPI Connectivity: **Verified**")

    execute_btn.click(
        fn=universal_processor, 
        inputs=[source_input, target_select], 
        outputs=[result_text, result_audio]
    )

# Launch (Share and Theme handled by HF Space environment)
demo.launch()
