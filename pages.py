import streamlit as st

def home():
    st.title("코코포리아 편집 사이트 사용법")
    st.subheader("① 텍스트 추출 사용법")
    st.markdown("1) 먼저 코코포리아에서 [전체 로그 추출], 혹은 그냥 [로그 추출]을 진행합니다.")
    st.image('imgs/edit_step1.png', caption='[전체 로그 추출]의 경우 모든 탭의 로그를, [로그 추출]의 경우 현재 내가 보고 있는 탭의 로그만 출력합니다.')
    st.divider()
    st.markdown("2) 이후, 다운로드 된 HTML 파일을 본 사이트의 [로그 자르기] 탭에 들어가 업로드합니다.")
    st.image('imgs/edit_step2.png')
    st.divider()
    st.markdown("3) 그 이후, HTML 파일 우클릭 > 연결 프로그램 > 메모장을 클릭해 HTML 파일을 메모장으로 엽니다.")
    st.image('imgs/edit_step3.png')
    st.divider()
    st.markdown("4) 메모장을 열어 로그를 자를 첫 부분을 선택합니다. 이때 해당 문장을 드래그했을 때 하단에 나타나는 Ln 옆의 숫자를 봐주세요.")
    st.image('imgs/edit_step4.png', caption="해당 사진에서 시작 라인은 77623입니다.")
    st.divider()
    st.markdown("5) 그리고 자를 부분의 마지막에 해당하는 대사를 드래그하고, 마찬가지로 하단의 Ln옆의 숫자를 확인합니다.")
    st.image('imgs/edit_step5.png', caption="해당 사진에서 종료 라인은 77671입니다.")
    st.divider()
    st.markdown("6) [시작 라인]과 [종료 라인]을 입력한 뒤 [편집 파일 다운로드]를 누르면, 해당 라인만큼 잘린 파일을 다운로드 받을 수 있습니다. 이후 해당 파일을 코코로드에 넣으면 됩니다.")
    st.image('imgs/edit_step6.png', caption="의도했던 텍스트만큼 잘린 걸 볼 수 있습니다.")
    st.divider()
    
    st.subheader("② 이미지 변경 사용법")
    st.markdown("1) 먼저 코코로그에서 로그 편집을 진행합니다.")
    st.image('imgs/img_step1.png', caption='코코로그에서 편집할 예시 파일입니다.')
    st.image('imgs/img_step2.png', caption='위의 HTML 파일을 코코로그에 넣어 해당 이미지처럼 편집합니다.')
    st.divider()
    st.markdown("2) 이후, 코코로그에서 다운로드 된 HTML 파일을 본 사이트의 [로그 자르기] 탭에 들어가 업로드합니다.")
    st.image('imgs/img_step3.png')
    st.divider()
    st.markdown("3) 그 이후, 해당 HTML을 파일 우클릭 > 연결 프로그램 > 메모장을 클릭해 HTML 파일을 메모장으로 엽니다.")
    st.image('imgs/img_step4.png')
    st.divider()
    st.markdown("4) 메모장을 열어 이미지를 변경할 첫 부분을 선택합니다. 이때 해당 문장을 드래그했을 때 하단에 나타나는 Ln 옆의 숫자를 봐주세요.")
    st.image('imgs/img_step5.png', caption="해당 사진에서 시작 라인은 34입니다.")
    st.divider()
    st.markdown("5) 그리고 이미지를 변경할 부분의 마지막에 해당하는 대사를 드래그하고, 마찬가지로 하단의 Ln옆의 숫자를 확인합니다.")
    st.image('imgs/img_step6.png', caption="해당 사진에서 종료 라인은 52입니다.")
    st.divider()
    st.markdown("6) [시작 라인]과 [종료 라인]을 입력하고, 코코로그 사용 시 사용했던 [기존 이미지 주소]와 [변경할 이미지 주소]를 입력하고 [편집 파일 다운로드]를 누르면, 선택했던 라인만큼 프로필 이미지가 변경된 HTML 파일을 다운로드 받을 수 있습니다.")
    st.image('imgs/img_step7.png', caption="의도했던 텍스트만큼 이미지가 수정되어 있는 걸 볼 수 있습니다.")


def edit_text():
    st.markdown("## 코코포리아 텍스트 추출하기")
    st.info("코코포리아에서 다운로드 받은 HTML 파일을 잘라, 편집된 HTML 파일을 다운 받을 수 있게 합니다.")
    
    st.markdown("#### 1) 파일 업로드")
    uploaded_files = st.file_uploader("코코포리아에서 [전체 로그 출력]으로 추출한 HTML 파일을 업로드 해주세요.", type=['html'])
    st.divider()
    st.markdown("#### 2) 시작 라인과 종료 라인 입력")
    st.caption("추출할 로그의 [시작 라인]과 [종료 라인]을 숫자로 지정해주세요. HTML 파일을 열어 메모장에서 추출을 시작하는 줄이 몇 번째 줄인지 확인해주시면 됩니다. 이때 만약 끝까지 출력한다면 [종료 라인]은 0 그대로 두셔도 됩니다.")

    col1, col2 = st.columns(2)
    with col1:
        start_line = st.number_input('시작 라인')
    with col2:
        end_line = st.number_input('종료 라인')

    # 파일 편집 파트
    first_text = "<!DOCTYPE html>\n<html lang=\"ja\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\" />\n    <title>ccfolia - logs</title>\n  </head>\n  <body>\n"
    second_text = "\n  </body>\n</html>"
    
    if uploaded_files is not None and start_line != 0.0:
    # 바이트 데이터를 문자열로 변환
        string_data = uploaded_files.getvalue().decode("utf-8")
        # print(string_data)
        p_tags_with_content = string_data.split("\n")
        

        if start_line == 0.0:
            start_line = 15
        else:
            start_line = int(start_line)

        if end_line == 0.0:
            end_line = len(p_tags_with_content)
        else:
            end_line = int(end_line)

        final_content = p_tags_with_content[start_line-5:end_line + 3]
        final_content.insert(0, first_text)
        final_content.append(second_text)
        final_text = '\n'.join(final_content)
        with open("ccfolia_edit_file.html", "w") as f:
            f.write(final_text)
        with open("ccfolia_edit_file.html", "r") as file:
            btn = st.download_button(
                    label="편집 파일 다운로드",
                    data=file,
                    file_name="ccfolia_edit_file.html",
                )

def image_change():
    st.markdown("## 코코포리아 로그 이미지 변경하기")
    st.info("코코로그에서 편집이 끝난 HTML 파일을 업로드해, 편집된 HTML 파일을 다운 받을 수 있게 합니다.")
    
    st.markdown("#### 1) 파일 업로드")
    uploaded_files = st.file_uploader("코코로그에서 편집이 끝난 HTML 파일을 업로드 해주세요.", type=['html'])
    st.divider()

    st.markdown("#### 2) 시작 라인과 종료 라인 입력")
    st.caption("로그에서 변경하고 싶은 부분의 [시작 라인]과 [종료 라인]을 숫자로 지정해주세요. HTML 파일을 열어 메모장에서 추출을 시작하는 줄이 몇 번째 줄인지 확인해주시면 됩니다. 이때 만약 끝까지 출력한다면 [종료 라인]은 0 그대로 두셔도 됩니다.")

    col1, col2 = st.columns(2)
    with col1:
        start_line = st.number_input('시작 라인')
    with col2:
        end_line = st.number_input('종료 라인')

    st.divider()
    st.markdown("#### 3) 외부 이미지 링크 입력")
    st.caption("기존의 이미지 링크와 변경할 이미지 링크를 작성해주세요.")

    col1, col2 = st.columns(2)
    with col1:
        before_img = st.text_input('기존 이미지 주소')

    with col2:
        after_img = st.text_input('변경할 이미지 주소')


    st.divider()

    if uploaded_files is not None and after_img != "":
    # 바이트 데이터를 문자열로 변환
        string_data = uploaded_files.getvalue().decode("utf-8")
        # print(string_data)
        p_tags_with_content = string_data.split("\n")
        

        if start_line == 0.0:
            start_line = 15
        else:
            start_line = int(start_line)

        if end_line == 0.0:
            end_line = len(p_tags_with_content)
        else:
            end_line = int(end_line)

        file_content = p_tags_with_content[start_line-7:end_line + 2]

        for i in range(start_line - 7, end_line + 3):
            if before_img in p_tags_with_content[i]:
                p_tags_with_content[i] = p_tags_with_content[i].replace(before_img, after_img)

        final_text = '\n'.join(p_tags_with_content)
        with open("ccfolia_edit_file.html", "w", encoding="UTF-8") as f:
            f.write(final_text)
        with open("ccfolia_edit_file.html", "r", encoding="UTF-8") as file:
            btn = st.download_button(
                    label="편집 파일 다운로드",
                    data=file,
                    file_name="ccfolia_img_edit_file.html",
                )