# Image to Audio Story Converter
Este projeto tem como objetivo transformar uma imagem em uma narrativa curta gerada por IA, e em seguida converter essa narrativa em áudio. Utilizamos modelos de IA para transformar imagens em texto e, a partir do texto, gerar uma história criativa que é finalmente convertida em um arquivo de áudio usando a API do Google Text-to-Speech (gTTS).

## Visão Geral
O projeto recebe uma imagem como entrada, utiliza o modelo Salesforce/blip-image-captioning-base para gerar uma descrição baseada na imagem, cria uma história curta com o modelo GPT-2, e converte essa história em áudio usando gTTS. A interface gráfica é construída com Streamlit para facilitar o upload de imagens e a exibição dos resultados.

## Funcionalidades
- Conversão de imagem para texto: Captura a descrição da imagem.
- Geração de histórias: Cria uma pequena narrativa com base na descrição da imagem.
- Conversão de texto para fala: Transforma a história gerada em áudio.
- Interface amigável: Interface gráfica desenvolvida em Streamlit para facilitar o uso
