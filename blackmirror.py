opcaoEscolhida = -1

while(opcaoEscolhida != 0):
	opcaoEscolhida = int(input(f''' 
======== B A N C O  A Z U L ========
    INFORME UMA DAS OPÇÕES ABAIXO:    
[1] - QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?
							

[2] - QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE
TELEVISÃO?

[3] - QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA
A NETFLIX NO EPISÓDIO?

[4] - COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?

[5] - QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE
ELA FAZ EM RESPOSTA?

[6] - QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE
BLACK MIRROR?

[7] - O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK
MIRROR? EXPLIQUE.        
====================================                       
: '''))
	if(opcaoEscolhida == 1):
		print("Joan Tait")
	elif(opcaoEscolhida == 2):
		print("O show é feito por um computador quântico usando atores virtuais baseados em CGI e dados em tempo real coletados dos dispositivos de Joan.")
	elif(opcaoEscolhida == 3):
		print("streamberry")
	elif(opcaoEscolhida == 4):
		print("Joan descobre a existência da série sobre sua vida quando ela começa a receber mensagens de estranhos que a reconhecem e citam eventos íntimos de sua vida.")
	elif(opcaoEscolhida == 5):
		print("eA reação inicial de Joan ao descobrir a série é de choque e incredulidade. Ela então decide confrontar Kenneth Walsh e, eventualmente, confronta os roteiristas sobre a invasão em sua vida pessoal..")		
	elif(opcaoEscolhida == 6):
		print("6 - Os temas principais explorados neste episódio de Black Mirror incluem a invasão de privacidade, os perigos do entretenimento reality sem limites éticos, e a desumanização que ocorre quando a vida de uma pessoa é transformada em um espetáculo.")	
	elif(opcaoEscolhida == 7):
		print("O episódio termina de maneira típica para a série Black Mirror, pois revela as consequências perturbadoras e muitas vezes sombrias das tecnologias emergentes e suas interações com a sociedade. No entanto, ao contrário de alguns episódios que terminam com um final totalmente sombrio, ''Joan is Awful'' termina com uma nota de esperança, sugerindo que Joan pode encontrar uma forma de recuperar o controle de sua vida.")	        
		
	else:
		print("!!!  O P Ç Ã O  I N V Á L I D A ")
