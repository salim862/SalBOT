import flet as ft
import cohere

co = cohere.Client(api_key="0jIkLpJtRGU3R16d2y5tvmwgU8mSixprpWYnxYSL")

def main(page):
    page.window.width = 360
    page.window.height = 700
    page.title = "SaBOT"

    response_display = ft.Text(value="", expand=1)

    message_input = ft.TextField(
        label="Message SaBOT:",
        prefix_icon=ft.icons.MESSAGE,
        width=page.window.width - 40
    )

    def get_response(e):
        message = message_input.value
        stream = co.chat_stream(
            model='command-r-plus',
            message=f'<{message}>',
            temperature=0.3,
            prompt_truncation='AUTO',
            connectors=[{"id":"web-search"}]
        )
        response_text = ""
        for event in stream:
            if event.event_type == "text-generation":
                response_text += event.text

        response_display.value = response_text
        page.update()
        
        message_input.value = ""
        page.update()

    send_button = ft.ElevatedButton(text="send", color="white", bgcolor="blue", on_click=get_response, width=200)

    page.add(
        ft.Column([
            response_display,
            message_input,
            ft.Container(height=10),
            ft.Row([send_button], alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True)
    )

ft.app(target=main)
