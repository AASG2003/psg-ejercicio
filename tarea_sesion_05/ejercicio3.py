# Convertir a cuantos días, horas, 
# minutos y segundos corresponde la 
# siguiente cantidad de segundos: 
# 288325

segundos_dados = 288325;
segundos = segundos_dados % 60;
minutos = segundos_dados // 60;
horas = minutos // 60;
dias = horas // 24;
minutos = minutos % 60;
horas = horas % 24;
print("{} corresponde a: {} dia, {} horas, {} minutos, {} segundos"
      .format(segundos_dados, dias, horas, minutos, segundos));
