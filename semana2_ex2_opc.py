seg=int(input("Por favor, entre com o numero de segundos que deseja converter: "))
dias=seg//86400
segrest1=seg % 86400
horas=segrest1//3600
segrest2=segrest1 % 3600
minutos=segrest2//60
segrest3=segrest2 % 60
print(dias,"dias,",horas,"horas,",minutos,"minutos","e",segrest3,"segundos.")