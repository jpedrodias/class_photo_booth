#!/bin/bash

echo 'Verificando Redis...';
python worker.py --verify;
if [ \$$? -eq 0 ]; then
  echo 'Redis está pronto!';
  echo 'Iniciando RQ worker em background...';
  python worker.py --forever &
  WORKER_PID=\$$!;
  echo \"RQ worker iniciado com PID: \$$WORKER_PID\";
  echo \"Running App: ${FLASKAPP_FILE}\";
  gunicorn -w 10 -b :5000 app:app;
else
  echo 'Falha na verificação do Redis. Saindo...';
  exit 1;
fi