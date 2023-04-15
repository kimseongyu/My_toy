# pip install openpyxl
import openpyxl
# pip install googletrans==4.0.0-rc1
import googletrans

# 엑셀 파일 열기
wb = openpyxl.load_workbook('translate.xlsx')

# 번역기 객체 생성
translator = googletrans.Translator()

# 현재 활성화된 시트 선택
sheet = wb.active

# A행에 대해 반복
for cell in sheet['A'][1:]:
    # 영어 단어와 품사 가져오기
    eng_word = cell.value
    
    # 한국어 단어로 번역 및 파싱
    korean_words = []
    while len(korean_words) == 0:
        try: korean_words = translator.translate(eng_word, src ='en', dest = 'ko').extra_data['parsed'][1][0][0][5][0][4]
        except: continue
    
    # 단어장에 삽입될 한국어 단어
    korean_word = ""
    
    # 단어장에 단어 추가, max:최대 단어 갯수
    max = 2
    count = 0 
    for i in korean_words:
        if count > max-1: break
        elif count == max-1:
            korean_word += i[0]
        else:
            korean_word += i[0] + ', '
        count += 1
    # c 행에 한국어 단어 쓰기
    try:sheet.cell(row=cell.row, column=3, value=korean_word)
    except:continue

# 변경 내용 저장
wb.save('translate.xlsx')