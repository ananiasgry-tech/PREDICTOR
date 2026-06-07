[app]
title = Predictor Futebol
package.name = predictorapp
package.domain = org.ananias
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# AQUI ESTÁ O SEGREDO: Adicionamos requests, urllib3, certifi e idna
requirements = python3,kivy,requests,urllib3,certifi,idna

# Permissão obrigatória para o seu app buscar os dados das partidas na internet
android.permissions = INTERNET

android.archs = armeabi-v7a, arm64-v8a
