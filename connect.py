import PyPDF2
import streamlit as st
from io import BytesIO

st.set_page_config(page_title='PDF結合')
st.markdown('#### PDF結合')

# ***ファイルアップロード 今期***
pdf1 = st.file_uploader('PDF1の読み込み', type='pdf', key='pdf1')

if not pdf1:
    st.info('PDF1を選択してください。')
    st.stop() 

pdf2 = st.file_uploader('PDF2の読み込み', type='pdf', key='pdf2')

if not pdf2:
    st.info('PDF2を選択してください。')
    st.stop()

#ファイル名取得
pdf1_name = pdf1.name
name1 = pdf1_name.split('_')[1]
name2 = pdf1_name.split('_')[2]
new_file_name = name1 + '_' + name2


#インスタンス化
pdf_join = PyPDF2.PdfMerger()

# pdf結合
for pdf_file in [pdf1, pdf2]:
    pdf_data = pdf_file.read()
    pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_data))
    pdf_join.append(pdf_reader)

    #BytesIOを使用してpdf_dataをバイトストリームに変換し、PyPDF2.PdfFileReader()を使用して
    # pdf_readerというPDFリーダーオブジェクトを作成

# 結合されたPDFデータを一時的に保存するためのBytesIOオブジェクトであるoutput_pdfを作成
output_pdf = BytesIO()
#結合されたPDFデータをoutput_pdfに書き込み
pdf_join.write(output_pdf)
#output_pdf.getvalue()によって取得される結合されたPDFデータがダウンロード
st.download_button('結合されたPDFをダウンロード', output_pdf.getvalue(), file_name=new_file_name)
